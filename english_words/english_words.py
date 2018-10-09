"""

This class is Iterator with mod rules

"""

import random
import copy


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

