# Importing the os module to utilize various os
import os
electioncsvpath = os.path.join('Resources', 'election_data.csv')

# Importing csv and reading the csv file
import csv
with open(electioncsvpath, newline= '') as electioncsvfile:

    #CSV reader with delimiter
    electioncsvreader = csv.reader(electioncsvfile, delimiter=',')
      
    # Read the header 
    electioncsv_header = next(electioncsvreader)
   # print(f"Election CSV Header: {electioncsv_header}")

   
   
    # Create variables to hold the voter, county, and candidate
    voter = []
    county = []
    # candidate = []
    voter_dictionary = {}
    
    # Append voter, county, and candidate data into their empty lists
    for row in electioncsvreader:
      
        voter.append(row[0])
        county.append(row[1])
        candidate =row[2]
        number_of_votes = 1
        if candidate not in voter_dictionary:
            voter_dictionary[candidate] = number_of_votes
        else: 
            voter_dictionary[candidate] +=1
    print(f' Election Results')
    print(f' -----------------')
    print(f' Total Votes: {len(voter)}')
    print(f' -----------------')
    for i in voter_dictionary:
        print(f'{i}: {((voter_dictionary[i]/len(voter))*100):.3f}% ({voter_dictionary[i]})')
    print(f' -----------------')

    print(f'Winner: {max(voter_dictionary, key=voter_dictionary.get)}')
    print(f' -----------------')
     

    # # Write file of the results to specified location
    
    poll_output_path = os.path.join ('Analysis', 'PyPoll_Analysis.txt')

    # # Open the file using "write" mode and specify variable for contents. 
    with open(poll_output_path, 'w', newline = '') as txtfile:

     #     #Write Summary Statistics to File
        txtfile.write(f' Election Results''\n')
        txtfile.write(f' -----------------''\n')
        txtfile.write(f' Total Votes: {len(voter)}''\n')
        txtfile.write(f' -----------------''\n')
        for i in voter_dictionary:
            txtfile.write(f' {i}: {((voter_dictionary[i]/len(voter))*100):.3f}% ({voter_dictionary[i]})''\n')
        txtfile.write(f' -----------------''\n')
        txtfile.write(f' Winner: {max(voter_dictionary, key=voter_dictionary.get)}''\n')
        txtfile.write(f' -----------------''\n')