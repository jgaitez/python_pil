# Models Imports
from heroe.models import Hero

def hayHeroe(pk):

    print("dentro de hay heroe")
    try:
        heroe = Hero.objects.get(id=pk)

        return [True, heroe]

    except:
        return [False]