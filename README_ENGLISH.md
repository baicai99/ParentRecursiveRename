# Parental Recursive Naming Script

[中文](README.md) | [English](README_ENGLISH.md)

#### Purpose

Parental recursive naming is a naming convention often used for naming files, folders, or variables, where longer names contain parts of shorter ones. This method of naming allows us to organize and identify things more clearly, similar to familial naming in genealogies.

#### Effect

~~~
- Family Photos
  - Family Photos_Holiday
    - Family Photos_Holiday_2022_Summer Holiday
    - Family Photos_Holiday_2023_Winter Holiday
  - Family Photos_Wedding
  - Family Photos_Birthday
~~~

![Snipaste_2024-01-17_23-20-07](Snipaste_2024-01-17_23-20-07.png)

### Update Log

##### v1.0.3

- 2024.1.19: Fixed a bug where executing multiple times in the same directory would cause the name to become infinitely long. Now it will check if the name is equal to the directory level.

##### v1.0.2

- 2024.1.18: Fixed a bug where the renaming levels were incorrect.