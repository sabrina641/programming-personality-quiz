"""A collection of function for doing my project."""

def my_func():
    pass

def my_other_func():
    pass

from IPython.display import YouTubeVideo

def game_choice():
    
    """Game choice will start quiz1 or quiz2 depending on input.
    
    Parameters
    ----------
    none : none
        none
        
    Returns
    -------
    quiz1 : function
        Function that returns what programming language you should learn.
    quiz2 : function
        Function that returns what programming language you should learn.
    """ 

    intro = input(""" \033[32m Welcome to the personality quiz that will help you decide
what programming language you should learn! 

You have to decide if you would like to take:
Quiz 1 that will help you decide between: Python, Java, and r!
or
Quiz 2 which will help you decide between: SQL, C++, and Swift!
\nPlease type: Quiz1 or Quiz2 \n""")

 
    #print(intro)
    
    if intro.lower() == "quiz1" or intro.lower() == "quiz 1":
        return quiz1()
    elif intro.lower() == "quiz2" or intro.lower() == "quiz 2":
        return quiz2()
    else:
        print("Thats not an option! Let's restart and try again!")

def quiz1():
    
    """Will return the dictionary key with the greatest value.
    
    Parameters
    ----------
    none : none
        none
        
    Returns
    -------
    python : dictionary key
        Result of quiz one and the functions within quiz1.
    java : dictionary key
        Result of quiz one and the functions within quiz1.
    r : dictionary key
        Result of quiz one and the functions within quiz1.

    """ 
    
    #This is a personality quiz that will tell you what type of programming language you should learn
    
    game_dict = {"python" : 0,
                "r" : 0,
                "java" : 0}

    user_name = input("\033[32m \nEnter name: ")
    greeting = "\n Hi, " + user_name + "! Let's find out what programming language you should learn?\n"
    print(greeting)

    start = input("\033[32m Are you ready to start? \n \nSelect: yes or no? \n")
    if start.lower() != "yes":
        print("Oh no! Come back to take the quiz later!")
        return
    
    print("Awesome lets begin!")

    print("\nPlease respond to the following questions with your answers corresponding letter. \n")
    
    q1 = input("""\033[32m What types of games do you like to play? 
    \n A: Puzzle games \n B: Simulation games \n C: Strategy games \n""")

    def part1(q1):
        
        if q1.lower() == "a":
            game_dict["python"] += 1
        elif q1.lower() == "b":
            game_dict["r"] += 1
        elif q1.lower() == "c":
            game_dict["java"] += 1
        elif q1.lower() != "a" or q1.lower() != "b"or q1.lower() != "c":
            print("\033[31m ERROR: Invalid input. Please restart and try again")
            
    part1(q1)

    q2 = input("""\033[32m \nWhat is your favorite subject in school? 
               \n A: Math \n B: Science \n C: English \n""")

    def part2(q2):
        
        if q2.lower() == "a":
            game_dict["r"] += 1
        elif q2.lower() == "b":
            game_dict["java"] += 1
        elif q2.lower() == "c":
            game_dict["python"] += 1
        elif q2.lower() != "a" or q2.lower() != "b"or q2.lower() != "c":
            print("\033[31m ERROR: Invalid input. Please restart and try again")
            
    part2(q2)


    q3 = input("""\033[32m \nHow much time are you willing to dedicate to learning your programming language? 
           \n A: 0 - 4 months \n B: 5 - 7 months \n C: 7+ months \n""")
    def part3(q3):
        
        if q3.lower() == "a":
            game_dict["python"] += 1
        elif q3.lower() == "b":
            game_dict["java"] += 1
        elif q3.lower() == "c":
            game_dict["r"] += 1
        elif q3.lower() != "a" or q3.lower() != "b"or q3.lower() != "c":
            print("\033[31m ERROR: Invalid input. Please restart and try again")
            
    part3(q3)

    q4 = input("""\033[32m \nWhat industry would you like to get into? 
               \n A: Cyber Security \n B: Data Analysis \n C: Research \n""")

    def part4(q4):
        
        if q4.lower() == "a":
            game_dict["java"] += 1
        elif q4.lower() == "b":
            game_dict["python"] += 1
        elif q4.lower() == "c":
            game_dict["r"] += 1
        elif q4.lower() != "a" or q4.lower() != "b"or q4.lower() != "c":
            print("\033[31m ERROR: Invalid input. Please restart and try again")
            
    part4(q4)

    
    def results():
        
        #I came up with this code because I didnt want people to be able to tie
        #The if statement makes sure that there was no invalid input that would result in a tie
        #the first three elifs are returning results if there is no tie
        #the last three elifs are asking tie breaker questions if two keys are exactly equal
        
        if game_dict["python"] <= 1 and game_dict["java"] <= 1 and game_dict["r"] <= 1:
            return "\033[31m \nIt looks like one of your responses recieved an error message. Please try again."
        elif game_dict["python"] > game_dict["r"] and game_dict["python"] > game_dict["java"]:
            return "\033[32m \nIt looks like you should learn python!"
        elif game_dict["r"] > game_dict["python"] and game_dict["r"] > game_dict["java"]:
            return "\033[32m \nIt looks like you should learn r!"
        elif game_dict["java"] > game_dict["r"] and game_dict["java"] > game_dict["python"]:
            return "\033[32m \nIt looks like you should learn java!"
        elif game_dict["python"] == game_dict["java"]:
            q5 = input("""\033[32m Which statement describes you best?:\n A: Slow and steady wins the race? 
            \n OR \n B: Early bird gets the worm!\n""")
            if q5.lower() == "a":
                game_dict["python"] += 1
            elif q5.lower() == "b":
                game_dict["java"] += 1
        elif game_dict["python"] == game_dict["r"]:
            q6 = input("\033[32m Are you more interested in: \n A: Machine Learning \n OR \n B: Statistical Analysis \n")
            if q6.lower() == "a":
                game_dict["python"] += 1
            elif q6.lower() == "b":
                game_dict["r"] += 1
        elif game_dict["r"] == game_dict["java"]:
            q7 = input("\033[32m Which do you value more? \n A: Compatability \n \tOR \n B: High Preformance \n")
            if q7.lower() == "a":
                game_dict["java"] += 1
            elif q7.lower() == "b":
                game_dict["r"] += 1

    results()

    def results_2():
        
        #this function is to produce a response if a tie breaker question was asked
        
        if game_dict["python"] < 2 and game_dict["java"] < 2 and game_dict["r"] < 2:
            print("\033[31m \nIt looks like one of your responses recieved an error message. Please try again.")
        elif game_dict["python"] > game_dict["r"] and game_dict["python"] > game_dict["java"]:
            print("\033[32m \nIt looks like you should learn python!")
        elif game_dict["r"] > game_dict["python"] and game_dict["r"] > game_dict["java"]:
            print("\033[32m \nIt looks like you should learn r!")
        elif game_dict["java"] > game_dict["python"] and game_dict["java"] > game_dict["r"]:
            print("\033[32m \nIt looks like you should learn java!")
            
    results_2()

