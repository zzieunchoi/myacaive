 

# 스캐너(scanner)

`ctrl + shift + o`단축키를 통해 import java.util.Scanner; 불러옴



입력하면 input 받은 것에 대해 출력해주는 것!

```java
Scanner scanner = new Scanner(System.in);
		String inputData;
		
		while(true) {
			inputData = scanner.nextLine();
			System.out.println("입력된 문자열: \"" + inputData + "\"");
			if(inputData.equals("q")) {
				break;
			}
		}
		
		System.out.println("종료");
```



*동일비교*

기본 타입 (byte, short, int, long, float, double, boolean) 의 값이 동일한지 비교 : ==

문자열 (string)이 동일한지 비교 : equals() 사용 

```java
int number = 3;
if (number == 3) {
    System.out.println("같음");
} else{
    System.out.println("아님");
}
// 같음

String name = "퐁깋동";
if (name.equals("퐁깋동")) {
    System.out.println("같음");
} else{
    System.out.println("아님");
}
// 같음
```

