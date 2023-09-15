class TV:
    def __init__(self):
        self.canal = 1
        self.volume = 50

    def mudarCanal(self, novo_canal):
        if 1 <= novo_canal <= 100:
            self.canal = novo_canal
        else:
            print("Canal inválido.")

    def aumentarVolume(self):
        if self.volume < 100:
            self.volume += 1
        else:
            print("Volume máximo alcançado.")

    def diminuirVolume(self):
        if self.volume > 0:
            self.volume -= 1
        else:
            print("Volume mínimo alcançado.")

# Exemplo de uso da classe TV
tv = TV()
print(f"Canal: {tv.canal}")
print(f"Volume: {tv.volume}")

tv.mudarCanal(5)
print(f"Canal após mudança: {tv.canal}")

tv.aumentarVolume()
print(f"Volume após aumento: {tv.volume}")

tv.diminuirVolume()
print(f"Volume após diminuição: {tv.volume}")

tv.mudarCanal(150)
tv.diminuirVolume()