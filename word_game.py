"""Compute a team's score for a (fictitious) word game.

In this game, two players independently find words in a matrix of letters.
Each player's words are added to a text file with one word per line. Duplicates
are removed from each player's list. For each word that appears on both players'
lists, the team's score increases by the number of letters in the word minus 2
(words less than three characters long are not worth any points).
"""


from argparse import ArgumentParser
import sys


# Replace this comment with your implementation of the PlayerWords class and the
# main() function.

class PlayerWords:
    
    def __init__(self, filepath):
        self.words = set()
        with open(filepath, 'r', encoding="utf-8") as file:
            for line in file:
                line.strip()
                self.words.add(line)
                
    def score(self, PlayerWords):
        points = 0
        combo = self.words.intersection(PlayerWords.words)
        for thing in combo:
            if len(thing) > 2:
                points += (len(thing) - 2)
        return points
        
def main(file1, file2):
    p1 = PlayerWords(file1)
    p2 = PlayerWords(file2)
    score = p1.score(p2)
    print(f"Your team scored {score} points!")


def parse_args(arglist):
    """Parse command line arguments.
    
    Expect two mandatory arguments:
        - str: path to a text file containing words found by player 1.
        - str: path to a text file containing words found by player 2.
    
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.

    """
    parser = ArgumentParser()
    parser.add_argument("wordfile1", help="file containing player 1's words")
    parser.add_argument("wordfile2", help="file containing player 2's words")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.wordfile1, args.wordfile2)
