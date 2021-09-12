<template>
  <div>
    <base-header class="pb-6 pb-8 pt-5 pt-md-8 bg-gradient-success">
     <div align="center">

       <b-form-file v-model="upload_file" accept=".md" ref="file-input" class="mb-2"></b-form-file>

       <b-button @click="onUploadFile" squared variant="primary">上传文件</b-button>

    </div>

      <div class="container mt-2">
      <h4>可用资料</h4>
      <b-list-group>
        <b-list-group-item>
          <div class="row"  >
        <p class="col" >资料名</p>
        <p class="col">贡献者</p>
        <p class="col">操作</p>
        </div>
        </b-list-group-item>


        <b-list-group-item v-for="(book_item, index) in book_list" :key="book_item">

          <div class="row">

            <p class="col">{{book_item.name}}</p>
            <p class="col">{{book_item.contributor}}</p>
            <p class ="col" >
              <b-button class="col-3"  @click="onAddToShelf(index)" variant="outline-primary" >添加到书架</b-button>
            </p>
          </div>
        </b-list-group-item>
      </b-list-group>
    </div>
    </base-header>



  </div>

</template>
<script>



  export default {
    data() {
      return {
        upload_file: null,
        book_list: [
        // {
        //   uuid:"1" ,
        //   name: "123",
        //   contributor: "1234"
        // }
      ]

      };
    },
    mounted(){
    this.getBookList();
  },
    methods:{
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
      onUploadFile(){
      var url = this.getHostUrl() + ':5000/file/upload/';
      var form = new FormData();
      form.append('file', this.upload_file);
      let config = {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      };

      this.axios.post(url, form, config).then(response => {
        console.log(response);
        window.alert("文件上传成功")
        window.location.reload();
      })
      .catch((error) => {
        console.log(JSON.stringify(error))
      });
    },
      getBookList(){
      var url = this.getHostUrl() + ':5000/file/list_all/';
      this.axios.get(url).then((response) => {
        if(response.data && response.status == 200){
          var book_list_tmp = response.data;
          book_list_tmp.forEach((book) => {
            this.book_list.push({
              uuid: book.id,
              name: book.filename,
              contributor: book.contributor
            });
            console.log(book);
          });
        }
      })
      .catch((error) => {
        console.log(error);
      });
    },
      onAddToShelf(index){
      let url = this.getHostUrl() + ':5000/file/add_collection/';
      var payload = JSON.stringify({book_id: this.book_list[index].uuid});
      this.axios.post(url, payload).then((response) => {
        if(response.data != undefined){
          if(response.data.status == '200'){
            window.alert("添加成功!");
            window.location.reload();

          }
        }
      })
      .catch((error) => {
        console.log(error);
      });

    }


    //   onReadingBook(index){
    //   this.$router.push({path: '/reader', query: {uuid: this.book_list[index].uuid}});
    // }
    }

  }
</script>
<style>

</style>




