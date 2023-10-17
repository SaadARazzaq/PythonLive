from time import sleep
from reloading import reloading

@reloading
def func(num):
    if num%2:
        print(f"The Number is {num} is odd")
    else:
        pass
    sleep(2)

for i in range(100):
    func(i)
