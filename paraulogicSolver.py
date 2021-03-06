def isChar(c):
    return isinstance(c, str) and len(c) == 1

class paraulogicSolver(object):
    """docstring for paraulogicSolver."""

    def __init__(self, blaves, vermella):
        """..."""
        if not isinstance(blaves, set) and len(set) != 6:
            raise TypeError("Blaves ha de ser un conjunt de mida exactament 6")
        for c in blaves:
            if not isChar(c):
                raise TypeError("Els elements del conjunt blaves han de ser caràcters")
        if not isChar(vermella):
            raise TypeError("Vermella ha de ser un caràcter")

        self.vermella = vermella # Needed letter
        self.blaves = blaves # Available letters
        self._all_letters = {'·','-'}
        self._all_letters = self._all_letters.union(self.blaves)
        self._all_letters.add(self.vermella)

        self._data = self._loadData()

        self.respostes = self._answers()
        self.tutis = self._allIn()

    def __repr__(self):
        """..."""
        return self.mostrarRespostes(True)

# ---------------------------------- PUBLIC ----------------------------------

    def mostrarRespostes(self, ret=False):
        """..."""
        output =  'AQUI TENS TOTES LES RESPOSTES QUE HE TROBAT!\n\n'
        output += '> RECORDA: No totes són necessariament vàlides per al joc,\n'
        output += '           jo em vaso en un diccionari terminològic i no en\n'
        output += '           l\'IEC directament. Això vol dir, que entre\n'
        output += '           d\'altres puc dir-te conjugacions de verbs; que\n'
        output += '           no valen al Paraulògic.\n\n'
        output += '------------------------------------------------------------\n\n'
        if ret:
            return output + self._prettyAnswers()
        print(output + self._prettyAnswers())

    def mostrarTutis(self):
        """..."""
        if len(self.tutis) == 0:
            print('Per la combinació d\'avui no he trobat tutis...\n')
            return

        output =  'AQUI TENS TOTS ELS TUTIS QUE HE TROBAT!\n\n'
        output += '> RECORDA: No totes són necessariament vàlides per al joc,\n'
        output += '           jo em vaso en un diccionari terminològic i no en\n'
        output += '           l\'IEC directament. Això vol dir, que entre\n'
        output += '           d\'altres puc dir-te conjugacions de verbs; que\n'
        output += '           no valen al Paraulògic.\n\n'
        output += '------------------------------------------------------------\n\n'
        print(output + self._prettyAnswers(False))

# ---------------------------------- PRIVATE ---------------------------------

    def _loadData(self):
        """..."""
        diccionary = open('DISC2-LP.txt', 'r')
        # remove '\n' and invalid short words
        return {line[:-1].lower() for line in diccionary if len(line[:-1]) >= 3}

    def _answers(self):
        """..."""
        answers = set()

        for word in self._data:
            if word.find(self.vermella) != -1:
                valid = True
                for letter in word:
                    if letter not in self._all_letters:
                        valid = False

                if valid:
                    answers.add(word)

        return answers

    def _allIn(self):
        """..."""
        answers = set()

        for word in self.respostes:
            valid = True
            for must in self._all_letters.difference({'·','-'}):
                if word.find(must) == -1:
                    valid = False
            if valid:
                answers.add(word)

        return answers

    def _prettyAnswers(self, all=True):
        """..."""
        output = ''
        to_display = self.respostes if all else self.tutis

        for i, word in enumerate(sorted(to_display)):
            tick = '+ ' if i%6 < 3 else '- '
            endline = '\n' if i%3 == 2 else ''
            spaces = ' '*(18-len(word))

            output += tick + word + spaces + endline

        return output
