# youtube project

1. youtube api key 발급

```
const API_KEY = 'AIzaSy...0hGOU'
const API_URL = 'https://www.googleapis.com/youtube/v3/search'
```



2. App.vue

```vue
<template>
  <div id="app">
    <h1>My First Youtube Project</h1>
    <header>
      <p>영상을 검색해보세요!</p> 
      <the-search-bar @input-change="onInputChange"></the-search-bar>
    </header>
    <br>
    <section>
      <video-detail :video="selectedVideo"></video-detail>
      <video-list :videos="videos" @select-video="onVideoSelect"></video-list>
    </section>
  </div>
</template>

<script>
import axios from 'axios'
import TheSearchBar from '@/components/TheSearchBar.vue'
import VideoList from '@/components/VideoList.vue'
import VideoDetail from './components/VideoDetail.vue'

const API_KEY = 'AIzaSy...0hGOU'
const API_URL = 'https://www.googleapis.com/youtube/v3/search'
export default {
  name: 'App',
  components: {
    TheSearchBar,
    VideoList,
    VideoDetail,
  },
  data: function (){
    return {
      inputValue: null,
      videos: [],
      selectedVideo:null, 
    }
  },
  methods: {
    onInputChange: function (inputText) {
      this.inputValue = inputText

      const params = {
        key: API_KEY,
        part: 'snippet',
        type: 'video',
        q: this.inputValue,
      }

      axios({
        method: 'get',
        url : API_URL,
        params,
      })
      .then(res => {
        console.log(res)
        this.videos = res.data.items
      })
      .catch(err => {
        console.log(err)
      })
    },
    onVideoSelect: function(video){
      this.selectedVideo = video
    }
  },
}
</script>
```

```
[template]
1. template은 항상 div 안에!
2. header에는 영상을 검색할 수 있는 검색창/ section에는 실제 영상과, 영상 리스트를 보여줌
 2-1. 검색창은 input-change가 되면 'onInputChange'를 실행시켜라 - method에 기재 
      @ : 'v-on:'의 약자, 이벤트 핸들러
 2-2. select-video를 하면 'onVideoSelect'를 실행시켜라 - method에 기재
      : : 'v-bind'의 약자, 동적 전달인자

[script]
1. app.vue에서 보여줄 component들 다 import 해오기
2. API_KEY, API_URL 미리 받아오기
3. export default에다가는 name, components, data, methods 명시
 3-1. name에는 이름 지정, App.vue니까 App으로 하는 것이 일반적
 3-2. components에는 위에 template에서 보여주는 component들 기재, import 해온것들!
 3-3. data는 항상 함수 형식으로 가져와야함
      return안에 data보여주기
      
```



## emit

emit은 다른 component에게 현재 component의 event나 data를 전달하기 위해 사용!

- 받아올 다른 component
  - @emit으로받아올event명="현재컴포넌트에서사용할 event명"
- emit을 사용하는 component
  - this.$emit('@에서작성한emit명칭', 현재 컴포넌트에서전송할 event나 data명)



this는 component





'inputValue' is not defined  no-undef
  46:12  error  'inputValue' is not defined  no-undef