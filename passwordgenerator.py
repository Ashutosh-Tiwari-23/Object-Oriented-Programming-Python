import string
from random import choices
from string import ascii_letters
from string import punctuation


class Password:
    """A password of customized strength and  length.
    Encapsulate a randomly generate password depending on the user - specified strrngth and length, where the latter is optional
    and automatically set depending on the strength  (low ->8, mid-> 12, high -> 16). If a length is user specidified these presets
    are overridden regardless of hte strength.
    :param strength : a measure of the password's effectiveness against brute-force guessing.
    :type strength : str, optional

    :param length : the length of the the password
    :type length : int, optional
    """

    INPUT_UNIVERSE = {
        "numbers": list(range(10)),
        "letters": list(ascii_letters),
        "punctuation": list(punctuation),
    }

    DEFAULT_LENGTH = {"low": 8, "mid": 12, "high": 16}

    @classmethod
    def show_input_universe(cls):
        """Return the complete input universe from which characters are sampled.

        :return: The universe of characters from which random sampling is done to generate passwords.
        :rtype : dict (of list-s)
        """
        return cls.INPUT_UNIVERSE

    def __init__(self, strength="mid", length=None):
        self.strength = strength
        self.length = length

        self._generate()

    def _generate(self):
        """Generates the password according to the strength and length specified at initialization.

        :return: The randomly generated password
        :rtype : str

        """

        population = self.INPUT_UNIVERSE["letters"]
        length = self.length or self.DEFAULT_LENGTH.get(self.strength)

        if self.strength == "high":
            population += (
                self.INPUT_UNIVERSE["numbers"] + self.INPUT_UNIVERSE["punctuation"]
            )
        else:
            population += self.INPUT_UNIVERSE["numbers"]

        self.password = "".join(list(map(str, choices(population, k=length))))


if __name__ == "__main__":
    p_weak = Password(strength="low")
    print("Weak password : " + p_weak.password)

    p_mid = Password(strength="mid")
    print("Mid password :" + p_mid.password)

    p_high = Password(strength="high")
    print("Strong password: " + p_high.password)
