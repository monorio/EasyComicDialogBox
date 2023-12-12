import tkinter as tk
from tkinter import filedialog, messagebox
from auto_dialogue import add_dialogue_box, generate_dialogue_parameter, rename_images, natural_sort_key
from PIL import Image
import os

class DialogueBoxApp:
    def __init__(self, master):
        self.master = master
        master.title("Dialogue Box Generator")

        # Set custom icon
        icon_path = "./favicon.ico"  # Replace with the actual path to your icon
        master.iconbitmap(icon_path)

        # Folder Path
        self.folder_path_label = tk.Label(master, text="Folder Path:")
        self.folder_path_label.grid(row=0, column=0, sticky="w")

        # Predefined text for the folder path entry
        default_folder_text = "Only support PNG files. Convert non-PNG files to PNG using the button 'Convert to PNG '."

        self.folder_path_entry = tk.Entry(master, width=50)
        self.folder_path_entry.insert(0, default_folder_text)
        self.folder_path_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5)
        self.browse_button = tk.Button(master, text="Browse", command=self.browse_folder)
        self.browse_button.grid(row=0, column=3, padx=5, pady=5)


        # MIN_SET
        self.min_set_label = tk.Label(master, text="MIN_SET:")
        self.min_set_label.grid(row=1, column=0, sticky="w")
        self.min_set_scale = tk.Scale(master, from_=-5.0, to=5.0, resolution=0.5, orient=tk.HORIZONTAL)
        self.min_set_scale.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

        # Font Type Path
        self.font_path_label = tk.Label(master, text="Font Type Path:")
        self.font_path_label.grid(row=2, column=0, sticky="w")
        self.font_path_entry = tk.Entry(master, width=50)
        self.font_path_entry.insert(0, 'C:/Windows/Fonts/Dengb.ttf')
        self.font_path_entry.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

        # Execute Button
        self.execute_button = tk.Button(master, text="Execute", command=self.execute_folder)
        self.execute_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Convert to PNG Button
        self.convert_button = tk.Button(master, text="Convert to PNG", command=self.convert_to_png)
        self.convert_button.grid(row=3, column=0, columnspan=4, pady=10)

        # Sort Images Button
        self.sort_button = tk.Button(master, text="Sort Images", command=self.sort_images)
        self.sort_button.grid(row=3, column=2, columnspan=16, pady=10)


        # Image Path Label
        self.image_path_label = tk.Label(master, text="Executing:")
        self.image_path_label.grid(row=4, column=0, sticky="w")
        self.image_path_var = tk.StringVar()
        self.image_path_entry = tk.Entry(master, textvariable=self.image_path_var, state='readonly', width=50)
        self.image_path_entry.grid(row=4, column=1, columnspan=2, padx=5, pady=5)


    def browse_folder(self):
        folder_path = filedialog.askdirectory()
        self.folder_path_entry.delete(0, tk.END)
        self.folder_path_entry.insert(0, folder_path)

    def execute_folder(self):
        folder_path = self.folder_path_entry.get()
        min_set = float(self.min_set_scale.get())
        font_path = self.font_path_entry.get()

        if folder_path and font_path:
            res_list = generate_dialogue_parameter(f'{folder_path}/script.txt')
            for i in res_list:
                img_name = i[0].replace('p', '')
                image_path = f'{folder_path}/{img_name}.png'

                # Update the image_path entry in the GUI
                self.image_path_var.set(image_path)

                # Update the GUI in real-time
                self.master.update_idletasks()
                add_dialogue_box(i, f'{folder_path}/', f'{folder_path}/output/', MIN_SET=min_set, font_type_path=font_path)
            messagebox.showinfo("Success", "Execution completed successfully.")
        else:
            messagebox.showerror("Error", "Please provide valid folder path and font type path.")

    def convert_to_png(self):
        folder_path = self.folder_path_entry.get()

        if folder_path:
            for filename in os.listdir(folder_path):
                if filename.lower().endswith(('.jpg', '.jpeg', '.gif', '.bmp')):
                    image_path = os.path.join(folder_path, filename)
                    img = Image.open(image_path)

                    # Convert the image to PNG format
                    png_path = os.path.splitext(image_path)[0] + '.png'
                    img.save(png_path, 'PNG')

                    # Optionally, you may want to delete the original non-PNG file
                    # os.remove(image_path)

            messagebox.showinfo("Conversion", "Non-PNG files converted to PNG format.")
        else:
            messagebox.showerror("Error", "Please provide a valid folder path.")

    def sort_images(self):
        folder_path = self.folder_path_entry.get()

        if folder_path:
            try:
                rename_images(folder_path)
                messagebox.showinfo("Sorting", "Images sorted successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Error sorting images: {str(e)}")
        else:
            messagebox.showerror("Error", "Please provide a valid folder path.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DialogueBoxApp(root)
    root.mainloop()
