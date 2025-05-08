import numpy as np

# 1. Scalar bir enerji verisi tanımla
def define_scalar_energy():
    # Tek bir sayı döndürmelidir.
    pass

# 2. Belirli bölgelerdeki suç oranlarını vektör olarak tanımla
def define_crime_vector():
    # np.array([..]) yapısıyla 1D array döndürmelidir.
    pass

# 3. Belirli sokaklardaki enerji tüketimini matris olarak tanımla
def define_energy_matrix():
    # 2D np.array döndürmelidir
    pass

# 4. İki suç oranı vektörünü toplayan fonksiyon
def add_crime_vectors(vec1, vec2):
    pass

# 5. Enerji matrisinden bir başka matrisi çıkaran fonksiyon
def subtract_energy_matrices(mat1, mat2):
    pass

# 6. Sensör matrisini transpozlayan fonksiyon
def transpose_sensor_matrix(matrix):
    pass

# 7. Enerji tüketim matrisi ile kaynak dağılım vektörünü çarp (dot product)
def dot_energy_source(matrix, vector):
    pass

# 8. Veri analizi neden önemlidir? Açıklamayı döndür (str)
def why_linear_algebra_is_important():
    # Açıklayıcı bir string döndürmelidir.
    pass

# 9. Ortalama suç oranını hesapla
def average_crime_rate(crime_vector):
    pass

# 10. En yüksek enerji tüketen sokağı bul
def max_energy_usage(matrix):
    # Her sokak bir satır, kolonlar saatlerdir. En çok tüketen satır bulunmalı.
    pass