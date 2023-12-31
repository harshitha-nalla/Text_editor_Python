import tkinter as tk
from tkinter import filedialog
from tkinter import font

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor")
        self.root.geometry("1000x500")

        self.text_widget = tk.Text(root, wrap='word', undo=True)
        self.text_widget.pack(expand='yes', fill='both')

        self.scroll_bar = tk.Scrollbar(self.text_widget, command=self.text_widget.yview)
        self.text_widget.config(yscrollcommand=self.scroll_bar.set)
        self.scroll_bar.pack(side='right', fill='y')

        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_file_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=root.destroy)

        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", command=self.text_widget.edit_undo)
        self.edit_menu.add_command(label="Redo", command=self.text_widget.edit_redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Change Font Size", command=self.change_font_size)
        self.edit_menu.add_command(label="Change Font Family", command=self.change_font_family)
        self.edit_menu.add_command(label="Change Font Color", command=self.change_font_color)

        # Default font settings
        self.current_font = font.nametofont("TkDefaultFont")

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.text_widget.delete(1.0, 'end')
                self.text_widget.insert('end', content)
            self.root.title(f"Text Editor - {file_path}")

    def save_file(self):
        if not hasattr(self, 'file_path'):
            self.save_file_as()
        else:
            content = self.text_widget.get(1.0, 'end-1c')
            with open(self.file_path, 'w') as file:
                file.write(content)
            self.root.title(f"Text Editor - {self.file_path}")

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            self.file_path = file_path
            self.save_file()

    def change_font_size(self):
        size = tk.simpledialog.askinteger("Font Size", "Enter font size:", initialvalue=self.current_font.cget('size'))
        if size:
            self.current_font.configure(size=size)
            self.text_widget.configure(font=self.current_font)

    def change_font_family(self):
        family = tk.simpledialog.askstring("Font Family", "Enter font family:", initialvalue=self.current_font.cget('family'))
        if family:
            self.current_font.configure(family=family)
            self.text_widget.configure(font=self.current_font)

    def change_font_color(self):
        color = tk.colorchooser.askcolor(initialcolor=self.current_font.cget('color'))
        if color[1]:
            self.current_font.configure(color=color[1])
            self.text_widget.configure(fg=color[1])

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()
