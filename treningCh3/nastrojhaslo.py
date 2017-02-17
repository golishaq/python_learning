#prezentuje działanie if-else oraz elif

from treningCh6 import slownik_test

password = input("Wprowadz haslo:")

if password == 'ptakilatajakluczem':
    print("Otwarte")
    print("Wyczuwam Twoją energię jesteś dziś...")
    mood = slownik_test.randint(1, 3)

    if mood == 1:
        #zjarany
        print("""
 ||||||||||||||||||||\
|||||||||||||||||||\\\\
|||/////////        \||
||/////   _____   ___\
||||||   / ___   /___/
|/   ||   /_(_) |/(_)
 | |  |          \  |
 |                \ /
 \__|   /      /___\
   |   /|\________\
   |    |\________|
   |    |      ||
   |    |  ____||___
   |    | /   __    \
   |    \/___/__\    \
   |   \________/\___/
   |            |""")
    elif mood == 2:
        #wątpiący
        print("""
  ,-'      `.
 /           |
 | __         |
 \   \__  -.  |
  ( o( o) 7/ /
 /  /     -|/
 \ (_     / |
  \ --.  /  | Wny
  (_____/   |
""")
    elif mood == 3:
        #zdziwiony
        print("""
      ,-"=-.
     .       |
     "='"=\   '
     `@] @'|   )
     ) ` ' ),-`
      \^_,  \,
  gpyy  ,(\,/ )`-.
""")
else:
    print("Error, error hasło nieprawidłowe!!")

input("\nAby zakończyć wciśniej 'ENTER'")
