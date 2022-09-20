# props로 삼항연산자

부모

```js
import Category from './Category.js';
const EpisodeButton = () => {
  return (
    <ScrollView>
      <View ...>
          <ScrollView ...>
            <Category
              imageUri={require('../../../../images/뇌.jpg')}
              name="OCD 살인"
              // blocked를 props로 보냄~
              blocked="false"></Category>
          </ScrollView>
      </View>
    </ScrollView>
  );
};
```



자식

```js
function Category(props) {
  // 바로 props.blocked가 true인지 아닌지 확인은 x
  // 따라서 값을 저장해놓고 true or false확인해야함
  const isblocked = props.blocked;
  return (
    <View>
      {isblocked == 'true' ? (
        ... 'true'일 경우 보여줄 것!
      ) : (
        ... 'true'가 아닐 경우 보여줄 것!
      )}
    </View>
  );
}
```

