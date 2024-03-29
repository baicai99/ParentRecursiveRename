# 父级递归命名脚本

[中文](README.md) | [English](README_ENGLISH.md)

#### 作用

父级递归命名是一种命名规则，通常用于给文件、文件夹或变量等命名，其中较长的名称包含了更短名称的一部分。这种命名方式让我们能够更清晰地组织和标识事物，就像家谱中的家族命名一样。

#### 效果

~~~
- 家庭照片
  - 家庭照片_假日
    - 家庭照片_假日_2022_夏季假日
    - 家庭照片_假日_2023_冬季假日
  - 家庭照片_婚礼
  - 家庭照片_生日
~~~

![Snipaste_2024-01-17_23-20-07](Snipaste_2024-01-17_23-20-07.png)

### 更新记录

##### v1.0.3

- 2024.1.19：修复bug，同一目录多次执行的话名字会变的无限长，现在会判定名字是否等于目录层级。

##### v1.0.2

- 2024.1.18：修复bug，重命名层级不正确。