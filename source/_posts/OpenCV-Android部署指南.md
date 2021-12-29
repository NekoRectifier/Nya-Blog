---
title: OpenCV_Android部署指南
date: 2021-12-22 16:17:41
tags: [Android, OpenCV]
---

## OpenCV Release获取

直接点击[这里]("https://github.com/opencv/opencv/releases/download/4.5.4/opencv-4.5.4-android-sdk.zip")下载opencv sdk 4.5.4

下载到本地后解压即可

![解压后图片](afterde.png)

## Android Studio相关配置

1.  新建一个项目,新建选项要选择 `Native C++` ,名称等配置随意.  

    ![Native](nativ.png)

2.  新建完后导入opencv模块, 在`File` > `New` > `Import Module` 里

    ![Module](importmodule.png)

    在打开的窗口内选择 `sdk` 文件夹导入即可  
(适用于有build.gradle在解压文件夹下的情况,如果没有则本片指南不适用于你的opencv版本)

3.  现在你的项目文件在 `Android` 视角下应该是这个样子  
![项目列表](projlist.png)

    -   如果导入后项目报 `kotlin` 相关错误, 则在 `build.gradle (Project: XXX)` 中,添加  

        `ext.kotlin_version="1.6.10"`和`classpath "org.jetbrains.kotlin:kotlin-gradle-plugin:1.6.10"`  

        使gradle文件如下所示:

        ```gradle
        build script{
            ext.kotlin_version="1.6.10"
            repositories {
                ...
            }

            dependencies {
            classpath "com.android.tools.build:gradle:XXX"
            classpath "org.jetbrains.kotlin:kotlin-gradle-plugin:1.6.10"
            }
            ...
        }
        ```

        如果没有则无视以上内容

    选择 `File` > `Project Structure`

    ![Proj](projstru.png)

    点击 `Module Dependency` 后在弹出的新窗口内选择刚刚添加的 `opencv sdk`即可

4.  打开 `build.gradle (Module: XXX.sdk)` 修改以下三个参数,使其与 `build.gradle (Module: app)` 中的相同

    ![build](build.png)

## 测试

在 `MainActivity.java` 中的 `onCreate` 方法里写

```java
if (OpenCVLoader.initDebug()) {
    Log.d("myTag", "OpenCV loaded")
}
```

然后部署到真机/模拟器查看log输出.

# 参考链接

[1] https://www.cnblogs.com/zhoushasha/p/10952148.html

[2] https://stackoverflow.com/questions/65570664/how-to-import-opencv-4-5-in-android-studio



