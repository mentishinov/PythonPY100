if __name__ == "__main__":

        spaces = 5
        word = ['H', 'e', 'l', 'l', 'o', ',', 'W', 'o', 'r', 'l', 'd']

        for i in range(len(word)):
            spaces += 1
            print(' ' * spaces + ' ' * i, word[i])

