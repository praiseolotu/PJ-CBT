def CBTtimer(question_prompt, time_limit):
    """ THIS function implements the timer,
    that times the users for answering the question
    for a specific amount of time. """

    #iterate through the questions
    for each_question in questions:
        print(each_question)

        #Start the timer
        begin_time = time.time()

        #wait for the user to input their answer
        answer = input(each_question.prompt)

        #Stop the timer and calculate the spent time
        endthe_time = time.time()
        elasped_time = endthe_time - begin_time

        #If the elasped time is greater than the time_limit, Break out of the loop
        if elasped_time > time_limit:
            print("thank you for your time.")
            break 

print("Thank you for participating in the CBT")

time_limit = 60 # 1 minute
CBTtimer(question_prompt, time_limit)
