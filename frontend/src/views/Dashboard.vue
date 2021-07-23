<template>
  <div class="row">
    <b-navbar type="light">
      <img alt="brog logo" src="../assets/logo.png" style="max-width: 60px">
      <h3>书蛙</h3>

      <b-navbar-nav class="ml-auto">
        <b-nav-item-dropdown text="我的" right>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-navbar>
    <b-card no-body class="col-3">
      <b-nav vertical tabs>
        <b-nav-item @click="onSwitchShelf">书架</b-nav-item>
        <b-nav-item @click="onSwitchCommunity">社区</b-nav-item>
      </b-nav>
    </b-card>

    <component :is="component_show" @change="onChangePage" class="col"></component>
  </div>
</template>

<script>
// @ is an alias to /src
import CommunityPage from '@/components/CommunityPage.vue'
import ShelfPage from '@/components/ShelfPage.vue'


export default {
  name: 'Sign',
  data(){
    return{
      component_show: ShelfPage
    }
  },
  methods: {
    onSwitchShelf(){
      this.component_show = ShelfPage;
    },
    onSwitchCommunity(){
      this.component_show = CommunityPage;
    },
    onChangePage(value){
      if(value == "community"){
        this.component_show = CommunityPage;
      }
    }
  }
}
</script>
