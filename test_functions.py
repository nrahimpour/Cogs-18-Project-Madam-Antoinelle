"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from functions import draw_a_card, interpret, do_a_reading, start
##
##

#tests if draw_a_card runs and if the return has 2 elements in the tuple
def test_card():
    assert draw_a_card() == None
    assert len(reading.draw_a_card()) == 2

#tests if interpret runs and if it returns the answers in a string format
def test_interpret():
    assert interpret() == None
    assert isinstance(reading.interpret('Major Arcana', 'The Fool')) == str

#tests if do_a_reading runs
def test_reading():
    assert do_a_reading() == None
    assert random_suit in tarot_deck.keys()
    assert random_draw in tarot_deck[random_suit].keys()

#tests if start runs and if the username returns as a string and if the exiting function works
def test_start():
    assert fortune_teller.start() == None
    assert type(user_name) == str
    assert start(['exit']) == True
                 
    