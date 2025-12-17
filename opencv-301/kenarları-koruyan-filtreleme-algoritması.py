import cv2 as cv
import numpy as np

# =========================
# 1) RESMİ OKU
# =========================
src = cv.imread("/home/kiyran/Masaüstü/opencv/opencv-201/kopek.png")

if src is None:
    raise SystemExit("Resim okunamadı!")

h, w = src.shape[:2]

# =========================
# 2) KENARLARI KORUYAN FİLTRE
# =========================
dst = cv.edgePreservingFilter(
    src,
    sigma_s=100, # blurluk
    sigma_r=0.4, # kenar bölgelerin umursanmasını belirtir.
    flags=cv.RECURS_FILTER
)

# =========================
# 3) YAN YANA BİRLEŞTİR
# =========================
result = np.zeros((h, w * 2, 3), dtype=src.dtype)
result[:, 0:w, :] = src
result[:, w:2*w, :] = dst

# =========================
# 4) EKRANA SIĞDIR (ORAN KORUNUR)
# =========================
max_w = 1200
max_h = 700

rh, rw = result.shape[:2]
scale = min(max_w / rw, max_h / rh, 1.0)

new_w = int(rw * scale)
new_h = int(rh * scale)

result = cv.resize(result, (new_w, new_h), interpolation=cv.INTER_AREA)

# =========================
# 5) GÖSTER
# =========================
cv.imshow("Edge Preserving Filter - Result", result)
cv.waitKey(0)
cv.destroyAllWindows()