def quiz2():
    
    """Will return the dictionary key with the greatest value.
    
    Parameters
    ----------
    none : none
        none
        
    Returns
    -------
    SQL : dictionary key
        Result of quiz one and the functions within quiz2.
    C++ : dictionary key
        Result of quiz one and the functions within quiz2.
    Swift : dictionary key
        Result of quiz one and the functions within quiz2.

    """ 
    
    #This is a personality quiz2 that will help decide between SQL, swift, and C++.
    #These are the same functions as Quiz1 but with a few different questions
    #using a new dictionary
    
    game2_dict = {"SQL" : 0,
                "c++" : 0,
                "swift" : 0}

    user_name = input("\033[32m \nEnter name: ")
    greeting = "\n Hi, " + user_name + "! Let's find out what programming language you should learn?"
    print(greeting)

    start = input("\033[32m Are you ready to start? \n \n Select: yes or no? \n")
    if start.lower() != "yes":
        print("\nOh no! Come back to take the quiz later!")
        return
    
    print("\nAwesome lets begin!")

    print("\nPlease respond to the following questions with your answers corresponding letter. \n")
    
    qa = input("""\033[32m What do you like to do in your free time?
    \n A: Read \n B: Video games \n C: Social Media \n""")

    def part_a(qa):
        
        if qa.lower() == "a":
            game2_dict["swift"] += 1
        elif qa.lower() == "b":
            game2_dict["c++"] += 1
        elif qa.lower() == "c":
            game2_dict["SQL"] += 1
        elif qa.lower() != "a" or qa.lower() != "b"or qa.lower() != "c":
            print("\033[31m ERROR: Invalid input. Please restart and try again")
            
    part_a(qa)

    qb = input("""\033[32m \nWhat is your favorite subject in school?
    \n A: Computer Science \n B: Accounting \n C: Marketing \n""")

    def part_b(qb):
        
        if qb.lower() == "a":
            game2_dict["c++"] += 1
        elif qb.lower() == "b":
            game2_dict["swift"] += 1
        elif qb.lower() == "c":
            game2_dict["SQL"] += 1
        elif qb.lower() != "a" or qb.lower() != "b"or qb.lower() != "c":
            print("\033[31m ERROR: Invalid input. Please restart and try again")
            
    part_b(qb)


    qc = input("""\033[32m \nHow much time are you willing to dedicate to learning your programming language?
    \n A: 0 - 4 months \n B: 5 - 7 months \n C: 7+ months \n""")
    def part_c(qc):
        
        if qc.lower() == "a":
            game2_dict["SQL"] += 1
        elif qc.lower() == "b":
            game2_dict["swift"] += 1
        elif qc.lower() == "c":
            game2_dict["c++"] += 1
        elif qc.lower() != "a" or qc.lower() != "b"or qc.lower() != "c":
            print("\033[31m ERROR: Invalid input. Please restart and try again")
            
    part_c(qc)

    qd = input("""\033[32m \nWhat industry would you like to get into?
    \n A: Game Development \n B: Finance \n C: Marketing \n""")

    def partd(qd):
        
        if qd.lower() == "a":
            game2_dict["c++"] += 1
        elif qd.lower() == "b":
            game2_dict["swift"] += 1
        elif qd.lower() == "c":
            game2_dict["SQL"] += 1
        elif qd.lower() != "a" or qd.lower() != "b"or qd.lower() != "c":
            print("\033[31m ERROR: Invalid input. Please restart and try again")
            
    partd(qd)

    
    def results_3():
        
        if game2_dict["swift"] <= 1 and game2_dict["SQL"] <= 1 and game2_dict["c++"] <= 1:
            return "\033[31m \nIt looks like one of your responses recieved an error message. Please try again."
        elif game2_dict["swift"] > game2_dict["SQL"] and game2_dict["swift"] > game2_dict["c++"]:
            return "\033[32m \nIt looks like you should learn Swift!"
        elif game2_dict["c++"] > game2_dict["SQL"] and game2_dict["c++"] > game2_dict["swift"]:
            return "\033[32m \nIt looks like you should learn C++!"
        elif game2_dict["SQL"] > game2_dict["swift"] and game2_dict["SQL"] > game2_dict["c++"]:
            return "\033[32m \nIt looks like you should learn SQL!"
        elif game2_dict["c++"] == game2_dict["swift"]:
            qe = input("""\033[32m Which statement describes you best?:
            \n A: You are always up for a challenge. \n OR \n B: You like to be a pioneer!\n""")
            if qe.lower() == "a":
                game2_dict["c++"] += 1
            elif qe.lower() == "b":
                game2_dict["swift"] += 1
        elif game2_dict["swift"] == game2_dict["SQL"]:
            qf = input("\033[32m What product do you like the best? in: \n A: Apple \n OR \n B: Microsoft \n")
            if qf.lower() == "a":
                game2_dict["swift"] += 1
            elif qf.lower() == "b":
                game2_dict["SQL"] += 1
        elif game2_dict["SQL"] == game2_dict["c++"]:
            qg = input("""\033[32m Which statement do you relate to the most? 
            \n A: You like to beat around the bush. \n \tOR 
            \n B: It's more about the journey rather than the destination. \n""")
            if qg.lower() == "a":
                game2_dict["SQL"] += 1
            elif qg.lower() == "b":
                game2_dict["c++"] += 1

    results_3()

    def results_4():
        
        if game2_dict["swift"] < 2 and game2_dict["SQL"] < 2 and game2_dict["c++"] < 2:
            print("\033[31m \nIt looks like one or more of your responses recieved an error message. Please try again.")
        elif game2_dict["swift"] > game2_dict["c++"] and game2_dict["swift"] > game2_dict["SQL"]:
            print("\033[32m \nIt looks like you should learn Swift!")
        elif game2_dict["c++"] > game2_dict["swift"] and game2_dict["c++"] > game2_dict["SQL"]:
            print("\033[32m \nIt looks like you should learn C++!")
        elif game2_dict["SQL"] > game2_dict["c++"] and game2_dict["SQL"] > game2_dict["swift"]:
            print("\033[32m \nIt looks like you should learn SQL!")
            
    results_4()
    
