class Persegipanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)

    def luas(self):
        return self.panjang * self.lebar

    def __str__(self):
        return f"Persegi panjang, panjangnya {self.panjang}cm dan lebarnya {self.lebar}cm"
    
def main():
    try:
        panjang = int(input("Masukkan panjangnya(cm): "))
        lebar = int(input("Masukkan lebarnya(cm): "))

        persegi_panjang = Persegipanjang(panjang, lebar)
        print(persegi_panjang)
        print(f"Keliling: {persegi_panjang.keliling()} cm")
        print(f"Luas: {persegi_panjang.luas()} cm^2")

    except ValueError:
        print("Input harus berupa angka!")

main()