#użycie break i continue

count = 0
while True:
    count += 1
    #koczy jeśli dojdzie do 10
    if count > 10:
        break
    #pominiecie liczby 5
    if count == 5:
        continue
    print(count)
input("\nAby zakończyć wciśniej 'ENTER'")