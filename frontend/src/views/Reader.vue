<template>
  <div class="reader">
    <MyReader  msg="Welcome to Your Reader"/>
  </div>
</template>

<script>
// @ is an alias to /src
import MyReader from '@/components/MyReader.vue'
import mdContract from '@/components/contract.md.vue'

export default {
  name: 'Reader',
  components: {
    MyReader,
    mdContract
  },
  data: {
    abc: ""
  },
  methods: {
    fun1(){
      this.abc 
    }
  }
}
</script>
