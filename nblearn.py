import glob
import sys

spamwords_count=0
hamwords_count=0
spam_key = dict()
ham_key = dict()
spam_key_prob = dict()
ham_key_prob = dict()
# location = sys.argv[1]
# C:/Users/niran/OneDrive/Desktop/sublime/Spam or Ham/train/**/*.txt
for name in glob.glob('C:/Users/niran/OneDrive/Desktop/sublime/Spam or Ham/train/**/*.txt', recursive=True):
    n=name.split('.')
    f = open(name,"r", encoding="latin1")
    text_file=f.read()
    words=text_file.split()
    if 'spam' in n:
        for word in words:
            if word.isalpha():
                if word in spam_key:
                    spam_key[word] = spam_key[word] + 1
                else:
                    spam_key[word] = 1 
                spamwords_count+=1
    else:
        for word in words:
            if word.isalpha(): 
                if word in ham_key:
                    ham_key[word] = ham_key[word] + 1
                else:
                    ham_key[word] = 1 
                hamwords_count+=1     

total_words= list(set(spam_key.keys()))+list(set(ham_key.keys()))
total_words= set(total_words)



for eachword in total_words:


    spam_key_temp = spam_key.get(eachword)
    ham_key_temp = ham_key.get(eachword)
    if spam_key.get(eachword):
        spam_key_prob[eachword] = (spam_key[eachword] + 1.0)/(spamwords_count + len(total_words))
    else:
        spam_key_prob[eachword] = (1.0)/(spamwords_count + len(total_words))
    if ham_key.get(eachword):
        ham_key_prob[eachword] = (ham_key[eachword] + 1.0)/(hamwords_count + len(total_words))
    else:
        ham_key_prob[eachword] = (1.0)/(hamwords_count + len(total_words))

p_spam= float(spamwords_count)/(spamwords_count+hamwords_count)
p_ham= float(hamwords_count)/(hamwords_count+hamwords_count)

file1 = open("nbmodel.txt","w")
file1.write(str(p_spam)) 
file1.write('\n')
file1.write(str(p_ham))
file1.write('\n')
file1.write(str(spam_key_prob))
file1.write('\n')
file1.write(str(ham_key_prob)) 
file1.close() 
