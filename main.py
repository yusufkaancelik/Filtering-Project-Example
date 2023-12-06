from tkinter import *
iller = {
"Adana" : {
   "Technology": "3",
      "Fashion": "2",
    "Accessory": "1",
  "Real Estate": "4"},

"Adıyaman" : {
   "Technology": "0",
      "Fashion": "3",
    "Accessory": "4",
  "Real Estate": "5"},

"Afyonkarahisar" : {
   "Technology": "1",
      "Fashion": "4",
    "Accessory": "3",
  "Real Estate": "3"},

"Ağrı" : {
   "Technology": "1",
      "Fashion": "8",
    "Accessory": "2",
  "Real Estate": "1"},

"Aksaray" : {
   "Technology": "1",
      "Fashion": "1",
    "Accessory": "1",
  "Real Estate": "2"},

"Amasya" : {
   "Technology": "0",
      "Fashion": "1",
    "Accessory": "0",
  "Real Estate": "4"},

"Ankara" : {
   "Technology": "1",
      "Fashion": "1",
    "Accessory": "2",
  "Real Estate": "9"},

"Antalya" : {
   "Technology": "2",
      "Fashion": "1",
    "Accessory": "1",
  "Real Estate": "1"},

"Ardahan" : {
   "Technology": "1",
      "Fashion": "0",
    "Accessory": "2",
  "Real Estate": "6"},

"Artvin" : {
   "Technology": "0",
      "Fashion": "1",
    "Accessory": "0",
  "Real Estate": "2"},

"Aydın" : {
   "Technology": "1",
      "Fashion": "1",
    "Accessory": "3",
  "Real Estate": "3"},

"Balıkesir" : {
   "Technology": "0",
      "Fashion": "1",
    "Accessory": "1",
  "Real Estate": "6"},

"Bartın" : {
   "Technology": "1",
      "Fashion": "1",
    "Accessory": "1",
  "Real Estate": "1"},

"Batman" : {
   "Technology": "2",
      "Fashion": "0",
    "Accessory": "1",
  "Real Estate": "3"},

"Bayburt" : {
   "Technology": "1",
      "Fashion": "0",
    "Accessory": "2",
  "Real Estate": "6"},

"Bilecik" : {
   "Technology": "1",
      "Fashion": "1",
    "Accessory": "2",
  "Real Estate": "4"},

"Bingöl" : {
   "Technology": "0",
      "Fashion": "3",
    "Accessory": "4",
  "Real Estate": "5"},

"Bitlis" : {
   "Technology": "1",
      "Fashion": "4",
    "Accessory": "3",
  "Real Estate": "3"},

"Bolu" : {
   "Technology": "1",
      "Fashion": "8",
    "Accessory": "2",
  "Real Estate": "1"},

"Burdur" : {
   "Technology": "1",
      "Fashion": "1",
    "Accessory": "1",
  "Real Estate": "2"},

"Bursa" : {
   "Technology": "0",
      "Fashion": "1",
    "Accessory": "0",
  "Real Estate": "4"},

"Çanakkale" : {
   "Technology": "1",
      "Fashion": "1",
    "Accessory": "2",
  "Real Estate": "9"},

"Çankırı" : {
   "Technology": "2",
      "Fashion": "1",
    "Accessory": "1",
  "Real Estate": "1"},

"Çorum" : {
   "Technology": "1",
      "Fashion": "0",
    "Accessory": "2",
  "Real Estate": "6"},

"Denizli" : {
   "Technology": "0",
      "Fashion": "1",
    "Accessory": "0",
  "Real Estate": "2"},

"Diyarbakır" : {
   "Technology": "1",
      "Fashion": "1",
    "Accessory": "3",
  "Real Estate": "3"},

"Düzce" : {
   "Technology": "0",
      "Fashion": "1",
    "Accessory": "1",
  "Real Estate": "6"},

"Edirne" : {
   "Technology": "1",
      "Fashion": "1",
    "Accessory": "1",
  "Real Estate": "1"},

"Elazığ" : {
   "Technology": "2",
      "Fashion": "0",
    "Accessory": "1",
  "Real Estate": "3"},

"Erzincan" : {
   "Technology": "1",
      "Fashion": "1",
    "Accessory": "2",
  "Real Estate": "4"},

"Erzurum" : {
   "Technology": "0",
      "Fashion": "3",
    "Accessory": "4",
  "Real Estate": "5"},

"Eskişehir" : {
   "Technology": "1",
      "Fashion": "4",
    "Accessory": "3",
  "Real Estate": "3"},

"Gaziantep" : {
   "Technology": "1",
      "Fashion": "8",
    "Accessory": "2",
  "Real Estate": "1"},

"Giresun" : {
   "Technology": "1",
      "Fashion": "1",
    "Accessory": "1",
  "Real Estate": "2"},

"Gümüşhane" : {
   "Technology": "0",
      "Fashion": "1",
    "Accessory": "0",
  "Real Estate": "4"},

"Hakkari" : {
   "Technology": "1",
      "Fashion": "1",
    "Accessory": "2",
  "Real Estate": "9"},

"Hatay" : {
   "Technology": "2",
      "Fashion": "1",
    "Accessory": "1",
  "Real Estate": "1"},

"Igdır" : {
   "Technology": "1",
      "Fashion": "0",
    "Accessory": "2",
  "Real Estate": "6"},

"Isparta" : {
   "Technology": "0",
      "Fashion": "1",
    "Accessory": "0",
  "Real Estate": "2"},

"İstanbul" : {
   "Technology": "12"},

"İzmir" : {
   "Technology": "0",
      "Fashion": "1",
    "Accessory": "1",
  "Real Estate": "6"},

"Kahramanmaraş" : {
   "Technology": "1",
      "Fashion": "1",
    "Accessory": "1",
  "Real Estate": "1"},

"Karabük" : {
   "Technology": "2",
      "Fashion": "0",
    "Accessory": "1",
  "Real Estate": "3"},

"Karaman" : {
   "Technology": "1",
      "Fashion": "1",
    "Accessory": "2",
  "Real Estate": "4"},

"Kars" : {
   "Technology": "0",
      "Fashion": "3",
    "Accessory": "4",
  "Real Estate": "5"},

"Kastamonu" : {
   "Technology": "1",
      "Fashion": "4",
    "Accessory": "3",
  "Real Estate": "3"},

"Kayseri" : {
   "Technology": "1",
      "Fashion": "8",
    "Accessory": "2",
  "Real Estate": "1"},

"Kırıkkale" : {
   "Technology": "1",
      "Fashion": "1",
    "Accessory": "1",
  "Real Estate": "2"},

"Kırklareli" : {
   "Technology": "1",
      "Fashion": "1",
    "Accessory": "1",
  "Real Estate": "2"},

"Kırşehir" : {
   "Technology": "0",
      "Fashion": "1",
    "Accessory": "0",
  "Real Estate": "4"},

"Kilis" : {
   "Technology": "1",
      "Fashion": "1",
    "Accessory": "2",
  "Real Estate": "9"},

"Kocaeli" : {
   "Technology": "2",
      "Fashion": "1",
    "Accessory": "1",
  "Real Estate": "1"},

"Konya" : {
   "Technology": "1",
      "Fashion": "0",
    "Accessory": "2",
  "Real Estate": "6"},

"Kütahya" : {
   "Technology": "0",
      "Fashion": "1",
    "Accessory": "0",
  "Real Estate": "2"},

"Malatya" : {
   "Technology": "1",
      "Fashion": "1",
    "Accessory": "3",
  "Real Estate": "3"},

"Manisa" : {
   "Technology": "0",
      "Fashion": "1",
    "Accessory": "1",
  "Real Estate": "6"},

"Mardin" : {
   "Technology": "1",
      "Fashion": "1",
    "Accessory": "1",
  "Real Estate": "1"},

"Mersin" : {
   "Technology": "2",
      "Fashion": "0",
    "Accessory": "1",
  "Real Estate": "3"},

"Mugla" : {
   "Technology": "1",
      "Fashion": "1",
    "Accessory": "2",
  "Real Estate": "4"},

"Muş" : {
   "Technology": "0",
      "Fashion": "3",
    "Accessory": "4",
  "Real Estate": "5"},

"Nevşehir" : {
   "Technology": "1",
      "Fashion": "4",
    "Accessory": "3",
  "Real Estate": "3"},

"Niğde" : {
   "Technology": "1",
      "Fashion": "8",
    "Accessory": "2",
  "Real Estate": "1"},

"Ordu" : {
   "Technology": "1",
      "Fashion": "1",
    "Accessory": "1",
  "Real Estate": "2"},

"Osmaniye" : {
   "Technology": "0",
      "Fashion": "1",
    "Accessory": "0",
  "Real Estate": "4"},

"Rize" : {
   "Technology": "1",
      "Fashion": "1",
    "Accessory": "2",
  "Real Estate": "9"},

"Sakarya" : {
   "Technology": "2",
      "Fashion": "1",
    "Accessory": "1",
  "Real Estate": "1"},

"Samsun" : {
   "Technology": "1",
      "Fashion": "0",
    "Accessory": "2",
  "Real Estate": "6"},

"Siirt" : {
   "Technology": "0",
      "Fashion": "1",
    "Accessory": "0",
  "Real Estate": "2"},

"Sinop" : {
   "Technology": "1",
      "Fashion": "1",
    "Accessory": "3",
  "Real Estate": "3"},

"Sivas" : {
   "Technology": "0",
      "Fashion": "1",
    "Accessory": "1",
  "Real Estate": "6"},

"Şanlıurfa" : {
   "Technology": "1",
      "Fashion": "1",
    "Accessory": "1",
  "Real Estate": "1"},

"Şırnak" : {
   "Technology": "2",
      "Fashion": "0",
    "Accessory": "1",
  "Real Estate": "3"},

"Tekirdağ" : {
   "Technology": "1",
      "Fashion": "1",
    "Accessory": "2",
  "Real Estate": "4"},

"Tokat" : {
   "Technology": "0",
      "Fashion": "3",
    "Accessory": "4",
  "Real Estate": "5"},

"Trabzon" : {
   "Technology": "1",
      "Fashion": "4",
    "Accessory": "3",
  "Real Estate": "3"},

"Tunceli" : {
   "Technology": "1",
      "Fashion": "8",
    "Accessory": "2",
  "Real Estate": "1"},

"Uşak" : {
   "Technology": "1",
      "Fashion": "1",
    "Accessory": "1",
  "Real Estate": "2"},

"Van" : {
   "Technology": "0",
      "Fashion": "1",
    "Accessory": "0",
  "Real Estate": "4"},

"Yalova" : {
   "Technology": "1",
      "Fashion": "1",
    "Accessory": "2",
  "Real Estate": "9"},

"Yozgat" : {
   "Technology": "2",
      "Fashion": "1",
    "Accessory": "1",
  "Real Estate": "1"},

"Zonguldak" : {
   "Technology": "1",
      "Fashion": "0",
    "Accessory": "2",
  "Real Estate": "6"}
}

