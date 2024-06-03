# hàng đợi dựng sẵn trong python

from queue import Queue

if __name__ == '__name__':
    q = Queue(-1)
    
    print('----- Put-----')
    for x in range(1,6):
        print(f'put {x}')
        q.put(x)
       
        
        
    print('---- Get----')
    while not q.empty() :
        gt = q.get()
        print(f'get -> {gt}')
        