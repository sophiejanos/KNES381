def printRocket(): 
    print(
          """
          -
        / * \\
        | - |
        |   |
       /  :) \\
      /       \\ 
         |||
       """)


printRocket()

delay = 1000000
for i in range(20):
    print('          /')
    print('          \\')
sleep(delay/10000) 
delay = delay *0.9
