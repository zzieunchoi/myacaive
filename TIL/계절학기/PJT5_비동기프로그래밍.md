# PJT 5

비동기 프로그래밍



비동기: 병렬적으로 TASK 구현

가능한 이유: 모든 TASK가 가능한게 아니라, 비동기식으로처리할 수 있는 TASK가 존재

EX) FILE r/w, TIMER, NETWORK I/O ... 

공통적인 특징: CPU가 많은 일을 하지 않은 TASK



node.js 먼저 설치!

[node.js 설치](https://nodejs.org/en/)



최신버전말고 안정성 있는 예전 버전으로 설치 !

설치 완료 된 후에 window 키 + R 키를 누른다음 cmd 입력 후 enter

C:\Users\zzieu>에 `node -v`입력

그 밑에 `node`를 입력해야 node.js 사용 가능!



aixos를 사용하기 위해서는

`npm install axios`로 해서 axios 설치



## promise

promise는 비동기 작업의 단위!

```js
const promise1 = new Promise((resolve, reject) => {
    //비동기 작업
});
```

* resolve: 이 비동기 작업이 성공했어!
* reject: 이 비동기 작업이 실패했어ㅠㅠ



promise가 끝나고 난 다음의 동작을 우리가 설정해줄 수 있는데, 그것이 바로 `then`메소드와 `catch`메소드

* then: 해당 promise가 성공했을 때의 동작을 지정 - 인자로 함수를 받음
* catch: 해당 promise가 실패했을 때의 동작을 지정 - 인자로 함수를 받음

```js
promise1
.then(() => {
    console.log("then!");
})
.catch(() => {
    console.log("catch!");
});
```



## ASYNC AWAIT

promise를 좀 더 편하게 사용 가능

`async`는 function 앞에 위치

```js
async function f() {
    return 1;
}
```



`await`는 async 안에서만 동작

```js
let value = await promise;
```

await 키워드를 만나면 promise가 처리될 때까지 기다림. 결과는 그 이후 반환

1초 후 이행되는 promise를 예시로 사용하여 await가 어떻게 동작하는지 예시

```js
async function f() {
    let promise = new Promise((resolve,reject) => {
        setTimeout(() => resolve('완료!'), 1000)
    });
    let result = await promise;
    
    alert(result);
}

f();
```

함수를 호출하고, 함수 본문이 실행되는 도중에 `let result = await promise`줄에서 실행이 잠시 '중단’되었다가 promise가 처리되면 실행이 재개. 이때 프라미스 객체의 `result` 값이 변수 result에 할당. 따라서 위 예시를 실행하면 1초 뒤에 '완료!'가 출력됩니다.



promise가 처리되길 기다리는 동안에 엔진이 다른 일을 할 수 있기 때문에, CPI 리소스가 낭비되지 않음



`promise`에서 `await`으로 변환하기 위해서는

1. `.then`호출을 `await`으로 변경
2. function 앞에 `async`를 붙여 `await`를 사용할 수 있도록 해야함



## chaining 처리(hard code)

두 가지 처리 방법 : `.then`(promise) `async wait` 

일관성있게 작성하는 것이 중요!

```js
<!--promise 방식-->
function delay_word(word, delay) {
  return new Promise(resolve => {
    setTimeout(function (){
      resolve(word)
    }, delay)
  })
}


delay_word('SAMSUNG', 500).then((resolve) => {

	console.log(resolve)

	delay_word('SW', 490).then((resolve) => { 

		console.log(resolve)
		
		delay_word('ACADEMY', 480).then((resolve) => {
			
			console.log(resolve)

			delay_word('FOR', 470).then((resolve) => {

				console.log(resolve)

				delay_word('YOUTH', 460).then((resolve) => {

					console.log(resolve)
				})
			})
		})
	})
})

```

```js
<!--async wait방식-->
function delay_word(word, delay) {
  return new Promise(resolve => {
    setTimeout(function (){
      resolve(word)
    }, delay)
  })
}


async function test(){
	const resolve_0 = await delay_word('SAMSUNG', 500)
	console.log(resolve_0)
	const resolve_1 = await delay_word('SW', 490)
	console.log(resolve_1)
	const resolve_2 = await delay_word('ACADEMY', 480)	
	console.log(resolve_2)
	const resolve_3 = await delay_word('FOR', 470)
	console.log(resolve_3)
	const resolve_4 = await delay_word('YOUTH', 460)
	console.log(resolve_4)
}

test()

```



promise 방식이란?

async wait 방식이란?



## chaining 처리(soft code)

```js
<!--promise 방식-->
function delay_word(word, delay) {
  return new Promise(resolve => {
    setTimeout(function (){
      resolve(word)      
    }, delay)
  })
}


const array = [{word:'SAMSUNG', delay:500}, {word:'SW', delay:490}, {word:'ACADEMY', delay:480}, {word:'FOR', delay:470}, {word:'YOUTH', delay:460}]

array.reduce((prev, item) => {

	return prev.then(() =>
		delay_word(item.word, item.delay).then((promise) => {console.log(promise)}))

}, Promise.resolve())

```

```js
<!--async wait방식-->
function delay_word(word, delay) {
  return new Promise(resolve => {
    setTimeout(function (){
      resolve(word)      
    }, delay)
  })
}


const array = [{word:'SAMSUNG', delay:500}, {word:'SW', delay:490}, {word:'ACADEMY', delay:480}, {word:'FOR', delay:470}, {word:'YOUTH', delay:460}]

async function test(){

	for(const item of array) {
		const resolve = await delay_word(item.word, item.delay)
	
		console.log(resolve)				
	}
}

test()

```



## ALL 처리(비순차 결과)

YOUTH 가 먼저 출력 됨

```js
<!--promise 방식-->
function delay_word(word, delay) {
  return new Promise(resolve => {
    setTimeout(function (){
      resolve(word)
    }, delay)
  })
}


const array = [{word:'SAMSUNG', delay:500}, {word:'SW', delay:490}, {word:'ACADEMY', delay:480}, {word:'FOR', delay:470}, {word:'YOUTH', delay:460}]


array.forEach(async (item) => {
	
	delay_word(item.word, item.delay).then((resolve) => {console.log(resolve)})			
})

```

```js
<!--async wait방식-->
function delay_word(word, delay) {
  return new Promise(resolve => {
    setTimeout(function (){
      resolve(word)
    }, delay)
  })
}


const array = [{word:'SAMSUNG', delay:500}, {word:'SW', delay:490}, {word:'ACADEMY', delay:480}, {word:'FOR', delay:470}, {word:'YOUTH', delay:460}]


array.forEach(async (item) => {
	
	delay_word(item.word, item.delay).then((resolve) => {console.log(resolve)})			
})

```





## ALL 처리(순차 결과)

먼저 실행한게 처리되지 않았다면 그 다음 코드는 대기 상태

```js
<!--promise 방식-->
function delay_word(word, delay) {
  return new Promise(resolve => {
    setTimeout(function (){
      resolve(word)      
    }, delay)
  })
}


const array = [{word:'SAMSUNG', delay:500}, {word:'SW', delay:490}, {word:'ACADEMY', delay:480}, {word:'FOR', delay:470}, {word:'YOUTH', delay:460}]

array.reduce((prev, item) => {

	return prev.then(() =>
		delay_word(item.word, item.delay).then((promise) => {console.log(promise)}))

}, Promise.resolve())

```

```js
<!--async await방식-->
function delay_word(word, delay) {
  return new Promise(resolve => {
    setTimeout(function (){
      resolve(word)
    }, delay)
  })
}


const array = [{word:'SAMSUNG', delay:500}, {word:'SW', delay:490}, {word:'ACADEMY', delay:480}, {word:'FOR', delay:470}, {word:'YOUTH', delay:460}]


async function test(){
	
	const async_fun_list = []

	for(item of array){	
	
		const async_fun = delay_word(item.word, item.delay)
	
		async_fun_list.push(async_fun)
	}
		
	for(async_fun of async_fun_list){
		
		const resolve = await async_fun
		
		console.log(resolve)
	}		
}

	
test()

```

