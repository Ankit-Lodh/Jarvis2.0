# this python file for to take the movie_conversations.txt file and create a csv file with questions and answers row
import sys
import numpy as np
import csv
import re

def main():
    if len(sys.argv) < 3 or len(sys.argv)>3:
        print("please add the movie_conversations.txt and also movie_lines.txt from cornell movie dialog corpus")
        raise NotImplementedError
    with open(sys.argv[1],"r") as file:
        read_file = file.readlines()
    with open(sys.argv[2],"r") as file2:
        read_file2 = file2.readlines()
    dic = {} # create a dictionary where location of dialog is keys and values is corresponding dialog
    for strings in read_file2:
        array1 = strings.split("+++$+++")[0].strip()
        array2 = strings.split("+++$+++")[-1]
        array3 = re.sub(r'\n',"",array2).strip()
        dic[array1] = array3
    arr = conversation_pair(read_file,dic)
    list_to_np = np.array(arr)
    fields = ["Input_text","Output_text"]
    # code below this is create a csv file name conversations.csv and give first columns name of "Input_text" and second columns name
    # of "Output_text"
    with open('conversations.csv','w',newline='') as f:
        write = csv.writer(f)
        write.writerow(fields)
        write.writerows(list_to_np)

def conversation_pair(arr_txt_file,dictionary):
    ''' this function take the input of movie_conversation.txt file and give the output of array of
    question-answer pair '''

    list_of_pairs = []
    for string in arr_txt_file:
        string_array = string.split("+++$+++")[-1]
        array = re.sub(r"[^a-zA-Z0-9]"," ",string_array).strip().split()
        all_pairs = possible_pair(array)
        for pairs in all_pairs:
            lines = dialog_line(pairs,dictionary)
            list_of_pairs.append(lines)
    return list_of_pairs


def possible_pair(adress_array):
    ''' function take the input of array of every location of conversation i.e if we open movie_conversations.txt
    file then we can see at every line such as ['L194', 'L195', 'L196', 'L197']. 'L194' is the location of lines
    of dialog in move that we find at the file movie_lines. This file give the output of list of possible pairs such as 
    possible pairs of ['L194', 'L195', 'L196', 'L197'] is ['L194', 'L195'],[ 'L195', 'L196'],['L196', 'L197']'''

    l = []
    for i in range(len(adress_array)-1):
        l.append(adress_array[i:i+2])
    return l


def dialog_line(adress_arr,dictionary):
    '''This function take the possible pairs such as ['L194', 'L195'] and convert the location of dialog into its
    corresponding lines of dialog'''
    l = []
    for j in adress_arr:
        l.append(dictionary[j])
    return l

if __name__ == "__main__":
    main()