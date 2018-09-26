# coding: utf-8

# In[ ]:


def copyright():
    print("{a:*^40}".format(a="ProgramWork2"))
    print("{a}".format(a="This function translate scores into grade"))
    print("{a}".format(a="5-A,4-B,3-C,2-D,1-F,0-F"))
    print("By:Liumao-SA18225243")
    print("Date:2018-07-25")
    print("*" * 40, "\n")


gradeLists = ['A', 'B', 'C', 'D', 'F', 'F']


# In[ ]:
def valiation(score):
    if score < 0 or score > 5:
        raise Exception
    else:
        pass


def score2grade():
    score = input("请输入你的分数（0-5，输入'D'结束退出）:")
    try:
        i_score = int(score)
        valiation(i_score)
        global gradeLists
        grade = gradeLists[len(gradeLists) - i_score - 1]
    except Exception:
        if score == 'D':
            print("程序结束退出！")
            return None
        print("你的输入有误！")
        grade = score2grade()
    return grade


# In[ ]:
def main():
    copyright()
    while 1:
        grade = score2grade()
        if grade is None:
            break
        else:
            print("你对应的等级是：", grade)
            continue


if __name__ == '__main__':
    main()
