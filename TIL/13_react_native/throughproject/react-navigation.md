# react-navigation

* 설치
  * `npm i @react-navigation/native @react-navigation/native-stack`

* android/app/src/main/java/com/baedalpjt/MainActivity.java

  ```java
  import android.os.Bundle;
  
  @Override
    protected void onCreate(Bundle savedInstanceState) {
      super.onCreate(null);
    }
  ```

  추가!

* `npm i react-native-screens react-native-safe-area-context`



## App.js

```js
import * as React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

const Stack = createNativeStackNavigator();

const App = () => {
  return (
    <NavigationContainer>
      // 순서대로 보여짐
      <Stack.Navigator>
        // 1번째 방법
        <Stack.Screen
          // 이 때 Name은 navigation할 때 페이지 이름
          name="Home"
          component={HomeScreen}
          // 스크린의 옵션들
          options={{ title: 'Welcome' }}
        />
        // 2번째 방법
        <Stack.Screen name="Profile" component={ProfileScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

export default App;
```

* navigationcontainer가 있어야지만 react-navigation이 실행됨
* stack.navigator: 페이지들의 묶음
* stack.screen:페이지

* options
  * title: 맨 위에 제목
  * headerShown: false - 위에 헤더를 보여주지 않음
  * 등등 엄청 많음

1번째 방법으로 props를 보내는 경우

```js
// HomeScreen.js
const HomeScreen = ({ navigation }) => {
  return (
    <Button
      title="Go to Jane's profile"
      onPress={() =>
        navigation.navigate('Profile', { name: 'Jane' })
      }
    />
  );
};
```

2번째 방법으로  props를 보내는 경우

```js
// ProfileScreen.js
const ProfileScreen = ({ navigation, route }) => {
  return <Text>This is {route.params.name}'s profile</Text>;
};
```



## navigation이 error 뜰 경우!

```js
import {useNavigation} from '@react-navigation/native';

// 컴포넌트 훅 함수 안에서 선언
const navigation = useNavigation();

// 그리고 navigation.navigate()사용!
```

