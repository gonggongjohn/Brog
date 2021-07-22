<template>
  <div class="row">
    <b-card no-body class="col-3">
      <b-nav vertical tabs>
        <b-nav-item @click="onSwitchShelf">书架</b-nav-item>
        <b-nav-item @click="onSwitchResource">资源库</b-nav-item>
      </b-nav>
    </b-card>

    <component :is="component_show" class="col"></component>
  </div>
</template>

<script>
// @ is an alias to /src
import ResourcePage from '@/components/ResourcePage.vue'
import ShelfPage from '@/components/ShelfPage.vue'


export default {
  name: 'Sign',
  data(){
    return{
      component_show: ResourcePage
    }
  },
  methods: {
    onSwitchShelf(){
      this.component_show = ShelfPage;
    },
    onSwitchResource(){
      this.component_show = ResourcePage;
    }
  }
}
</script>
