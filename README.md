# Snake_Game

# 🐍 AI Snake: Otonom Yol Bulma ve Oyun Geliştirme

Bu proje, Oyun Geliştirme ve Yapay Zeka'nın kesişim noktasını keşfetmek amacıyla geliştirilmiştir. Python (Pygame) ile oluşturulmuş klasik Yılan oyununu temel alır ve **Genişlik Öncelikli Arama (BFS)** algoritmasını kullanarak yeme giden en kısa yolu bulan otonom bir ajan içerir.

## 📺 Demo: İnsan vs. Yapay Zeka

Aşağıda manuel oynanış ile otonom yapay zeka ajanının karşılaştırmasını görebilirsiniz.

| **Mod 1: Manuel Oynanış** (İnsan) | **Mod 2: Otonom Yapay Zeka** (BFS Algoritması) |
| :---: | :---: |
| *(https://github.com/user-attachments/assets/39d71157-dba5-4ea6-9253-8dfcb10857d6)* | *(https://github.com/user-attachments/assets/702d8ac3-8e78-4076-baa4-294587c6b159)* |
| *Klavye ile kontrol edilir.* | *En uygun yolu otomatik olarak hesaplar.* |

## 🚀 Özellikler

* **Genişlik Öncelikli Arama (BFS):** Yapay zeka, yılanın başından yeme giden en kısa yolu gerçek zamanlı olarak hesaplar.
* **Yol Görselleştirme:** AI'nın "düşünce sürecini" ve planladığı rotayı gösteren dinamik bir mavi çizgi (Path Visualization) içerir.
* **Çarpışma Önleme:** Algoritma, oyunun bitmemesi için duvarları ve yılanın kendi kuyruğunu engel olarak algılar ve etrafından dolaşır.
* **Dinamik Izgara Sistemi:** Pygame kullanılarak ölçeklenebilir bir ızgara sistemi üzerine kurulmuştur.

## 🛠️ Teknoloji Yığını

* **Dil:** Python 
* **Kütüphane:** Pygame
* **Algoritma:** Breadth-First Search (BFS) - Yol bulma (Pathfinding) için.
* **Veri Yapıları:** Deque (Çift uçlu kuyruk) - Verimli grafik taraması için.

## 🧠 Yapay Zeka Nasıl Çalışır? (Algoritma Mantığı)

1.  **Durum Analizi:** Oyun ızgarası, her karenin bir düğüm (node) olduğu bir grafik (graph) olarak ele alınır.
2.  **Kuyruk Başlatma:** Arama işlemini başlatmak için yılanın başı bir kuyruğa (Queue) eklenir.
3.  **Keşif (Exploration):** Algoritma, komşu kareleri (Yukarı, Aşağı, Sol, Sağ) katman katman tarar.
4.  **Kısıtlama Kontrolü:** Taranan karenin ekran sınırları içinde olup olmadığı ve yılanın vücuduna denk gelip gelmediği kontrol edilir.
5.  **Yolu Geri Çizme (Path Reconstruction):** Yem bulunduğu anda, algoritma hedeften geriye (başlangıç noktasına) doğru iz sürerek en kısa yolu oluşturur.
6.  **Uygulama:** Yılan, hesaplanan bu rotanın ilk adımını atar.

## 📂 Proje Yapısı

* `snake_manual.py`: Oyunun klavye ile oynanan klasik versiyonu.
* `snake_ai.py`: BFS algoritması ve görselleştirme içeren otonom versiyon.
