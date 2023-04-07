"""
Aplikasi deteksi gempa terkini
Modularisasi dengan Function
Modularisasi dengan package
"""
# from gempaterkini import akstraksi_data, tampilkan_data
#
# if __name__ == '__main__':
#     print("Aplikasi utama")
#     result = akstraksi_data()
#     tampilkan_data(result)

#ini adalah import data yang sesuai
import gempaterkini

if __name__ == '__main__':
    print("Aplikasi utama")
    result = gempaterkini.akstraksi_data()
    gempaterkini.tampilkan_data(result)
