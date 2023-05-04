from Bio import SeqIO


with open("Sequencia.fasta") as sequencia:
    for n in SeqIO.parse(sequencia, "fasta"):
        seq = str(n.seq)

contar = {'Amina': seq.count('A'),
          'Timina': seq.count('T'),
          'Guanina': seq.count('G'),
          'Citosina': seq.count('C')
          } #contar os nucleotídeos

soma = sum(contar.values())
porcentagem = {base: count/soma*100 for base, count in contar.items()} #dar a porcentagem para cada nucleotídeos

i = 0
seqt = []

for base, porcentagem in porcentagem.items():
  seqt.append(f'{base}: {porcentagem:.2f}%\n')
  print(f"{base}: {porcentagem:.2f}%")
  i = i + 1


with open('porcentagens.txt', 'w') as arq:
    for i in range(len(seqt)) :
      arq.write(seqt[i])
    
