def parse_nrc():
	word_emotion_dict={}
	f=open("NRC-Emotion-Lexicon-Senselevel-v0.92.txt")
	list_lines= f.readlines()

	word_emotion_dict={}

	for line in list_lines:
		splitted= line.split("--")
		word=splitted[0]

		word_emotion_dict[word]={}




	for line in list_lines:

		splitted= line.split("--")
		word=splitted[0]

		splitted2= splitted[1].split("\t")
		emot_score=splitted2[-1].strip("\n")
		emot=splitted2[-2]

		word_emotion_dict[word][emot]= emot_score
		#print(splitted2)
		#print(emot)
		#print(emot_score)
	return(word_emotion_dict)




if __name__=="__main__":
	#print(get_transcript())
	print(parse_nrc())
