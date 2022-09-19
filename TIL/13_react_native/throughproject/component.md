# component

## app.js

```js
import React from 'react';
import {
  SafeAreaView, // 노치를 잘라줌
  StyleSheet,
  Text, // span이랑 비슷
  useColorScheme,
  View, // div랑 비슷
} from 'react-native';

// jsx는 import 가 안됨
// component 가져올 때는 첫 글자는 대문자!
import StartPage from './src/pages/start/index.js';

const App: () => Node = () => {
    return (
    <SafeAreaView>
        <StartPage />
    </SafeAreaView>
    )
}

export default App;
```



## src/pages/start/index.js

```js
import React from 'react';
// 필요한 요소들을 모두 import
import {
  View,
  Text,
  ImageBackground,
  StyleSheet,
  TouchableOpacity,
  Alert,
} from 'react-native';

function StartPage() {
  return (
    // 다음페이지로 넘어가기
    <TouchableOpacity onPress={() => Alert.alert('다음 게임 진행')}>
      // image를 절대 주소로 가져오는 방법 알아보기
      <ImageBackground
        source={}>
        <View style={styles.container}>
          <Text style={styles.text}>게임을 시작하려면 화면을 터치하세요</Text>
        </View>
      </ImageBackground>
    </TouchableOpacity>
  );
}

// css 주는 방법
const styles = StyleSheet.create({
  container: {
    marginTop: 300,
  },
  text: {
    fontSize: 20,
    textAlign: 'center',
  },
});

export default StartPage;
```

[react-native css](https://github.com/vhpoet/react-native-styling-cheat-sheet)

* style를 styleSheet에서 준다

  * 속성을 줄 때는 camelCase로 넣어줌

  * 축약형 안 됨 ( 'solid black 1px' 이런거는 안됨)

  * 조건문을 쓸수 없기 때문에 조건문이 필요한 style같은 경우에는 inline으로 줌

    ```js
    <Text
    style={[
           styles.sectionTitle,
           {
               color: isDarkMode ? Colors.white : Colors.black,
           },
           ]}>
        {title}
    </Text>
    ```

    

  * 이때 marginTop뒤에 나오는 숫자는 안드로이드의 dip이라는 단위를 가지고 한다

    * 가로 360dp 기기에서 120이면 33% 차지

  * px은 안됨!

  * %는 가능!



* status bar
  * 배터리 잔량, 시간 보여주는 최상단 
  * react-native-status-bar-height 라이브러리로 높이 구함



* ScrollView
  * 내부 컨텐츠가 길어질 때는 scroll View를 써야 스크롤이 가능해짐
  * 내용이 너무 많아지면 flatlist 쓰기
