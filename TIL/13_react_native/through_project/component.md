# component

## app.js

```js
import React from 'react';
import {
  SafeAreaView,
  StyleSheet,
  Text,
  useColorScheme,
  View,
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

