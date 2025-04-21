from scrapper import get_conjugation

from anki_writer import DeckWriter


writer = DeckWriter("DutchVerbs")


verbs = open("verbs.txt")


for line in verbs.readlines():
    verb = line.strip()
    try:
        writer.add_verb(verb, "TODO", get_conjugation(verb))
    except Exception:
        print("Could not add verb: " + verb)



writer.flush()

