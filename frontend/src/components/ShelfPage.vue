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
    this.getBookCollections();
  },
  methods: {
    getHostUrl(){
      let full_path = window.document.location.href;
      let protocol_index = full_path.indexOf("://");
      let protocol_str = full_path.substring(0, protocol_index);
      let full_path_stripped = full_path.substring(protocol_index + 3);
      let router_path =  this.$route.path;
      let host_index = full_path_stripped.indexOf(router_path);
      let full_host = full_path_stripped.substring(0, host_index);
      console.log(full_path);
      let pred_index = full_host.lastIndexOf(":");
      let pure_host = full_host.substring(0, pred_index);
      return protocol_str + "://" + pure_host;
    },
    getBookCollections(){
      var url = this.getHostUrl() + ":5000/file/list_collection";
      this.axios.get(url).then((response) => {
        if(response.data && response.status == 200){
          var book_list_tmp = response.data;
          book_list_tmp.forEach((book) => {
            this.book_list.push({
              uuid: book.id,
              name: book.filename
            });
          });
        }
      })
      .catch((error) => {
        console.log(error);
      });
    },
    onAddBook(){
      this.$emit('change', 'community');
    },
    onReadingBook(index){
      this.$router.push({path: '/reader', query: {uuid: this.book_list[index].uuid}});
    }
  }
}
</script>
