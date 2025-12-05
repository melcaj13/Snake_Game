import pygame
import sys
import random

# --- AYARLAR ---
GENISLIK, YUKSEKLIK = 1500, 800
KARE_BOYUTU = 30 
FPS = 10 # Hızı buradan ayarlayabilirsin

# Renkler
SIYAH = (0, 0, 0)
YESIL = (0, 255, 0)
KIRMIZI = (255, 0, 0)

# Yönler
YUKARI = (0, -1)
ASAGI = (0, 1)
SOL = (-1, 0)
SAG = (1, 0)

def yem_olustur(yilan_vucudu):
    """Yılanın üstüne gelmeyecek rastgele bir koordinat üretir."""
    while True:
        # Ekran sınırları içinde rastgele x, y seç (0-19 arası kareler)
        x = random.randint(0, (GENISLIK // KARE_BOYUTU) - 1) * KARE_BOYUTU
        y = random.randint(0, (YUKSEKLIK // KARE_BOYUTU) - 1) * KARE_BOYUTU
        
        # Eğer üretilen yer yılanın üstünde değilse onayla
        if (x, y) not in yilan_vucudu:
            return (x, y)

def main():
    pygame.init()
    ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
    pygame.display.set_caption("Otonom Yılan - Adım 3: Tam Oyun")
    saat = pygame.time.Clock()

    # Başlangıç Durumu
    yilan = [(300, 300), (300 + KARE_BOYUTU, 300), (300 + 2*KARE_BOYUTU, 300)]
    yon = YUKARI 
    yem = yem_olustur(yilan) # İlk yemi koy
    puan = 0

    while True:
        # 1. Olayları Dinle
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and yon != ASAGI: yon = YUKARI
                elif event.key == pygame.K_DOWN and yon != YUKARI: yon = ASAGI
                elif event.key == pygame.K_LEFT and yon != SAG: yon = SOL
                elif event.key == pygame.K_RIGHT and yon != SOL: yon = SAG

        # 2. Hareket Hesapla
        bas_x, bas_y = yilan[0]
        degisim_x, degisim_y = yon
        yeni_bas = (bas_x + (degisim_x * KARE_BOYUTU), bas_y + (degisim_y * KARE_BOYUTU))

        # --- ÇARPIŞMA KONTROLÜ (GAME OVER) ---
        # Duvara çarptı mı?
        if yeni_bas[0] < 0 or yeni_bas[0] >= GENISLIK or yeni_bas[1] < 0 or yeni_bas[1] >= YUKSEKLIK:
            print(f"Oyun Bitti! Duvara çarptın. Puan: {puan}")
            pygame.quit(); sys.exit()
        
        # Kendine çarptı mı? (Yeni baş, vücudun geri kalanında var mı?)
        if yeni_bas in yilan:
            print(f"Oyun Bitti! Kuyruğunu ısırdın. Puan: {puan}")
            pygame.quit(); sys.exit()

        # Yılanı İlerlet
        yilan.insert(0, yeni_bas)

        # --- YEM KONTROLÜ ---
        if yeni_bas == yem:
            puan += 1
            yem = yem_olustur(yilan) # Yeni yem koy
            # Not: pop() yapmıyoruz, böylece yılan uzuyor!
        else:
            yilan.pop() # Yem yemediysen kuyruğu sil (hareket illüzyonu)

        # 3. Çizim
        ekran.fill(SIYAH)
        
        # Yemi çiz
        pygame.draw.rect(ekran, KIRMIZI, pygame.Rect(yem[0], yem[1], KARE_BOYUTU, KARE_BOYUTU))
        
        # Yılanı çiz
        for parca in yilan:
            pygame.draw.rect(ekran, YESIL, pygame.Rect(parca[0], parca[1], KARE_BOYUTU, KARE_BOYUTU))
        
        pygame.display.flip()
        saat.tick(FPS)

if __name__ == "__main__":
    main()