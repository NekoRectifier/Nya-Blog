---
title: MATLAB Cheat sheet
date: 2021-12-18 16:15:39
tags: [MATLAB]
---

# Misc (杂项)

*   用 `"` 来标识字符串(String); 用 `'` 来表示字符类型(Char)  

*   优雅的MATLAB脚本是有 `;` 作为休止符的
    > 对赋值命令使用 `;` 则其复制结果不会出现在命令区。

*   使用 `clear` 来清空变量, `clc` 来情况命令区输出

*   `.*` 通过将对应的元素相乘来将数组 A 和 B 相乘。A 和 B 的大小必须相同或兼容。(<i>即 A和 B都是数组之类的玩意 ?</i> )

    > 作图时貌似是很重要的玩意, 必须要有。

![mutlibyelementormartrix](mutlibyelementormartrix.png)

*   使用`format`来控制变量显示的精度  
    如: `format long`   显示15位小数  
        `format short`  再切换回4位小数

*   `linspace()` 与 `:` 的区别  
    ![colonoperatorandlinspace](colonoperatorandlinspace.png)
    -   `linspace(a,b,N)` 作用:   
        用于产生从 `a` 到 `b` 之间的N点行线性的矢量。其中 `a` 、`b` 、`N` 分别为起始值、终止值、元素个数。若默认无 `N` ，默认点数为100。  
    -   `a:S:b` 作用:
        用于产生从 `a` 到 `b` 之间的矢量。其中 `S` 指代每个数之间的间隔单位。
    > 可以使用 `x'` 将横向数组换成纵向数组。

*   `meshgrid()` 的使用
    范例: `[X,Y,Z] = meshgrid(x,y,z)`  
    > 当只有 `X` 和 `Y` 参数时, 返回二维坐标点, 反之亦然。  

    作为参数的 `x` 和 `y` 的定义应如下所示: `x = 1:3`

*   获取函数的多个输出 : 用`[]`  
    `[row, col] = size(x)`  
    得到数组的横纵长度值  
    `[value, index] = max(x)`  
    得到数组最大值和其索引值

*   `numel()`  
    <b>Number of array elements</b>  
    用于获得数组/矩阵的元素个数

*   `length()`  
    获取数组/矩阵(未查证)的长度

# 矩阵相关

## 常用函数

### `rand(x,y)`

用于生成随机数的矩阵, `x` 指代行 `y` 指代列。
### `zeros(x,y)`

用于生成 `0` 的矩阵, `x` 指代行 `y` 指代列。

### `size(x)`

查看矩阵的大小,返回 `行 · 列`的格式。
### 统计函数

|函数|用途|
|---|----|
|`min`|最小值|
|`max`|最大值|
|`mean`|平均数|
|`median`|中位数|
|`mode`|众数|
|`std`|标准差|
|`var`|方差|
|`sum`|求和|
|`prod`|元素乘积|

> 可以用已有的矩阵的大小来创建新的数列。如: `rand(size(x))`。

## 矩阵操作

### 清空指定位置的元素值

`data({索引}) = []`

### 排序

`[xSorted,idx] = sort({v},"descend")`

*   `xSorted` 是已排序的数组, 顺序有后面的 `descend` 决定
*   `idx` 是正确顺序的针对现有数组的索引
*   `descend` -> 递减 `ascend` -> 递增
*   可以指定 `"MissingPlacement"` 的值为 `"last"`来放置不太正常的值到排序后数组的最下面

### 通过索引提取特定值

#### 一维数组

使用 `x(index)` 来指定即可。

#### 二维数组 / 矩阵

使用 `x(row,column)` 来指定。

> 指定后可以对特定值直接进行赋值操作。

*   
    使用 `end` 关键字可以指定"最后"的行或列  
    如: `x = data(end, 3);`

*   使用 `:` 可代表所有"行"或"列"  
    如: `x = data(:,3);`

*   如果只使用一种索引 `x` (线性索引), 则它将按顺序从上到下遍历每列。

*   索引可以是非连续的 如: `x = data([1 4 6])`

*   可以构建出比较复杂的索引 如: `x = M([1 2], [1 end])`  
    如上的代码会选出矩阵中第1,2行的最前和最后的元素

![lineartosub](linearidtosubid.png)

#### 使用逻辑索引来提取

`x = data(data > {数值})`  

这样就会将满足条件的元素添加到 `x` 中去

同样的,这个也支持逻辑运算符 `& and` 和 `| or`  
如: `x = v1(v1>6 | v1<2)`

*   `isnan(v)` 输出逻辑向量来说明被判断的值是否为空 (1代表空)

### 数组运算

#### 基础运算

*   数组支持基于相同大小的数组的四则运算  
    `sum = x + y;`

