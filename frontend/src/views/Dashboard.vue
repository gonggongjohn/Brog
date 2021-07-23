<template>
  <div class="row">
    <b-navbar type="light">
      <h3>Navbar</h3>
    </b-navbar>
    <b-card no-body class="col-3">
      <b-nav vertical tabs>
        <b-nav-item @click="onSwitchShelf">书架</b-nav-item>
        <b-nav-item @click="onSwitchCommunity">社区</b-nav-item>
      </b-nav>
    </b-card>

    <component :is="component_show" class="col"></component>
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
    }
  }
}
</script>
