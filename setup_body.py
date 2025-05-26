from PIL import Image
import numpy as np

class Body:
    def __init__(self, type, distortion):
        self.types = {0: "Torso", 1: "Head", 2: "Legs", 3: "Right_arm", 4: "Left_arm", 5: 'Joints'}
        self.name = self.types[type]
        if type < 5:
            self.img = Image.open(f'Feld_v/{self.name}.png').convert("RGBA")
        self.x = self.img.width
        self.y = self.img.height
        self.distortion = distortion

    def change_color(self):
        self.data = np.array(self.img)
        if self.distortion > 0:
            new_color = (int(255 * self.distortion), int(255 * (1 - self.distortion)), 0)
        else:
            new_color = (0, int(255 * (1 - abs(self.distortion))), int(255 * abs(self.distortion)))
        inv_pixels = self.data[:, :, 3] > 0
        for i in range(3):
            self.data[inv_pixels, i] = new_color[i]
        self.img = Image.fromarray(self.data)

class Body_part(Body):
    def __init__(self, type: int, distortion):
        super().__init__(type, distortion)

    def resize(self):
        self.img = self.img.resize(
            (int(self.x * (1 + self.distortion/2)), 
             int(self.y * (1 + self.distortion/2))),
            
        )
        self.x, self.y = self.img.size
        self.img.convert('RGBA')  # Обновляем размеры

def assemble_body():
    torso = Body_part(0, 1)
    head = Body_part(1, 0.5)
    left_arm = Body_part(4, 0)
    right_arm = Body_part(3, 0)
    legs = Body_part(2, -1)
    
    for item in [torso, head, left_arm, right_arm, legs]:
        item.change_color()
        item.resize()
        
    
    width = torso.x + left_arm.x + right_arm.x 
    height = head.y + torso.y + legs.y
    human = Image.new('RGBA', (width, height), (0, 0, 0, 0))

    human.paste(head, ((width - head.x) // 2, 0), head.img)
    human.paste(torso, (right_arm.x, head.y), torso.img)
    human.paste(left_arm, (right_arm.x + torso.x, head.y), left_arm.img)
    human.paste(right_arm, (0, head.y), right_arm.img)
    human.paste(legs, ((width - legs.x) // 2, head.y + torso.y), legs.img)

    human.save('human_final.png')

assemble_body()