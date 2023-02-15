Guide = {'0':6,'1':2,'2':5,'3':5,'4':4,'5':5,'6':6,'7':3,'8':7,'9':6}

T = int(input())

for i in range(T):

   N = str(input())

   counter = 0

   for i in N:

       counter += Guide[i]

   result = ''

   if counter%2 == 0:

       for i in range(int(counter/2)):

           result += '1'

   else:

       for i in range(int((counter-3)/2)):

           result += '1'

       result = '7'+result

   print(result)