*   或是任意数组与任意标量的运算  
    `a = x + 2;`

    > 此处隐含着 "标量扩张" ([Scalar Expansion](https://blogs.mathworks.com/loren/2006/02/22/scalar-expansion-and-more-take-2/)) 的概念

*   同样的任意大小的数组也支持进行各种函数运算  
    如: `sin(data)` 和 `sqrt(data)`

#### 求平均值

`mean({v})`

-   针对矩阵的使用: 指定对行还是对列  
    -   对行: `mean({v},2)`
    -   对列: `mean({v},1)`

-   针对存在 `NaN` 的解决方案:  
    1. 使用 `isNaN()` 进行确认
    2. 使用 `mean({v},"omitnan")`计算

    > 可使用 `nnz({v}})` 获知具体的 `NaN` 数量


### 数组串接 (Concatenation)

![串接 (Concatenation)](concatenation.png)

1.  横向串接  
    `x = [A, B]`  
    *   要求两矩阵的行数(`row`)相同即可
    *   貌似不要 `,` 也行, 直接 `x = [A B]`
2.  纵向串接
    `x = [A; B]`
    *   要求两矩阵的纵数(`col`)相同即可

### 矩阵构建

#### 函数生成

*   `rand({row},{col})`    生成随机的(0-1)矩阵

*   `zeros({row},{col})`   生成全是0的矩阵

*   `ones({row},{col})`    生成全是1的矩阵
#### 格式转换

*   `reshape({ori},{row},{col})`  
    将一维的 `vector` 转化为矩阵, 或将原有矩阵改变形状
    
    >   `{row}` 或 `{col}` 可采用 `[]` 作为通配符代替

    常见转换: matrix to one col `x(:)` & `reshape(x,[],1)`

# 制图相关

<b>[总指南](https://www.mathworks.com/help/matlab/creating_plots/types-of-matlab-plots.html)</b>

## 标识与图例

*   `xlabel()` 与 `ylabel()` 分别给 `x` 轴和 `y` 轴添加标识。

*   `title()` 用于给图表添加标识。

*   `legend("{sth1}","{sth2}")` 用于添加图例。  
    ![legend](legend.png)
## 2D制图

### 图表类型

*   折线图 `plot()`  
    使用方法:  
    -   `plot(x,y)`
    -   `plot(x1,y1,x2,y2)` 或 `plot(x,[y1 y2 ...]`
    -   `plot({matrix})` 效果见图:  
    ![plotmatrix](plotmatrix.png)

*   散点图 `scatter()`  
    基本输入与 `plot()` 相同
    -   更改点的大小 (第三个参数)  
        `scatter(x,y,{size})`  
        看起来好像没有上限的样子, 要做成随图像变化的样子则需要标记大小参数长度与 `x` 和 `y` 相同
    -   更改点的颜色 (第四个参数)
        



### 作图相关

* 改变图线: 通过在 `plot()` 的第三个参数中指定颜色/样式/端点形状.  
稍微具体一点的格式如下:

|颜色|样式|形状|
|----|----|----|
|r|--|o|
|g|:|+|
|b|-.|*|
|c|-|.|
|m|'none'|>|

*   使用 `"linewidth",{线宽}` 作为最后的参数可设置线宽。

*   绘制多图: 在 `plot()` 完后,执行 `hold on` 再去 `plot()` 下一个。

*   `xlim` 与 `ylim`  
    用于手动设置图像范围. 用法: `x/ylim([{起始} {终止}])`

## 3D制图

先使用 `meshgrid` 生成一组 `(X,Y)` 点, 再声明新的函数因变量, 如 `F = X.*exp(-X.^2-Y.^2);` .  

*   曲面图生成  
    `surf(X,Y,F);`.

    ![`surfc()` 的样子](surfc.png)

*   曲面点图生成  
    `mesh(X,Y,F);`

    > 还有 `meshc()` 和 `meshz()` , `c` 是等高线; 而 `z` 是底部加固体填充. 具体见图片.

![`meshc()`](meshc.png)

![`meshz()`](meshz.png)

![`plot3()`](plot3.png)

>   `surfc()` 相比原来的 `surf()` 是多加了个等高线在 `X-Y` 面上.

- 使用 `colorbar` 来添加颜色栏 

## 子图绘制 `subplot`

```MatlabScript
    subplot(m,n,p);
    subplot(m,n,p,'replace');
    subplot(m,n,p,'align');
```

>   `m` / `n` 指代建立的网格横纵数  
    `p` 指代该图像放在网格的位置 (从左到右数)  

# 编程与脚本

## 创建脚本

使用 `edit [文件名]` 即可.

## 添加注释

在行首添加 `%` .

## 运行脚本

在命令区内输入脚本名称

## 循环语句

```MatlabScript
    for n = 0:{MAX}
        [Other codes]
    end
```

以上代码展示了自变量 `n` 由0遍历至MAX值的循环语句

> 看起来是使用严格的缩进和"开始","结束"标识符来进行代码的分层

## 判断语句

```MatlabScript
    if num > 100
        a = 1000
    elseif num < 0
        a = -1
    else
        a = 0
    end
```

(不做过多解释)

