import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import time

# --- Uygulama Ayarları ---
ARKAPLAN = "arkaplan.png"
LIMONLU_ICON = "limonlu_icon.png"
BOGURTLEN_ICON = "bogurtlenli_icon.png"
POS_ICON = "pos_cihazi.png"

class IcecekUygulamasi(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("İçecek Makinesi")
        self.attributes("-fullscreen", True)
        self.bind("<Escape>", lambda e: self.destroy())  # ESC ile çıkmak için

        self.ekran_genislik = self.winfo_screenwidth()
        self.ekran_yukseklik = self.winfo_screenheight()

        self.arkaplan_resmi = ImageTk.PhotoImage(
            Image.open(ARKAPLAN).resize((self.ekran_genislik, self.ekran_yukseklik))
        )
        self.limonlu_icon = ImageTk.PhotoImage(Image.open(LIMONLU_ICON).resize((150, 150)))
        self.bogurtlen_icon = ImageTk.PhotoImage(Image.open(BOGURTLEN_ICON).resize((150, 150)))
        self.pos_resmi = ImageTk.PhotoImage(Image.open(POS_ICON).resize((300, 300)))

        self.canvas = tk.Canvas(self, width=self.ekran_genislik, height=self.ekran_yukseklik)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor="nw", image=self.arkaplan_resmi)

        self.ana_ekran()
    def ana_ekran(self):
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor="nw", image=self.arkaplan_resmi)
        self.canvas.create_text(
            self.ekran_genislik // 2,
            self.ekran_yukseklik // 6,
            text="İçeceğinizi Seçin",
            font=("Helvetica", 48, "bold italic"),
            fill="#FFFACD"
        )

        self.limonlu_buton = tk.Button(self, image=self.limonlu_icon, command=lambda: self.odeme_ekrani("Limonlu"))
        self.bogurtlen_buton = tk.Button(self, image=self.bogurtlen_icon, command=lambda: self.odeme_ekrani("Böğürtlenli"))

        self.canvas.create_window(self.ekran_genislik // 3, self.ekran_yukseklik // 3, window=self.limonlu_buton)
        self.canvas.create_window(2 * self.ekran_genislik // 3, self.ekran_yukseklik // 3, window=self.bogurtlen_buton)
        # Add labels for drinks
        self.canvas.create_text(
            self.ekran_genislik // 3,
            self.ekran_yukseklik // 3 + 100,
            text="Limonlu Frozen",
            font=("Helvetica", 24, "bold"),
            fill="white"
        )
        self.canvas.create_text(
            2 * self.ekran_genislik // 3,
            self.ekran_yukseklik // 3 + 100,
            text="Böğürtlenli Frozen",
            font=("Helvetica", 24, "bold"),
            fill="white"
        )
    def odeme_ekrani(self, icecek):
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor="nw", image=self.arkaplan_resmi)
        self.canvas.create_text(
            self.ekran_genislik // 2,
            self.ekran_yukseklik // 5,
            text=f"{icecek} içeceği seçildi!",
            font=("Helvetica", 36, "bold italic"),
            fill="#FFDEAD"
        )
        self.canvas.create_text(
            self.ekran_genislik // 2,
            self.ekran_yukseklik // 4,
            text="Lütfen ödeme yapınız",
            font=("Helvetica", 28, "bold"),
            fill="#FFE4B5"
        )
        self.canvas.create_image(
            self.ekran_genislik // 2,
            self.ekran_yukseklik // 2,
            image=self.pos_resmi
        )

        self.odeme_buton = tk.Button(self, text="Ödeme Yapıldı", font=("Arial", 14), command=self.hazirlaniyor_ekrani)
        self.canvas.create_window(
            self.ekran_genislik // 2,
            self.ekran_yukseklik // 2 + 200,
            window=self.odeme_buton
        )

    def hazirlaniyor_ekrani(self):
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor="nw", image=self.arkaplan_resmi)
        self.canvas.create_text(
            self.ekran_genislik // 2,
            self.ekran_yukseklik // 3,
            text="İçeceğiniz Hazırlanıyor...",
            font=("Helvetica", 32, "bold"),
            fill="#ADD8E6"
        )

        style = ttk.Style(self)
        style_name = "Custom.Horizontal.TProgressbar"
        style.theme_use('default')
        style.configure(
            style_name,
            thickness=38,
            troughcolor='#e0e0e0',
            background='#76c7c0',
            bordercolor='#333333'
        )
        self.progress = ttk.Progressbar(
            self,
            orient=tk.HORIZONTAL,
            length=1400,
            mode='determinate',
            maximum=100,
            style=style_name
        )
        self.canvas.create_window(
            self.ekran_genislik // 2,
            self.ekran_yukseklik // 2,
            window=self.progress
        )

        self.progress_value = 0
        self.bari_doldur()

    def bari_doldur(self):
        if self.progress_value <= 100:
            self.progress['value'] = self.progress_value
            self.progress_value += 5
            self.after(150, self.bari_doldur)
        else:
            self.afiyet_olsun()
    def afiyet_olsun(self):
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor="nw", image=self.arkaplan_resmi)
        self.canvas.create_text(
            self.ekran_genislik // 2,
            self.ekran_yukseklik // 2,
            text="Afiyet olsun!",
            font=("Helvetica", 48, "bold italic"),
            fill="#90EE90"
        )
        self.after(2000, self.ana_ekran)

if __name__ == "__main__":
    app = IcecekUygulamasi()
    app.mainloop()