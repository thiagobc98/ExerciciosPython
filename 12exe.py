manha = {
 "aluno1": {
  "nome": "Clara",
  "disciplina": "Redes"
 },
 "aluno2": {
  "nome": "Jonas",
  "disciplina": "Banco de Dados"
 }
}
tarde = {
 "aluno2": {
  "nome": "Ana",
  "disciplina": "Algoritmos"
 },
 "aluno3": {
  "nome": "Rafael",
  "disciplina": "Grafos"
 }
}


def leitura():
 for chave in manha:
  if chave in tarde.keys():
   print("%s, %s" % (chave, manha[chave]))
   print("%s, %s" % (chave, tarde[chave]))


leitura()



