import csv
import chardet
import WordCloud

#job1: import csv and read it
# encoding scheme error, have to import chardet to solve it. The error was "[charmap' codec can't decode byte 0x90 in position 1800: character maps to <undefined>]"
with open('E:\AI Task1\dataset-medical.csv', 'rb') as f:
    result = chardet.detect(f.read())

with open('E:\AI Task1\dataset-medical.csv', 'r', encoding=result['encoding']) as f: #define coding scheme due to chardet
    reader = csv.reader(f)
    #Skip the first row as it contains headers
    next(reader)
    #empty list to store keywords
    keywords = []
    for row in reader:
        #Append the keywords in the second column to the list we need keywords only not doi
        keywords.append(row[1])

# Job2: Separate words using ';' separator
words_list = [] #necessary to go throught the whole data lists inside lists
for keyword in keywords:
    # Split the keyword string using ';' as the separator
    words = keyword.split(';')
    words_list.extend(words) #add all the same words
    
    
#program is keep running 
# for word in words_list:
#     print(words)

# Job3: Count Frequency of each word
word_count = {}
for word in words_list: #to iterate in the new created list
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Print the word count
for word, count in word_count.items():
    print(word, count)

#Job4: There is a library called WordCloud which takes input as a python dictionary (word: frequency of word).

word_cloud = WordCloud(
        width=3000,
        height=2000,
        random_state=1,
        background_color="salmon",
        colormap="Pastel1",
        collocations=False,
        stopwords=STOPWORDS,
        ).generate(text)