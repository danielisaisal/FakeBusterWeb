from . import palm
from datetime import datetime

def buscarInformacionDelTitulo(titulo):
    informacionTitulo = f"Explicame este texto: {titulo}?"  
    infomracionEncontradaDelTitulo = palm.buscarInformacion(informacionTitulo)
    return infomracionEncontradaDelTitulo


def buscarInformacionDelAutor(autor):
    if (autor == "ninguno" or autor == "" or autor == "Ninguno"):
        return "Es posible que su noticia sea falsa, recomendamos que si no existe autor verifque la veracidad de la noticia"
    else:
        informacionAutor = f"Dame información sobre este autor, empresa, escritor o periodista: {autor}"   
        infomracionEncontradaDelAutor = palm.buscarInformacion(informacionAutor)
        return infomracionEncontradaDelAutor

def informacionDeLaFecha(fecha, titulo):
    informacionFecha = f"¿Podrías verificar la autenticidad del siguiente evento: {titulo}? Además, necesito confirmar si sucedió en la fecha especificada: {fecha}. En caso de que sea verídico, ¿me proporcionarías más detalles sobre lo acontecido? Si resulta ser falso, ¿podrías explicarme las razones detrás de esta conclusión?"  
    infomracionEncontradaDelaFecha = palm.buscarInformacion(informacionFecha)
    return infomracionEncontradaDelaFecha