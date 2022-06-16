# PJT 5

비동기 프로그래밍



비동기: 병렬적으로 TASK 구현

가능한 이유: 모든 TASK가 가능한게 아니라, 비동기식으로처리할 수 있는 TASK가 존재

EX) FILE r/w, TIMER, NETWORK I/O ... 

공통적인 특징: CPU가 많은 일을 하지 않은 TASK



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

