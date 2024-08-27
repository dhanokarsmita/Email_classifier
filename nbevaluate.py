f = open("nboutput.txt", "r")
correct_spam=0
correct_ham=0

classify_spam=0
classify_ham=0

belong_spam=0
belong_ham=0

documents=0
output=f.read()
line=output.split("\n")
for eachLine in line:
	documents+=1
	s=eachLine.split("\t")
	path=s[1].split(".")
	if 'spam' in path:
		belong_spam+=1
	else:
		belong_ham+=1
	if s[0]=='spam':
		classify_spam+=1
	else:
		classify_ham+=1
	if s[0] in path:
		if s[0]=='spam':
			correct_spam+=1
		else:
			correct_ham+=1

accuracy = float(correct_ham+correct_spam)/documents
print("Accuracy:",accuracy)

precision_spam= float(correct_spam)/classify_spam
precision_ham= float(correct_ham)/classify_ham

print("precision_spam:",precision_spam)
print("precision_ham:",precision_ham)

recall_spam= float(correct_spam)/belong_spam
recall_ham= float(correct_ham)/belong_ham

print("recall_spam:",recall_spam)
print("recall_ham:",recall_ham)

fscore_spam=(2*precision_spam*recall_spam)/(precision_spam+recall_spam)
fscore_ham =(2*precision_ham*recall_ham)/(precision_ham+recall_ham)

print("fscore_spam:",fscore_spam)
print("fscore_ham:",fscore_ham)