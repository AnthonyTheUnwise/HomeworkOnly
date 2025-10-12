# Question 16(b)
# Student name: Anthony Frtus
Names = []
Scores = []
Error = 0
def StudentNames():
    Name = ""
    while Name.lower() != "end":
        if Name != "":
            Names.append(Name)
        Name = input("Please enter the students name and enter \"end\" or \"End\" when complete:")
def StudentScores():
    Score = -2
    while Score != -1:
        if Score != -2:
            Score = Score / 2
            Scores.append(Score)
        Score = float(input("Please enter the students result and enter \"-1\" when complete:"))

StudentNames()
StudentScores()

if len(Names) != len(Scores):
    print("ERROR i cant be bothered im sorry i forgot to finish this its now midnight")
    Error = 1
print("Student results are:", Scores)
print("Student names are:", Names)

if Error == 1:
    Name = int(input("Enter the student missing:"))
    Index = int(input("What was their index:"))
    Names.insert(Index, Name)
High = 0
HighPos = 0
Low = 1000
LowPos = 0
Total = 0
for y in range(0, len(Scores)):
    if Scores[y] > High:
        High = Scores[y]
        HighPos = y
    if Scores[y] < Low:
        Low = Scores[y]
        LowPos = y
    Total += Scores[y]
print("The highest result was", High, "% by", Names[HighPos])
print("The lowest result was", Low, "% by", Names[LowPos])
print("The average was", Total//len(Names), "%")
