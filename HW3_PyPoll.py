# Module for reading CSV files
import os
import csv
#Open the CSV file and skip the header
csvpath = os.path.join('PyPoll','Resources','election_data.csv')
txtpath = os.path.join('PyPoll','Resources','election_results.txt')
with open (csvpath, newline="") as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)
    # create the varibles
    total_votes = 0
    khan_count = 0
    correry_count = 0
    li_count = 0
    otooley_count = 0
       
    # read one line at a time
    for row in csv_reader:
        #increase counter for votes
        total_votes = total_votes + 1

        #loop for candidate count:
        candidate_name = row[2]

        if candidate_name == "Khan":
            khan_count = khan_count + 1
        elif candidate_name == "Correy":
            correry_count = correry_count + 1
        elif candidate_name == "Li":
            li_count = li_count + 1
        elif candidate_name == "O'Tooley":
            otooley_count = otooley_count + 1
        
    #calculate candidate percent
    khan_percent = (khan_count/total_votes)*100
    correry_percent = (correry_count/total_votes)*100
    li_percent = (li_count/total_votes)*100
    otooley_percent = (otooley_count/total_votes)*100

    #calculate the winner 
    if khan_percent > max(correry_percent, li_percent, otooley_percent):
        winner = "Khan"
    elif correry_percent > max(khan_percent, li_percent, otooley_percent):
        winner = "Correy"  
    elif li_percent > max(correry_percent, khan_percent, otooley_percent):
        winner = "Li"
    else:
        winner = "O'Tooley"

    #print results to terminal
    print("------------------------------")
    print(f"Election Results")
    print("------------------------------")
    print(f"Total votes: {total_votes}")
    print("------------------------------")
    print(f"Khan: %{round(khan_percent,2)}({khan_count})")
    print(f"Correy: %{round(correry_percent,2)}({correry_count})")
    print(f"Li: %{round(li_percent,2)}({li_count})")
    print(f"O'Tooley: %{round(otooley_percent,2)}({otooley_count})")
    print("------------------------------")
    print(f"Winner!: {winner}")
    print("------------------------------")

    #print to text file
    with open("election_results.txt", "w") as text_file:
        text_file.write("------------------------------\n")
        text_file.write(f"Election Results\n")
        text_file.write("------------------------------\n")
        text_file.write(f"Total votes: {total_votes}\n")
        text_file.write("------------------------------\n")
        text_file.write(f"Khan: %{round(khan_percent,2)}({khan_count})\n")
        text_file.write(f"Correy: %{round(correry_percent,2)}({correry_count})\n")
        text_file.write(f"Li: %{round(li_percent,2)}({li_count})\n")
        text_file.write(f"O'Tooley: %{round(otooley_percent,2)}({otooley_count})\n")
        text_file.write("------------------------------\n")
        text_file.write(f"Winner!: {winner}\n")
        text_file.write("------------------------------\n")