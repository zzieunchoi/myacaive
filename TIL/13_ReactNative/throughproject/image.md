# 이미지 가져오기

```js
import { Image } from 'react-native'

<Image source={URL} />
```



URL에 들어갈 수 있는 값은 2가지

1. {uri: '이미지 주소'}

   * 외부 주소를 통해 가져오기

     ```js
     <Image source={{uri: "URL"}} />
     
     혹은
     
     const imgSrc = {uri: "URL"}
     <Image source={imgSrc}>
     ```

2. require('로컬 경로')

   * 로컬에 저장되어 있는 이미지 불러오기

     ```js
     <Image source={require("로컬 주소")} />
     ```

     