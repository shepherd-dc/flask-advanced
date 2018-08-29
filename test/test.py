import threading
import time

from werkzeug.local import Local, LocalStack

my_local = Local()
my_local.a = 'a'

my_stack = LocalStack()
my_stack.push(1)
print(my_stack.top)

def worker():
    print('I am a thread worker')
    print(my_stack.top)
    t = threading.current_thread()
    # time.sleep(10)
    print(t.getName())
    my_local.a = 'b'
    print(my_local.a)
    my_stack.push(2)
    print(my_stack.top)


new_t1 = threading.Thread(target=worker, name='new thread1')
new_t1.start()
# new_t2 = threading.Thread(target=worker, name='new thread2')
# new_t2.start()
time.sleep(1)

t = threading.current_thread()
print(t.getName())
print(my_local.a)
print(my_stack.top)