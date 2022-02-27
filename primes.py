"""
This module help you to find prime numbers in a range and
prime numbers of a certain sequence length.
You can run it from command line or import it as a module.
"""

import argparse


parser = argparse.ArgumentParser(
    prog="primes", description="Find primes in a range or a sequence"
)
parser.add_argument("range", nargs="*", type=int, help="Start position")
args = parser.parse_args()


class Prime:
    """
    Just a class defining...
    """

    def __init__(self, start=0, stop=0):
        self.start = start
        self.stop = stop

    def prime_rng(self) -> "generator":
        """
        The function calculates prime numbers in a range of 'start' to 'stop-1'

        Args:
                an instance containing start and stop values

        Returns:
                generator: a generator of prime numbers
        """

        for i in range(self.start, self.stop):
            if is_prime(i):
                yield i

    def prime_seq(self) -> list:
        """
        The function returnes a list of prime numbers of length of 'start' to 'stop'

        Args:
                an instance containing start and stop values

        Returns:
                List[int]: a list of prime numbers
        """

        primes = []
        step = self.start
        while len(primes) < self.stop - self.start:
            if is_prime(step):
                primes.append(step)
            step += 1

        return primes


def is_prime(num: int) -> bool:
    """
    This function checks if a number is a prime number

        Args:
        num (int): a number to check

        Returns:
        bool: True if a number is a prime else False
    """

    flag = True
    for i in range(2, int((num) ** 0.5) + 1):
        if not num % i:
            flag = False
            break
    return flag and num > 1


def main() -> None:
    """
    The function is used to display results if the file run as a script
    """
    prime = Prime(*args.range)
    print(f"\nPrime numbers in a range of {prime.start} to {prime.stop}:")
    print(" \n\t", *list(prime.prime_rng()), end="\n\n")
    print(f"Prime numbers sequence of length from {prime.start} to {prime.stop}:")
    print(" \n\t", *prime.prime_seq(), end="\n\n")


if __name__ == "__main__":
    main()
else:
    print("primes loaded as a module\n")
