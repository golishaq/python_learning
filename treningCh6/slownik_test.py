#losowe wybieranie klucza ze slownika
from random import choice
# d={"wake up":"obudzic sie", "cheap":"tani", "sight":"widok"}
# el = choice(list(d.keys()))
# print(el)

d1={"make":"robic","candlelight":"blask swiecy","addiction ":"nalog","get":"dostac", "take off":"zdejmowac"}

for y in range(51):
    r=choice(list(d1.keys()))
    #x=input(r)
    print (r, d1[r])
