# text input

```js
const UselessTextInput = () => {
  const [text, onChangeText] = React.useState("Useless Text");

  return (
    <SafeAreaView>
      <TextInput
        style={styles.input}
        onChangeText={onChangeText}
        value={text}
      />
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  input: {
    height: 40,
    margin: 12,
    borderWidth: 1,
    padding: 10,
  },
});

export default UselessTextInput;
```

위에 방법대로 하면 Useless Text라는 것이 인풋 박스에 들어가 있어서 useLess Text를 수정하는 것!



```js
const UselessTextInput = () => {
  const [number, onChangeNumber] = React.useState(null);

  return (
    <SafeAreaView>
      <TextInput
        style={styles.input}
        onChangeText={onChangeNumber}
        value={number}
        placeholder="useless placeholder"
        keyboardType="numeric"
      />
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  input: {
    height: 40,
    margin: 12,
    borderWidth: 1,
    padding: 10,
  },
});

export default UselessTextInput; 
```

이 방법대로 하면 placeholder만 useless placeholder이고 따로 수정할 것 없이 처음부터 입력가능!

keyboardType="numeric"은 클릭하면 어떤 키보드 타입이 나올지 정하는 건데 숫자가 나옴!