def gonder():
    secilen_sehir = acilir.get()
    secilen_kategoriler = [index for index, value in enumerate(var) if value.get() == 1]

    hata_mesaji.set("")
    if secilen_sehir in iller:
        il_verileri = iller[secilen_sehir]
        secilen_kategoriler_isim = [kategori for kategori in kategori_isimleri if
                                     kategori in il_verileri and kategori_isimleri.index(kategori) in secilen_kategoriler]

        if secilen_kategoriler_isim:
            veri_frame = Frame(bg, bg="#DB9C1A")
            veri_frame.place(relx=0, rely=0.515, relwidth=1, relheight=0.218)

            metin = f"{secilen_sehir}:\n"
            metin += ' '.join([f"{kategori}: {il_verileri[kategori]}\n" for kategori in secilen_kategoriler_isim])

            etiket = Label(veri_frame, text=metin, font="Gilroy-bold 16 bold", fg="black", bg="#DB9C1A")
            etiket.pack(padx=10, pady=10)
        else:
            hata_mesaji.set("Invalid category selection.")
    else:
        hata_mesaji.set("Invalid city selection.")

master = Tk()

canvas = Canvas(master, height=750, width=450)
canvas.pack()

bg= Frame(master, bg="#111111")
bg.place(relx=0,rely=0,relwidth=1,relheight=1)

