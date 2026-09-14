# 6.100A Fall 2022
# Problem Set 3
# Written by: sylvant, muneezap, charz, anabell, nhung, wang19k, asinelni, shahul, jcsands

# Problem Set 3
# Name:
# Collaborators:

# Purpose: Check for similarity between two texts by comparing different kinds of word statistics.

import string
import math


### DO NOT MODIFY THIS FUNCTION
def load_file(filename):
    """
    Args:
        filename: string, name of file to read
    Returns:
        string, contains file contents
    """
    # print("Loading file %s" % filename)
    inFile = open(filename, 'r')
    line = inFile.read().strip()
    for char in string.punctuation:
        line = line.replace(char, "")
    inFile.close()
    return line.lower()


### Problem 0: Prep Data ###
def text_to_list(input_text):
    """
    Args:
        input_text: string representation of text from file.
                    assume the string is made of lowercase characters
    Returns:
        list representation of input_text, where each word is a different element in the list
    """
    return input_text.split()
    pass


### Problem 1: Get Frequency ###
def get_frequencies(input_iterable):
    """
    Args:
        input_iterable: a string or a list of strings, all are made of lowercase characters
    Returns:
        dictionary that maps string:int where each string
        is a letter or word in input_iterable and the corresponding int
        is the frequency of the letter or word in input_iterable
    Note: 
        You can assume that the only kinds of white space in the text documents we provide will be new lines or space(s) between words (i.e. there are no tabs)
    """
    dictionary = {}
    for i in input_iterable:
        if dictionary.get(i) == None:
            dictionary.update({i: 1})
        elif dictionary.get(i) != None:
            dictionary[i] += 1
    return dictionary


### Problem 2: Letter Frequencies ###
def get_letter_frequencies(word):
    """
    Args:
        word: word as a string
    Returns:
        dictionary that maps string:int where each string
        is a letter in word and the corresponding int
        is the frequency of the letter in word
    """
    return get_frequencies(word)


