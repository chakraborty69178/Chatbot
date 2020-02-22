#import tensorflow as tf
import numpy as np
import os
import preprocessing

lines = open('Datasets/cornell movie-dialogs corpus/movie_lines.txt' , encoding ='utf-8', errors ='ignore').read().split('\n')
conv = open('Datasets/cornell movie-dialogs corpus/movie_conversations.txt' , encoding ='utf-8', errors ='ignore').read().split('\n')

sorted_questions,sorted_answers,questionswords2int,answerswords2int,answersint2words = preprocessing.getMoveCorpus(lines,conv)

sorted_question_array = np.array(sorted_questions)
sorted_answers_array=np.array(sorted_answers)