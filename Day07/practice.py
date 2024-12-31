from wd_message.message_send import send
from wd_message.message_receive import receive
import os
import sys


def file_read():
    file = open('file1', mode='r', encoding='utf-8')
    text = file.read()
    print(text)
    file.close()


def file_write():
    file = open('file1', mode='w', encoding='utf-8')
    file.write('20241231')
    file.close()


def file_rw():
    file = open('file1', mode='r+', encoding='utf-8')
    txt = file.read()
    print(txt)
    file.write('hahaha')
    file.close()


def read_line():
    file = open('file1', mode='r', encoding='utf-8')
    while True:
        txt = file.readline()
        if not txt:
            break
        print(txt, end='')
    file.close()


def dir_func():
    file_list = os.listdir('.')
    print(file_list)
    cwd = os.getcwd()
    print(cwd)
    os.chdir('./wd_message')
    print(os.getcwd())


def seek_test():
    f = open('file1', 'r', encoding='utf-8')
    f.seek(5, 0)  # 从起始位置往后偏移5个字节
    t = f.read()
    print(t)
    f.close()


def seek_b_test():
    f = open('file1', 'rb')
    f.seek(2, 0)  # 从起始位置向后偏移2个字节
    t = f.read(4)
    print(t)
    f.seek(3, 1)  # 从当前位置向后偏移3和字节
    t = f.read(4)
    print(t)
    f.seek(-4, 2)  # 从末尾向前偏移4个字节
    t = f.read()
    print(t)
    f.close()


def scan_dir(file_path, deepth):
    file_dir = os.listdir(file_path)
    for f_d in file_dir:
        print(' '*deepth, f_d)
        new_path = file_path+'/'+f_d
        if os.path.isdir(new_path):
            scan_dir(new_path, deepth+4)


if __name__ == '__main__':
    # 1.完成包的使用（与上课一致）
    send()
    msg = receive()
    print(msg)

    # 2.完成文件的文本模式的读，写（与上课一致）
    file_read()
    file_write()
    file_rw()
    read_line()

    # 3.完成目录的listdir，getcwd,chdir的使用（与上课一致）
    dir_func()

    # 4.完成python的传参练习（与上课一致）
    # print(sys.argv[1])
    # 在cmd执行：python  ./practice.py 123
    # 输出结果即为传入的123

    # 5、完成普通文件文件的seek，二进制文件的seek（代码编写与上课一致即可）
    seek_test()
    seek_b_test()

    # 6、完成目录深度优先遍历（代码编写与上课一致即可）
    scan_dir('.', 0)
