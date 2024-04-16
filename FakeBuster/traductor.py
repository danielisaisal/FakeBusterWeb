from mtranslate import translate

def traducirAIngles(textoATraducir) :
    textoTraducido = translate(textoATraducir, "en")
    return textoTraducido

def traducirAEspañol(textoATraducir):
    textoTraducido = translate(textoATraducir, "es")
    return textoTraducido