from faker import Faker

fkr = Faker()

rubrics_with_tags = {
    "Computer science": (
        "windows", "linux", "macos", "ios", "pc", "hardware", "software"
    ),
    "Automobiles": (
        "sport cars", "racing", "cars", "rally", "formula 1"
    ),
    "Sport": (
        "football", "swimming", "basketball", "hockey", "volleyball", "rhytmic gymnastics"
    ),
    "Computer gemes": (
        "strategy", "shotting games", "MMORPG", "quests", "simulators", "fighting games"
    ),
    "Fashion": (
        "classic style", "casual", "sports style", "glamour", "new look", "lingerie"
    ),
    "Science": (
        "geophysics", "cryptography", "psychology", "materials science", "religious science", "natural science"
    ),
    "Medicine": (
        "neurosurgery", "surgical dentisty", "otorhinolaryngology", "plastic surgery", "gynecology and urology"
    ),
    "Culture": (
        "spirital", "artistic", "physical", "mass culture", "material"
    ),

}


def get_jobs(amount=1):
    return [fkr.job() for _ in range(amount)]


def get_names(amount=1):
    return [fkr.name() for _ in range(amount)]


def get_emails(amount=1):
    return [fkr.email() for _ in range(amount)]


def get_title(words=3):
    return [fkr.sentence(nb_words=words, variable_nb_words=False)]


def get_content(sentences=20):
    return [fkr.paragraph(nb_sentences=sentences)]