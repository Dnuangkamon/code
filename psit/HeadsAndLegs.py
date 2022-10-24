"""HeadsAndLegs"""
def main(numa, numb):
    """HeadsAndLegs"""
    rabbit = int(abs((numa*2-(numb))/2))
    bird = int(numa - abs((numa*2-(numb))/2))
    if numa == 0 and numb == 0:
        print("0 0")
    elif abs(rabbit*4) + abs(bird*2) == numb and numa != 0 and numb != 0:
        print(rabbit, bird)
    else:
        print("Impossible")
main(int(input()), int(input()))


def main():
    """HeadsAndLegs"""
    animals, legs = int(input()), int(input())
    rabbit = legs/2 - animals
    bird = animals - rabbit
    if rabbit < 0 or bird < 0 or not rabbit.is_integer() or not bird.is_integer():
        print("Impossible")
    else:
        print(int(rabbit), int(bird))
main()

"""HeadsAndLegs"""
def main(heads, legs):
    """HeadsAndLegs"""
    rabbit = (legs/2)-heads
    crow = heads-rabbit
    if rabbit < 0 or crow < 0 or legs % 2 != 0:
        return "Impossible"
    return "%d %d"%(rabbit, crow)
print(main(int(input()), int(input())))