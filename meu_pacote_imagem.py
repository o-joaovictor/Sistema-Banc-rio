# meu_pacote_imagem/processamento.py
from PIL import Image, ImageFilter

def converter_para_cinza(caminho_imagem):
    """
    Converte uma imagem colorida para escala de cinza.

    Args:
        caminho_imagem (str): O caminho para o arquivo da imagem de entrada.

    Returns:
        PIL.Image.Image: A imagem convertida para escala de cinza.
    """
    try:
        img = Image.open(caminho_imagem)
        img_cinza = img.convert("L")  # "L" para escala de cinza
        return img_cinza
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado em {caminho_imagem}")
        return None
    except Exception as e:
        print(f"Ocorreu um erro ao converter a imagem para cinza: {e}")
        return None

def aplicar_desfoque_gaussiano(caminho_imagem, raio=2):
    """
    Aplica um filtro de desfoque Gaussiano a uma imagem.

    Args:
        caminho_imagem (str): O caminho para o arquivo da imagem de entrada.
        raio (int): O raio do desfoque Gaussiano. Default é 2.

    Returns:
        PIL.Image.Image: A imagem com o desfoque aplicado.
    """
    try:
        img = Image.open(caminho_imagem)
        img_desfocada = img.filter(ImageFilter.GaussianBlur(raio))
        return img_desfocada
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado em {caminho_imagem}")
        return None
    except Exception as e:
        print(f"Ocorreu um erro ao aplicar desfoque: {e}")
        return None

if __name__ == "__main__":
    # Exemplo de uso (apenas para teste direto do arquivo)
    # Você precisaria de um arquivo de imagem (ex: 'exemplo.jpg') na mesma pasta
    # para testar este bloco.

    print("Testando funções de processamento de imagem...")
    # Crie um arquivo de imagem de teste, por exemplo, 'test_image.jpg'
    # para que este exemplo funcione.

    # Exemplo de imagem de teste (substitua pelo caminho real de uma imagem sua)
    imagem_teste = "caminho/para/sua/imagem.jpg" # <--- MUDE ISSO PARA O CAMINHO DE UMA IMAGEM REAL!

    # Testando converter para cinza
    img_cinza = converter_para_cinza(imagem_teste)
    if img_cinza:
        img_cinza.save("imagem_cinza.jpg")
        print("Imagem convertida para cinza e salva como 'imagem_cinza.jpg'")

    # Testando aplicar desfoque
    img_desfocada = aplicar_desfoque_gaussiano(imagem_teste, raio=5)
    if img_desfocada:
        img_desfocada.save("imagem_desfocada.jpg")
        print("Imagem desfocada e salva como 'imagem_desfocada.jpg'")