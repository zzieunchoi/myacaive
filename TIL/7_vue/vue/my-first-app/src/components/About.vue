<template>
  <div>
    <input
    type = "text"
    @keyup.enter="childInputChange"
    v-model="childInputData"
    >
  </div>
</template>

<script>
export default {
  name: 'About-a',
  data: function () {
    return {
      childInputData: null,
    }
  },
  methods: {
    childInputChange: function () {
      this.$emit('child-input-change', this.childInputData)
    }
  }
}
</script>