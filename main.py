import tkinter as tk
from tkinter import ttk

class SlushieMachineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Buzlu İçecek Makinesi")
        self.root.geometry("400x320")
        self.root.configure(bg="#e0f7fa")  # Açık mavi arka plan
        self.root.resizable(False, False)
        self.preparing_time = 3
        self.create_main_menu()

    def create_main_menu(self):
        self.clear_screen()
        tk.Label(self.root, text="Bir içecek seçin:", font=("Arial", 18, "bold"),
                 bg="#e0f7fa", fg="#006064").pack(pady=20)

        tk.Button(self.root, text="🍋 Limonlu", font=("Arial", 14, "bold"), width=20,
                  bg="#fff9c4", fg="#f57f17", activebackground="#fff176",
                  command=lambda: self.show_payment_screen("Limonlu")).pack(pady=10)

        tk.Button(self.root, text="🍇 Böğürtlenli", font=("Arial", 14, "bold"), width=20,
                  bg="#f3e5f5", fg="#6a1b9a", activebackground="#ce93d8",
                  command=lambda: self.show_payment_screen("Böğürtlenli")).pack(pady=10)

    def show_payment_screen(self, flavor):
        self.selected_flavor = flavor
        self.clear_screen()

        tk.Label(self.root, text=f"{flavor} İçeceği Seçildi", font=("Arial", 14, "bold"),
                 bg="#e0f7fa", fg="#004d40").pack(pady=10)
        tk.Label(self.root, text="Lütfen 39.90₺ ödeme yapınız", font=("Arial", 14),
                 bg="#e0f7fa", fg="#004d40").pack(pady=5)
        tk.Label(self.root, text="[POS cihazı burada olacak]", font=("Arial", 10, "italic"),
                 bg="#e0f7fa", fg="gray").pack(pady=5)

        tk.Button(self.root, text="✅ Ödeme Yapıldı", font=("Arial", 12), bg="#c8e6c9", fg="#1b5e20",
                  activebackground="#81c784", command=self.start_preparation).pack(pady=20)

    def start_preparation(self):
        self.clear_screen()
        tk.Label(self.root, text="İçeceğiniz hazırlanıyor...", font=("Arial", 14, "bold"),
                 bg="#e0f7fa", fg="#004d40").pack(pady=10)

        style = ttk.Style()
        style.theme_use('default')
        style.configure("TProgressbar", thickness=20, background="#4db6ac")

        self.progress = ttk.Progressbar(self.root, length=300, mode='determinate', style="TProgressbar")
        self.progress.pack(pady=20)
        self.progress['value'] = 0

        self.progress_value = 0
        self.update_progress()

    def update_progress(self):
        if self.progress_value < 100:
            self.progress_value += (100 / self.preparing_time)
            self.progress['value'] = self.progress_value
            self.root.after(1000, self.update_progress)
        else:
            self.show_completion_screen()

    def show_completion_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Afiyet olsun!", font=("Arial", 18, "bold"),
                 bg="#e0f7fa", fg="#2e7d32").pack(pady=30)
        tk.Button(self.root, text="🔁 Ana Menüye Dön", font=("Arial", 12),
                  bg="#bbdefb", fg="#0d47a1", activebackground="#90caf9",
                  command=self.create_main_menu).pack(pady=20)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root.configure(bg="#e0f7fa")  # Temizlerken rengi koru


if __name__ == "__main__":
    root = tk.Tk()
    app = SlushieMachineApp(root)
    root.mainloop()