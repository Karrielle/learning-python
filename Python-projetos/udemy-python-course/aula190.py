
import json

dados = {
    "nome": "João aaa",
    "idade": 30,
    "cidade": "São Paulo"
}
with open("dados.json", "w", encoding='utf8') as arquivo:
    json.dump(
        dados,
        arquivo,
        ensure_ascii=False,
        indent=2,    
    )

with open("dados.json", "r", encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)
    print(type(pessoa))