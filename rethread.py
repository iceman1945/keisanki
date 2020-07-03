from threading import　Semaphore, Thread

def my_function1():
  for i in range(10):
    with semaphore:
      print("123")
      print("456")
      print("789")

def my_function2():
  for i in range(10):
    with semaphore:
      print("abc")
      print("def")
      print("ghi")

def my_function3():
  for i in range(10):
    with semaphore:
      print("ABC")
      print("DEF")
      print("GHI")

if __name__ == "__main__":
  semaphore = Semaphore(1)
  t1 = Thread(target = my_function1   
  t2 = Thread(target = my_function2)  
  t3 = Thread(target = my_function3)