ust= Frame(master, bg="#DB5F1A")
ust.place(relx=0,rely=0,relwidth=1,relheight=0.1)

s_yazi= Label(ust,bg="#DB5F1A",text="Filtering Project Example",font="Gilroy-bold 24 bold", pady=20)
s_yazi.pack()

acilir_bg= Frame(master, bg="#DB9C1A")
acilir_bg.place(relx=0,rely=0.101,relwidth=1,relheight=0.05)

sehirsec_yazi= Label(acilir_bg,bg="#DB9C1A",text="Select City:",font="Gilroy-bold 20 bold", fg="black")
sehirsec_yazi.pack(side= LEFT)

acilir= StringVar(acilir_bg)
acilir.set("\t")

acilir_menu=OptionMenu(
    acilir_bg,
    acilir,
    "Adana",
    "Adıyaman",
    "Afyonkarahisar",
    "Ağrı",
    "Aksaray",
    "Amasya",
    "Ankara",
    "Antalya",
    "Ardahan",
    "Artvin",
    "Aydın",
    "Bartın",
    "Batman",
    "Bayburt",
    "Bilecik",
    "Bingöl",
    "Bitlis",
    "Bolu",
    "Burdur",
    "Bursa",
    "Çanakkale",
    "Çankırı",
    "Çorum",
    "Denizli",
    "Diyarbakır",
    "Düzce",
    "Edirne",
    "Elazığ",
    "Erzincan",
    "Erzurum",
    "Eskişehir",
    "Gaziantep",
    "Giresun",
    "Gümüşhane",
    "Hakkâri",
    "Hatay",
    "Iğdır",
    "Isparta",
    "İstanbul",
    "İzmir",
    "Kahramanmaraş",
    "Karabük",
    "Karaman",
    "Kars",
    "Kastamonu",
    "Kayseri",
    "Kırıkkale",
    "Kırklareli",
    "Kırşehir",
    "Kilis",
    "Kocaeli",
    "Konya",
    "Kütahya",
    "Malatya",
    "Manisa",
    "Mardin",
    "Mersin",
    "Muğla",
    "Muş",
    "Nevşehir",
    "Niğde",
    "Ordu",
    "Osmaniye",
    "Rize",
    "Sakarya",
    "Samsun",
    "Siirt",
    "Sinop",
    "Sivas",
    "Şanlıurfa",
    "Şırnak",
    "Tekirdağ",
    "Tokat",
    "Trabzon",
    "Tunceli",
    "Uşak",
    "Van",
    "Yalova",
    "Yozgat",
    "Zonguldak",
    "Gebze"
)
acilir_menu.pack(padx=10, pady=10, side=LEFT)


radio_bg= Frame(master, bg="#DB9C1A")
radio_bg.place(relx=0,rely=0.152,relwidth=1,relheight=0.3)

radio_yazi=Label(radio_bg,bg="#DB9C1A",text="Select category:",font="Gilroy-bold 20 bold", fg="black")
radio_yazi.pack(anchor=NW)

var = [IntVar() for _ in range(4)]

check_buttons = []
kategori_isimleri = ["Technology", "Fashion", "Accessory", "Real Estate"]
for index, kategori in enumerate(kategori_isimleri):
    check_button = Checkbutton(radio_bg, text=kategori, variable=var[index], bg="#DB9C1A", font="Gilroy-bold 16 bold",
                               fg="black")
    check_button.pack(anchor=NW, pady=5, padx=15)
    check_buttons.append(check_button)

btn = Button(bg, text="Getir", font="Gilroy-bold 16 bold", command=gonder)
btn.place(rely=0.453, relwidth=1)

hata_mesaji = StringVar()
hata_etiket = Label(bg, textvariable=hata_mesaji, font="Gilroy-bold 16 bold", fg="white", bg="#111111")
hata_etiket.place(rely=0.75, relwidth=1)

master.mainloop()
