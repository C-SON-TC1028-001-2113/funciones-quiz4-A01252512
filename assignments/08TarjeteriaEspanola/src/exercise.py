def cant_tarjetas(pliego, plumon):
    tarjetasPlumon = plumon * 35
    tarjetasPliego = pliego * 12

    if tarjetasPlumon >= tarjetasPliego:
        return tarjetasPliego

    else:
        return tarjetasPlumon

def main():
    #escribe tu código abajo de esta línea
    pliegos = int(input('Dame la cantidad de pliegos de papel albanene: '))
    plumones = int(input('Dame la cantidad de plumones: '))
    tarjetasMax = cant_tarjetas(pliegos, plumones)

    print(f'El número máximo de tarjetas que se pueden hacer es: {tarjetasMax}')
    
if __name__=='__main__':
    main()
