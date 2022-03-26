---
title: Android权限请求写法
date: 2022-03-26 11:18:41
tags: Android
---

## 前言

在Android中进行权限获取向来不是件容易事，尤其是在API23后Android引入了运行时权限的机制，这个机制的原理是通过检查应用程序的权限状态来控制应用程序的行为。同样也使得开发者在开发应用程序时需要更多考虑权限的问题。  
以下便是在StackOverflow上看到的比较好的一个处理方法。

## `onRequestPermissionsResult()` 替代品

在AndroidX时代，我们可以使用`registerForActivityResult()`来代替`onRequestPermissionsResult()`，这个方法可以让我们更加方便地处理权限请求的结果。

```Java

// 写在Fragment的onViewCraeted()方法外就行

    private final ActivityResultLauncher<String> permission_result = registerForActivityResult(
            new ActivityResultContracts.RequestPermission(),
            result -> {
                if (result) {
                    //granted
                } else {

                }
            }
    );
```

然后在`onCreate()`/`onViewCreated()`方法中调用`permission_result.launch(permission)`即可。

```Java

public void onCreate(Bundle savedInstanceState) {
    permission_result.launch(Manifest.permission.CAMERA);
    permission_result.launch(Manifest.permission.ACCESS_FINE_LOCATION);
    permission_result.launch(Manifest.permission.ACCESS_COARSE_LOCATION);
    permission_result.launch(Manifest.permission.READ_PHONE_STATE);
}
```

Kotlin实现：

```Kotlin
val permReqLuncher = registerForActivityResult(ActivityResultContracts.RequestPermission()){
  if (it) {
     // Good pass
  } else {
     // Failed pass
  }
}
```

## 请求结果

![req](req.jpg)

就如图片所示，代码中请求的提示框会一个一个的弹出给用户提示。

## 参考链接

[1] https://stackoverflow.com/questions/66551781/android-onrequestpermissionsresult-is-deprecated-are-there-any-alternatives
