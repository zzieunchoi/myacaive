# javascript 심화

## DOM

:document object model

문서 html 조작



dom이란 문서를 구조화하고 구조화된 구성 요소를 하나의 객체로 취급하여 다루는 논리적 트리 모델

문서사 구조화되어 있으며 각 요소는 객체로 취급

- window: dom을 표현하는 창, 가장 최상위 객체(작성시 생략 가능)
- document: 페이지 콘텐츠의 entry point역할을 함
- navigator, location, history, scree



DOM 관련 객체의 상속 구조

* Event Target

  :event listener를 가질 수 있는 객체가 구현하는 dom 인터 페이스

* Node

  : 여러가지 dom 타입들이 상속하는 인터 페이스

* element

  부모인 node와 그 부모인 eventtarger의 속성을 상속

* document

* html element



dom 선택 - 선택 관련 메서드

* document.querySelector(selector)

  제공한 선택ㄷ자와 일치하는 element하나 선택

  제공한 css selector를 만족하는첫 번째 element 객체 반환(없다면 null)

* document.querySelectorAll(selector)

  제공한 선택자와 일치하는 여러 element를 선택

  지정된 셀렉터에 일치하는 node list를 반환



dom 조작

```javascript
<h1>Hello SSAFY</h1>
  <h2 id="location-header">Location</h2>
  <div>
    <ul>
      <li class="ssafy-location">서울</li>
      <li class="ssafy-location">대전</li>
      <li class="ssafy-location">광주</li>
      <li class="ssafy-location">구미</li>
      <li class="ssafy-location">부울경</li>
    </ul>
  </div>
```



```javascript
console.log(window)
//
console.log(document)
//
console.log(window.document)
//

const h1 = document.querySelector('h1')
h1.innerText //
h1.innerText = '쉬는시간?!' // h1이 쉬는시간?!으로 변경
const h2 = document.querySelector('h2')
const secondH2 = document.querySelector('#location-header')
const selectUlTag = document.querySelector('div > ul')

//결과는 동일
const liTags = document.querySelectorAll('li')
const secondLiTags = document.querySelectorAll('.ssafy-location')
```

creation & append

```javascript
// create element
const ulTag = document.querySelector('ul')
const newLiTag = document.createElement('li')

ulTag.append(newLiTag)
ulTag.append('문자열도 추가 가능')
newLiTag.innerText = '새로운 리스트 태그'

const new1 = document.createElement('li')
new1.innerText = '리스트 1'
const new2 = document.createElement('li')
new2.innerText = '리스트 2'
const new3 = document.createElement('li')
new3.innerText = '리스트 3'
ulTag.append(new1, new2, new3)

// appendChild
// 한번에 오직 하나의 node만 추가가능
// 한 NODE를 특정 부모 NODE의 자식 NODE LIST 중 마지막에 추가
const ulTag = document.querySelector('ul')
const newLiTag = document.createElement('li')
newLiTag.innerText = '새로운 리스트 태그'
ulTag.appendChild(newLiTag)
ulTag.appendChild('문자열은 추가 불가') // typeError

const new1 = document.createElement('li')
new1.innerText = '리스트 1'
const new2 = document.createElement('li')
new2.innerText = '리스트 2'
ulTag.appendChild(new1, new2)
```



append와 appendChild의 차이

43페이지



DOM 변경 - 변경 관련 속성(property)

* node.innerText

node 객체와 그 자손의 텍스트 컨텐츠를 표현(해당 요소 내부의 raw text)

* Element.innerHTML

: xss 공격에 취약하므로 사용 지양

```javascript
const ulTag = document.querySelector('ul')
const liTag1 = document.createElement('li')
liTag1.innerText = '<strong>춘천</strong>' // => 이 자체로 <strong>가 문자열 그대로 들어감
const liTag2 = document.createElement('li')
liTag2.innerHTML = '<strong>춘천</strong>' // => 굵은 글씨체로 들어감
ulTag.append(liTag1, liTag2)

const ulTag = document.querySelector('ul')
ulTag.innerHTML = '<li><a href="javascript:alert(\'당신의 개인정보 유출\')">춘천</a></li>'
```



DOM 삭제

* childNode.remove()

  node가 속한 트리에서 해당 node를 제거

* node.removeChild()

  DOM에서 자식 node를 제거하고 제거된 node반환

```javascript
const header = document.querySelector('#location-header')
header.remove()


const parent = document.querySelector('ul')
const child = document.querySelector('ul > li')
const removedChild = parent.removeChild(child)
console.log(removedChild)
```



DOM 속성

* element.setAttribute(name, value)

  지정된 요소의 값을 설정

  속성이 이미 존재하면 값을 갱신, 존재하지 않으면 지정된 이름과 값으로 새 속성을 추가

* element.getAttribute(attributeName)

  해당 요소의 지정된 값을 반환

  인자는 값을 얻고자 하는 속성의 이름

```javascript
// setAttribute
const header = document.querySelector('#location-header')
header.setAttribute('class', 'ssafy-location')

// getAttribute
const getAttr = document.querySelector('.ssafy-location')
getAttr.getAttribute('class')
getAttr.getAttribute('style')

// element styling
li1.style.cursor = 'pointer'
li2.style.color = 'blue'
li3.style.background = 'red'

// css 적용
<style>
    .focus {
        color: gold;
        background-color: navy;
        font-weight : 300;
    }
</style>
// 넣은 다음에
li1.setAttribute('class','focus')
```



DOM 실습

```HTML
<script>
// 배경색 설정
    const body= document.querySelector('body')
    body.setAttribute('id','main')

// 요소 중앙정렬(nav, header, section)
    const nav = document.querySelector('nav')
    const header = document.querySelector('header')
    const section = document.querySelector('section')
    
    // 두가지 방법 다 가능
    nav.setAttribute('class','box-container')
    header.classList.add('box-container')
    section.setAttribute('class','box-container')

// 테두리 설정
    const questionDivs = document.querySelectorAll('section div')
    questionDivs.forEach(frunction (div) {
                         div.setAttribute('class', 'box-items')
                         })

// 버튼 설정
    const button = document.querySelector('#main > section > form > input[type = submit]')
    
// 이미지 사이즈
    const navImage = document.querySelector('nav > a > img')
    navImage.width = '600'
    // 클래스 만들어서 클래스 적용하는게 가장 좋은 방법
    
// footer
    const footer = document.createElement('footer')
    footer.innerText = '구글 설문지를 통해 비밀번호를 제출하지 마시오!'
    body.append(footer)
    footer.setAttribute('class','box-container')
    
// input 요소 스타일링
    const nameInput = document.querySelector('name')
    nameInput.style.marginTop = '50'
    
</script>
```



