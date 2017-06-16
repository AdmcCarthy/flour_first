#!/usr/bin/python


def choose_which_bread(flour_t, flour_w, bread_t, baby=true):
    """Like choose youré own
    adventure but with more
    bread.

    Find out which bread suits
    today.

    flout_t is the type of flour
    availble while flour_w is the
    weight of this flour.

    bread_t is the type of bread
    that´s wanted.

    baby=True implies this recipe
    should be suitable for a small
    baby or child. Minize salt and sugar.
    No honey.
    """

    bread_list = ["white", "brown"]
    flour_list = ["all purpose", "rye"]

    assert bread_t in bread_list
    assert flour_t in flour_list
