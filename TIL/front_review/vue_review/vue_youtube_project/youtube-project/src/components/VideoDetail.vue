<template>
  <div v-if="video" class="video-detail">
    <iframe :src="videoURI" frameborder="0"></iframe>
  </div>
</template>

<script>

export default {
  name: 'VideoDetail-a',
  props: {
    video : {
      type: Object,
    },
  },
  computed:{
    videoURI: function(){
      const videoId = this.video.id.videoId
      return `https://www.youtube.com/embed/${videoId}`
    },
  },
}
</script>
