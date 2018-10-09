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
    try:
        data = tools.get_data_from_file("./tmp/data.txt")

        test_data = data
        results = dict(
            total=len(test_data),
            success_answer=0,
            wrong_answer=0,
            wrong_success_answer=0
        )

        if not results.get('total'):
            print("No data to show")
            sys.exit(0)

        tools.show_start_message()

        randomize_collection = tools.get_boolean_user_option(
            default=True,
            text_question="Randomize it"
        )
        if not randomize_collection:
            sort_collection_by_name = tools.get_boolean_user_option(
                default=False,
                text_question="Sort by name"
            )
        else:
            sort_collection_by_name = False

        show_familiar_words = tools.get_boolean_user_option(
            default=True,
            text_question="Do you want to show familiar words"
        )

        english_word_iterator = EnglishWordsIterator(
            word_collections=test_data,
            randomize_collection=randomize_collection,
            sort_collection_by_name=sort_collection_by_name)

        tools.show_all_words(
                    english_word_iterator=english_word_iterator,
                    results=results,
                    show_familiar_words=show_familiar_words)

        tools.show_statistic(results)
    except EOFError:
        print("The forced stop method is used")
