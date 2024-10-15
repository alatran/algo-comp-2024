import numpy as np
from typing import List, Tuple

def run_matching(scores: List[List], gender_id: List, gender_pref: List) -> List[Tuple]:
    """
    TODO: Implement Gale-Shapley stable matching!
    :param scores: raw N x N matrix of compatibility scores. Use this to derive a preference rankings.
    :param gender_id: list of N gender identities (Male, Female, Non-binary) corresponding to each user
    :param gender_pref: list of N gender preferences (Men, Women, Bisexual) corresponding to each user
    :return: `matches`, a List of (Proposer, Acceptor) Tuples representing monogamous matches

    Some Guiding Questions/Hints:
        - This is not the standard Men proposing & Women receiving scheme Gale-Shapley is introduced as
        - Instead, to account for various gender identity/preference combinations, it would be better to choose a random half of users to act as "Men" (proposers) and the other half as "Women" (receivers)
            - From there, you can construct your two preferences lists (as seen in the canonical Gale-Shapley algorithm; one for each half of users
        - Before doing so, it is worth addressing incompatible gender identity/preference combinations (e.g. gay men should not be matched with straight men).
            - One easy way of doing this is setting the scores of such combinations to be 0
            - Think carefully of all the various (Proposer-Preference:Receiver-Gender) combinations and whether they make sense as a match
        - How will you keep track of the Proposers who get "freed" up from matches?
        - We know that Receivers never become unmatched in the algorithm.
            - What data structure can you use to take advantage of this fact when forming your matches?
        - This is by no means an exhaustive list, feel free to reach out to us for more help!
    """
    """
    sorry ahead of time for the pseudocode. The combination of not being at the meeting along with not being too familiar with
    python made this a bit difficult to implement.
    """

    "first, we have a 9 x 10 matrix of scores in raw_scores.txt, so we can use create a 9x10 matrix and fill it with the values in the text file"

    "we create a list using genders.txt with the genders of all the people who submitted"

    "we will also create a list using gender_preferences.txt with the preferences of each user"

    "we can go through the scores and sort them in ascending numerical order"
    
    "we should then locate the user who the score belongs to"
    
    "if we have users 0, 1, and 2, we start at user 1"
    "subtract user 1's scores by user 0's score and take abs value"
    "subtract user 1's scores by user 2's score and take abs value"
    "if the first difference is greater than the second"
        "if user 0's preference equals user 1's gender and if user 1's preference equals user 0's gender, then we can consider them a match"
    "else"
        "if user 2's preference equals user 1's gender and if user 1's preference equals user 2's gender, then we can consider them a match"
        "else"
            "if user 0's preference equals user 1's gender and if user 1's preference equals user 0's gender, then we can consider them a match"
    "we can set user 1 as the proposer and the other user as the receiver and add them to the list matches"
    "we can remove the values in the lists and matrix/set them to null"
    "continue this process"

    "we then go through again and repeat this process, trying to find the closest scores and making sure preferences match"
    "insert these values in the match list"

    "if the table is completely null, then we return matches"

    

    
    matches = [()]
    return matches

if __name__ == "__main__":
    raw_scores = np.loadtxt('raw_scores.txt').tolist()
    genders = []
    with open('genders.txt', 'r') as file:
        for line in file:
            curr = line[:-1]
            genders.append(curr)

    gender_preferences = []
    with open('gender_preferences.txt', 'r') as file:
        for line in file:
            curr = line[:-1]
            gender_preferences.append(curr)

    gs_matches = run_matching(raw_scores, genders, gender_preferences)
