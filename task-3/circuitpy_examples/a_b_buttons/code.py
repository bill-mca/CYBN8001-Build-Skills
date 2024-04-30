# Source Code From: https://learn.adafruit.com/make-it-sense/circuitpython-3
# This code imports the audiobusio, time, board, array and math libraries. 
import array
import math
import time

import audiobusio
import board

# There are also two helper functions. The first one "mean(values)" uses math to return a mean, or average. 
# It is used in the second helper. 
def mean(values):
    return sum(values) / len(values)

# The second helper function "normalized_rms(values)" uses math to return a normalised rms average. 
# These functions are then used to take multiple sound samples really quickly and average them 
# to get a more accurate reading.
def normalized_rms(values):
    minbuf = int(mean(values))
    sum_of_samples = sum(
        float(sample - minbuf) * (sample - minbuf)
        for sample in values
    )

    return math.sqrt(sum_of_samples / len(values))

# Next the microphone object and the samples variable are set. 
# Then initialization of the mic object so it's ready for use.

mic = audiobusio.PDMIn(
    board.MICROPHONE_CLOCK,
    board.MICROPHONE_DATA,
    sample_rate=16000,
    bit_depth=16
)
# So many questions
# What is the MICROPHONE CLOCK?
# What is the MICROPHONE DATA?
#  Can you ask for different sample rates?
#  Can you ask for different bit depths?
#  What resolution might you need for your application?
samples = array.array('H', [1] * 32)
# How many samples do you need?
# Try 8, 16, 32, 64, 128
# Are there differences?

mic.record(samples, len(samples))

while True:
    # The mic object starts taking sound samples. 
    # The normalised rms is used to find the average of a given set of samples, 
    # and that is the magnitude. Last, print the magnitude to the serial console.
    mic.record(samples, len(samples))
    magnitude = normalized_rms(samples)
    print(((magnitude),))
    time.sleep(0.1)
    
   
# Press the Serial button to see the values being printed out. 
# Press the Plotter icon to have Mu plot those values also. 
# Note that the Mu plotter looks for tuple values to print. 
# Tuples in Python come in parentheses () with comma separators. 
# If you have two values, a tuple would look like (1.0, 3.14) 
# Since we have only one value, we need to have it print out like (1.0,) 
# note the parentheses around the number, and the comma after the number. 
# Thus the extra parentheses and comma in print(((magnitude),)).

