 [中文](README.md) | [English](README_EN.md)


This is an easy-to-use batch comic dialog box quick generator that will quickly generate a white background dialog box at the bottom of the comic and automatically adjust the font size to fit the dialog box size based on the text counts.

Effect:
![1](https://github.com/monorio/EasyComicDialogBox/assets/39545032/90a0a80c-bbae-4830-b735-3fca25ca5850)
![2](https://github.com/monorio/EasyComicDialogBox/assets/39545032/869af741-0df9-4dc5-9b9a-b45fe0eb9bf8)

不同字体
![1](https://github.com/monorio/EasyComicDialogBox/assets/39545032/614a8292-e753-4a1a-99e0-9f22a003a9b7)
![2](https://github.com/monorio/EasyComicDialogBox/assets/39545032/43e39ca2-4729-46bb-b747-d96f44d73111)


Gui_app.exe and gui_app_CHN.exe can be directly downloaded to the WINDOWS system to use (other systems have not been tested). However, it should be noted that the project's favicon.ico ![image](https://github.com/monorio/EasyComicDialogBox/assets/39545032/67a4f19e-1824-48fd-b9e3-1f5e92f6a73f) icon must be in the same folder with the exe file, otherwise, it will report an error, although it is an icon file and does not affect the function.


Tutorial of gui_app.exe (same for gui_app_CHN.exe):
1. Run the program
   
2. Click the ‘Browse’ button ![image](https://github.com/monorio/EasyComicDialogBox/assets/39545032/9dd4d5f1-d0f9-4e5b-aadb-c26105b98823)

3. Locate the selected folder in the Pictures folder ![image](https://github.com/monorio/EasyComicDialogBox/assets/39545032/666aeca8-1766-4b93-9eb1-df4aac6e0f27)
   
4. Adjust the font scaling by MIN_SET (512 * 768 scaling set to -1.5 effect is better, 1920 * 180 set to 0 effect is better, you can adjust according to their situations) ![image](https://github.com/monorio/EasyComicDialogBox/assets/39545032/40bf98e5-ce0f-4c08-b497-67f3c46691cb)

5. Replace your favorite font, the default is Dengb.ttf, no need to adjust. If you don't have Dengb.ttf font type in your system, under Windows system, search C:/Windows/Fonts/, right-click ttf font properties to view the path, and paste the corresponding font path here. ![image](https://github.com/monorio/EasyComicDialogBox/assets/39545032/c8ae4b38-2b5f-486d-8984-84ed2970a8a0)

6. Click the "Execute" button to finish creating the dialog box. The finished image is in the output directory under the Pictures folder.

Extra Functions:
1. Because this APP only converts pictures in PNG format, it provides the function for converting other pictures to PNG format, which is executed by directly clicking the 'Convert to PNG' button after selecting the directory path.
2. Pictures should sorted by numerical order before generating the dialog box. However, many pictures are not sorted in ascending order according to numbers, but with other sorting methods. This APP provides a re-sorting function, the output pictures will be in the 'sorted' directory after clicking the 'Sort Images' button.

Important!!! :
1.favicon.ico must not be removed or it will report an error. You can use other ICO files instead.
2. Important step (the content format of script.txt):
2.1 Take the demo folder in this project as an example.
2.2 A file named script.txt must be created in the directory where the image is generated, as shown in the following figure.
! [image](https://github.com/monorio/EasyComicDialogBox/assets/39545032/a281f992-ba38-44e7-8ae7-5344e4e31c96)
2.3 The script of each image corresponds to the format of Arabic numerals + p. If an image has more than one paragraph, you can change the line, and separate the scripts of different images with an empty line. As shown in the picture, you can also refer to the script.txt file under the demo folder in the project to write the scripts.
! [image](https://github.com/monorio/EasyComicDialogBox/assets/39545032/e2d2fc50-456e-4057-8927-d550d278cf48)

PS:
In addition to using the exe program, you can also use py files to run, the code has examples of usage. Re-development is also welcome.
Problems unsolved:
1. This project has limited support for special characters and may display boxes. May be related to font library support.
2. Poor support for the English characters, the effect is limited, the effect of Chinese characters is better. Preliminary judgment is that the English characters occupy fewer units, the version of this app may be updated.

   

