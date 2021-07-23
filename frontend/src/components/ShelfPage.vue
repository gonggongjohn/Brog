<template>
  <div class="container">
    <h3>我的书架</h3>
    <b-button @click="onAddBook" variant="outline-success">添加书籍</b-button>
    <div class="row row-cols-3" style="margin-top: 3%">
      <div class="container" v-for="(book_item, index) in book_list" :key="book_item.name">
        <b-card>
          <h3>{{book_item.name}}</h3>
          <b-button @click="onReadingBook(index)" variant="outline-primary">进入阅读</b-button>
        </b-card>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ShelfPage',
  data() {
    return{
      book_list: [
        {
          uuid: 1,
          name: "1234"
        },
        {
          uuid: 2,
          name: "5678"
        },
        {
          uuid: 3,
          name: "2351"
        }
      ]
    }
  },
  mounted(){
    
  },
  methods: {
    getHostUrl(){
      let full_path = window.document.location.href;
      let protocal_index = full_path.indexOf("://");
      let protocal_str = full_path.substring(0, protocal_index);
      let full_path_stripped = full_path.substring(protocal_index + 3);
      let router_path =  this.$route.path;
      let host_index = full_path_stripped.indexOf(router_path);
      let full_host = full_path_stripped.substring(0, host_index);
      console.log(full_path);
      let pred_index = full_host.lastIndexOf(":");
      let pure_host = full_host.substring(0, pred_index);
      return protocal_str + "://" + pure_host;
    },
    onAddBook(){
      this.$router.push('/library');
    },
    onReadingBook(index){
      this.$router.push({path: '/reader', query: {uuid: this.book_list[index].uuid}});
    }
  }
}
</script>
