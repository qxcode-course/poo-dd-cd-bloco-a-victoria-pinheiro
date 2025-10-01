class Towel:  #meu tipo toalha é:
    def __init__(self, color: str, size: str):   #objeto seco e vazio, o construtor
        self.color: str = color  #atributo com propriedade cor
        self.size: str = size  #atributo com propriedade tamanho
        self.wetness: int = 0
    def __str__(self) -> str:
        return f"{self.color}: {self.size}: {self.wetness}"

print("Qual a cor e o tamanho da sua toalha?")
color = input()
size = input()
towel: Towel = Towel(color, size)
print (f"Sua toalha é {towel.color} e {towel.size}")


