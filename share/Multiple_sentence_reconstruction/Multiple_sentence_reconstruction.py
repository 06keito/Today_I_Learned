#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Make each line consisting of multiple sentences a new line.
# > pip install googletrans==4.0.0-rc1
# > python Multiple_sentence_reconstruction.py

from googletrans import Translator
import sys,re
import regex

def input_text_data():
     S,data = str(),list()
     with open('input.txt',mode='r',encoding='utf-8') as fr:
          array = list(regex.split(r'(?<=[.])(?!$)',fr.read().replace('\n',' ')))
     line_count = len(array) # get line len

     if array[-1]!=' ': # add dummy line
          array += [' ']
          line_count += 1

     for i in range(line_count-1):
          S += array[i].lstrip().rstrip()
          if re.search(r'[.,[]', array[i+1][0]) or str.isnumeric(array[i+1][0]) or (array[i+1][0].islower()):
               continue
          else:
               data.append(S)
               S = ''

     return data,line_count

def print_error_log(error_frame_point,error_msg):
     print('{frame} : {msg}'\
          .format(frame=error_frame_point,msg=error_msg))

def output_justification_text_data(data,line_count):
     with open('output.txt',mode='w',encoding='utf-8') as fw:
          for line in data:
               try:
                    fw.write('{l_br}'.format(l_br=line+'\n'))
               except Exception as error_msg:
                    print_error_log(sys._getframe().f_code.co_name,error_msg)
                    continue

def output_trancerated_text_data(data,line_count):
     translator = Translator()
     with open('output_trancerated.txt',mode='w',encoding='utf-8') as fw:
          for line in data:
               try:
                    tr = translator.translate(line,src='en', dest='ja').text
                    fw.write('{l_br}'.format(l_br=tr+'\n'))
               except Exception as error_msg:
                    print_error_log(sys._getframe().f_code.co_name,error_msg)
                    continue

def main():
     text_data,line_count = input_text_data() #get text data
     output_justification_text_data(text_data,line_count)
     output_trancerated_text_data(text_data,line_count)

if __name__ == '__main__':
     main()