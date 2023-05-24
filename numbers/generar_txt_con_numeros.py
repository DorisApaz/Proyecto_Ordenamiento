import random

def generate(totalDeNumerosAGenerar):
    numeros_aleatorios = [random.randint(1, 1000) for _ in range(totalDeNumerosAGenerar)]

    with open(str(totalDeNumerosAGenerar) + '.txt', 'w') as archivo:
        for numero in numeros_aleatorios:
            archivo.write(str(numero) + '\n')

    print(f"Archivo '{str(totalDeNumerosAGenerar)}.txt' creado exitosamente con {totalDeNumerosAGenerar} números aleatorios.")

# generate(100)
# generate(500)
# generate(1000)
# generate(2000)
# generate(3000)
# generate(4000)
# generate(5000)
# generate(6000)
# generate(7000)
# generate(8000)
# generate(9000)
# generate(10000)
# generate(20000)
# generate(30000)
# generate(40000)
# generate(50000)
# generate(60000)
# generate(70000)
# generate(80000)
# generate(90000)
# generate(100000)
