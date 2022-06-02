# 문자열

문자열은 받아 올 때 input()으로 받아올 수 있음!



문자열 뒤집는 방법 3가지!

1. slice 사용하는 방법

```python
# string[::1]

string = 'Hello, World!'
reversed_str = string[::-1]
```

2. reversed()를 이용하는 방법

```python
# reverse와 join 사용

string = 'Hello, World!'
reversed_str = "".join(reversed(string))
```

3. for loop 사용 방법

```python
string = 'Hello, World!'
reversed_str = ''
for i in string:
    reversed_str = i + reversed_str
```

