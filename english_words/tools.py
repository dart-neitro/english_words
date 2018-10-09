"""

Functions for fork with this project

"""


def get_data_from_file(filename: str) -> list:
    """
    Get data from file. Trasform data to format.

    :param filename: filename file with data

    :return: formating list
    """
    try:
        with open(filename) as f:
            data = f.read()
        return trasform_data_from_file(data)
    except Exception as e:
        print(e)
    return []


def trasform_data_from_file(junk_data: str) -> list:
    """
    Clear data to need format
    :param junk_data:
    :return:
    """
    if not isinstance(junk_data, str):
        return []
    try:
        data = [
            [y.strip() for y in x.split('-')]
            for x in junk_data.lower().split('\n') if '-' in x]
    except Exception as e:
        print(e)
        data = []
    return data


def show_start_message() -> None:
    """
    Show start message with rules and description.

    :return: None
    """
    print(
        """
        Rules:
        * If you know translate this word or fraze enter "+";
        * If you NOT know translate this word or fraze enter "-";
        * If you want stop process enter "stop";
        * If you push enter (Clear message) use default value
        * For finish process show message "The end";

        Thank you for attention and Good Luck! Let's do it!
        
        """
    )
    return


def get_boolean_user_option(default: bool=False, text_question: str='') -> bool:
    """
    Get option from user via console

    :param default: default value
    :param text_question: Text message

    :return:
    """
    response = input("%s?" % text_question)
    if set('+-') - set(response) == set('+-'):
        return default
    elif '+' in response:
        return True
    return False


def show_word(
        english_word_iterator: object, results: dict={},
        show_familiar_words: bool=False) -> None:
    """
    Show 1 word

    :param english_word_iterator: Iteraror object
    :param results: statistic object
    :param show_familiar_words: Show translation if the word is familiar

    :return: None
    """

    next(english_word_iterator)
    response = input(
        "\nWord: %s " %
        english_word_iterator.current[0]
    )
    if not response:
        return

    if response and 'stop' in response:
        print('Stopping process')
        raise StopIteration('Stopping process')

    if '-' in response:
        results['wrong_answer'] += 1
        print(
            "Translate: %s" %
            english_word_iterator.current[1])

    elif '+' in response:
        results['success_answer'] += 1
        if show_familiar_words:
            print(
                "Translate: %s" %
                english_word_iterator.current[1])


