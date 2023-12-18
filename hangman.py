import random             
HANGMAN_PICS = ['''
    --------
    |  |
    |  
    |
    |
    |
     ''', '''
    --------
    |  |
    |  0
    |
    |
    |
    ''' , '''
    --------
    |  |
    |  0
    | /
    |
    |
    ''', '''
    --------
    |  |
    |  0
    | /| 
    |
    |
    ''', '''
    --------
    |  |
    |  0
    | /|\ 
    |
    |
    ''', ''' 
    --------
    |  |
    |  0
    | /|\ 
    | /
    |
    ''', ''' 
    --------
    |  |
    |  0
    | /|\ 
    | / \ 
    |
    ''']

# Lista de palavras
words = 'mochila barba calebo vertido roupa gato cachorro carro casa panda ovelha tartatura coelho rato corvo zebra'.split()

# Função para retornar uma palavra aleatória da lista de palavras
def getRandomWord(wordlist):
    wordIndex = random.randint(0, len(wordlist) - 1)
    return wordlist[wordIndex]


def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Letras erradas:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    # Troca os espaço vázios com as letras acertadas
    for i in range(len(secretWord)): 
        if secretWord[i] in  correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    # mostra palavra que precisa acertar com espaços entre cada letra
    for letter in blanks: 
        print(letter, end=' ')
    print()


# retorna a letra que o jogador colocou. Isso está aqui para ter certeza que o jogador colocou uma letra e nada diferente disso
def getGuess(alreadyGuessed):
    while True:
        print('Digite uma letra!')
        guess = input()
        guess = guess.lower()  
        if len(guess) != 1:
            print('Só vale colocar uma letra por vez')        
        elif guess in alreadyGuessed:
            print('Essa letra já foi! Tente outra')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Só valem letras!')
        else: 
            return guess 

# A função vai retornar True se o jogador quiser jogar de novo, fora isso vai retornar False 
def playAgain():
    print('Você quer jogar de novo? (sim ou não)', end=' ')
    return input().lower().startswith('s')


print('   F  O  R  C  A')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    # Deixar o jogador colocar as letras
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # ver se o jogador ganhou 
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print(f'Sim! A palavra era {secretWord}. Você ganhou!!!')
            gameIsDone = True 
    else:
        missedLetters =  missedLetters + guess

        # verificar se o jogador tentou muitas vezes e perdeu
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
             displayBoard(missedLetters, correctLetters, secretWord)
             print('Você ficou sem tentativas!\nDepois de ' +
                       str(len(missedLetters)) + ' tentativas e ' +
                   str(len(correctLetters)) + ' Acertos, a palavra era "' + secretWord + '"')
             gameIsDone = True

    #Perguntar se o jogador que jogar de novo (mas só caso o jogo já tiver terminado)
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else: 
            break
