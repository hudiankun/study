#定义字典，并往里添加单词及释义，并且可查
myDic={}
while 1:
   xuanze=input("'a' to Add ,'l' to look up,'q' to quit:")

   if xuanze=='a':
      my_word=input('Type the word:')
      my_definition=input('Type the definition:')
      myDic[my_word]=[my_definition]
      print('Word added!')
   elif xuanze=='l':
        my_word=input('Type the word:')
        if my_word in myDic.keys():
           print(myDic[my_word])
        else:
          print('That word isnot in the dictionary yet.')
   elif xuanze=='q':
         break