from hello import greet

def test_greet_with_name():
    assert greet("Santiago") == "Hola, Santiago!"

def test_greet_default():
    assert greet() == "Hola, mundo!"
