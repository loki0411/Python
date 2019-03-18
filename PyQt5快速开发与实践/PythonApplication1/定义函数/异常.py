
def excep():
  try:
    num1 = int( input('输入num1：') )
    num2 = int( input('输入num2：') )
    print(num1/num2)

  except Exception as err:
    print( Exception )
    print(err)
  except ZeroDivisionError as err :
      print('error')
      print( ZeroDivisionError )
      print(err)
  except (ValueError,BufferError):
    print('lalala')
  else:
    print('everything is ok')
  finally:
    print('close')


with open('test.txt') as f:
  f.writelines('hello world')
  
  f.close
  pass
