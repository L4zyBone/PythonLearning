import copy
import re


# 1、练习深copy与浅copy
def copy_test():
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]
    list_c = [list_a, list_b]
    # 浅拷贝
    list_d = copy.copy(list_c)
    # 深拷贝
    list_e = copy.deepcopy(list_c)
    list_a[0] = 11
    print(list_d)  # 浅拷贝的新对象内部的引用关系与原来的对象一样
    print(list_e)  # 深拷贝的新对象内部的引用也产生了新的副本


# 2、练习上课匹配单个字符，多个字符，匹配分组的正则表达式案例
# 单个字符匹配
def single():
    result = re.match('h.llo', 'hello')
    print(result.group())
    result = re.match('[Hh]', 'Hello')
    print(result.group())
    result = re.match('今年[0-6]月', '今年4月')
    print(result.group())
    result = re.match(r'嫦娥\d号', '嫦娥1号发射成功')
    print(result.group())


# 多个字符匹配
def multiple():
    result = re.match('[A-Z][a-z]{3}', 'Hello Python')
    print(result.group())
    result = re.match(r'\w*123', 'Python学习12344')
    print(result.group())
    # 命名规范，字母或下划线开头
    names = ["name1", "_name", "2_name", "__name__"]
    for i in names:
        result = re.match(r'[a-zA-Z_]+\w*', i)
        if result:
            print(f'{result.group()}是规范的')
        else:
            print(f'{i}不规范')


# 匹配分组
def split_group():
    # 匹配0到100
    result = re.match(r'[1-9]?\d$|100', '100')
    print(result.group())
    # 匹配1-99
    result = re.match('[1-9][0-9]|[1-9]', '89')
    print(result.group())
    # 匹配邮箱
    result = re.match(r'[A-Za-z0-9]{4,20}@[a-zA-Z0-9]{4,8}\.com', 'sdfS21@sSq2.com')
    if result:
        print(result.group())
    else:
        print('邮箱格式不正确')
    # 电话号分组
    result = re.match('([^-]+)-([0-9]*)', '010-21312312')
    print(result.group(0))
    print(result.group(1))
    print(result.group(2))

    result = re.match(r'<[a-zA-Z]+>\w*</[a-zA-Z]+>', '<html>hh</html>')
    print(result.group())

    result = re.match(r'<([a-zA-Z]+)>\w*</\1>', '<html>hh</html>')
    print(result.group())

    result = re.match(r'<(?P<name1>[a-zA-Z]+)><(?P<name2>[a-zA-Z]+)>\w*</(?P=name2)></(?P=name1)>',
                      '<html><a>hh</a></html>')
    print(result.group())


# 3、练习上课的search，findall,sub等案例
# search只搜第一个
def search_test():
    result = re.search(r'\d+', '播放9999，点赞888')
    print(result.group())


# findall返回所有符合的数据
def findall_test():
    result = re.findall(r'\d+', 'Python=1000, Java=2000, C++=3000')
    print(result)


# sub按照表达式进行替换
def add(x):
    return str(int(x.group())+90)


def sub_test():
    result = re.sub(r'\d+',lambda x: str(int(x.group())+90),'Python=1312')
    print(result)
    result1 = re.sub(r'\d+', add, 'Python=1312')
    print(result1)


if __name__ == '__main__':
    copy_test()
    single()
    multiple()
    split_group()
    search_test()
    findall_test()
    sub_test()