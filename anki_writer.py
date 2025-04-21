import genanki


# Define the model for the flashcards
my_model = genanki.Model(
    123454321,
    'Dutch verb Model',
    fields=[
        {'name': 'Front'},
        {'name': 'Back'},
        {'name': 'details'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Front}}',
            'afmt': '{{Back}}<hr id="answer">{{details}}',
        },
    ],
    css="""
        .card {
            font-family: arial;
            font-size: 20px;
            text-align: center;
            color: black;
            background-color: white;
        }

        .answer
        {
            font-weight: bold;
        }

        .mybox
        {
            position: absolute;
            width: 200px;
            left: 50%;
            margin-left: -100px;
        }

        .conj-person
        {
            color: green;
        }


        .conj-item {
            display: flex;
                justify-content: space-between;
        }
        """
)


class DeckWriter:
    def __init__(self, deck_name) -> None:
        self.my_deck = genanki.Deck(
            2059400110,  # A unique ID for the deck
            deck_name)
        

    def add_verb(self, dutch, english, conjugation):
        self.my_deck.add_note(genanki.Note(
            model=my_model,
            fields=[dutch, english, conjugation],
        ))

    def flush(self):
        my_package = genanki.Package(self.my_deck)
        my_package.write_to_file(self.my_deck.name + '.apkg')