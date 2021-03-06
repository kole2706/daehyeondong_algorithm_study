from collections import deque
import sys
input=sys.stdin.readline

class NM:
    def read(self):
       self.N,self.M=map(int,input().split())
  
       
    def BFS(self): #BFS
        use=[str(i) for i in range(1,self.N+1)]
        for i in range(1,self.N+1):
            search_queue=deque()
            search_queue+=[str(i)]
            root=str(i)
            while search_queue:
                person=search_queue.popleft()
                if len(person)-(self.M-1)==self.M:
                    print(person)    
                else:
                    root=person 
                    search_queue+=[root+' '+item for item in use]
                  
nm=NM()
nm.read()
nm.BFS()