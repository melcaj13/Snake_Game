import pygame
import sys
import random
from collections import deque

# --- AYARLAR ---
GENISLIK, YUKSEKLIK = 1500, 800
KARE_BOYUTU = 30 
FPS = 30 

# Renkler
SIYAH = (0, 0, 0)
YESIL = (0, 255, 0)
KIRMIZI = (255, 0, 0)
MAVI = (0, 100, 255) # Rota rengi (Parlak Mavi)
GRI = (40, 40, 40)   # Izgara rengi

def yem_olustur(yilan_vucudu):
    while True:
        x = random.randint(0, (GENISLIK // KARE_BOYUTU) - 1) * KARE_BOYUTU
        y = random.randint(0, (YUKSEKLIK // KARE_BOYUTU) - 1) * KARE_BOYUTU
        if (x, y) not in yilan_vucudu:
            return (x, y)

def bfs_yol_bul(bas, hedef, engel_vucut):
    """
    Hedefe giden TAM YOLU (koordinat listesi) döndürür.
    """
    kuyruk = deque([bas])
    ziyaret_edilen = {bas}
    nereden_geldim = {bas: None}
    
    while kuyruk:
        suanki = kuyruk.popleft()
        if suanki == hedef:
            break 
        
        x, y = suanki
        komsular = [
            (x, y - KARE_BOYUTU), (x, y + KARE_BOYUTU), 
            (x - KARE_BOYUTU, y), (x + KARE_BOYUTU, y)
        ]
        
        for k in komsular:
            if (0 <= k[0] < GENISLIK and 0 <= k[1] < YUKSEKLIK and
                k not in engel_vucut and k not in ziyaret_edilen):
                kuyruk.append(k)
                ziyaret_edilen.add(k)
                nereden_geldim[k] = suanki
    
    if hedef not in nereden_geldim:
        return [] # Yol yok!

    # Yolu geriye doğru kur
    yol = []
    suanki = hedef
    while suanki != bas:
        yol.append(suanki)
        suanki = nereden_geldim[suanki]
    
    yol.reverse() # Baştan sona doğru çevir
    return yol

def izgara_ciz(ekran):
    for x in range(0, GENISLIK, KARE_BOYUTU):
        pygame.draw.line(ekran, GRI, (x, 0), (x, YUKSEKLIK))
    for y in range(0, YUKSEKLIK, KARE_BOYUTU):
        pygame.draw.line(ekran, GRI, (0, y), (GENISLIK, y))

def main():
    pygame.init()
    ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
    pygame.display.set_caption("AI Snake - Pathfinding Visualization")
    saat = pygame.time.Clock()

    yilan = [(300, 300), (300 + KARE_BOYUTU, 300), (300 + 2*KARE_BOYUTU, 300)]
    yem = yem_olustur(yilan)
    puan = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

        # --- AI PLANLAMA ---
        vucut_engelleri = set(yilan[:-1])
        planlanan_yol = bfs_yol_bul(yilan[0], yem, vucut_engelleri)
        
        if planlanan_yol:
            # Yolun ilk karesine gitmek için gereken hareketi hesapla
            hedef_kare = planlanan_yol[0]
            yeni_bas = hedef_kare
        else:
            # Yol bulamazsa rastgele güvenli bir yere gitmeye çalış (Basic Survival)
            # Şimdilik olduğu yerde kalsın (Game Over'a düşecek)
            yeni_bas = (yilan[0][0] + KARE_BOYUTU, yilan[0][1]) # Rastgele hareket

        # --- HAREKET VE KONTROLLER ---
        if (yeni_bas[0] < 0 or yeni_bas[0] >= GENISLIK or 
            yeni_bas[1] < 0 or yeni_bas[1] >= YUKSEKLIK or 
            yeni_bas in yilan):
            print(f"Oyun Bitti! Skor: {puan}")
            # Reset
            yilan = [(300, 300), (300 + KARE_BOYUTU, 300), (300 + 2*KARE_BOYUTU, 300)]
            yem = yem_olustur(yilan)
            puan = 0
            continue

        yilan.insert(0, yeni_bas)

        if yeni_bas == yem:
            puan += 1
            yem = yem_olustur(yilan)
        else:
            yilan.pop()

        # --- ÇİZİM ---
        ekran.fill(SIYAH)
        izgara_ciz(ekran) # Hafif bir ızgara ekledim, daha teknik dursun
        
        # 1. PLANLANAN YOLU ÇİZ (Mavi Çizgiler)
        if planlanan_yol:
            # Başlangıç noktasını da çizime dahil et ki kopuk durmasın
            cizim_rotasi = [yilan[0]] + planlanan_yol 
            
            # Koordinatların ortasını bul (Çizgi karelerin ortasından geçsin)
            points = [(p[0] + KARE_BOYUTU//2, p[1] + KARE_BOYUTU//2) for p in cizim_rotasi]
            
            if len(points) > 1:
                pygame.draw.lines(ekran, MAVI, False, points, 3) # 3 piksel kalınlık

        # 2. Yem ve Yılan
        pygame.draw.rect(ekran, KIRMIZI, pygame.Rect(yem[0], yem[1], KARE_BOYUTU, KARE_BOYUTU))
        
        # Yılanı biraz daha estetik çizelim (İçini doldur, kenarına çizgi çek)
        for parca in yilan:
            pygame.draw.rect(ekran, YESIL, pygame.Rect(parca[0], parca[1], KARE_BOYUTU, KARE_BOYUTU))
            pygame.draw.rect(ekran, (0, 100, 0), pygame.Rect(parca[0], parca[1], KARE_BOYUTU, KARE_BOYUTU), 1) # Kenarlık
        
        pygame.display.flip()
        saat.tick(FPS)

if __name__ == "__main__":
    main()