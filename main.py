import tkinter as tk
from tkinter import ttk

class MeasurementsWindow:
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel(parent)
        self.window.title("Антропометрические промеры")
        self.window.geometry("800x900")
        
        # Создаем Notebook для разделения на вкладки
        self.notebook = ttk.Notebook(self.window)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Создаем вкладки
        self.real_frame = self.create_scrollable_frame("Реальные промеры")
        self.perceived_frame = self.create_scrollable_frame("Воспринимаемые промеры")
        
        self.notebook.add(self.real_frame, text="Реальные")
        self.notebook.add(self.perceived_frame, text="Воспринимаемые")
        
        self.entries = {"real": {}, "perceived": {}}
        self.create_measurement_fields()
        
        # Кнопки сохранения и отмены
        btn_frame = ttk.Frame(self.window)
        btn_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(btn_frame, text="Сохранить", command=self.save_measurements).pack(side=tk.RIGHT, padx=5)
        ttk.Button(btn_frame, text="Отмена", command=self.window.destroy).pack(side=tk.RIGHT, padx=5)
    
    def create_scrollable_frame(self, title):
        """Создает фрейм с прокруткой для вкладки"""
        container = ttk.Frame(self.notebook)
        canvas = tk.Canvas(container)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        return container
    
    def create_measurement_field(self, parent, label_text, measurement_type):
        """Создает поле для ввода одного параметра"""
        frame = ttk.Frame(parent)
        frame.pack(fill=tk.X, padx=5, pady=2)
        
        label = ttk.Label(frame, text=label_text, width=40)
        label.pack(side=tk.LEFT)
        
        entry = ttk.Entry(frame)
        entry.pack(side=tk.RIGHT, fill=tk.X, expand=True)
        
        self.entries[measurement_type][label_text] = entry
        return entry
    
    def create_measurement_fields(self):
        """Создаем поля для ввода всех антропометрических параметров"""
        parameters = [
            # Реальные промеры
            ("Высота головы (см):", "real"),
            ("Ширина головы (см):", "real"),
            ("Длина шеи (см):", "real"),
            ("Длина левого плеча от яремной ямки (см):", "real"),
            ("Длина правого плеча (см):", "real"),
            ("Длина от плеча до локтя левой руки (см):", "real"),
            ("Длина от плеча до локтя правой руки (см):", "real"),
            ("Ширина локтевого сустава левой руки (см):", "real"),
            ("Ширина локтевого сустава правой руки (см):", "real"),
            ("Длина левого предплечья от локтя до кисти (см):", "real"),
            ("Длина правого предплечья от локтя до кисти (см):", "real"),
            ("Длина левой кисти (см):", "real"),
            ("Длина правой кисти (см):", "real"),
            ("Длина туловища от яремной ямки до пупка (см):", "real"),
            ("Длина от пупка до паха (см):", "real"),
            ("Ширина груди (см):", "real"),
            ("Ширина талии (см):", "real"),
            ("Ширина таза (см):", "real"),
            ("Длина левой ноги от паха до колена (см):", "real"),
            ("Длина правой ноги от паха до колена (см):", "real"),
            ("Ширина левой ноги в коленном суставе (см):", "real"),
            ("Ширина правой ноги в коленном суставе (см):", "real"),
            ("Длина левой ноги от колена до косточки ступни (см):", "real"),
            ("Длина правой ноги от колена до косточки ступни (см):", "real"),
            ("Длина левой стопы (см):", "real"),
            ("Длина правой стопы (см):", "real"),
            
            # Воспринимаемые промеры (те же параметры, но субъективные)
            ("Воспринимаемая высота головы (см):", "perceived"),
            ("Воспринимаемая ширина головы (см):", "perceived"),
            ("Воспринимаемая длина шеи (см):", "perceived"),
            ("Воспринимаемая длина левого плеча (см):", "perceived"),
            ("Воспринимаемая длина правого плеча (см):", "perceived"),
            ("Воспринимаемая длина от плеча до локтя левой руки (см):", "perceived"),
            ("Воспринимаемая длина от плеча до локтя правой руки (см):", "perceived"),
            ("Воспринимаемая ширина локтя левой руки (см):", "perceived"),
            ("Воспринимаемая ширина локтя правой руки (см):", "perceived"),
            ("Воспринимаемая длина левого предплечья (см):", "perceived"),
            ("Воспринимаемая длина правого предплечья (см):", "perceived"),
            ("Воспринимаемая длина левой кисти (см):", "perceived"),
            ("Воспринимаемая длина правой кисти (см):", "perceived"),
            ("Воспринимаемая длина туловища до пупка (см):", "perceived"),
            ("Воспринимаемая длина от пупка до паха (см):", "perceived"),
            ("Воспринимаемая ширина груди (см):", "perceived"),
            ("Воспринимаемая ширина талии (см):", "perceived"),
            ("Воспринимаемая ширина таза (см):", "perceived"),
            ("Воспринимаемая длина левой ноги до колена (см):", "perceived"),
            ("Воспринимаемая длина правой ноги до колена (см):", "perceived"),
            ("Воспринимаемая ширина левого колена (см):", "perceived"),
            ("Воспринимаемая ширина правого колена (см):", "perceived"),
            ("Воспринимаемая длина левой ноги от колена (см):", "perceived"),
            ("Воспринимаемая длина правой ноги от колена (см):", "perceived"),
            ("Воспринимаемая длина левой стопы (см):", "perceived"),
            ("Воспринимаемая длина правой стопы (см):", "perceived")
        ]
        
        # Создаем поля для всех параметров
        for param, param_type in parameters:
            if param_type == "real":
                self.create_measurement_field(self.real_frame.winfo_children()[2], param, param_type)
            else:
                self.create_measurement_field(self.perceived_frame.winfo_children()[2], param, param_type)
    
    def save_measurements(self):
        """Сохранение промеров"""
        real_measurements = {k: v.get() for k, v in self.entries["real"].items()}
        perceived_measurements = {k: v.get() for k, v in self.entries["perceived"].items()}
        
        # Здесь можно обработать сохраненные параметры
        print("Реальные промеры:")
        for name, value in real_measurements.items():
            print(f"{name}: {value}")
        
        print("\nВоспринимаемые промеры:")
        for name, value in perceived_measurements.items():
            print(f"{name}: {value}")
        
        self.window.destroy()

class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Антропометрические измерения")
        self.root.geometry("400x300")
        
        self.btn_open_measurements = ttk.Button(
            root, 
            text="Открыть промеры", 
            command=self.open_measurements_window
        )
        self.btn_open_measurements.pack(expand=True, padx=20, pady=20)
    
    def open_measurements_window(self):
        MeasurementsWindow(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()