from tkinter import *
iller = {
"Adana" : {
    "Teknoloji": "3",
         "Moda": "2",
     "Aksesuar": "1",
        "Emlak": "4"},

"Adıyaman" : {
    "Teknoloji": "0",
         "Moda": "3",
     "Aksesuar": "4",
        "Emlak": "5"},

"Afyonkarahisar" : {
    "Teknoloji": "1",
         "Moda": "4",
     "Aksesuar": "3",
        "Emlak": "3"},

"Ağrı" : {
    "Teknoloji": "1",
         "Moda": "8",
     "Aksesuar": "2",
        "Emlak": "1"},

"Aksaray" : {
    "Teknoloji": "1",
         "Moda": "1",
     "Aksesuar": "1",
        "Emlak": "2"},

"Amasya" : {
    "Teknoloji": "0",
         "Moda": "1",
     "Aksesuar": "0",
        "Emlak": "4"},

"Ankara" : {
    "Teknoloji": "1",
         "Moda": "1",
     "Aksesuar": "2",
        "Emlak": "9"},

"Antalya" : {
    "Teknoloji": "2",
         "Moda": "1",
     "Aksesuar": "1",
        "Emlak": "1"},

"Ardahan" : {
    "Teknoloji": "1",
         "Moda": "0",
     "Aksesuar": "2",
        "Emlak": "6"},

"Artvin" : {
    "Teknoloji": "0",
         "Moda": "1",
     "Aksesuar": "0",
        "Emlak": "2"},

"Aydın" : {
    "Teknoloji": "1",
         "Moda": "1",
     "Aksesuar": "3",
        "Emlak": "3"},

"Balıkesir" : {
    "Teknoloji": "0",
         "Moda": "1",
     "Aksesuar": "1",
        "Emlak": "6"},

"Bartın" : {
    "Teknoloji": "1",
         "Moda": "1",
     "Aksesuar": "1",
        "Emlak": "1"},

"Batman" : {
    "Teknoloji": "2",
         "Moda": "0",
     "Aksesuar": "1",
        "Emlak": "3"},

"Bayburt" : {
    "Teknoloji": "1",
         "Moda": "0",
     "Aksesuar": "2",
        "Emlak": "6"},

"Bilecik" : {
    "Teknoloji": "1",
         "Moda": "1",
     "Aksesuar": "2",
        "Emlak": "4"},

"Bingöl" : {
    "Teknoloji": "0",
         "Moda": "3",
     "Aksesuar": "4",
        "Emlak": "5"},

"Bitlis" : {
    "Teknoloji": "1",
         "Moda": "4",
     "Aksesuar": "3",
        "Emlak": "3"},

"Bolu" : {
    "Teknoloji": "1",
         "Moda": "8",
     "Aksesuar": "2",
        "Emlak": "1"},

"Burdur" : {
    "Teknoloji": "1",
         "Moda": "1",
     "Aksesuar": "1",
        "Emlak": "2"},

"Bursa" : {
    "Teknoloji": "0",
         "Moda": "1",
     "Aksesuar": "0",
        "Emlak": "4"},

"Çanakkale" : {
    "Teknoloji": "1",
         "Moda": "1",
     "Aksesuar": "2",
        "Emlak": "9"},

"Çankırı" : {
    "Teknoloji": "2",
         "Moda": "1",
     "Aksesuar": "1",
        "Emlak": "1"},

"Çorum" : {
    "Teknoloji": "1",
         "Moda": "0",
     "Aksesuar": "2",
        "Emlak": "6"},

"Denizli" : {
    "Teknoloji": "0",
         "Moda": "1",
     "Aksesuar": "0",
        "Emlak": "2"},

"Diyarbakır" : {
    "Teknoloji": "1",
         "Moda": "1",
     "Aksesuar": "3",
        "Emlak": "3"},

"Düzce" : {
    "Teknoloji": "0",
         "Moda": "1",
     "Aksesuar": "1",
        "Emlak": "6"},

"Edirne" : {
    "Teknoloji": "1",
         "Moda": "1",
     "Aksesuar": "1",
        "Emlak": "1"},

"Elazığ" : {
    "Teknoloji": "2",
         "Moda": "0",
     "Aksesuar": "1",
        "Emlak": "3"},

"Erzincan" : {
    "Teknoloji": "1",
         "Moda": "1",
     "Aksesuar": "2",
        "Emlak": "4"},

"Erzurum" : {
    "Teknoloji": "0",
         "Moda": "3",
     "Aksesuar": "4",
        "Emlak": "5"},

"Eskişehir" : {
    "Teknoloji": "1",
         "Moda": "4",
     "Aksesuar": "3",
        "Emlak": "3"},

"Gaziantep" : {
    "Teknoloji": "1",
         "Moda": "8",
     "Aksesuar": "2",
        "Emlak": "1"},

"Giresun" : {
    "Teknoloji": "1",
         "Moda": "1",
     "Aksesuar": "1",
        "Emlak": "2"},

"Gümüşhane" : {
    "Teknoloji": "0",
         "Moda": "1",
     "Aksesuar": "0",
        "Emlak": "4"},

"Hakkari" : {
    "Teknoloji": "1",
         "Moda": "1",
     "Aksesuar": "2",
        "Emlak": "9"},

"Hatay" : {
    "Teknoloji": "2",
         "Moda": "1",
     "Aksesuar": "1",
        "Emlak": "1"},

"Igdır" : {
    "Teknoloji": "1",
         "Moda": "0",
     "Aksesuar": "2",
        "Emlak": "6"},

"Isparta" : {
    "Teknoloji": "0",
         "Moda": "1",
     "Aksesuar": "0",
        "Emlak": "2"},

"İstanbul" : {
    "Teknoloji": "12"},

"İzmir" : {
    "Teknoloji": "0",
         "Moda": "1",
     "Aksesuar": "1",
        "Emlak": "6"},

"Kahramanmaraş" : {
    "Teknoloji": "1",
         "Moda": "1",
     "Aksesuar": "1",
        "Emlak": "1"},

"Karabük" : {
    "Teknoloji": "2",
         "Moda": "0",
     "Aksesuar": "1",
        "Emlak": "3"},

"Karaman" : {
    "Teknoloji": "1",
         "Moda": "1",
     "Aksesuar": "2",
        "Emlak": "4"},

"Kars" : {
    "Teknoloji": "0",
         "Moda": "3",
     "Aksesuar": "4",
        "Emlak": "5"},

"Kastamonu" : {
    "Teknoloji": "1",
         "Moda": "4",
     "Aksesuar": "3",
        "Emlak": "3"},

"Kayseri" : {
    "Teknoloji": "1",
         "Moda": "8",
     "Aksesuar": "2",
        "Emlak": "1"},

"Kırıkkale" : {
    "Teknoloji": "1",
         "Moda": "1",
     "Aksesuar": "1",
        "Emlak": "2"},

"Kırklareli" : {
    "Teknoloji": "1",
         "Moda": "1",
     "Aksesuar": "1",
        "Emlak": "2"},

"Kırşehir" : {
    "Teknoloji": "0",
         "Moda": "1",
     "Aksesuar": "0",
        "Emlak": "4"},

"Kilis" : {
    "Teknoloji": "1",
         "Moda": "1",
     "Aksesuar": "2",
        "Emlak": "9"},

"Kocaeli" : {
    "Teknoloji": "2",
         "Moda": "1",
     "Aksesuar": "1",
        "Emlak": "1"},

"Konya" : {
    "Teknoloji": "1",
         "Moda": "0",
     "Aksesuar": "2",
        "Emlak": "6"},

"Kütahya" : {
    "Teknoloji": "0",
         "Moda": "1",
     "Aksesuar": "0",
        "Emlak": "2"},

"Malatya" : {
    "Teknoloji": "1",
         "Moda": "1",
     "Aksesuar": "3",
        "Emlak": "3"},

"Manisa" : {
    "Teknoloji": "0",
         "Moda": "1",
     "Aksesuar": "1",
        "Emlak": "6"},

"Mardin" : {
    "Teknoloji": "1",
         "Moda": "1",
     "Aksesuar": "1",
        "Emlak": "1"},

"Mersin" : {
    "Teknoloji": "2",
         "Moda": "0",
     "Aksesuar": "1",
        "Emlak": "3"},

"Mugla" : {
    "Teknoloji": "1",
         "Moda": "1",
     "Aksesuar": "2",
        "Emlak": "4"},

"Muş" : {
    "Teknoloji": "0",
         "Moda": "3",
     "Aksesuar": "4",
        "Emlak": "5"},

"Nevşehir" : {
    "Teknoloji": "1",
         "Moda": "4",
     "Aksesuar": "3",
        "Emlak": "3"},

"Niğde" : {
    "Teknoloji": "1",
         "Moda": "8",
     "Aksesuar": "2",
        "Emlak": "1"},

"Ordu" : {
    "Teknoloji": "1",
         "Moda": "1",
     "Aksesuar": "1",
        "Emlak": "2"},

"Osmaniye" : {
    "Teknoloji": "0",
         "Moda": "1",
     "Aksesuar": "0",
        "Emlak": "4"},

"Rize" : {
    "Teknoloji": "1",
         "Moda": "1",
     "Aksesuar": "2",
        "Emlak": "9"},

"Sakarya" : {
    "Teknoloji": "2",
         "Moda": "1",
     "Aksesuar": "1",
        "Emlak": "1"},

"Samsun" : {
    "Teknoloji": "1",
         "Moda": "0",
     "Aksesuar": "2",
        "Emlak": "6"},

"Siirt" : {
    "Teknoloji": "0",
         "Moda": "1",
     "Aksesuar": "0",
        "Emlak": "2"},

"Sinop" : {
    "Teknoloji": "1",
         "Moda": "1",
     "Aksesuar": "3",
        "Emlak": "3"},

"Sivas" : {
    "Teknoloji": "0",
         "Moda": "1",
     "Aksesuar": "1",
        "Emlak": "6"},

"Şanlıurfa" : {
    "Teknoloji": "1",
         "Moda": "1",
     "Aksesuar": "1",
        "Emlak": "1"},

"Şırnak" : {
    "Teknoloji": "2",
         "Moda": "0",
     "Aksesuar": "1",
        "Emlak": "3"},

"Tekirdağ" : {
    "Teknoloji": "1",
         "Moda": "1",
     "Aksesuar": "2",
        "Emlak": "4"},

"Tokat" : {
    "Teknoloji": "0",
         "Moda": "3",
     "Aksesuar": "4",
        "Emlak": "5"},

"Trabzon" : {
    "Teknoloji": "1",
         "Moda": "4",
     "Aksesuar": "3",
        "Emlak": "3"},

"Tunceli" : {
    "Teknoloji": "1",
         "Moda": "8",
     "Aksesuar": "2",
        "Emlak": "1"},

"Uşak" : {
    "Teknoloji": "1",
         "Moda": "1",
     "Aksesuar": "1",
        "Emlak": "2"},

"Van" : {
    "Teknoloji": "0",
         "Moda": "1",
     "Aksesuar": "0",
        "Emlak": "4"},

"Yalova" : {
    "Teknoloji": "1",
         "Moda": "1",
     "Aksesuar": "2",
        "Emlak": "9"},

"Yozgat" : {
    "Teknoloji": "2",
         "Moda": "1",
     "Aksesuar": "1",
        "Emlak": "1"},

"Zonguldak" : {
    "Teknoloji": "1",
         "Moda": "0",
     "Aksesuar": "2",
        "Emlak": "6"}
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

            metin = f"{secilen_sehir} \nAdetler: "
            metin += ' '.join([f"{kategori}: {il_verileri[kategori]}\n" for kategori in secilen_kategoriler_isim])

            etiket = Label(veri_frame, text=metin, font="Gilroy-bold 16 bold", fg="black", bg="#DB9C1A")
            etiket.pack(padx=10, pady=10)
        else:
            hata_mesaji.set("Geçersiz kategori seçimi.")
    else:
        hata_mesaji.set("Geçersiz şehir seçimi.")

master = Tk()

canvas = Canvas(master, height=750, width=450)
canvas.pack()

bg= Frame(master, bg="#111111")
bg.place(relx=0,rely=0,relwidth=1,relheight=1)

ust= Frame(master, bg="#DB5F1A")
ust.place(relx=0,rely=0,relwidth=1,relheight=0.1)

s_yazi= Label(ust,bg="#DB5F1A",text="Filtreleme Örnek Proje",font="Gilroy-bold 24 bold", pady=20)
s_yazi.pack()

acilir_bg= Frame(master, bg="#DB9C1A")
acilir_bg.place(relx=0,rely=0.101,relwidth=1,relheight=0.05)

sehirsec_yazi= Label(acilir_bg,bg="#DB9C1A",text="Şehir seç :",font="Gilroy-bold 20 bold", fg="black")
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

radio_yazi=Label(radio_bg,bg="#DB9C1A",text="Kategori seç:",font="Gilroy-bold 20 bold", fg="black")
radio_yazi.pack(anchor=NW)

var = [IntVar() for _ in range(4)]

check_buttons = []
kategori_isimleri = ["Teknoloji", "Moda", "Aksesuar", "Emlak"]
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