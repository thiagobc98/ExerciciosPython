biblioteca_manha= {
 "Thiago": {
  "livro1": "O Gigante",
  "livro2": "Cruzeiro",
  "livro3": "live",
  "livro4": "python"
},
 "João": {
  "livro1": "banco de dados",
  "livro2": "php",
  "livro3": "java"
 }
}
biblioteca_noite = {
 "ana": {
    "livro1" : "engenharia",
     "livro2" : "direito"
 },
 "Thiago": {
  "livro1": "bmw",
  "livro2": "mercedez"


 }
}
def iguais(b1, b2):
    for chave in b1:
        if chave in b2.keys():
            print("%s, %s" % (chave, b1[chave]))
            print("%s, %s" % (chave, b2[chave]))
iguais(biblioteca_manha, biblioteca_noite)