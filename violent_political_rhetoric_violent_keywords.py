###### author details: Taegyoon Kim, taegyoon@psu.edu
###### purpose: This script is used to extract top-weight n-grams on predicted probabilities in text classification
###### last edit: 27 Oct 2021


##### packages

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer


##### read data and 

path_jigsaw = '' # https://www.kaggle.com/c/jigsaw-unintended-bias-in-toxicity-classification/data?select=train.csv
toxicity_corpus = pd.read_csv(path_jigsaw + 'train.csv') 
toxicity_corpus.head()
toxicity_corpus.shape
toxicity_corpus = toxicity_corpus[toxicity_corpus['comment_text'].apply(lambda x: len(x)<281)] # subset comments whose length is about a tweet
toxicity_corpus.shape


##### get the feature matrix and threat label

count_vectorizor = CountVectorizer(ngram_range=(1, 2))
X = count_vectorizor.fit_transform(toxicity_corpus["comment_text"]) # creating count matrix on the comment feature
y = np.where(toxicity_corpus['threat'] >= 0.5, 1, 0)


##### fit logistic regression

lr = LogisticRegression(C=5, random_state=1, solver='sag', max_iter=3000, n_jobs=-1)
lr.fit(X, y) 


##### define a fucnion that identifies top-weight features

labelid = list(lr.classes_).index(0)
feature_names = count_vectorizor.get_feature_names()
coefs = lr.coef_[labelid]
topn = zip(coefs, feature_names)
topn = sorted(zip(lr.coef_[labelid], feature_names))[-10:]
topn.reverse()
bottomn = sorted(zip(lr.coef_[labelid], feature_names))[:10]


def most_informative_feature_for_class(count_vectorizor, lr, classlabel, n=10):
    labelid = list(lr.classes_).index(classlabel)
    feature_names = count_vectorizor.get_feature_names()
    topn = sorted(zip(lr.coef_[labelid], feature_names))[-n:]
    topn.reverse()
    bottomn = sorted(zip(lr.coef_[labelid], feature_names))[:n]
    bottomn.reverse()
    for coef, feat in topn:
        print(feat)    
    #for coef, feat in bottomn:
        #print(classlabel, "lowest ", feat, coef)    
        

##### get the top-200 
        
most_informative_feature_for_class(count_vectorizor, lr, 0, n=200)


##### raw prints

kill
shoot
exterminate
hang
die
execute
castration
stab
executed
castrate
killing
hanged
kick
guillotine
fire this
bullet
starve
burn
choke
light em
punch
bang on
neutered
slap
death to
suicide
throat
shot
shooting
piffle
killed
spanking
death
spank
invade canada
fire the
bomb
shoots
be hung
kills
exterminated
be blood
torture
deserves
stop breathing
invade
be dead
crush
slaughter
white genocide
fire
be exterminated
punched
kicked
destroy them
drown
burned
stabbing
killing it
smash
kill it
fired the
fester
run over
destroy
eradicate
dies
execute him
nail that
agree take
stake
castrated
execution
tortured
cull
euthanized
tear it
firing
president keep
choke time
be neutered
burn them
burn it
eliminate these
females
bombing
it collapse
explode
butts out
beheading
poison his
be tazed
vaporize
head off
another win
be castrated
cull the
go kill
just triggering
bomb it
remove
are dead
tazed
beating
kicking
string em
lynching
go jump
be shot
gas them
hung
word torture
it first
dead
agonizing
her with
be destroyed
get cancer
dangle
should die
shotgun
be euthanized
throttled
forget back
triggering you
beat
fire that
just fire
vaporize it
plundering begin
destroy females
the missiles
ugly tear
by governor
them then
being tortured
alwaysthere hit
hits fan
feces hits
violence is
the plundering
box she
be killed
lynched
hang the
in bottle
poison
some countries
kill em
should butts
start killing
idea tear
be incinerated
beat up
sure attack
heads
bastards
fry
better push
executing
incinerated
neck
to thrill
kill all
punch nazi
shotgun would
burn the
plundering
out quick
fry him
neighbours
hammered
be eliminated
end the
him going
crucify
the lynching
eliminate
punk
that punk
throw everyone
fire those
hillary should
love bashing
bashing your
starving the
strike
head
just run
destroyed
breathing then
get hammered
electric chair
agreed they
her dangle
hanged for
bash
to murder
fire donny
yet do
