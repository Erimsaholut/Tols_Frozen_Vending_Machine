import tkinter as tk
from tkinter import ttk
import time


class IceDrinkMachine:
    def __init__(self, root):
        self.root = root
        self.root.title("Buzlu İçecek Makinesi")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.preparing_time = 3  # Hazırlık süresi (saniye cinsinden)
        self.create_main_screen()

    def clear_screen(self):
        """Ekrandaki tüm widget'ları temizler."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_main_screen(self):
        """Ana ekranı (içecek seçimi) oluşturur."""
        self.clear_screen()

        # Ana pencereye daha canlı bir arka plan rengi atayalım
        self.root.configure(bg="#87CEEB")  # Gökyüzü Mavisi

        # Başlık etiketi
        self.title_label = tk.Label(self.root, text="Lütfen İçeceğinizi Seçin", font=("Helvetica", 36, "bold"),
                                    fg="#FFFFFF", bg="#87CEEB")  # Beyaz metin, arka plan uyumlu
        self.title_label.pack(pady=50)

        # Butonları içeren çerçeve
        self.button_frame = tk.Frame(self.root, bg="#87CEEB")  # Çerçeve arka planı uyumlu
        self.button_frame.pack(pady=20)

        # Limonlu içecek butonu
        self.lemon_button = tk.Button(self.button_frame, text="🍋 Limonlu", font=("Helvetica", 24, "bold"),
                                      width=15, height=5, bg="#FFD700", fg="#333333",
                                      # Altın sarısı buton, koyu gri metin
                                      activebackground="#FFEA00",  # Tıklandığında daha açık sarı
                                      relief="raised", borderwidth=5, cursor="hand2",
                                      # Kabarık, kalın kenarlık, el imleci
                                      command=lambda: self.show_payment_screen("Limonlu"))
        self.lemon_button.pack(side=tk.LEFT, padx=20)

        # Böğürtlenli içecek butonu
        self.blackberry_button = tk.Button(self.button_frame, text="🍇 Böğürtlenli", font=("Helvetica", 24, "bold"),
                                           width=15, height=5, bg="#9932CC", fg="#FFFFFF",
                                           # Koyu mor buton, beyaz metin
                                           activebackground="#A020F0",  # Tıklandığında daha açık mor
                                           relief="raised", borderwidth=5, cursor="hand2",
                                           # Kabarık, kalın kenarlık, el imleci
                                           command=lambda: self.show_payment_screen("Böğürtlenli"))
        self.blackberry_button.pack(side=tk.RIGHT, padx=20)

    def show_payment_screen(self, drink_name):
        """Ödeme ekranını oluşturur."""
        self.clear_screen()

        # Ana pencereye farklı bir canlı arka plan rengi atayalım
        self.root.configure(bg="#FF6347")  # Domates Kırmızısı

        self.selected_drink = drink_name
        self.payment_label = tk.Label(self.root, text=f"Lütfen 39.90₺ ödeme yapınız\n({drink_name})",
                                      font=("Helvetica", 32, "bold"), fg="#FFFFFF",
                                      bg="#FF6347")  # Beyaz metin, arka plan uyumlu
        self.payment_label.pack(pady=50)

        # POS cihazı görüntüsü için yer tutucu
        self.pos_image_label = tk.Label(self.root, text="[ TEMASSIZ ÖDEME İÇİN DOKUNDURUN ]",
                                        font=("Helvetica", 20, "italic"), fg="#FFFF00", padx=50, pady=50,
                                        relief="groove", borderwidth=3, bg="#FF6347")  # Sarı metin, oluklu kenarlık
        self.pos_image_label.pack(pady=20)

        # Ödeme yapıldı butonu
        self.payment_done_button = tk.Button(self.root, text="Ödeme Yapıldı", font=("Helvetica", 18, "bold"),
                                             bg="#32CD32", fg="white", width=20, height=3,  # Canlı yeşil buton
                                             activebackground="#00FF00", relief="raised", borderwidth=4, cursor="hand2",
                                             command=self.start_preparation)
        self.payment_done_button.pack(pady=30)

    def start_preparation(self):
        """İçecek hazırlık ekranını başlatır."""
        self.clear_screen()

        # Ana pencereye farklı bir canlı arka plan rengi atayalım
        self.root.configure(bg="#6A5ACD")  # Kayrak Mavi

        self.preparation_label = tk.Label(self.root, text="İçeceğiniz hazırlanıyor...", font=("Helvetica", 32, "bold"),
                                          fg="#FFFFFF", bg="#6A5ACD")  # Beyaz metin, arka plan uyumlu
        self.preparation_label.pack(pady=50)

        # İlerleme çubuğu
        # Stil tanımlaması ile ilerleme çubuğunu renklendirebiliriz
        s = ttk.Style()
        s.theme_use('clam')  # 'clam' teması daha fazla özelleştirme imkanı sunar
        s.configure("TProgressbar", thickness=30, background="#FFD700", troughcolor="#E0E0E0", borderwidth=2,
                    relief="flat")  # Altın sarısı dolgu, gri boşluk

        self.progress_bar = ttk.Progressbar(self.root, orient="horizontal", length=600, mode="determinate",
                                            style="TProgressbar")
        self.progress_bar.pack(pady=30)
        self.progress_bar["maximum"] = 100
        self.progress_bar["value"] = 0

        self.root.update_idletasks()
        self.animate_progress_bar(0)

    def animate_progress_bar(self, value):
        """İlerleme çubuğunu animasyonlu olarak doldurur."""
        if value <= 100:
            self.progress_bar["value"] = value
            self.root.update_idletasks()
            # Hazırlık süresini kullanarak ilerleme hızını ayarlayalım
            # (100 / self.preparing_time) her adımda ilerleme çubuğunun ne kadar dolacağını belirler
            self.root.after(int(self.preparing_time * 1000 / 100), self.animate_progress_bar,
                            value + 1)  # Her saniye 100/saniye adımı
        else:
            self.show_enjoy_message()

    def show_enjoy_message(self):
        """Afiyet olsun mesajını gösterir ve ana ekrana döner."""
        self.clear_screen()

        # Ana pencereye son bir canlı arka plan rengi atayalım
        self.root.configure(bg="#3CB371")  # Orta Deniz Yeşili

        self.enjoy_label = tk.Label(self.root, text="Afiyet Olsun!", font=("Helvetica", 48, "bold"),
                                    fg="#FFFFFF", bg="#3CB371")  # Beyaz metin, arka plan uyumlu
        self.enjoy_label.pack(pady=100)

        self.root.after(3000, self.create_main_screen)  # 3 saniye sonra ana ekrana dön


if __name__ == "__main__":
    root = tk.Tk()
    app = IceDrinkMachine(root)
    root.mainloop()
