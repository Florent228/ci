import random

def obtenir_citation():
    citations = [
        "La vie est ce qui arrive quand on a d'autres projets. — John Lennon",
        "Le seul moyen de faire du bon travail est d'aimer ce que vous faites. — Steve Jobs",
        "L'imagination est plus importante que le savoir. — Albert Einstein"
    ]
    return random.choice(citations)

if __name__ == "__main__":
    print(obtenir_citation())
