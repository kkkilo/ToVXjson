#encoding:utf-8
import sys
import os

#读取json文件
def inputJson():
    try:
        with open('data.json', 'r',encoding = 'utf-8') as datajson:
            prejson = datajson.read()
            return prejson
    except Exception as e:
        print('inputJson读取json文件异常!')
        print(e)
        sys.exit()

#拆分各个部分组合成数组
def getSplitArray(json, str):
    try:
        arr = json.split(str)
        return arr
    except Exception as e:
        print('getSplitArray拆分json出错!')
        print(e)
        print('json:',json,'分割符号：',str)
        sys.exit()

#去掉开头结尾的括号
def arrTrim(arr):
    try:
        if arr[0][:2] == '[{':
            arr[0] = arr[0][2:]
        elif arr[0][0] == '{':
            arr[0] = arr[0][1:]
        length = len(arr)
        tailLen = len(arr[length-1])
        if arr[length-1][tailLen-2:] == '}]':
            arr[length-1] = arr[length-1][:tailLen-2]
        elif arr[length-1][tailLen-1] == '}':
            arr[length-1] = arr[length-1][:tailLen-1]
        return arr
    except Exception as e:
        print('arrTrim去掉开头结尾括号出错!')
        print(e)
        print('arr[0]:',arr[0],'arr['+(tailLen-1)+']',str)
        sys.exit()
   
#替换关键词
def transform(preArr):
    try:
        aftArr = []
        flagStack = [False]       #栈：存储是否要忽略key去当成数组一样只存储value
        index = 0                 #与上面的栈配合使用
        for item in preArr:
            if len(item) > 28 and item[:28] == '"SEPERATION_TAG_OBJECT_BEGIN':
                aftArr.append(item[28:] + ':{')
                flagStack.append(False)
                index+=1
            elif len(item) > 27 and item[:27] == '"SEPERATION_TAG_ARRAY_BEGIN':
                aftArr.append(item[27:] + ':[')
                flagStack.append(True)
                index+=1
            elif len(item) > 26 and item[:26] == '"SEPERATION_TAG_OBJECT_END':
                aftArr.append('}')
                flagStack.pop()
                index-=1
            elif len(item) > 25 and item[:25] == '"SEPERATION_TAG_ARRAY_END':
                aftArr.append(']')
                flagStack.pop()
                index-=1
            elif flagStack[index]:
                aftArr.append(item.split(':')[1])
            else :
                aftArr.append(item)
            print('替换符号完成！')
        if len(flagStack) > 1:
            print('SEPERATINO分隔符的标志写错啦，注意检查一下BEGIN和ENDING是不是写错啦')
        return mergeAndClean(aftArr)
    except Exception as e:
        print('transform函数转化出错!')
        print(e)
        sys.exit()

#去掉括号前后的逗号
def mergeAndClean(arr):
    try:
        print('开始清理逗号')
        json = (',').join(arr)
        json = json.replace(',[', '[')
        json = json.replace(',{', '{')
        json = json.replace(',]', ']')
        json = json.replace(',}', '}')
        json = json.replace('[,', '[')
        json = json.replace('{,', '{')
        json = "{" + json + "}"
        return json
        print('清理完成')
    except Exception as e:
        print('mergeAndClean函数清理出错!')
        print(e)
        sys.exit()

#输出json文件
def outputJson(text):
    try:
        with open('output.json', 'wb') as f:
            f.write(text.encode("utf-8"))
    except Exception as e:
        print('outputJson输出函数清理出错!')
        print(e)
        sys.exit()

#主函数
def main():
    print('开始读取文件')
    jsonText = inputJson()
    print('已读取文件')
    #print(jsonText)

    print('开始拆分')
    jsonArr = getSplitArray(jsonText,'},{')
    print('拆分完毕')

    print('预处理开始')
    jsonArr = arrTrim(jsonArr)
    print('预处理完毕')

    print('开始转化，总量为：'+str(len(jsonArr)))
    i = 0
    finalJson = ''
    for item in jsonArr:
        preArr = getSplitArray(item, ',')
        text = transform(preArr)
        print("已经转化数量：",str(i)+"/"+str(len(jsonArr)-1))
        i+=1
        finalJson += text
    print('转化完毕')

    print('开始输出json文件')
    outputJson(finalJson)
    print('输出完成！')
    os.system('pause')
    
main()


