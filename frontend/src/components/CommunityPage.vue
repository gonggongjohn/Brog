<template>
  <div class="container">
    <div class="container">
      <h4>贡献资源</h4>
      <b-form-file plain v-model="upload_file" accept=".pdf"></b-form-file>
      <b-button @click="onUploadFile" variant="outline-success">上传文件</b-button>
    </div>
    <div class="container mt-2">
      <h4>可用资料</h4>
      <b-list-group>
        <b-list-group-item v-for="(book_item, index) in book_list" :key="book_item">
          <div class="row">
            <p class="col">资料名：{{book_item.name}}</p>
            <p class="col">贡献者：{{book_item.contributor}}</p>
            <b-button class="col-3" @click="onAddToShelf(index)" variant="outline-primary">添加到书架</b-button>
          </div>
        </b-list-group-item>
      </b-list-group>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CommunityPage',
  data() {
    return{
      upload_file: null,
      book_list: [
        {
          uuid: 1,
          name: "1234",
          contributor: "1234"
        }
      ]
    }
  },
  mounted(){
    this.getBookList();
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
    getBookList(){
      var url = this.getHostUrl() + ':5000/file/list_all/';
      this.axios.get(url).then((response) => {
        if(response.data && response.data.status == "200"){
          var book_list_tmp = response.data.result;
          book_list_tmp.forEach((book) => {
            this.book_list.push({
              uuid: book.id,
              name: book.filename,
              contributor: book.contributor
            });
          });
        }
      })
      .catch((error) => {
        console.log(error);
      });
    },
    onUploadFile(){
      var url = this.getHostUrl() + ':5000/file/upload/';
      var form = new FormData();
      form.append('file', this.upload_file);
      let config = {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      };
      this.axios.post(url, form, config).then((response) => {
        console.log(response);
      })
      .catch((error) => {
        console.log(error);
      });
    },
    onAddToShelf(index){
      let url = this.getHostUrl() + ':5000/file/add/';
      var payload = {id: this.book_list[index].uuid};
      this.axios.post(url, payload).then((response) => {
        if(response.data != undefined){
          if(response.data.status == '200'){
            alert("添加成功!");
          }
        }
      })
      .catch((error) => {
        console.log(error);
      });
    }
  }
}
</script>
