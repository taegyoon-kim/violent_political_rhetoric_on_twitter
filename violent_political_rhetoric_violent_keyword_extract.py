###### author details: Taegyoon Kim, taegyoon@psu.edu
###### purpose: This script is used to extract top-weight n-grams on predicted probabilities in text classification
###### last edit: 27 May 2021


##### packages

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer


##### read data and 

path_jigsaw = '/Users/taegyoonkim/Google Drive/downloads/jigsaw-toxic-comment-classification-challenge/' # https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/data
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
        print(classlabel, "highest", feat, coef)    
    for coef, feat in bottomn:
        print(classlabel, "lowest ", feat, coef)    
        

##### get the top-200 
        
most_informative_feature_for_class(count_vectorizor, lr, 0, n=200)


##### list of initial violent keywords (n=200)

keyword = 'kill|shoot|hang|die|exterminate|execute|executed|stab|killing|castration|kick|hanged|castrate|bullet|burn|fire this|starve|punch|choke|slap|suicide|throat|neutered|shot|death to|shooting|killed|death|fire the|bang on|shoots|guillotine|bomb|spank|kills|spanking|exterminated|be hung|torture|crush|fire|deserves|kicked|slaughter|burned|be dead|punched|light em|kill it|destroy|drown|be exterminated|execution|destroy them|run over|stake|smash|dies|euthanized|firing|execute him|stabbing|stop breathing|castrated|bombing|head off|explode|eradicate|invade|beheading|fired the|cull|hung|be neutered|killing it|kicking|go kill|beating|females|tortured|burn them|remove|dead|her with|fester|should die|invade canada|beat|be shot|go jump|shotgun|heads|be blood|be castrated|eliminate these|neck|eliminate|tear it|head|be euthanized|kill all|be destroyed|nail that|executing|be killed|the missiles|kill em|start killing|beat up|lynching|bash|agonizing|electric chair|just fire|destroyed|hammered|hang the|crucify|punk|fire that|some countries|hit|be eliminated|them then|burn the|throttled|burn it|punching|over with|hanging|to murder|fry|human life|lynched|destroy females|poison|be executed|piffle|bastards|hanged for|strike|cull the|nuke|traitors|neighbours|and be|taken out|beast|be burned|gas chamber|starving the|get shot|on killing|be incinerated|cut|let kill|shotgun would|house down|incinerated|butts out|we kill|the trigger|bury|kill yourself|get hammered|tear|slay|the face|kill them|bite|killing people|fire those|you all|are dead|be removed|don\'t like|what was|burning|nazis|it over|as long|been shot|murdering|about killing|the lynching|alive|gun up|hammer|or in|cutting|this kind|just run|raped|catch them|slapping|bullets|em|getting shot|eliminated|head shake'
keyword_start = r'\bkill|\bshoot|\bhang|\bdie|\bexterminate|\bexecute|\bexecuted|\bstab|\bkilling|\bcastration|\bkick|\bhanged|\bcastrate|\bbullet|\bburn|\bfire this|\bstarve|\bpunch|\bchoke|\bslap|\bsuicide|\bthroat|\bneutered|\bshot|\bdeath to|\bshooting|\bkilled|\bdeath|\bfire the|\bbang on|\bshoots|\bguillotine|\bbomb|\bspank|\bkills|\bspanking|\bexterminated|\bbe hung|\btorture|\bcrush|\bfire|\bdeserves|\bkicked|\bslaughter|\bburned|\bbe dead|\bpunched|\blight em|\bkill it|\bdestroy|\bdrown|\bbe exterminated|\bexecution|\bdestroy them|\brun over|\bstake|\bsmash|\bdies|\beuthanized|\bfiring|\bexecute him|\bstabbing|\bstop breathing|\bcastrated|\bbombing|\bhead off|\bexplode|\beradicate|\binvade|\bbeheading|\bfired the|\bcull|\bhung|\bbe neutered|\bkilling it|\bkicking|\bgo kill|\bbeating|\bfemales|\btortured|\bburn them|\bremove|\bdead|\bher with|\bfester|\bshould die|\binvade canada|\bbeat|\bbe shot|\bgo jump|\bshotgun|\bheads|\bbe blood|\bbe castrated|\beliminate these|\bneck|\beliminate|\btear it|\bhead|\bbe euthanized|\bkill all|\bbe destroyed|\bnail that|\bexecuting|\bbe killed|\bthe missiles|\bkill em|\bstart killing|\bbeat up|\blynching|\bbash|\bagonizing|\belectric chair|\bjust fire|\bdestroyed|\bhammered|\bhang the|\bcrucify|\bpunk|\bfire that|\bsome countries|\bhit|\bbe eliminated|\bthem then|\bburn the|\bthrottled|\bburn it|\bpunching|\bover with|\bhanging|\bto murder|\bfry|\bhuman life|\blynched|\bdestroy females|\bpoison|\bbe executed|\bpiffle|\bbastards|\bhanged for|\bstrike|\bcull the|\bnuke|\btraitors|\bneighbours|\band be|\btaken out|\bbeast|\bbe burned|\bgas chamber|\bstarving the|\bget shot|\bon killing|\bbe incinerated|\bcut|\blet kill|\bshotgun would|\bhouse down|\bincinerated|\bbutts out|\bwe kill|\bthe trigger|\bbury|\bkill yourself|\bget hammered|\btear|\bslay|\bthe face|\bkill them|\bbite|\bkilling people|\bfire those|\byou all|\bare dead|\bbe removed|\bdon\'t like|\bwhat was|\bburning|\bnazis|\bit over|\bas long|\bbeen shot|\bmurdering|\babout killing|\bthe lynching|\balive|\bgun up|\bhammer|\bor in|\bcutting|\bthis kind|\bjust run|\braped|\bcatch them|\bslapping|\bbullets|\bem|\bgetting shot|\beliminated|\bhead shake'
keyword_both = r'\bkill\b|\bshoot\b|\bhang\b|\bdie\b|\bexterminate\b|\bexecute\b|\bexecuted\b|\bstab\b|\bkilling\b|\bcastration\b|\bkick\b|\bhanged\b|\bcastrate\b|\bbullet\b|\bburn\b|\bfire this\b|\bstarve\b|\bpunch\b|\bchoke\b|\bslap\b|\bsuicide\b|\bthroat\b|\bneutered\b|\bshot\b|\bdeath to\b|\bshooting\b|\bkilled\b|\bdeath\b|\bfire the\b|\bbang on\b|\bshoots\b|\bguillotine\b|\bbomb\b|\bspank\b|\bkills\b|\bspanking\b|\bexterminated\b|\bbe hung\b|\btorture\b|\bcrush\b|\bfire\b|\bdeserves\b|\bkicked\b|\bslaughter\b|\bburned\b|\bbe dead\b|\bpunched\b|\blight em\b|\bkill it\b|\bdestroy\b|\bdrown\b|\bbe exterminated\b|\bexecution\b|\bdestroy them\b|\brun over\b|\bstake\b|\bsmash\b|\bdies\b|\beuthanized\b|\bfiring\b|\bexecute him\b|\bstabbing\b|\bstop breathing\b|\bcastrated\b|\bbombing\b|\bhead off\b|\bexplode\b|\beradicate\b|\binvade\b|\bbeheading\b|\bfired the\b|\bcull\b|\bhung\b|\bbe neutered\b|\bkilling it\b|\bkicking\b|\bgo kill\b|\bbeating\b|\bfemales\b|\btortured\b|\bburn them\b|\bremove\b|\bdead\b|\bher with\b|\bfester\b|\bshould die\b|\binvade canada\b|\bbeat\b|\bbe shot\b|\bgo jump\b|\bshotgun\b|\bheads\b|\bbe blood\b|\bbe castrated\b|\beliminate these\b|\bneck\b|\beliminate\b|\btear it\b|\bhead\b|\bbe euthanized\b|\bkill all\b|\bbe destroyed\b|\bnail that\b|\bexecuting\b|\bbe killed\b|\bthe missiles\b|\bkill em\b|\bstart killing\b|\bbeat up\b|\blynching\b|\bbash\b|\bagonizing\b|\belectric chair\b|\bjust fire\b|\bdestroyed\b|\bhammered\b|\bhang the\b|\bcrucify\b|\bpunk\b|\bfire that\b|\bsome countries\b|\bhit\b|\bbe eliminated\b|\bthem then\b|\bburn the\b|\bthrottled\b|\bburn it\b|\bpunching\b|\bover with\b|\bhanging\b|\bto murder\b|\bfry\b|\bhuman life\b|\blynched\b|\bdestroy females\b|\bpoison\b|\bbe executed\b|\bpiffle\b|\bbastards\b|\bhanged for\b|\bstrike\b|\bcull the\b|\bnuke\b|\btraitors\b|\bneighbours\b|\band be\b|\btaken out\b|\bbeast\b|\bbe burned\b|\bgas chamber\b|\bstarving the\b|\bget shot\b|\bon killing\b|\bbe incinerated\b|\bcut\b|\blet kill\b|\bshotgun would\b|\bhouse down\b|\bincinerated\b|\bbutts out\b|\bwe kill\b|\bthe trigger\b|\bbury\b|\bkill yourself\b|\bget hammered\b|\btear\b|\bslay\b|\bthe face\b|\bkill them\b|\bbite\b|\bkilling people\b|\bfire those\b|\byou all\b|\bare dead\b|\bbe removed\b|\bdon\'t like\b|\bwhat was\b|\bburning\b|\bnazis\b|\bit over\b|\bas long\b|\bbeen shot\b|\bmurdering\b|\babout killing\b|\bthe lynching\b|\balive\b|\bgun up\b|\bhammer\b|\bor in\b|\bcutting\b|\bthis kind\b|\bjust run\b|\braped\b|\bcatch them\b|\bslapping\b|\bbullets\b|\bem\b|\bgetting shot\b|\beliminated\b|\bhead shake'

