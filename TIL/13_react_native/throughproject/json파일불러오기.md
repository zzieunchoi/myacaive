# js 파일 불러오기

우리는 대사, 배경화면 등 다양한 설정들이 들어있는 js 파일을 각 chapter마다 만들기로 했다.

그러고 chapter 숫자만 변경해서 넣으면  ingame/index.js에서 재활용할 수 있도록!



```js
// src/data/e101.js

const e101 = {
  setting: {
    chapterbg: require('../images/room.png'),
    background: ['../images/background/ep1_toilet.jpg'],
    episode: 1,
    chapter: 1,
  },
  clue: [
    {
      name: 'bottle',
      start_index: [8, 11],
      isasaved: 1,
      image: '../images/clue/ep1_bottle.jpg',
      isdetected: 0,
    },
  ],
  backgroundsetting: {
    index: 0,
    location: ['80%', '60%'],
    size: ['20%', '25%'],
  },
  scripts: [
    {
      name: '배교수',
      text: '살인 사건이 발생했네',
      img: '../images/character/prof.jpg',
      type: 0,
      audio: '../audio/episode1/chapter1/dg1',
      sfx: 0,
      index: 0,
    },
  ],
};

export default e101;
```



이 파일을 불러오기

```js
// src/pages/ingame/index.js

import React, {useEffect, useState} from 'react';
import { ImageBackground, TouchableOpacity } from 'react-native';
import e101 from '../../data/e101.js';

function IngamePage(props) {
    const dataa = e101;
    const epiImgBg = dataa.setting.chapterbg;
    
    return (
        <TouchableOpacity activeOpacity={1} onPress={orderIncrease}>
          <ImageBackground
           source={epiImgBg}
           style={{width: '100%', height: '100%'}}></ImageBackground>
        </TouchableOpacity>
    )
```



원래는 js 파일 대신 json 파일로 {}를 불러오려고 했는데

이미지 파일을 불러올 때 

```js
const dict = {a: '123', b: '234'}
const a = dict.a
const req_a = require(a)
```

로 하면 require이 안됨. 즉, 객체 안의 값이나 키로 require함수를 넣으면 require이 되지 않음 ㅠㅠ 

따라서 

```js
const dict = {uri : require('../../img.png')}
const req_a = require(dict.uri)
```

로 해야 가능!