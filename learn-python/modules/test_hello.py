# test_hello.py
import hello  # Import the hello module


def test_world(capfd):
    hello.world()
    out, err = capfd.readouterr()
    assert (
        out == "Hello, World!\n"
    ), "The world function does not print the correct statement"


def test_shark():
    assert hello.shark == "Sammy", "The shark variable is not correctly defined"


def test_octopus(capfd):
    octopus = hello.Octopus("Ollie", "red")
    octopus.tell_me_about_the_octopus()
    out, err = capfd.readouterr()
    expected_output = "This octopus is red.\nOllie is the octopus's name.\n"
    assert (
        out == expected_output
    ), "The tell_me_about_the_octopus method does not work correctly"
