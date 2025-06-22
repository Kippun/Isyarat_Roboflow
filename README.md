# 🤟 Real-Time Hand Sign Detection (BISINDO) with Roboflow + OpenCV

Proyek ini merupakan implementasi sistem deteksi isyarat tangan secara real-time menggunakan kamera laptop. Sistem ini memanfaatkan model deteksi objek dari [Roboflow](https://roboflow.com) yang telah dilatih untuk mengenali beberapa gestur Bahasa Isyarat Indonesia (BISINDO). Deteksi dilakukan dengan mengakses webcam dan menampilkan bounding box serta label kelas secara langsung pada tampilan video.

---

## 🚀 Fitur Utama

- 🎥 **Webcam Real-Time Detection**  
  Menggunakan `cv2.VideoCapture()` untuk membaca input langsung dari kamera.

- 🤖 **Integrasi Roboflow API**  
  Model yang sudah dilatih di Roboflow digunakan untuk mendeteksi gestur tangan secara instan.

- 📦 **Deteksi Multi-Kelas Bahasa Isyarat**  
  Bisa mengenali berbagai gestur BISINDO yang telah dilabeli dalam dataset.

- 📐 **Bounding Box + Confidence Display**  
  Menampilkan prediksi model lengkap dengan skor keyakinannya (`confidence threshold: 15%`).

---

## 🧰 Teknologi yang Digunakan

- [Python 3.x](https://www.python.org)
- [OpenCV](https://opencv.org/)
- [Roboflow Python SDK](https://github.com/roboflow-ai/roboflow-python)
- Kamera internal/laptop

---

## ⚙️ Instalasi

1. **Clone repository:**
   ```bash
   git clone https://github.com/username/nama-repo.git
   cd nama-repo

2.  **Instalasi Library **
    pip install opencv-python roboflow

MIT License © 2025 — [Kelompok 1 TUBES PSI D3TT 4701]
