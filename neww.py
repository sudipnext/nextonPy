import matplotlib.pyplot as plt
import numpy as np
import random


def coinFlip():
    out = np.random.choice(["Head", "Tail"])
    return out

no_of_flips = int(input("Enter the total no. of flips"))
head_count = 0
no_head_array = []
no_of_flips_array =[]
for i in range(no_of_flips):
    outcome = coinFlip()
    if outcome == "Head":
        head_count += 1
    no_head_array.append(head_count/ (i+1))
    no_of_flips_array.append(i+1)

plt.plot(no_of_flips_array, no_head_array)
plt.xlabel("No. of flips")
plt.ylabel("No. of heads")
plt.axhline(y = 0.5, color = 'g', label= "True Probability", linestyle = '-')
plt.legend()
plt.show()
