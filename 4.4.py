for i in range(1,200):
    i=int(input("Enter your point:"))
    if i>=1 and i<=51:
        print("Sorry!No prize this time")
        break
    elif i>=52 and i<=150:
        print("Congratulations1 You have won a wooden dog")
        break
    elif i>=152 and i<=180:
        print("Congratulations1 You have won a  Book")
        break
    else:
        print("Invalid point entered")
        break
