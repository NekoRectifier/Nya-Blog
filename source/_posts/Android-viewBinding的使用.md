---
title: Android viewBinding的使用
date: 2022-02-13 10:42:29
tags: Android, Jetpack
---

## 前言

之前只听说过`dataBinding`，在网上关于它的讲解一大把。如：[Android DataBinding 从入门到进阶](https://juejin.cn/post/6844903609079971854)。但是很少注意到`viewBinding`。  
直到最近才发现Android Studio中默认生成的java Fragment中有这么几行：

```java
    private FragmentCommunicationTripCodeBinding binding;

    @Override
    public View onCreateView(
            @NonNull LayoutInflater inflater, ViewGroup container,
            Bundle savedInstanceState
    ) {

        binding = FragmentCommunicationTripCodeBinding.inflate(inflater, container, false);
        return binding.getRoot();
    }
```

而且有了以上代码，对应布局文件中的组件就可以直接通过`binding.<id>`获取到了。使用起来十分方便。

## 具体食用方法

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
    在布局文件中的根组件中，添加以下代码：

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

    > xml名称首字母需大写, 如：`FragmentCommunicationTripCodeBinding`

4. 最后就可以通过`binding.<id>`获取到对应的组件了。

....有待后续更新
