import random

class Words:
  #This class is used to select a random word from a list of words. It has two properties, wordsArr and selected.
  def __init__(self):
    self._wordsArr = ['aabca', 'anger', 'apple', 'bread', 'break', 'hotel', 'house', 'music', 'night', 'plane', 'plant', 'right', 'river', 'smoke', 'speed', 'thing', 'trust', 'whole']
    self._selected = ''

  #This method is used to retreive the selected word
  def getWord(self):
    return self._selected

  #This method is used to select a word from the array at random
  def chooseWord(self):
    index = random.randint(0, len(self._wordsArr) - 1)

    self._selected = self._wordsArr[index]

class Letters:
  #This class is to store the guessed letters and the hint. It has two properties, guessed letters and correct letters. Correct letters shows the hints and the correct letters
  def __init__(self):
    self._guessedLetters = ''
    self._correctLetters = '_ _ _ _ _'
  
  #This method will take in a word and a letter. You use this to see if the letter that was guessed was right or not, then add it to the guessed letters and if it was in the word, update the hint to show that
  def guessLetter(self, letter, word):
    if letter in self._guessedLetters:
      return 'Letter already guessed.'

    if len(self._guessedLetters) > 0:
      self._guessedLetters += f', '

    
    self._guessedLetters += f'{letter}'

    if letter in word:
      i = 0
      for character in word:
        if character == letter:
          reassigned = list(self._correctLetters)

          reassigned[i] = letter

          self._correctLetters = ''.join(reassigned)
        
        i += 2

      if '_' in self._correctLetters:
        return 'Letter was in the word!'
      else:
        return f'You won! The word was {word}!'
    else:
      return 'Letter was not in the word.'

  # This method is to show the hint and the correct letters
  def showLetters(self):
    return self._correctLetters

  # This method is to show the already guessed letters
  def showGuessed(self):
    return self._guessedLetters

class Parachute:
  # This class keeps track of the parachute and how many guesses have been made. It's only property is the list of strings to show the stickman parajumper
  def __init__(self):
    self._parachuteStrings = ['  ___  ', ' /___\ ', ' \   / ', '  \ /  ', '   0   ', '  /|\  ', '  / \  ']

  # This method is used to view the parajumper
  def showParachute(self):
    for level in self._parachuteStrings:
      print(level)

  # This method removes a level from the parajumper on a wrong guess, and informs when the user loses
  def loseLevel(self):
    if(self._parachuteStrings[0] == '  \ /  '):
      self._parachuteStrings.pop(0)
      self._parachuteStrings[0] = '   X   '
      return True
    else:
      self._parachuteStrings.pop(0)
      return False

class Game:
  # This class keep track of the game. It has one property, the letters a user could guess
  def __init__(self):
    self._avalaibleLetters = 'abcdefghijklmnopqrstuvwxyz'

  #This method is used to make sure the user made a valid guess, that it was a single letter and a letter from the english alphabet
  def checkLetter(self, letter):
    if len(letter) > 1 or len(letter) <= 0:
      return False
    elif letter in self._avalaibleLetters:
      return True
    else:
      return False

  # This method takes a turn. It goes through and uses other classes to check if the users letter is in the word, update the guessed letters, update the parachute and inform the user when the game ends and if they win or lose
  def takeTurn(self, letter, words, letters, parachute):
    response = letters.guessLetter(letter, words.getWord())

    if response == 'Letter already guessed.':
      print(response)
      return True

    else:
      if response == 'Letter was not in the word.':
        lose = parachute.loseLevel()

        if lose:
          print('')
          parachute.showParachute()
          print('')
          print('^^^^^^^')
          print(f'You lose! The word was {words.getWord()}!')
          return False

      elif response != 'Letter was in the word!':
        print(response)
        return False

      print(letters.showLetters())
      print('')
      parachute.showParachute()
      print('')
      print('^^^^^^^')
      print('')
      print(f'Guessed: [{letters.showGuessed()}]')
      return True

def main():
  words = Words()
  letters = Letters()
  parachute = Parachute()
  game = Game()

  words.chooseWord()

  print('Welcome, please enjoy!')
  print(letters.showLetters())
  print('')
  parachute.showParachute()
  print('')
  print('^^^^^^^')
  print('')

  while True:
    chosenLetter = input('Choose a letter (a-z}: ')

    if game.checkLetter(chosenLetter):
      res = game.takeTurn(chosenLetter, words, letters, parachute)
      if res == False:
        break
    else:
      print('That is not an acceptable input, please choose a single lowercase character a-z.')

if __name__ == '__main__':
  main()