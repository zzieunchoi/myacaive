# 컴포넌트 생성

src 디렉토리에 MyComponent.js 파일 생성

```js
const MyComponent = () => {
    return <div>나의 새롭고 멋진 컴포넌트</div>;
};

/* 모듈 내보내기 */
export default MyComponent;
```



App.js에서 component 불러오기

```js
import MyComponent from './MyComponent';

const App = () => {
    return <MyComponent />;
};

export default App;
```



## props

MyComponent 컴포넌트에서 name이라는 props를 렌더링하도록 설정

```js
const MyComponent = props => {
    return <div>안녕하세요, 제 이름은 {props.name}입니다.</div>;
};

export default MyComponent;
```



App 컴포넌트에서 MyComponent의 props 값을 지정

```js
import MyComponent from './MyComponent';

const App = () => {
    return <MyComponent name="React"/>;
};

export default App;
```



## default Props

MyComponent에서 name이 없을 시 기본적으로 보여줄 수 있는 기본 값 설정

```js
const MyComponent = props => {
    return <div>안녕하세요, 제 이름은 {props.name}입니다.</div>;
};

MyComponent.defaultProps = {
    name: '기본 이름'
};

export default MyComponent;
```



## children

태그 사이의 내용을 보여준 props

```js
/*App.js*/
import MyComponent from './MyComponent';

const App = () => {
    return <MyComponent>리액트</MyComponent>;
};

export default App;
```



```js
/*MyComponent.js*/
const MyComponent = props => {
    return {
        <div>
        	안녕하세요, 제 이름은 {props.name}입니다. <br />
            children 값은 {props.children}입니다.
        </div>
    };
};

MyComponent.defaultProps = {
    name: '기본 이름'
};

export default MyComponent;
```

안녕하세요, 제이름은 기본 이름입니다.

children 값은 리액트입니다.



## 비구조화 할당 문법 통해 props 내부 값 추출

```js
/*MyComponent.js*/
const MyComponent = ({ name, children }) => {
    return {
        <div>
        	안녕하세요, 제 이름은 {name}입니다. <br />
            children 값은 {children}입니다.
        </div>
    };
};

MyComponent.defaultProps = {
    name: '기본 이름'
};

export default MyComponent;
```



```js
/*App.js*/
import MyComponent from './MyComponent';

const App = () => {
    return <MyComponent name="React" favoriteNumber={1}>리액트</MyComponent>;
};

export default App;
```



## propTypes를 통한 props 검증

컴포넌트의 필수 props를 지정하거나 props의 타입을 지정할 때는 propTypes를 사용

```js
/*MyComponent.js*/
import PropTypes from 'prop-types';

const MyComponent = ({ name, children }) => {
    return {
        <div>
        	안녕하세요, 제 이름은 {name}입니다. <br />
            children 값은 {children}입니다.
        </div>
    };
};

MyComponent.defaultProps = {
    name: '기본 이름'
};

/*name 값은 무조건 문자열 형태로 전달해야 된다!
숫자를 보내면 console창에 에러뜸*/
MyComponent.propTypes = {
    name: PropTypes.string
}
export default MyComponent;
```



isRequired를 사용하여 필수 propsTypes 설정

propTypes를 지정하지 않았을 때 경고 메시지를 띄워줌

```js
/*MyComponent.js*/
import PropTypes from 'prop-types';

const MyComponent = ({ name, favoriteNumber, children }) => {
    return {
        <div>
        	안녕하세요, 제 이름은 {name}입니다. <br />
            children 값은 {children}입니다. <br />
            제가 좋아하는 숫자는 {favoriteNumber}입니다.
        </div>
    };
};

MyComponent.defaultProps = {
    name: '기본 이름'
};

MyComponent.propTypes = {
    name: PropTypes.string,
    /*favoriteNumber를 설정하지 않으면 경고*/
    favoriteNumber: PropTypes.number.isRequired
}
export default MyComponent;
```



proptypes 종류

array/ arrayOf/ bool/ func/ number/ object/ string/ symbol/ node/ instanceOf/ oneOf/ oneOfType/ objectOf/ shape/ any



## 클래스형 컴포넌트에서 props 사용하기

```js
/*MyComponent.js*/
import { Component } from 'react';
import PropTypes from 'prop-types';

class MyComponent extends Component {
    /*default Props와 PropTypes을 여기서 설정 가능
    static defaultProps = {
        name:'기본 이름'
    };
    static propTypes = {
        name: PropTypes.string,
        favoriteNumber: PropTypes.number.isRequired
    }; */
    render() {
        const { name, favoriteNumber, children } = this.props;
        return {
            <div>
            안녕하세요, 제 이름은 {name}입니다.
            children 값은 {children}입니다.
            제가 좋아하는 숫자는 {favoriteNumber}입니다.
        };
    }
}

MyComponent.defaultProps = {
    name:'기본 이름'
};

MyComponent.propTypes = {
    name: PropTypes.string,
    favoriteNumber: PropTypes.number.isRequired
};


export default MyComponent;
```

