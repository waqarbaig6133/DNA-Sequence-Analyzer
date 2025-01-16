def kmer(DNA, k):
  kmers = []
  if k == 1:
    for x in DNA:
      if x not in kmers:
        kmers.append(x)
    print(kmers) #It will add each different nucleotide respectively in the order found in the sequence
  elif k == len(DNA):
    print(DNA)
  else:
    i = 0
    j = k
    for x in range(k-1,len(DNA)): #if the k was 3, the last letter of the first sequence will be the third nucleotide, therefore proceed from there until the last letter
      kmers.append(DNA[i:j]) #
      i+=1
      j+=1
  i = 0
  for x in kmers:
    print(f"{i*' '}{x}")
    i+=1
#Example of possible arguments
DNA = 'GTAGAGCTGT'
k = int(input('Enter your k value: '))
kmer(DNA, k)
