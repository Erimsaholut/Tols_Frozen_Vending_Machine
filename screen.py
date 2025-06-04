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
        self.bind("<Escape>", lambda e: self.destroy())

        self.ekran_genislik = self.winfo_screenwidth()
        self.ekran_yukseklik = self.winfo_screenheight()

        self.buton_ops_mid = {
            "font": ("Arial", 22, "bold"),
            "width": 22,
            "height": 5,
            "bg": "#ffffff",
            "fg": "black",
            "relief": "flat",
            "activebackground": "#dddddd"
        }
        self.buton_ops_small = {
            "font": ("Arial", 22, "bold"),
            "width": 7,
            "height": 3,
            "bg": "#ffffff",
            "fg": "black",
            "relief": "flat",
            "activebackground": "#dddddd"
        }


        # --- Sabitler ---
        self.FIYATLAR = {"Medium": 34.99, "Large": 39.99, "X-Large": 44.99}
        self.HAZIRLAMA_SURELERI = {"Medium": 3, "Large": 4, "X-Large": 5}
        self.BARDAK_BOYUTLARI = {"Medium": 300, "Large": 380, "X-Large": 450}
        self.secilen_icecek = None
        self.secilen_boyut = None
        self.secilen_fiyat = 0.0

        # --- Resimleri Yükle ---
        try:
            self.arkaplan_resmi = ImageTk.PhotoImage(Image.open(ARKAPLAN).resize((self.ekran_genislik, self.ekran_yukseklik)))
            self.limonlu_icon = ImageTk.PhotoImage(Image.open(LIMONLU_ICON).resize((150, 150)))
            self.bogurtlen_icon = ImageTk.PhotoImage(Image.open(BOGURTLEN_ICON).resize((150, 150)))
            self.pos_resmi = ImageTk.PhotoImage(Image.open(POS_ICON).resize((300, 300)))
        except FileNotFoundError as e:
            print(f"Hata: {e}")
            self.destroy()
            return

        self.canvas = tk.Canvas(self, width=self.ekran_genislik, height=self.ekran_yukseklik)
        self.canvas.pack()
        self.ana_ekran()

    def ana_ekran(self):
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor="nw", image=self.arkaplan_resmi)
        self.canvas.create_text(self.ekran_genislik // 2, self.ekran_yukseklik // 6,
                                text="İçeceğinizi Seçin", font=("Helvetica", 48, "bold italic"), fill="#FFFACD")

        self.limonlu_buton = tk.Button(self, image=self.limonlu_icon,
                                       command=lambda: self.boyut_secim_ekrani("Limonlu"))
        self.bogurtlen_buton = tk.Button(self, image=self.bogurtlen_icon,
                                         command=lambda: self.boyut_secim_ekrani("Böğürtlenli"))

        self.canvas.create_window(self.ekran_genislik // 3, self.ekran_yukseklik // 2.5, window=self.limonlu_buton)
        self.canvas.create_window(2 * self.ekran_genislik // 3, self.ekran_yukseklik // 2.5, window=self.bogurtlen_buton)

        self.canvas.create_text(self.ekran_genislik // 3, self.ekran_yukseklik // 2.5 + 100,
                                text="Limonlu Frozen", font=("Helvetica", 24, "bold"), fill="white")
        self.canvas.create_text(2 * self.ekran_genislik // 3, self.ekran_yukseklik // 2.5 + 100,
                                text="Böğürtlenli Frozen", font=("Helvetica", 24, "bold"), fill="white")

    def boyut_secim_ekrani(self, icecek):
        self.secilen_icecek = icecek
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor="nw", image=self.arkaplan_resmi)
        self.canvas.create_text(self.ekran_genislik // 2, self.ekran_yukseklik // 6,
                                text=f"{icecek} Frozen İçin Boyut Seçin", font=("Helvetica", 48, "bold italic"), fill="#FFFACD")

        medium_text = f"Medium ({self.BARDAK_BOYUTLARI['Medium']} ml)\n{self.FIYATLAR['Medium']:.2f} TL"
        large_text = f"Large ({self.BARDAK_BOYUTLARI['Large']} ml)\n{self.FIYATLAR['Large']:.2f} TL"
        xlarge_text = f"X-Large ({self.BARDAK_BOYUTLARI['X-Large']} ml)\n{self.FIYATLAR['X-Large']:.2f} TL"

        medium_buton = tk.Button(self, text=medium_text, command=lambda: self.odeme_ekrani(icecek, "Medium"), **self.buton_ops_mid)
        large_buton = tk.Button(self, text=large_text, command=lambda: self.odeme_ekrani(icecek, "Large"), **self.buton_ops_mid)
        xlarge_buton = tk.Button(self, text=xlarge_text, command=lambda: self.odeme_ekrani(icecek, "X-Large"), **self.buton_ops_mid)
        geri_buton = tk.Button(self, text="< Geri", command=self.ana_ekran, **self.buton_ops_small)

        self.canvas.create_window(self.ekran_genislik // 4, self.ekran_yukseklik // 2, window=medium_buton)
        self.canvas.create_window(self.ekran_genislik // 2, self.ekran_yukseklik // 2, window=large_buton)
        self.canvas.create_window(3 * self.ekran_genislik // 4, self.ekran_yukseklik // 2, window=xlarge_buton)
        self.canvas.create_window(100, self.ekran_yukseklik - 50, window=geri_buton)

    def odeme_ekrani(self, icecek, boyut):
        self.secilen_boyut = boyut
        self.secilen_fiyat = self.FIYATLAR[boyut]
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor="nw", image=self.arkaplan_resmi)

        self.canvas.create_text(self.ekran_genislik // 2, self.ekran_yukseklik // 5,
                                text=f"{icecek} Frozen ({boyut}) seçildi!", font=("Helvetica", 36, "bold italic"), fill="#FFDEAD")
        self.canvas.create_text(self.ekran_genislik // 2, self.ekran_yukseklik // 3.5,
                                text=f"Tutar: {self.secilen_fiyat:.2f} TL", font=("Helvetica", 32, "bold"), fill="#FFE4B5")
        self.canvas.create_image(self.ekran_genislik // 2, self.ekran_yukseklik // 1.8, image=self.pos_resmi)

        odeme_buton = tk.Button(self, text="Ödeme Yapıldı", command=self.hazirlaniyor_ekrani, **self.buton_ops_mid)
        self.canvas.create_window(self.ekran_genislik // 2, self.ekran_yukseklik // 1.8 + 200, window=odeme_buton)

        geri_buton = tk.Button(self, text="< Geri", command=lambda: self.boyut_secim_ekrani(self.secilen_icecek))
        self.canvas.create_window(100, self.ekran_yukseklik - 50, window=geri_buton)

    def hazirlaniyor_ekrani(self):
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor="nw", image=self.arkaplan_resmi)

        hazirlama_suresi = self.HAZIRLAMA_SURELERI[self.secilen_boyut]
        self.canvas.create_text(self.ekran_genislik // 2, self.ekran_yukseklik // 3,
                                text=f"{self.secilen_icecek} Frozen ({self.secilen_boyut}) hazırlanıyor...",
                                font=("Helvetica", 32, "bold"), fill="#ADD8E6")

        style = ttk.Style(self)
        style_name = "Custom.Horizontal.TProgressbar"
        style.theme_use('default')
        style.configure(style_name, thickness=38, troughcolor='#e0e0e0', background='#76c7c0', bordercolor='#333333')

        self.progress = ttk.Progressbar(self, orient=tk.HORIZONTAL, length=1400, mode='determinate', maximum=100, style=style_name)
        self.canvas.create_window(self.ekran_genislik // 2, self.ekran_yukseklik // 2, window=self.progress)

        self.progress_value = 0
        self.progress_interval = int((hazirlama_suresi * 1000) / 100)
        self.bari_doldur()

    def bari_doldur(self):
        if self.progress_value <= 100:
            self.progress['value'] = self.progress_value
            self.progress_value += 5
            self.after(self.progress_interval, self.bari_doldur)
        else:
            self.afiyet_olsun()

    def afiyet_olsun(self):
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor="nw", image=self.arkaplan_resmi)
        self.canvas.create_text(self.ekran_genislik // 2, self.ekran_yukseklik // 2,
                                text="Afiyet olsun!", font=("Helvetica", 48, "bold italic"), fill="#90EE90")
        self.after(2000, self.ana_ekran)

if __name__ == "__main__":
    app = IcecekUygulamasi()
    app.mainloop()