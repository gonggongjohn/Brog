<template>
  <div class="container">
    <b-form-file plain v-model="upload_file" accept=".pdf"></b-form-file>
    <b-button @click="onUploadFile" variant="outline-success">上传文件</b-button>
  </div>
</template>

<script>
export default {
  name: 'ResourcePage',
  data() {
    return{
      upload_file: null
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
    onUploadFile(){
      console.log(this.upload_file);
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
    }
  }
}
</script>
