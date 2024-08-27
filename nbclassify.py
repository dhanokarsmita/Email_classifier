import glob
import math

d3= dict()
d4= dict()
f = open("nbmodel.txt", "r")
p_spam=float(f.readline())
p_ham = float(f.readline())
#eval(f.read())
d3 =eval(f.readline())
d4 = eval(f.readline())
count=0
count2=0
count3=0

l=[]
for name in glob.glob('C:/Users/niran/OneDrive/Desktop/sublime/Spam or Ham/dev/**/*.txt', recursive=True):
	count+=1
	f = open(name,"r", encoding="latin1")
	prob_spam=math.log(p_spam)
	prob_ham=math.log(p_ham)
	text_file=f.read()
	words=text_file.split()
	for word in words:
		if d3.get(word):
			prob_spam=prob_spam+math.log(d3[word])
		if d4.get(word):
			prob_ham=prob_ham+math.log(d4[word])
			
	if(prob_ham>=prob_spam):
		count2+=1
		l.append("ham" + "\t" + str(name))
	else:
		count3+=1
		l.append("spam" + "\t" + str(name))
	l.append("\n")


l = l[:-1]
file2 = open("nboutput.txt","w")
file2.writelines(l)
file2.close()




               
                
            
            
        

        