---
title: Android viewBinding的使用
date: 2022-02-13 10:42:29
tags: Android, Jetpack
---

## 前言

`viewBinding`相当于`dataBinding`的精简版。功能上能够方便的获取视图组件的实例，避免了`findViewById()`的繁琐操作，但是不能将数据绑定到视图组件上。不过在开发轻量级应用时，这个功能足够满足需求了。  
关于`dataBinding`，在网上关于它的讲解不少。如：[Android DataBinding 从入门到进阶](https://juejin.cn/post/6844903609079971854)。  

## 开始使用

在Android Studio中默认生成项目中的java中有这么几行：

```java
    private <xml名称>Binding binding;

    @Override
    public View onCreateView(
            @NonNull LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState
    ) {

        binding = <xml名称>Binding.inflate(inflater, container, false);
        return binding.getRoot();
    }
```

而且有了以上代码，对应布局文件中的组件就可以直接通过`binding.<id>`获取到了。使用起来十分方便。

### 具体食用方法

1. 开启viewBinding功能
    在`build.gradle(Module)`中添加以下代码：

    ```gradle
        android {

            ...

            buildFeatures {
                viewBinding true
            }
        }
    ```
  
    > 注意你所使用的gradel版本，写法可能与我有所不同。

2. 修改布局文件
    在布局文件中的**根**组件中，添加以下代码：

    ```xml
      tools:context=".NationalGovernmentPlatformFragment"
    ```

    总体看起来是这样：

    ```xml
    <androidx.constraintlayout.widget.ConstraintLayout
        xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:tools="http://schemas.android.com/tools"
        android:id="@+id/fragment_communication_trip_code"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        tools:context=".NationalGovernmentPlatformFragment" >

        ...

    </androidx.constraintlayout.widget.ConstraintLayout>
    ```

3. 在对应java文件中添加`binding`变量
    在对应java文件中添加以下代码：(这是在Fragment中的情况)

    ```java
    private <xml名称>Binding binding = <xml名称>Binding.inflate(inflater, container, false);
    ```

    > xml名称首字母需大写, 如：`FragmentCommunication`

4. 最后就可以通过`binding.<id>`获取到对应的组件了。

    ```java
    public void onViewCreated(View view, Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);

        binding.tvTitle.setText("我是标题");
    }
    ```

    > 注意：`binding.<id>`中的`<id>`是根据布局文件中的组件的id来写的。

