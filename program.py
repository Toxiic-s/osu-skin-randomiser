import os
import random
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime

class OsuSkinRandomizer:
    def __init__(self, master):
        self.master = master
        self.master.title("osu! Skin Randomizer")
        self.master.geometry("400x200")

        self.skins_folder = ""

        self.select_button = tk.Button(master, text="Select osu! Skins Folder", command=self.select_folder)
        self.select_button.pack(pady=10)

        self.folder_label = tk.Label(master, text="No folder selected")
        self.folder_label.pack(pady=5)

        self.randomize_button = tk.Button(master, text="Randomize Skin Elements", command=self.randomize_skin, state=tk.DISABLED)
        self.randomize_button.pack(pady=10)

        self.status_label = tk.Label(master, text="")
        self.status_label.pack(pady=5)

    def select_folder(self):
        self.skins_folder = filedialog.askdirectory(title="Select osu! Skins Folder")
        if self.skins_folder:
            self.folder_label.config(text=f"Selected folder: {self.skins_folder}")
            self.randomize_button.config(state=tk.NORMAL)

    def randomize_skin(self):
        if not self.skins_folder:
            messagebox.showerror("Error", "Please select a skins folder first.")
            return

        new_skin_folder = os.path.join(self.skins_folder, f"RandomizedSkin_{datetime.now().strftime('%Y%m%d_%H%M%S')}")
        os.makedirs(new_skin_folder, exist_ok=True)

        elements = ['approachcircle', 'hitcircle', 'cursor']
        for element in elements:
            self.randomize_element(new_skin_folder, element)

        self.status_label.config(text=f"Skin randomized and saved to:\n{new_skin_folder}")

    def randomize_element(self, new_skin_folder, element_name):
        files = []
        for root, _, filenames in os.walk(self.skins_folder):
            for filename in filenames:
                if filename.startswith(element_name):
                    files.append(os.path.join(root, filename))

        if files:
            random_file = random.choice(files)
            shutil.copy(random_file, new_skin_folder)

if __name__ == "__main__":
    root = tk.Tk()
    app = OsuSkinRandomizer(root)
    root.mainloop()
