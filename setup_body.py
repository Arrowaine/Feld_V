from PIL import Image,ImageDraw
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QBuffer, QIODevice,Qt
import numpy as np

types = {0: "Head", 1: "Torso", 2: "Legs", 3: "Right_arm", 4: "Left_arm"}
joints_points = {"Left_arm" : (0.342, 0.412),
                 "Right_arm": (0.65, 0.412),
                 "Head": [[0.228, 0.849], [0.771, 0.849]],
                 'Legs': [[0.274, 0.478], [0.713, 0.478]]}

def limit_and_scale(value):
    clamped = max(-1.0, min(1.0, value))
    if clamped > 0.5:
        return 1
    elif clamped < -0.5:
        return -1
    else:
        return clamped * 2

class Body:
    def __init__(self, type, distortion ):

        self.name = types[type]
        if type < 5:
            self.img = Image.open(f'assets\\{self.name}.png').convert("RGBA")       #  или без него
        self.x = self.img.width
        self.y = self.img.height
        if isinstance(distortion,tuple):
            self.distortion = (limit_and_scale(distortion[0]),limit_and_scale(distortion[1]))    
        else:
            self.distortion = limit_and_scale(distortion)

    def change_color(self):
        self.data = np.array(self.img)
        if isinstance(self.distortion, int) or isinstance(self.distortion, float):
            if self.distortion > 0:
                new_color = (int(255 * self.distortion), int(255 * (1 - self.distortion)), 0)
            else:
                new_color = (0, int(255 * (1 - abs(self.distortion))), int(255 * abs(self.distortion)))
        else:
            if self.distortion[0] > 0.0:
                new_color = (int(255 * self.distortion[0] ), int(255 * (1 - self.distortion[0] )), 0)
            else:
                new_color = (0, int(255 * (1 - abs(self.distortion[0] ))), int(255 * abs(self.distortion[0] )))
        inv_pixels = self.data[:, :, 3] > 0
        for i in range(3):
            self.data[inv_pixels, i] = new_color[i]
        self.img = Image.fromarray(self.data).convert("RGBA")
        

class Body_part(Body):
    def __init__(self, type: int, distortion):
        super().__init__(type, distortion)
        
    def resize(self):
        if isinstance(self.distortion, tuple):
            self.img = self.img.resize( (int(self.x * (1 + self.distortion[0]/2)), 
                                        int(self.y * (1 + self.distortion[1]/2))))       
        else:
            self.img.resize( 
                (int(self.x * (1 + self.distortion/2)),  
                 int(self.y * (1 + self.distortion/2))))

        self.x, self.y = self.img.size
        self.img.convert('RGBA')  

    def close_img(self):
        self.img.close()

    def create_joint(self,  distortion):
        
        if self.name in joints_points:
            joint = ImageDraw.Draw(self.img)
            joint_pos = joints_points.get(self.name)
            if isinstance(joint_pos,tuple):
                
                x = self.x * joint_pos[0]
                y = self.y * joint_pos[1]
                if distortion > 0:
                    color = (int(255 * distortion), int(255 * (1 - distortion)), 0)
                    joint.circle((x,y), 195*(distortion), fill = color, outline = "#000000", width= 5)
                else:
                    color = (0, int(255 * (1 - abs(distortion))), int(255 * abs(distortion)))
                    joint.circle((x,y), 195* (1 - abs(distortion)), fill = color, outline = "#000000", width= 5)
            else:
                for i in range(len(joint_pos)):
              
                    x = self.x * joint_pos[i][0]
                    y = self.y * joint_pos[i][1]
                    if distortion > 0:
                        color = (int(255 * distortion), int(255 * (1 - distortion)), 0)
                        joint.circle((x,y), 200*(distortion), fill = color, outline = "#000000", width= 5)
                    else:
                        color = (0, int(255 * (1 - abs(distortion))), int(255 * abs(distortion)))
                        joint.circle((x,y), 200* (1 - abs(distortion)), fill = color, outline = "#000000", width= 5)

def pil_to_pixmap(pil_image):

    buffer = QBuffer()
    buffer.open(QIODevice.ReadWrite)
    pil_image.save(buffer, "PNG")
    
    pixmap = QPixmap()
    pixmap.loadFromData(buffer.data(), "PNG")
    return pixmap

def pil_to_pixmap2(pil_image):

    qimage = QImage(
            pil_image.tobytes(),
            pil_image.width,
            pil_image.height,
            pil_image.width * 4,  # Bytes per line (4 канала: R, G, B, A)
            QImage.Format_RGBA8888
    )
    return QPixmap.fromImage(qimage)

def assemble_body(factors):
    # Инициализируем части тела
    factors = [factor/100 for factor in factors]
    torso = Body_part(1, (factors[3], factors[6]))
    head = Body_part(0, factors[5])
    left_arm = Body_part(4, factors[1])
    right_arm = Body_part(3, factors[1])
    legs = Body_part(2, factors[2])
    
    # подгоняем под факторы 
    for item in [torso, head, left_arm, right_arm, legs]:  
        item.change_color()
        item.resize()
    # определяем размеры итоговой картинки
    width = max(torso.x + left_arm.x + right_arm.x, head.x, legs.x)
    height = head.y + torso.y + legs.y
    human = Image.new('RGBA', (width, height), (0,0,0,0))
    # Создаем суставы для рук, ног и плеч

    head.create_joint(factors[4])
    left_arm.create_joint(factors[4])
    right_arm.create_joint(factors[4])
    legs.create_joint(factors[4])

    # Вставляем все части тела
    human.paste(im = head.img, box = ((width - head.x)//2, 0), mask = head.img)
    human.paste(torso.img, (right_arm.x, head.y), torso.img)
    human.paste(left_arm.img, (right_arm.x + torso.x, head.y), left_arm.img)
    human.paste(right_arm.img, (0, head.y), right_arm.img)
    human.paste(legs.img, ((width - legs.x)//2, head.y + torso.y), legs.img)

    #Закрываем картинки 
    for item in [torso, head, left_arm, right_arm, legs]:
        item.close_img()

    return pil_to_pixmap(human)