def video():
    
    #I learned how to do this online. It was really easy to do, it is mostly all done...
    #In the imports at the top of the program
    
    """ stores and returns programming lesson videos from youtube.
    ----------
    none : none
        none
        
    Returns
    -------
    python_video : variable
        Video lesson on python.
    java_video : variable
        Video lesson on java.
    r_video : variable
        Video lesson on r.
    sql_video : variable
        Video lesson on sql.
    swift_video : variable
        Video lesson on swift.
    c_video : variable
        Video lesson on c.

    """ 
    
    python_video = YouTubeVideo("t8pPdKYpowI")
    java_video = YouTubeVideo("grEKMHGYyns")
    r_video = YouTubeVideo("KlsYCECWEWE")
    sql_video = YouTubeVideo("AA7i2GcTGwU")
    swift_video = YouTubeVideo("FcsY1YPBwzQ")
    c_video = YouTubeVideo("vLnPwxZdW4Y")
    
    more_info = input("""\033[32m Would you like to start learning a programming language now? 
    \nChoose one of the following:\n A: Python\n B: Java\n C: r \n D: SQL \n E: Swift \n F: C++
    \n or enter any other character to exit the program\n""")
    
    if more_info.lower() == "a":
        display(python_video)
    elif more_info.lower() == "b":
        display(java_video)
    elif more_info.lower() == "c":
        display(r_video)
    elif more_info.lower() == "d":
        display(sql_video)
    elif more_info.lower() == "e":
        display(swift_video)
    elif more_info.lower() == "f":
        display(c_video)
    else:
        print("Okay! See you later!")
        return

game_choice()
video()
