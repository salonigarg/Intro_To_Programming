ques_list=["Hi. My name is _1_.Red has _2_ letters in it.Purple contain _3_ letters. What about blue. How many letters does it contain? _4_.",
    "Hyper text markup up language is abbreviated to _1_.It is used for building _2_ structures.Our browsers make requests to the server through _3_.WWW stands for _4_.",
    "There are five ways for a programmer to approach a problem.He shoud have _1_ thinking._2_ thinking is also necessary for a progammer.Tag em stands for _3_.Tag b stands for _4_."]
#Question list have questions corresponding to each level and each level have four blanks to fill in.
     
ans_list=[['saloni','three','six','four'],['html','web','internet','world wide web'],['procedural','abstract','emphasis','bold']]
#answer list contains answer of each level corresponding to the ques_list.

no_of_blank=4
#number of blank in each question is four.

beginner_index=0
intermediate_index=1
hard_index=2
no_of_level=['beginner','intermediate','hard']
#number of levels are three.

#level_choosen() function is defined here which takes the question and the answer list for that question according to the level choosen.
def level_choosen(ques,ans):
    ans_index=0
    #initially the answer given is none and since the total number of blank is four so a while loop is used which keeps the track of number of blanks filled.
    while ans_index<no_of_blank:
        #input taken from the user to fill the blank.
        input1=raw_input("What should come in "+str(ans_index+1)+"st blank:")
        if input1.lower()==ans[ans_index]:
            #if the input is correct then is is temporarily filled in the question.
            ques=ques.replace('_'+str(ans_index+1)+'_',ans[ans_index])
            ans_index+=1
            #question is displayed only with those filled answers which are given by user.
            print ques
        else:
            #if answer is incorrect,user again have to give answer for that blank.
            print "Wrong answer:(.Try again"

#level_no function is defined here.Its takes the level choosen by user as the argument and returns the question number to be displayed according to the level.
def level_no(user_input):
    if user_input.lower()=="beginner":
        return beginner_index;
    elif user_input.lower()=="intermediate":
        return intermediate_index;
    else:
        return hard_index;
    
#input() function is defined here.        
def input():
    #input is taken from the user in which user choose a level.
    user_input=raw_input("Enter the level you want to play:Beginner,Intermediate,Hard:\n")
    if user_input.lower() in no_of_level:
    #if user input exist in the number of level then a function level number is called which returns the question number to be displayed.
        ques_no=level_no(user_input)
        #question is displayed to the user according to the level choosen.
        print ques_list[ques_no]
        #level_choosen() function is called which takes the question and the answer list of that question number as the argument.
        level_choosen(ques_list[ques_no],ans_list[ques_no])
        #if the user want to continue playing,he/she press 'y' key else presses any other key to exit.
        print "Do you want to continue?"
        reply=raw_input("y if yes else press any key to exit:")
        if reply.lower() =='y':
            #input() function is called as the user want to continue playing.
            input()
        else:
            print "You choosed to quit.Thankyou for playing :)"
    else:
        print "You choosed wrong level:(.Please Enter the level again"
        #input() function is again called as the user choosed the wrong level.
        input()
    

input()
#input function is called that takes input from the user to choose a level.
