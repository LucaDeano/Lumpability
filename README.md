# Lumpability

Il file python AlogritmoLumping.py contiene l'implementazione dello pseudo-codice che si trova all'interno dell'articolo scientifico sotto citato.
*  [Compressing Neural Networks via Formal Methods]([https://www.example.com/articolo](https://www.sciencedirect.com/science/article/pii/S0893608024003356))


## Esecuzione del codice
Sotto la definizione dell'algoritmo di pruning si trova un esempio di struttura di una piccola rete neurale. La struttura della rete neurale può essere modellata a piacimento modificando i parametri come segue:
* k ---> numero di layer della rete
* S ---> definizione del numero e del nome dei neuroni per ogni layer: {0, 1} se voglio due neuroni in un layer, {0, 1, 2} se ne voglio 3 ecc...
* W ---> definisco per ogni layer i collegamenti tra i neuroni e il relativo peso: 1: {(0, 2): 0.1...  indica che per il layer 1 il neurone 0 si collega al neurone 2 del layer successivo con un peso di 0.1
* b ---> definisco il baias di ciascun neurone dei layer nascosti
* A ---> definisco la funzione di attivazione per ogni neurone dei layer nascosti: 1: {2: 'ReLU', 3: 'ReLU'} se per il primo layer nascosto entrambi i neuroni usano la ReLU

## Risultato
Viene riportato su terminale come segue:
* k ---> mostra numero di laye della rete
* S_prime ---> mostra il dizionario contenente le classi di equivalenza per ogni layer
* W_prime ---> mostra i nuovi pesi della rete
* b_prime ---> mostra i bias della rete
* A_prime ---> mostra le funzioni di attivazione
