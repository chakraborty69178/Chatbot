#Cleaning dataset file


"""
This is the section where we try to clean our dataset to proceed forward with our model

"""
# importing required library
import pandas as pd
import numpy as np
import re

# Definning all the clening functions
def getMoveCorpus(lines, conv):
    
    """
    This method is deffined to clean the Cornel movie Dataset it takes the argument as the unclean dataset
    and returns clean dataset
    """
    #creating Dictnary tht maps each lines with its id
    id2line = {}
    for line in lines:
        _line =  line.split(" +++$+++ ")
        # Getting the records which shure to have all attribute present to reduce missing data and noice
        if len(_line) == 5:
            id2line[_line[0]] =_line[4]
    # loding the group of Ids for rach conversations       
    conversations_ids = []
    for conversations in conv[:-1]:
        _conversations = conversations.split(" +++$+++ ")[-1][1:-1].replace("'","").replace(" ","")
        conversations_ids.append(_conversations.split(","))
    
    # mapping Questions and answers
    questions = []
    answers =[]
    for conversation in conversations_ids:
        for i in range(len(conversation) -1):
            questions.append(id2line[conversation[i]])
            answers.append(id2line[conversation[i+1]])
            
    cleaned_questions = []
    cleaned_answers =[]
    #Cleaned Questions
    for question in questions:
        cleaned_questions.append(clean_text(question))
    
    # cleaned Answers
    for answer in answers:
        cleaned_answers.append(clean_text(answer))
    
    #Reducing the number of words occered less
    word2count = {}
    for question in cleaned_questions:
        for word in question.split():
            if word not in word2count:
                word2count[word] =1
            else:
                word2count[word] += 1             
    for answer in cleaned_answers:
        for word in answer.split():
            if word not in word2count:
                word2count[word] =1
            else:
                word2count[word] += 1
    
    # Creting Two dict that maps the question words and answer words to an Integer
    threshold =20
    questionswords2int ={}
    word_number =0
    for word,count in word2count.items():
        if  count>= threshold:
            questionswords2int[word] = word_number
            word_number+= 1
    answerswords2int ={}
    word_number =0
    for word,count in word2count.items():
        if  count>= threshold:
            answerswords2int[word] = word_number
            word_number+= 1
            
    # Adding SOS and EOS in our Dictnary
    tokens =  ['<PAD>' ,'<EOS>' ,'<OUT>','<SOS>']
    for token in tokens:
        questionswords2int[token] = len(questionswords2int)+1
        answerswords2int[token] =len(answerswords2int)+1
    # creating the inverse mappings to create Sec to sec model
    answersint2word = {w_i:w for w, w_i in answerswords2int.items()}
   
    
    # adding EOS to end of every answers
    for i in range(len(cleaned_answers)):
        cleaned_answers[i]+=" <EOS>"
    # replacing all the Questions and answers into integers
    questions_into_int = [] 
    for questions in cleaned_questions:
        ints = []
        for word in questions.split():
            if word not in questionswords2int:
                ints.append(questionswords2int['<OUT>'])
            else:
                ints.append(questionswords2int[word])
        questions_into_int.append(ints)
    answers_into_int = [] 
    for answer in cleaned_answers:
        ints = []
        for word in answer.split():
            if word not in answerswords2int:
                ints.append(answerswords2int['<OUT>'])
            else:
                ints.append(questionswords2int[word])
        answers_into_int.append(ints)
        
    #Sorting all the Question lista nd answer list for Optimization perpose
    sorted_questions =[]
    sorted_answers=[]
    for i in range(1,25):
        for j in range(0, len(questions_into_int)-1):
            if len(questions_into_int[j]) == i:
                sorted_questions.append(questions_into_int[j])
                sorted_answers.append(answers_into_int[j])
    
    return sorted_questions,sorted_answers,questionswords2int,answerswords2int,answersint2word






def getUbuntuCorpus(dataset1,dataset2,dataset3):
    """
    This method is deffined to clean the Cornel movie Dataset it takes the argument as the unclean dataset
    and returns clean dataset
    """
    return cleaned_datasetX,cleaned_datasetY














# Definning the Support Functions
def clean_text(text):
    """
        Takes the string of conversations and apply some preprocessing and returns the Cleaned String
            This is a Support method to clean text
    
    """
    text = text.lower()
    text = re.sub(r"i'm" , "i am", text)
    text = re.sub(r"he's" , "he is", text)
    text = re.sub(r"she's" , "she is", text)
    text = re.sub(r"what's" , "what is", text)
    text = re.sub(r"where's" , "where is", text)
    text = re.sub(r"\'ll" , "will", text)
    text = re.sub(r"\'ve" , "have", text)
    text = re.sub(r"\'re" , "are", text)
    text = re.sub(r"won't" , "wont", text)
    text = re.sub(r"can't" , "cannot", text)
    text = re.sub( r"[-()\"#/@;:.{}+-^|]" , "", text)
    cleaned_line = text                 
    return cleaned_line