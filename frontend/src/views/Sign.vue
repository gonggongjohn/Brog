<template>
  <div>
    <img alt="brog logo" src="../assets/logo.png" class="mb-4" style="max-width: 100px">
    <component :is="component_show" @change="onChangeComponent"></component>
  </div>
</template>

<script>
// @ is an alias to /src
import LoginCard from '@/components/LoginCard.vue'
import RegisterCard from '@/components/RegisterCard.vue'


export default {
  name: 'Sign',
  data(){
    return{
      component_show: LoginCard
    }
  },
  methods: {
    onChangeComponent(value){
      if(value == "register"){
        this.component_show = RegisterCard;
      }
      else if(value == "login"){
        this.component_show = LoginCard;
      }
    }
  }
}
</script>
