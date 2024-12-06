import os
import time

# txt write example


txt_data = 'I like pizza'
file_path = 'output.txt'

os.chdir(os.getcwd())

#with open(file_path, 'w') as file:
 # file.write(txt_data)
#print(f'.txt file {file_path} was created')

try:
  if os.path.exists(file_path):
    os.remove(file_path)
    print(f'{file_path} was removed')
  else:
    print(f'creating {file_path}')
    with open(file_path, 'w') as file:
      file.write(txt_data)
    print(f'.txt file {file_path} was created')
except Exception as e:
  print('Error while creating on deleting file')