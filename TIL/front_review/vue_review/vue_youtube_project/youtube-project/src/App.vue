<template>
  <div id="app">
    <h1>My First Youtube Project</h1>
    <the-search-bar @input-change="onInputChange"></the-search-bar>
  </div>
</template>

<script>
import TheSearchBar from '@/components/TheSearchBar'

export default {
  name: 'App',
  components: {
    TheSearchBar,
  },
  data: function (){
    return {
      inputValue: null, 
    }
  },
  // 93
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
