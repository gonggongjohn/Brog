<template>
  <div class="container">
    <b-card border-variant="info">
      <h1>用户注册界面</h1>
      <b-form @submit="onRegister">
        <b-form-group class="row mb-4" id="group-username" label-cols-sm="2" label="用户名：" label-for="input-username">
          <b-form-input id="input-username" v-model="register_form.username" placeholder="请输入用户名" required></b-form-input>
        </b-form-group>

        <b-form-group class="row mb-4" id="group-password" label-cols-sm="2" label="密码：" label-for="input-password">
          <b-form-input id="input-password" v-model="register_form.password" placeholder="请输入密码" required></b-form-input>
        </b-form-group>
        
        <b-form-group class="row mb-4" id="group-email" label-cols-sm="2" label="邮箱：" label-for="input-email">
          <b-form-input id="input-email" type="email" v-model="register_form.email" placeholder="请输入邮箱" required></b-form-input>
        </b-form-group>

        <b-button type="submit" size="lg" variant="outline-primary" style="margin-right: 50px">注册</b-button>
        <b-button @click="jumpLogin" size="lg" variant="outline-success">返回</b-button>
      </b-form>
    </b-card>
  </div>
</template>

<script>
export default {
  name: 'RegisterCard',
  data() {
    return{
      register_form: {
        username: "",
        password: "",
        email: ""
      }
    }
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
    onRegister(){
      let url = this.getHostUrl() + ':5000/user/register/';
      this.axios.post(url, this.register_form).then((response) => {
        if(response.data != undefined){
          if(response.data.status == '200'){
              console.log(response);
          }
        }
      })
      .catch((error) => {
        console.log(error);
      });
    },
    jumpLogin(){
      this.$emit('change', 'login');
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
