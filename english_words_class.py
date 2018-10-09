"""

This class is Iterator with mod rules

"""

import random
import copy
import sys


class EnglishWordsIterator:
    current = [None, None]

    def __init__(
            self, word_collections: list=[], randomize_collection: bool=False,
            sort_collection_by_name: bool=False):
        """
        Init iterator

        :param word_collections: collection couple [word, translate]
        :param randomize_collection: randomize list word_collection or not
        :param sort_collection_by_name: if not randomize list word_collection
        you can sorted by words

        """

        self.word_collections = copy.deepcopy(word_collections)

        if randomize_collection:
            random.shuffle(self.word_collections)
        elif sort_collection_by_name:
            self.word_collections = sorted(
                self.word_collections, key=lambda x: x[0])

    def __next__(self):
        """
        Iterator method

        :return: next value
        """

        if self.word_collections:
            self.current = self.word_collections.pop(0)
            return self.current
        raise StopIteration()

    def __repr__(self):
        """
        method __repr__

        :return:
        """

        return "%s => %s" % tuple(self.current)


if __name__ == "__main__":

    """
    Testing Iterator
    """

    test_data_junk = """
    aim - цель
    approximately - примерно
    attempt - попытка / пробовать
    accessible - доступные
    agenda - повестка дня
    arises - возникать
    amend - изменить
    awareness - осведомленность
    adequate - адекватный 
    
    Bootcamp - учебный лагерь
    beyond - за / вне/ выше
    badge - значек
    bring - предлагать
    burden - бремя
    
    consist - состоять
    cause - причина / дело
    Confluence - пересечение
    comply - соблюдать
    
    decide - принимать решение
    disclosed - раскрывать
    
    edge - край
    effort - усилия
    excellence - превосходство
    essential - существенный / неотъемлемость / предметы первой необходимости
    establish -  установать
    
    frequently - часто
    
    grade - оценка
    
    handout materials - раздаточные материалы
    harness - впрягать / жгут
    
    influence - влияние/влиять
    involve - вовлеченность
    instead - взамен
    intervene - вмешиваться
    improper - неправильный
    
    leakage - утечка
    
    mindset - образ мышления
    measure - измерение / мера
    meanwhile - тем временем / между тем
    misuse - злоупотреблять
    
    perform - выполнять
    pipe - труба
    pipeline - турбопровод / источник информации
    provision - положение
    propositions - предложения
    propagate - распространять
    promptly  - быстро
    phase - фаза
    preparation - подготовка
    prohibit - запрещать
    
    robust - крепкий
    
    governance - управление
    
    same - тот же
    
    thoroughly - тщательно
    threat - угроза
    
    reliably - надежно
    reflect - отражать
    
    quizzes - викторины
    
    vulnerability - уязвимость / ранимость
    
    weak - слабый
    """

    test_data = [
        [y.strip() for y in x.split('-')]
        for x in test_data_junk.lower().split('\n') if '-' in x]

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
