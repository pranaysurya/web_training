def score():

    packages = int(input("Select how many packages were delivered: "))

    collisions = int(input("Select how many collisions happened: "))

    packages_score = packages * 50

    collisions_score = collisions * -10

    total_score = packages_score + collisions_score

    if packages > collisions:
        total_score += 500

    print("The score is " + str(total_score))

score()