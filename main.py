from cars_smart import CarroInteligente
from cars_sport import CarroSportivo
from cars_race import CarroCorrida

def test_drive(carro):
    print(f"\n Testando {carro.__class__.__name__}:")
    carro.acelera()
    carro.exibe_velocidade()

if __name__ == "__main__":
    cars_smart = CarroInteligente(10)
    print("Carro Inteligente:")
    cars_smart.acelera()
    cars_smart.exibe_velocidade()
    cars_smart.estacionar()
    test_drive(cars_smart)
    print()

    #TESTANDO CARRO ESPORTIVO
    cars_sport = CarroSportivo(50)
    print("Carro Sportivo:")
    cars_sport.turbo()
    cars_sport.exibe_velocidade()
    cars_sport.freia()
    cars_sport.exibe_velocidade()
    test_drive(cars_sport)

    cars_race = CarroCorrida(100)
    test_drive(cars_race)