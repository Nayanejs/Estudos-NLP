# Passo 1: Instalar a biblioteca (uma só vez)
# pip install deep-translator

# Passo 2: Importar o tradutor
from deep_translator import GoogleTranslator

# Passo 3: Texto de exemplo
texto = "Oi, esse é o meu primeiro projeto em NLP."

# Passo 4: Traduzir para inglês
traducao = GoogleTranslator(source='pt', target='en').translate(texto)

# Passo 5: Exibir resultado
print("Texto original:", texto)
print("Tradução:", traducao)

