# ToVXjson
转化标准格式的json文件成微信小程序所支持的对象嵌套的json文件

### 输入json格式要求
* 在ToVXjson.py文件同目录放置data.json文件（即你所要转化的文件）
* 最外面要有中括号包围;
* 中括号内的每个最外围的对象（即紧跟在中括号后面的{}包围的同层的整体对象）之间用，隔开;
* 必须是压缩后的json文件
* 压缩后的json文件里面不允许有多余的空格

以下各类图供理解：   
![所要转化的目的json格式图](https://raw.githubusercontent.com/kkkilo/ToVXjson/master/readmeImg/%E6%89%80%E8%A6%81%E8%BD%AC%E5%8C%96%E7%9A%84%E7%9B%AE%E7%9A%84%E6%A0%BC%E5%BC%8F.jpg)   
![所要求的json格式图](https://raw.githubusercontent.com/kkkilo/ToVXjson/master/readmeImg/%E6%89%80%E8%A6%81%E6%B1%82%E6%A0%BC%E5%BC%8F%E7%9A%84json.jpg)  
![json对比图](https://raw.githubusercontent.com/kkkilo/ToVXjson/master/readmeImg/json%E5%AF%B9%E6%AF%94%E5%9B%BE.jpg)   
![json对应的前身excel图](https://raw.githubusercontent.com/kkkilo/ToVXjson/master/readmeImg/json%E5%AF%B9%E5%BA%94excel%E6%A0%BC%E5%BC%8F.jpg)   


### 注意点
* 脚本其中会用到split函数，以英文逗号进行分隔，所以对于key或value中使用到英文逗号都会造成失败，如果可以请将他们换成中文逗号
* 