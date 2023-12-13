 [中文](README.md) | [English](README_EN.md)


这是一个易用的批量漫画对话框快速生成器，会在漫画底部快速生成一个白底对话框，并且根据字体长度自动调整字体大小以适应对话框大小。
效果展示：
![1](https://github.com/monorio/EasyComicDialogBox/assets/39545032/90a0a80c-bbae-4830-b735-3fca25ca5850)
![2](https://github.com/monorio/EasyComicDialogBox/assets/39545032/869af741-0df9-4dc5-9b9a-b45fe0eb9bf8)

不同字体
![1](https://github.com/monorio/EasyComicDialogBox/assets/39545032/614a8292-e753-4a1a-99e0-9f22a003a9b7)
![2](https://github.com/monorio/EasyComicDialogBox/assets/39545032/43e39ca2-4729-46bb-b747-d96f44d73111)




其中，gui_app.exe和gui_app_CHN.exe可以直接下载到WINDOWS系统下使用（其它系统未测试），无须其它依赖文件。但要注意的是，项目中的favicon.ico![image](https://github.com/monorio/EasyComicDialogBox/assets/39545032/67a4f19e-1824-48fd-b9e3-1f5e92f6a73f) 图标需要和exe文件在同一文件夹下，否则报错，这是图标文件，对功能没有影响。

gui_app_CHN.exe 使用教程(gui_app.exe同理)：
1. 运行程序
2.点击浏览
![image](https://github.com/monorio/EasyComicDialogBox/assets/39545032/37e6cea7-c0fa-4140-abdb-8560a83f0771)
3. 定位到图片文件夹中选择文件夹
![image](https://github.com/monorio/EasyComicDialogBox/assets/39545032/666aeca8-1766-4b93-9eb1-df4aac6e0f27)
4. 调整字体缩放 (512*768缩放设置为-1.5效果较好，1920*180设置为0效果较好，可以根据自己情况调整)
![image](https://github.com/monorio/EasyComicDialogBox/assets/39545032/b9d7a592-dff5-4c45-8cef-b80aa258c9ee)
5. 更换自己喜欢的字体，默认为等线中文，可以不调整。系统中没有等线中文字体的话，Windows 系统下到 C:/Windows/Fonts/ 右键ttf字体属性查看路径，复制对应字体路径。
![image](https://github.com/monorio/EasyComicDialogBox/assets/39545032/84f43498-a34b-4242-9fdb-9a39dd0b87c3)
6. 点击执行按钮完成对话框制作，完成后的图片在图片文件夹下的output目录中

额外功能：
1.因为本APP只转换PNG格式的图片，所以提供了其它图片转PNG格式的功能，选好目录路径后直接点击‘转换为PNG’按钮执行。
2.图片按阿拉伯数字自动排序功能。很多图片并非按照数字升序排序，而是其它排序方式，这个APP提供重新排序功能，输出图片在图片目录下的sorted中。

重要！！！：
1.favicon.ico不得移除，否则会报错。或者可以使用其它ico文件替代。
2.重要的步骤，对script.txt内容的编排，也就是图片对应脚本文件的设置。

2.1 
以本项目中的demo文件夹举例

2.2 
生成图片的目录中必须创建一个名字为 script.txt的文件，如图所示
![image](https://github.com/monorio/EasyComicDialogBox/assets/39545032/a281f992-ba38-44e7-8ae7-5344e4e31c96)

2.3
每个图片的脚本对应阿拉伯数字+p的格式，如果一张图片有多个段落，可以换行，不同图片脚本空一行隔开。具体如图片所示，也可以参考项目中的demo文件夹下的script.txt文件的格式编写脚本
![image](https://github.com/monorio/EasyComicDialogBox/assets/39545032/e2d2fc50-456e-4057-8927-d550d278cf48)

除了使用exe程序，也可以使用py文件运行，代码中有使用实例。也欢迎进行二次开发。

未解决问题：
1. 本项目对特殊字符支持有限，可能会显示方框，可能和字体库支持有关。
2.  对英文的支持较差，效果有限，中文效果较好。初步判断是英文字符占用单位较少，之后可能会更新版本。

   
