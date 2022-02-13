from screen_display import animation
from functions import getWord
def playGame():

    wordInformation = getWord()
    word = wordInformation['word'].lower()
    dica = wordInformation['definition']
    wordAsList = list(word)
    alphabet ="abcdefghijklmnopqrstuvwxyz"
    maxTries = 6

    wrongLetters = 0
    triedLetters = ""
    success = [""] * len(word)
    displayWord = "  |  "
    displayWord += "_ " * len(word)
    print("Para ter uma dica escreva 'dica'")
    print("A palvra que você deve adivinhar é:")
    animation(wrongLetters)
    print(displayWord)

    wrongTriedLetters = ""
    while wrongLetters < maxTries:
        
        print("Insira uma letra ou a palavra completa:")
        guessedLetter = input()
        guessedLetter = guessedLetter.lower()

        #RULES
        if guessedLetter == "dica" or guessedLetter == "\'dica\'":
            print(f'A definição da palavra é: {dica}')
            continue
        
        if guessedLetter == word:
            print(f'Parabéns! A palavra era {word}')
            break

        if guessedLetter not in alphabet or guessedLetter == "":
            print("Essa letra não é valida. Escolha outra!")
            continue

        if guessedLetter in triedLetters:
            print("Essa letra já foi inserida. Escolha outra!")
            continue

        if len(guessedLetter) > 1:
            if guessedLetter != word:
                print("Insira uma letra por vez!")
                continue


        triedLetters += guessedLetter

        if guessedLetter in word:
            print(f'A letra {guessedLetter} faz parte da palavra')
            print(f"Letras tentadas: {wrongTriedLetters}")
            animation(wrongLetters)
            indexesList = [i for i, x in enumerate(wordAsList) if x == guessedLetter]
            for i in indexesList:
                success[i] = guessedLetter

        else:
            wrongLetters += 1
            print(f'A letra {guessedLetter} NÃO faz parte da palavra')
            wrongTriedLetters += guessedLetter
            print(f"Letras tentadas: {wrongTriedLetters}")
            animation(wrongLetters)
        if success == wordAsList:
            animation(wrongLetters)
            print(f'Parabéns! A palavra era {word}')
            break
        
        displayWord = "  |  "
        for i in success:
            if i == "":
                displayWord += "_ "
            else:
                displayWord += i+" "
        
        print(displayWord)
    animation(wrongLetters)
    print(f'A palavra era {word}')

playGame()