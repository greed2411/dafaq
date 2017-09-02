from nltk.corpus import wordnet as wn
import sys


def main():

	if len(sys.argv) > 1:

		word = sys.argv[1]
	else :
		word = input('Enter the word that needs meaning : ')

	for index, word_meaning in enumerate(wn.synsets(word)):
		print('\n', str(index + 1)+ '. ' + word_meaning.definition() + '.\n')


if __name__ == "__main__":
	main()
