# props로 이미지 열기

부모

```js
import Category from './Category.js';

const EpisodeButton = () => {
  return (
    <ScrollView>
      <View style={{flex: 1, backgroundColor: '(0, 0, 0, 10)', paddingTop: 20}}>
        <View style={{marginTop: 20}}>
          <ScrollView horizontal={true} showsHorizontalScrollIndicator={false}>
            <Category
              imageUri={require('../../../../images/뇌.jpg')}
              name="OCD 살인"
              blocked="false"></Category>
          </ScrollView>
        </View>
      </View>
    </ScrollView>
  );
};
```



자식

```js
function Category(props) {
  return (
    <View>
     <TouchableOpacity .... >
          <ImageBackground
            source={props.imageUri}
            style={{
              width: '100%',
              height: '100%',
              flex: 4,
              borderRadius: 40,
            }}
            imageStyle={{borderRadius: 35}}>
            ....
          </ImageBackground>
        </TouchableOpacity>
    </View>
  );
}
```



! 아 그리고 imagebackground는 borderradius 줄 때

`imageStyle={{borderRadius: 35}}` 이걸로 줘야함!

