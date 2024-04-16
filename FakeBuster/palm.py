import google.generativeai as palm
from . import traductor

def buscarInformacion(texto):
    textoTraducidoAlIngles = traductor.traducirAIngles(texto)
    
    palm.configure(api_key='tu API key aqui')

    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    model = models[0].name
    print(model)

    prompt = textoTraducidoAlIngles

    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0,
        # The maximum length of the response
        max_output_tokens=800,
    )
    
    textoTraducidoAlEspañol = traductor.traducirAEspañol(completion.result)

    return textoTraducidoAlEspañol