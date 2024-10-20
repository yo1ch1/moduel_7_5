import os
import time



print('Текущая дериктория: ', os.getcwd())
if os.path.exists('test_dir1'):
    os.chdir('test_dir1')
else:
    os.mkdir('test_dir1')
    os.chdir('test_dir1')
print('Текущая дериктория: ', os.getcwd())
# for i in os.walk('.'):
#     print(i)
os.chdir(r'C:\PytonProject\Lessons\moduel_7_5')
print('Текущая дериктория: ', os.getcwd())
file_1 = [f for f in os.listdir() if os.path.isfile(f)]
dirs_1 = [d for d in os.listdir() if os.path.isdir(d)]
print(file_1)
print(dirs_1)

directory = os.getcwd()
for root, dirs, files in os.walk(directory):
    for file in files:
         filepath = os.path.join(root, file)
         filetime = os.path.getmtime(filepath)
         formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
         filesize = os.path.getsize(filepath)
         parent_dir = os.path.dirname(filepath)
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
