from pydioc.rng import RNG, FakeRNG


def run():
    fr = FakeRNG()
    print(fr.randInt())
    print(isinstance(fr, RNG))
    print(isinstance("fr", RNG))


if __name__ == "__main__":
    run()