### Problem 3: Similarity ###
def calculate_similarity_score(freq_dict1, freq_dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        freq_dict1: frequency dictionary of letters of word1 or words of text1
        freq_dict2: frequency dictionary of letters of word2 or words of text2
    Returns:
        float, a number between 0 and 1, inclusive
        representing how similar the words/texts are to each other

        The difference in words/text frequencies = DIFF sums words
        from these three scenarios:
        * If an element occurs in dict1 and dict2 then
          get the difference in frequencies
        * If an element occurs only in dict1 then take the
          frequency from dict1
        * If an element occurs only in dict2 then take the
          frequency from dict2
         The total frequencies = ALL is calculated by summing
         all frequencies in both dict1 and dict2.
        Return 1-(DIFF/ALL) rounded to 2 decimal places
    """
    diff = 0
    ALL = 0
    for keys in freq_dict1.keys()|freq_dict2.keys():
        if freq_dict1.get(keys) != None and freq_dict2.get(keys) != None:
           diff += abs(freq_dict1.get(keys) - freq_dict2.get(keys))
           ALL += freq_dict1.get(keys) + freq_dict2.get(keys) 
        elif freq_dict1.get(keys) == None and freq_dict2.get(keys) != None:
            diff += freq_dict2.get(keys)
            ALL += freq_dict2.get(keys) 
        elif freq_dict1.get(keys) != None and freq_dict2.get(keys) == None:
            diff += freq_dict1.get(keys)
            ALL += freq_dict1.get(keys)
    return round(1 - (diff/ALL), 2)
    pass


### Problem 4: Most Frequent Word(s) ###
def get_most_frequent_words(freq_dict1, freq_dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        freq_dict1: frequency dictionary for one text
        freq_dict2: frequency dictionary for another text
    Returns:
        list of the most frequent word(s) in the input dictionaries

    The most frequent word:
        * is based on the combined word frequencies across both dictionaries.
          If a word occurs in both dictionaries, consider the sum the
          freqencies as the combined word frequency.
        * need not be in both dictionaries, i.e it can be exclusively in
          dict1, dict2, or shared by dict1 and dict2.
    If multiple words are tied (i.e. share the same highest frequency),
    return an alphabetically ordered list of all these words.
    """
    highest_freq = 0
    most_frequent_word = []
    for keys in freq_dict1.keys()|freq_dict2.keys():
        if freq_dict1.get(keys) != None and freq_dict2.get(keys) != None:            
            if freq_dict1.get(keys) + freq_dict2.get(keys) > highest_freq:
                highest_freq = freq_dict1.get(keys) + freq_dict2.get(keys)
                most_frequent_word = []
                most_frequent_word.append(keys)
            elif freq_dict1.get(keys) + freq_dict2.get(keys) == highest_freq:
                most_frequent_word.append(keys)
        
        elif freq_dict1.get(keys) == None and freq_dict2.get(keys) != None:        
            if freq_dict2.get(keys) > highest_freq:
                highest_freq = freq_dict2.get(keys)
                most_frequent_word = []
                most_frequent_word.append(keys)
            elif freq_dict2.get(keys) == highest_freq:
                most_frequent_word.append(keys)
        
        
        elif freq_dict1.get(keys) != None and freq_dict2.get(keys) == None:       
            if freq_dict1.get(keys) > highest_freq:
                highest_freq = freq_dict1.get(keys)
                most_frequent_word = []
                most_frequent_word.append(keys)
            elif freq_dict1.get(keys) == highest_freq:
                most_frequent_word.append(keys) 
    most_frequent_word.sort()
    return most_frequent_word

### Problem 5: Finding TF-IDF ###
def get_tf(file_path):
    """
    Args:
        file_path: name of file in the form of a string
    Returns:
        a dictionary mapping each word to its TF

    * TF is calculatd as TF(i) = (number times word *i* appears
        in the document) / (total number of words in the document)
    * Think about how we can use get_frequencies from earlier
    """
    file_content = load_file(file_path)
    word_list = text_to_list(file_content) # Chuyển chuỗi thành danh sách từ
    file_dict = get_frequencies(word_list)
    return_dict = {}
    total = sum(file_dict.values())
    for i in file_dict.keys():
        return_dict.update({i : file_dict.get(i)/total})
    return return_dict



def get_idf(file_paths):
    """
    Args:
        file_paths: list of names of files, where each file name is a string
    Returns:
       a dictionary mapping each word to its IDF

    * IDF is calculated as IDF(i) = log_10(total number of documents / number of
    documents with word *i* in it), where log_10 is log base 10 and can be called
    with math.log10()

    """
    list_dict = []
    return_dict = {}
    set_keys = set()
    for i in file_paths:
        word_list = text_to_list(load_file(i))
        file_freqs = get_frequencies(word_list)
        list_dict.append(file_freqs)
    for i in range(len(list_dict)):
        set_keys.update(list_dict[i].keys())
    for i in set_keys:
        temp = 0
        for k in range(len(list_dict)): #Calculate number of doc with word i
            if list_dict[k].get(i,0) != 0:
                temp += 1
        return_dict.update({i:math.log10(len(file_paths)/temp)}) #IDF Formula
    return return_dict




def get_tfidf(tf_file_path, idf_file_paths):
    """
        Args:
            tf_file_path: name of file in the form of a string (used to calculate TF)
            idf_file_paths: list of names of files, where each file name is a string
            (used to calculate IDF)
        Returns:
           a sorted list of tuples (in increasing TF-IDF score), where each tuple is
           of the form (word, TF-IDF). In case of words with the same TF-IDF, the
           words should be sorted in increasing alphabetical order.

        * TF-IDF(i) = TF(i) * IDF(i)
        """
    text_idf = get_idf(idf_file_paths)
    text_tf = get_tf(tf_file_path)
    return_list = []
    temp_tfidf = 0
    for i in text_tf.keys():
        temp_tfidf = text_idf.get(i,0) * text_tf.get(i)
        return_list.append((i,temp_tfidf))
    return sorted(return_list,key = lambda i: (i[1], i[0]))

if __name__ == "__main__":
    pass
    ###############################################################
    ## Uncomment the following lines to test your implementation ##
    ###############################################################

    ## Tests Problem 0: Prep Data
    # test_directory = "tests/student_tests/"
    # hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    # world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    # print(world)      # should print ['hello', 'world', 'hello']
    # print(friend)     # should print ['hello', 'friends']

    ## Tests Problem 1: Get Frequencies
    # test_directory = "tests/student_tests/"
    # hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    # world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    # world_word_freq = get_frequencies(world)
    # friend_word_freq = get_frequencies(friend)
    # print(world_word_freq)    # should print {'hello': 2, 'world': 1}
    # print(friend_word_freq)   # should print {'hello': 1, 'friends': 1}

    ## Tests Problem 2: Get Letter Frequencies
    # freq1 = get_letter_frequencies('hello')
    # freq2 = get_letter_frequencies('that')
    # print(freq1)      #  should print {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    # print(freq2)      #  should print {'t': 2, 'h': 1, 'a': 1}

    ## Tests Problem 3: Similarity
    # test_directory = "tests/student_tests/"
    # hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    # world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    # world_word_freq = get_frequencies(world)
    # friend_word_freq = get_frequencies(friend)
    # word1_freq = get_letter_frequencies('toes')
    # word2_freq = get_letter_frequencies('that')
    # word3_freq = get_frequencies('nah')
    # word_similarity1 = calculate_similarity_score(word1_freq, word1_freq)
    # word_similarity2 = calculate_similarity_score(word1_freq, word2_freq)
    # word_similarity3 = calculate_similarity_score(word1_freq, word3_freq)
    # word_similarity4 = calculate_similarity_score(world_word_freq, friend_word_freq)
    # print(word_similarity1)       # should print 1.0
    # print(word_similarity2)       # should print 0.25
    # print(word_similarity3)       # should print 0.0
    # print(word_similarity4)       # should print 0.4

    ## Tests Problem 4: Most Frequent Word(s)
    #freq_dict1, freq_dict2 = {"hello": 5, "world": 1}, {"hello": 1, "world": 5}
    #most_frequent = get_most_frequent_words(freq_dict1, freq_dict2)
    #print(most_frequent)      # should print ["hello", "world"]

    ## Tests Problem 5: Find TF-IDF
    # tf_text_file = 'tests/student_tests/hello_world.txt'
    # idf_text_files = ['tests/student_tests/hello_world.txt', 'tests/student_tests/hello_friends.txt']
    # tf = get_tf(tf_text_file)
    # idf = get_idf(idf_text_files)
    # tf_idf = get_tfidf(tf_text_file, idf_text_files)
    # print(tf)     # should print {'hello': 0.6666666666666666, 'world': 0.3333333333333333}
    # print(idf)    # should print {'hello': 0.0, 'world': 0.3010299956639812, 'friends': 0.3010299956639812}
    # print(tf_idf) # should print [('hello', 0.0), ('world', 0.10034333188799373)]