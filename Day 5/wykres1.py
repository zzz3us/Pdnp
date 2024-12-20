import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, color="yellow")
plt.grid()
plt.xticks([1, 2, 3, 4, 5, 6])
plt.xlabel("Oś X")
plt.ylabel("Oś Y")
plt.title("Prosta liniowa")

plt.show()