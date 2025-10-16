"""Utility functions for timing the preparation and baking of
'Guido's gorgeous lasagna'.

Constants
---------
- EXPECTED_BAKE_TIME: total minutes the lasagna should bake.
- PREPARATION_TIME : minutes of preparation per layer.

Functions
---------
- bake_time_remaining(elapsed_bake_time)
- preparation_time_in_minutes(number_of_layers)
- elapsed_time_in_minutes(number_of_layers, elapsed_bake_time)
"""



EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_time_in_minutes):
    """Return remaining oven time in minutes.

    :param x: int - minutes the lasagna has already baked.
    :return: int - minutes left to reach EXPECTED_BAKE_TIME.

    Computes the time still needed in the oven by subtracting the
    elapsed bake time from EXPECTED_BAKE_TIME.
    """
    return EXPECTED_BAKE_TIME - elapsed_time_in_minutes


# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.

def preparation_time_in_minutes(layers):
    """
    Return preparation time in minutes.

    :param layers: int - number of lasagna layers to assemble.
    :return: int - total preparation time (layers × PREPARATION_TIME).

    Calculates the time required to prepare the specified number of layers
    using the PREPARATION_TIME per layer constant.
    """
    
    return layers*PREPARATION_TIME

# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.
    



def elapsed_time_in_minutes(layers, elapsed_bake_time):
    """
    Return total elapsed time in minutes.

    :param layers: int - number of layers prepared.
    :param elapsed_bake_time: int - minutes already spent baking.
    :return: int - total time spent so far (prep + baking).

    Adds the preparation time for the given number of layers to the
    minutes already spent baking.
    """

    
    return preparation_time_in_minutes(layers)+elapsed_bake_time

    
