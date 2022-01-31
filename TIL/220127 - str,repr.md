# str과 repr 다른 점

``` 
__str__ 과 같이 __가 있는 메서드는 이미 내장되어있는 메서드
그렇다면 __str__: 사람이 보기 편한 것 user friendly
__repr__: for developer 개발자를 위해서 만들어짐
같이 있으면 str이 더 우선순위!
repr, str에서 print를 쓰면 결과를 보여줌

str, repr 메소드를 부르지 않으면 print를 해도 결과가 출력이 안됨!
-> <main.Person object at xxxx> 이렇게 출력이 됨
```



