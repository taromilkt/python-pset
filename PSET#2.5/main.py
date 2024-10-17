# programmer: Lindsey Nguyen
# date of submission: 10/23/2024

# PSET 2
# ==============================

# Problem #5: Find interesting words

# This program removes common stop words from a text, counts word frequencies, and reports words that appear more than a specified threshold.

from collections import Counter

stop_words = ["a", "an", "and", "are", "as", "at", "be", "been", "by", "for",
"from", "has", "have", "had", "his", "her", "he", "in", "is", "it", "its", "it’s",
"of", "that", "the", "there", "to", "was", "were", "will", "with", "which"]

def filter_stop_words(text, stop_words, custom_stop_words=None):
    if custom_stop_words:
        stop_words = stop_words + custom_stop_words

    filter_list = []
    words = text.split()
    for word in words:
        if word not in stop_words:
            filter_list.append(word)
    return filter_list

def find_interesting_words(text, stop_words, threshold,custom_stop_words=None):
    filtered_words = filter_stop_words(text, stop_words, custom_stop_words)

    word_counts = Counter(filtered_words)

    interesting_words = {}
    for word, count in word_counts.items():
        if count > threshold:
            interesting_words[word] = count
    return interesting_words

def test_1():
    text = """There are many works that have been pointed to as) possible sources for Shakespeare's play—from ancient 
Greek tragedies to Elizabethan plays. The editors of the Arden Shakespeare question the idea of "source hunting",
pointing out that it presupposes that authors always require ideas from other works for their own, and
suggests that no author can have an original idea or be an originator. When Shakespeare wrote, there 
were many stories about sons avenging the murder of their fathers, and many about clever avenging
sons pretending to be foolish in order to outsmart their foes. This would include the story of the ancient
Roman, Lucius Junius Brutus, which Shakespeare apparently knew, as well as the story of Amleth, which was preserved
in Latin by 13th-century chronicler Saxo Grammaticus in his Gesta Danorum, and printed in Paris in 1514. The Amleth
story was subsequently adapted and then published in French in 1570 by the 16th-century scholar
François de Belleforest. It has a number of plot elements and major characters in common with Shakespeare’s
Hamlet, and lacks others that are found in Shakespeare. Belleforest's story was first published in English in 1608,
after Hamlet had been written, though it's possible that Shakespeare had encountered it in the French-language version.
"""
    threshold = 2 # repeated words shown twice
    interesting_words = find_interesting_words(text, stop_words, threshold)

    print(f"Interesting words (occurrences > {threshold}):")
    for word in interesting_words:
        print(f"{word}: {interesting_words[word]}")


def test_2():
    text = """ Dandadan is a Japanese manga series created by Yukinobu Tatsu. The story blends supernatural and science fiction elements, 
    following two high school students, Momo Ayase and Ken Takakura (Okarun). Momo believes in ghosts but not in aliens, while Okarun 
    believes in aliens but not in ghosts. Their worlds collide when they encounter both paranormal entities and extraterrestrial beings, 
    leading to exciting battles and strange adventures. The series is known for its dynamic mix of humor, romance, action, and supernatural elements, 
    making it unique in its genre.Dandadan is serialized in Shonen Jump+, with an anime adaptation set to release in October 2024. Fans of quirky, 
    fast-paced storytelling will enjoy the wild ride as Momo and Okarun face off against ghosts, aliens, and even more bizarre foes. The story is fast-paced,
     with Momo and Okarun constantly encountering strange entities like ghosts, aliens, and paranormal beings. This keeps the story interesting, with action, humor, and romance throughout. 
     The series has quickly become a favorite in the Shonen Jump+ lineup due to its unique storytelling and mix of genres. Fans of science fiction, supernatural, 
     and comedy are sure to find Dandadan an entertaining read."""

    threshold = 3 # repeated words shown twice
    custom_stop_words = ["story", "series"]
    interesting_words = find_interesting_words(text, stop_words, threshold, custom_stop_words)

    print(f"Interesting words (occurrences > {threshold}):")
    for word in interesting_words:
        print(f"{word}: {interesting_words[word]}")

def test_3():
    text = """ To make pho, a traditional Vietnamese soup, you start by simmering a rich, flavorful broth made from beef bones or chicken bones, depending on your choice of pho. 
    The broth is the heart of pho and takes several hours to develop its deep, savory flavor. Along with the bones, you'll add onions, ginger, 
    and a mix of spices like star anise, cinnamon, cloves, and cardamom. Once the broth is ready, it’s poured over rice noodles, thin slices of beef or chicken, 
    and garnished with fresh herbs such as cilantro, basil, and green onions. To enhance the flavor, serve with optional toppings like lime, bean sprouts, hoisin sauce, and sriracha.
     The key to great pho is balancing the savory broth with the fresh toppings, creating layers of flavor in every bite."""

    threshold = 1 # repeated words shown twice
    custom_stop_words = ["make", "made","add", "or"]
    interesting_words = find_interesting_words(text, stop_words, threshold, custom_stop_words)

    print(f"Interesting words (occurrences > {threshold}):")
    for word in interesting_words:
        print(f"{word}: {interesting_words[word]}")

def test_4():
    text = """ To play soccer, the main objective is to control the ball.
     Players pass the ball to teammates and dribble the ball down the field. 
     When a player kicks the ball into the goal, their team scores.
     Passing the ball requires accuracy, and players must keep the ball away from opponents. 
     Dribbling the ball involves moving quickly while maintaining control of the ball. 
     The ball can also be kicked to clear it away from defenders or towards the goal.
     Keeping the ball under control is key to winning in soccer"""

    threshold = 5 # repeated words shown twice
    custom_stop_words = ["game","hit"]
    interesting_words = find_interesting_words(text, stop_words, threshold, custom_stop_words)

    print(f"Interesting words (occurrences > {threshold}):")
    for word in interesting_words:
        print(f"{word}: {interesting_words[word]}")

def test_5():
    text = """There are many works that have been pointed to as possible sources for Shakespeare's play"""
    threshold = 500  # Unreasonably high threshold
    interesting_words = find_interesting_words(text, stop_words, threshold)
    print(interesting_words)  # This will likely print an empty dictionary

def test_6():
    text = 445678  # Passing an integer instead of a string
    threshold = 2
    interesting_words = find_interesting_words(text, stop_words, threshold)
    print(interesting_words)


if __name__ == '__main__':
    #valid test cases
    test_1()
    test_2()
    test_3()
    test_4()

    #invalid test cases
    test_5()
    test_6()