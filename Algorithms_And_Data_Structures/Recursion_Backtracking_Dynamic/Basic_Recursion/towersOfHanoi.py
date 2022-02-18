def towersOfHanoi(disk, source="Peg 1", middle="Peg 2", destination="Peg 3"):
    # We manipulate the smallest disk in the base case
    if disk == 0:
        print(f"Disk {disk} from {source} to {destination}")
        return
    # now move from source peg to destination peg using "helper" peg
    else:
        towersOfHanoi(disk-1, source, destination, middle)
        print(f"Disk {disk} from {source} to {destination}")
        towersOfHanoi(disk-1, middle, source, destination)

towersOfHanoi(2)



#Case for n == 3, read from lef to right

# 210   21      2       2       _       _       1       1       _       _
# _     _       1       10      10      1       _       0       0       _
# _     0       0       _       2       20      20      2       21      210

# starting_rod, source, A
# middle_rod, middle, B
# end_rod, destination, C