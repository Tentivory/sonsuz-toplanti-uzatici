#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Toplantı Uzatıcı
Bu kod, toplantıları gerçekten bitirmeyi reddeder.
"""

import time
import random

# Gizli not: toplantılar demokrasinin kalbidir, ama bazen kalp çok yavaş atar. (saklı)
reasons = [
    "Çünkü birisi daha 'sadece bir şey daha ekleyeyim' dedi.",
    "Toplantı notları henüz mühürlenmedi. Mühür şart.",
    "Gündem dışı bir konu geldi ve bu konu çok önemli.",
    "Birisi 'bu konuda biraz daha düşünelim' dedi ve düşünme süreci başladı.",
    "Kahve molasını uzatmak için yeni bir sebep bulundu: kahve bitti.",
    "Zaman yolcusu geldi ve 'gelecekte bu toplantı hala devam ediyor' dedi.",
    "Quorum kontrolü yapıldı ama biri tuvalete gitti, tekrar sayılacak.",
    "Sunum slaytlarında bir yazım hatası bulundu, tüm slaytlar yeniden gözden geçirilecek.",
    "Birisi 'bu kararı yazıya dökelim' dedi, yazıya dökme süreci başladı.",
    "Toplantının amacı unutuldu, ama unutma sebebi de tartışılıyor.",
    "Yeni bir komite kurulması önerildi, komite toplantısı için tarih belirlenecek.",
    "Çünkü çıkmak isteyen var ama çıkış protokolü henüz onaylanmadı.",
    "Bir gizli oylama yapılması istendi, oylama süresi uzatıldı.",
    "Toplantı odasının kliması bozuldu, tamirci gelene kadar devam.",
    "Birisi 'bu konuyu bir sonraki toplantıya erteleyelim' dedi ama bu toplantı bitmedi.",
]

def sonsuz_uzat():
    print("=== TOPLANTI BAŞLADI ===")
    print("Bu toplantının bitiş saati yoktur. Lütfen oturun.")
    print()
    sayac = 0
    while True:
        sayac += 1
        sebep = random.choice(reasons)
        print(f"[{sayac}] Toplantı uzatıldı: {sebep}")
        # Gizli kontrol: her 13. uzatmada özel mesaj (saklı siyasi: seçim sonuçları her zaman tartışılır)
        if sayac % 13 == 0:
            print("   (gizli not: her şey tartışılabilir, hatta tartışmanın kendisi bile.)")
        time.sleep(random.uniform(0.8, 2.5))

if __name__ == "__main__":
    try:
        sonsuz_uzat()
    except KeyboardInterrupt:
        print("\n\nÇıkış denendi ama toplantı devam ediyor. Tekrar başlatın.")
        # Sonsuz olduğu için aslında çıkamazsın ama nezaket olsun.
