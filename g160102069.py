with open("g160102069.txt", "w") as text_file:
    import random
    import sys
    import time
    print("DÖNEM SONU STOK DEGER VE DEVIR HIZI TESPITI", file=text_file)
    print("SUREKLI KONTROL SISTEMI VE FIFO YONTEMI", file=text_file)
    print("HAZIRLAYAN: g160102069 - Okancan ÖZDEMİR", file=text_file)
    print("Rassal degerlerin gerceklesme olasiliklari esit olarak kabul edilmistir.", file=text_file)

    m = int(input('simulasyon kac gun calistirilacak = '))
    print(f"simulasyon {m} gun calisacak.", file=text_file)
    n = 1
    x = bool
    x = True
    toplam_cikis_maliyeti = 0
    q = int(input('siparis miktari (q) = '))
    print(f"q = {q}", file=text_file)
    r = int(input('yeniden siparis noktasi (r) = '))
    print(f"r = {r}", file=text_file)
    if r >= q:
        print("r, q'dan buyuk olamaz. tekrar giriniz.", file=text_file)
        r = int(input('yeniden siparis noktasi (r) = '))
    stok_degeri = [None] * m
    eldeki_miktar = [None] * (m + 1)
    cikis_maliyeti = [None] * m
    eldeki_miktar[0] = q
    birim_fiyat = list()
    talep_gun = list()
    talep_miktari = list()
    print("baslangic stogu q kadar alinmistir.", file=text_file)
    birim_fiy_fre_say = int(input("birim fiyat icin kac farkli rassal deger kullanilacak = "))
    print("birim fiyat rassal degerlerini giriniz. ")
    bf = 1
    birim_fiyat_degerler = list()
    while (bf <= birim_fiy_fre_say):
        bfd = int(input(" siradaki rassal degeri giriniz = "))
        birim_fiyat_degerler.append(bfd)
        bf = bf + 1
    birim_fiyat.append(random.choice(birim_fiyat_degerler))
    print(f"atanan degere gore eldeki mallarin birim fiyati = {birim_fiyat[-1]}", file=text_file)
    talep_mik_fre_say = int(input("talep miktari icin kac farkli rassal deger kullanilacak = "))
    print("talep miktari rassal degerlerini giriniz.")
    tm = 1
    talep_miktar_degerler = list()
    while tm <= talep_mik_fre_say:
        tmd = int(input(" siradaki rassal degeri giriniz. = "))
        if tmd >= (2 * q):
            print("talep miktari 2*q'dan fazla olamaz. tekrar giriniz.")
            tmd = int(input(" siradaki rassal degeri giriniz = "))
            talep_miktar_degerler.append(tmd)
        else:
            talep_miktar_degerler.append(tmd)
        tm = tm + 1
    talep_miktari.append(random.choice(talep_miktar_degerler))
    print(f"atanan degere gore baslangicta talep miktari = {talep_miktari[-1]}", file=text_file)
    talep_dagilim_gun_fre_say = int(input("talepler arasi gun sayisi icin kac farkli rassal deger kullanilacak = "))
    print("talepler arasi gun sayisi rassal degerlerini giriniz.")
    td = 1
    talep_dagilim_degerler = list()
    while (td <= talep_dagilim_gun_fre_say):
        tdg = int(input(" siradaki rassal degeri giriniz = "))
        talep_dagilim_degerler.append(tdg)
        td = td + 1
    talep_gun.append(random.choice(talep_dagilim_degerler))
    print(f"atanan degere gore baslangic talebinin cikis gunu = {talep_gun[-1]}", file=text_file)
    tedarik_sur_fre_say = int(input("tedarik suresi gun sayisi icin kac farkli rassal deger kullanilacak = "))
    print("tedarik suresi gun sayisi rassal degerlerini giriniz.")
    ts = 1
    tedarik_suresi_degerler = list()
    while (ts <= tedarik_sur_fre_say):
        tsg = int(input(" siradaki rassal degeri giriniz = "))
        tedarik_suresi_degerler.append(tsg)
        ts = ts + 1
    stok_degeri = [None] * m
    cikis_maliyeti = [None] * m
    tedarik_suresi = [None] * 100
    a = 0
    print("veriler kaydedildi. simulasyon calistiriliyor.")
    time.sleep(5)

    while n <= m:
        if (tedarik_suresi[-1] == n) and (eldeki_miktar[a] <= 0):
            print(f"{n}.gun siparis girisi var.", file=text_file)
            eldeki_miktar[a] = q
            birim_fiyat.append(random.choice(birim_fiyat_degerler))
            print(f"atanan degere gore giren siparisin birim fiyati = {birim_fiyat[-1]}", file=text_file)
        elif (tedarik_suresi[-1] == n) and (eldeki_miktar[a] > 0):
            print(f"{n}.gun siparis girisi var.", file=text_file)
            birim_fiyat.append(random.choice(birim_fiyat_degerler))
            print(f"atanan degere gore giren siparisin birim fiyati = {birim_fiyat[-1]}", file=text_file)
            eldeki_miktar[a] = q + eldeki_miktar[a]

        if talep_gun[-1] == n:
            if (eldeki_miktar[a] - talep_miktari[-1]) <= 0 and (talep_miktari[-1] <= q):
                cikis_maliyeti[a] = eldeki_miktar[a] * birim_fiyat[-1]
                eldeki_miktar[a] = 0
                print(f"{n}. gun cikis maliyeti = {cikis_maliyeti[a]}", file=text_file)
            elif (eldeki_miktar[a] - talep_miktari[-1] <= 0) and (talep_miktari[-1] > q):
                if eldeki_miktar[a] <= q:
                    cikis_maliyeti[a] = eldeki_miktar[a] * birim_fiyat[-1]
                    eldeki_miktar[a] = 0
                    print(f"{n}. gun cikis maliyeti = {cikis_maliyeti[a]}", file=text_file)
                elif eldeki_miktar[a] > q:
                    cikis_maliyeti[a] = (q * birim_fiyat[-1]) + ((eldeki_miktar[a] - q) * birim_fiyat[-2])
                    eldeki_miktar[a] = 0
                    print(f"{n}. gun cikis maliyeti = {cikis_maliyeti[a]}", file=text_file)
            elif (eldeki_miktar[a] - talep_miktari[-1]) > 0 and (eldeki_miktar[a] <= q):
                cikis_maliyeti[a] = talep_miktari[-1] * birim_fiyat[-1]
                print(f"{n}. gun cikis maliyeti = {cikis_maliyeti[a]}", file=text_file)
                eldeki_miktar[a] = eldeki_miktar[a] - talep_miktari[-1]
            elif (eldeki_miktar[a] - talep_miktari[-1]) > 0 and (eldeki_miktar[a] > q):
                if talep_miktari[-1] < q:
                    cikis_maliyeti[a] = ((eldeki_miktar[a] - q) * birim_fiyat[-2]) + (
                                (talep_miktari[-1] - (eldeki_miktar[a] - q)) * birim_fiyat[-1])
                    print(f"{n}. gun cikis maliyeti = {cikis_maliyeti[a]}", file=text_file)
                    eldeki_miktar[a] = eldeki_miktar[a] - talep_miktari[-1]
                elif talep_miktari[-1] > q:
                    cikis_maliyeti[a] = (q * birim_fiyat[-1]) + ((eldeki_miktar[a] - q) * birim_fiyat[-2])
                    print(f"{n}. gun cikis maliyeti = {cikis_maliyeti[a]}", file=text_file)
                    eldeki_miktar[a] = eldeki_miktar[a] - talep_miktari[-1]
            toplam_cikis_maliyeti = toplam_cikis_maliyeti + cikis_maliyeti[a]
            talep_miktari.append(random.choice(talep_miktar_degerler))
            print(f"atanan degere gore yeni talep miktari = {talep_miktari[-1]}", file=text_file)
            talep_gun.append(random.choice(talep_dagilim_degerler))
            talep_gun[-1] = talep_gun[-1] + talep_gun[-2]
            print(f"atanan degere gore yeni talebin cikis gunu = {talep_gun[-1]}", file=text_file)

        if (eldeki_miktar[a] <= r) and (x == True):
            print('yeni siparis aciliyor.', file=text_file)
            tedarik_suresi[-1] = n
            tedarik_suresi.append(random.choice(tedarik_suresi_degerler))
            tedarik_suresi[-1] = tedarik_suresi[-1] + tedarik_suresi[-2]
            print(f'atanan degere gore yeni siparisin giris gunu = {tedarik_suresi[-1]}', file=text_file)
            x = False
        elif (eldeki_miktar[a] <= r) and (tedarik_suresi[-1] == n):
            print('yeni siparis aciliyor.', file=text_file)
            tedarik_suresi.append(random.choice(tedarik_suresi_degerler))
            tedarik_suresi[-1] = tedarik_suresi[-1] + tedarik_suresi[-2]
            print(f'atanan degere gore yeni siparisin giris gunu = {tedarik_suresi[-1]}', file=text_file)
        elif (eldeki_miktar[a] <= r) and (tedarik_suresi[-1] < n):
            print('yeni siparis aciliyor.', file=text_file)
            tedarik_suresi.append(random.choice(tedarik_suresi_degerler))
            tedarik_suresi[-1] = tedarik_suresi[-1] + tedarik_suresi[-2]
            print(f'atanan degere gore yeni siparisin giris gunu = {tedarik_suresi[-1]}', file=text_file)

        if eldeki_miktar[a] <= q:
            stok_degeri[a] = (eldeki_miktar[a] * birim_fiyat[-1])
            print(f"{n}. gun eldeki miktar(hepsinin birim fiyati sabit) = {eldeki_miktar[a]}", file=text_file)
            print(f"eldeki partinin birim fiyati = {birim_fiyat[-1]}", file=text_file)
            print(f"{n}. gun stok degeri = {stok_degeri[a]}", file= text_file)
        elif eldeki_miktar[a] > q:
            stok_degeri[a] = (q * birim_fiyat[-1]) + ((eldeki_miktar[a] - q) * birim_fiyat[-2])
            print(f"{n}. gun eldeki miktar(birim fiyatlar farkli) = {eldeki_miktar[a]}", file=text_file)
            print(f"yeni partinin miktari ve birim fiyati = {q}, {birim_fiyat[-1]}", file=text_file)
            print(f"eski partinin miktari ve birim fiyati = {(eldeki_miktar[a] - q)}, {birim_fiyat[-2]}", file=text_file)
            print(f"{n}. gun stok degeri = {stok_degeri[a]}", file=text_file)
        eldeki_miktar[a + 1] = eldeki_miktar[a]
        a = a + 1
        n = n + 1

    print(f"{m}. gun yani donem sonu stok degeri = {stok_degeri[-1]} tl", file=text_file)
    if (m % 2) == 0:
        print(f"ilk gun stok degeri = {stok_degeri[0]} tl", file=text_file)
        print(f"donem ortasi stok degeri =  {stok_degeri[(m // 2) - 1]} tl", file=text_file)
        print(f"donem sonu stok degeri = {stok_degeri[-1]} tl", file=text_file)
        ortalama_stok_tutari = ((stok_degeri[0] + stok_degeri[(m // 2) - 1] + stok_degeri[-1]) / 3)
        print(f"ortalama stok tutari = {ortalama_stok_tutari} tl", file=text_file)
        print(f"toplam cikis maliyeti = {toplam_cikis_maliyeti} tl", file=text_file)
        stok_devir_hizi = toplam_cikis_maliyeti / ortalama_stok_tutari
        print(f"stok devir hizi = {stok_devir_hizi}", file=text_file)
    else:
        print(f"ilk gun stok degeri = {stok_degeri[0]} tl", file=text_file)
        print(f"donem ortasi stok degeri =  {stok_degeri[(m // 2)]} tl", file=text_file)
        print(f"donem sonu stok degeri = {stok_degeri[-1]} tl", file=text_file)
        ortalama_stok_tutari = ((stok_degeri[0] + stok_degeri[(m // 2)] + stok_degeri[-1]) / 3)
        print(f"ortalama stok tutari = {ortalama_stok_tutari} tl", file=text_file)
        print(f"toplam cikis maliyeti = {toplam_cikis_maliyeti} tl", file=text_file)
        stok_devir_hizi = toplam_cikis_maliyeti / ortalama_stok_tutari
        print(f"stok devir hizi = {stok_devir_hizi}", file=text_file)
    print("simulasyon tamamlandi. sonuclar g160102069.txt dosyasindan incelenebilir. program kapatiliyor.")
    time.sleep(5)
    sys.exit
