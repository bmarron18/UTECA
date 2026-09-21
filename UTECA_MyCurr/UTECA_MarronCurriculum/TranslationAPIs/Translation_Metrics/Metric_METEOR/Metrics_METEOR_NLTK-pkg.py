#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 11:35:19 2025
Updated 23 Jun 2026
@author: bmarron
"""

# %%

'''
METEOR Metric using the Natural Language Tool Kit (ntlk)

'''

# %%

    # after import NLTK package, need to download files
    # nltk.download()  <==  opens a separate window to select items

    
import nltk
nltk.download('punkt_tab')
nltk.download('wordnet')



# %%

'''
METEOR Score: Test Run
'''
from nltk.tokenize import word_tokenize
from nltk.translate.meteor_score import single_meteor_score


 
    # Define the reference text
reference_text= "The quick brown fox jumps over the lazy dog. \
    And finds himself caught." 
    
    # Define the translated (candidate) text
candidate_text = "A fast brown fox leaps over a lazy dog. \
    And is captured."


ref = word_tokenize(reference_text, "english")
hypo = word_tokenize(candidate_text, "english")


# Calculate METEOR score 
score = single_meteor_score(ref, hypo)

# Print the result 
print(f"METEOR Score: {score:.4f}")
# METEOR Score: 0.6621

# %%

'''
METEOR Score Example
'''
from nltk.tokenize import word_tokenize
from nltk.translate.meteor_score import single_meteor_score


 
   # Define a reference text created by a human translator
   # The quotes define a "string" in Python
reference_text= "The Ministry of Labor and Social Welfare (MLSW) must approve \
    or reject the registration request within twenty days after its receipt in the \
    offices of the MLSW. If the MLSW fails to do so, the applicants may formally \
    require that the MLSW resolve the issue within three business days. If, after \
    this second period has elapsed without notification of the status of the \
    registration request, the registration request will be deemed approved for \
    all applicable legal purposes."
    
    # Define the candidate text created by an AI translator
    # The quotes define a "string" in Python
candidate_text = "The Ministry of Labor and Social Welfare must decide on the \
    registration request within twenty days of receiving it. If it fails to do so \
    the applicants may request that it issue the corresponding resolution within three \
    days of submitting the request. After thid period has elapsed without notification \
    of the resolution, the registration will be deemed to have been made for the legal \
    purposes to which it gives rise"


ref = word_tokenize(reference_text, "english")
cand = word_tokenize(candidate_text, "english")


# Calculate METEOR score 
score = single_meteor_score(ref, cand)

# Print the result 
print(f"METEOR Score: {score:.4f}")
# METEOR Score: 0.5640

# %%

'''
METEOR Score for My Work
'''
from nltk.tokenize import word_tokenize
from nltk.translate.meteor_score import single_meteor_score


 
   # Define a reference text created by a human translator
   # The quotes define a "string" in Python
reference_text= "Copy your reference text here. Watch the quotes!."
    
    # Define the candidate text created by an AI translator
    # The quotes define a "string" in Python
candidate_text = "Copy the AI translation here. In quotes!!"

    # change language as needed
ref = word_tokenize(reference_text, "english")
cand = word_tokenize(candidate_text, "english")


# Calculate METEOR score 
score = single_meteor_score(ref, cand)

# Print the result 
print(f"METEOR Score: {score:.4f}")



# %%

'''
METEOR Score for My Work (HW Task 2)
'''
from nltk.tokenize import word_tokenize
from nltk.translate.meteor_score import single_meteor_score

# excerpt is from the "Joy Luck Club", Ch. Lena St. Clair
'''
And just after my father died last year, she said she knew this would happen. Because
a philodendron plant my father had given her had withered and died, despite the fact
that she watered it faithfully. She said the plant had damaged its roots and no water
could get to it. The autopsy report she later received showed my father had had
ninety-percent blockage of the arteries before he died of a heart attack at the age
of seventy-four. My father was not Chinese like my mother, but English-Irish American,
who enjoyed his five slices of bacon and three eggs sunnyside up every morning.
'''
 
   # Define a reference text created by a human translator
   # The quotes define a "string" in Python
reference_text= "Y justo después de que mi padre muriera el año pasado, ella dijo que sabía que esto pasaría. Porque \
un filodendro que mi padre le había regalado se había marchitado y muerto, a pesar del hecho \
de que ella lo regaba fielmente. Dijo que la planta tenía las raíces dañadas y que el agua no \
podía llegar a ella. El informe de la autopsia que recibió después mostró que mi padre había tenido \
una obstrucción del noventa por ciento en las arterias antes de morir de un ataque al corazón a la edad \
de setenta y cuatro años. Mi padre no era chino como mi madre, sino un estadounidense anglo-irlandés, \
que disfrutaba de sus cinco rebanadas de tocino y tres huevos estrellados cada mañana."
    
    # Define the candidate text created by an AI translator
    # The quotes define a "string" in Python
candidate_text = "Y justo después de que mi padre muriera el año pasado, ella dijo que sabía que esto pasaría. Porque \
un filodendro que mi padre le había regalado se había marchitado y muerto, a pesar del hecho \
de que ella lo regaba fielmente. Dijo que la planta tenía las raíces dañadas y que el agua no \
podía llegar a ella. El informe de la autopsia que recibió después mostró que mi padre había tenido \
una obstrucción del noventa por ciento en las arterias antes de morir de un ataque al corazón a la edad \
de setenta y cuatro años. Mi padre no era chino como mi madre, sino un estadounidense anglo-irlandés, \
que disfrutaba de sus cinco lonchas de tocino y tres huevos fritos cada mañana."


ref = word_tokenize(reference_text, "spanish")
cand = word_tokenize(candidate_text, "spanish")


# Calculate METEOR score 
score = single_meteor_score(ref, cand)

# Print the result 
print(f"METEOR Score: {score:.4f}")
# METEOR Score: 0.9850

