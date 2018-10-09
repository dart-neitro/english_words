"""

This class is Iterator with mod rules

"""
import sys

from english_words.english_words import EnglishWordsIterator
from english_words import tools


if __name__ == "__main__":

    """
    Testing Iterator
    """
    data = tools.get_data_from_file("./tmp/data.txt")
    print(data)

    test_data = []

    randomize_collection = False
    sort_collection_by_name = False
    show_familiar_words = False

    if test_data:

        print("""
        Rules:
        * If you know translate this word or fraze enter "+";
        * If you NOT know translate this word or fraze enter "-";
        * If you want stop process enter "stop";
        * For finish process show message "The end";

        Thank you for attention and Good Luck! Let's do it!
        """)

        response = input("Randomize it? ")
        if '+' in response:
            randomize_collection = True

        if not randomize_collection:
            response = input("Sort by name? ")
            if '+' in response:
                sort_collection_by_name = True

        response = input("Do you want to show familiar words? ")
        if '+' in response:
            show_familiar_words = True

    english_word_iterator = EnglishWordsIterator(
        word_collections=test_data,
        randomize_collection=randomize_collection,
        sort_collection_by_name=sort_collection_by_name)

    total, success_answer, wrong_answer = len(test_data), 0, 0

    while True:
        try:
            next(english_word_iterator)
            response = input(
                "\nWord: %s " %
                english_word_iterator.current[0]
            )
            if not response:
                continue

            if response and 'stop' in response:
                print('Stopping process')
                break

            if '-' in response:
                wrong_answer += 1
                print(
                    "Translate: %s" %
                    english_word_iterator.current[1])

            elif '+' in response:
                success_answer += 1
                if show_familiar_words:
                    print(
                        "Translate: %s" %
                        english_word_iterator.current[1])

        except StopIteration:
            break
        except Exception as e:
            print('raise Exception')
            print(e)

    if not total:
        print("No data to show")
        sys.exit(0)

    total_answer = success_answer + wrong_answer
    print("Process: %.2f%%" % (float(100 * total_answer) / total))
    print("Total words: %s" % total)
    print("Use words: %s" % total_answer)

    print("Success rate: %.2f%%" % (
            100 * float(success_answer) / total_answer))
    print("Success answers: %s" % success_answer)
    print("Wrong answers: %s" % wrong_answer)

    print('The end')