<template>
  <div class="container">
    <b-card border-variant="info">
      <h1>用户登录界面</h1>
      <b-form @submit="onLogin">
        <b-form-group class="row mb-4" id="group-username" label-cols-sm="2" label="用户名：" label-for="input-username">
          <b-form-input id="input-username" v-model="login_form.username" placeholder="请输入用户名" required></b-form-input>
        </b-form-group>

        <b-form-group class="row mb-4" id="group-password" label-cols-sm="2" label="密码：" label-for="input-password">
          <b-form-input id="input-password" v-model="login_form.password" placeholder="请输入密码" required></b-form-input>
        </b-form-group>

        <b-form-checkbox v-model="rem_flag" class="mb-3">记住用户名和密码</b-form-checkbox>

        <b-button type="submit" size="lg" variant="outline-primary" style="margin-right: 50px">登录</b-button>
        <b-button @click="jumpRegister" size="lg" variant="outline-success">注册账户</b-button>
      </b-form>
    </b-card>
  </div>
</template>

<script>
export default {
  name: 'LoginCard',
  data() {
    return{
      login_form: {
        username: "",
        password: "",
      },
      rem_flag: false
    }
  },
  mounted(){
    let username_tmp = localStorage.getItem("username");
    let password_tmp = localStorage.getItem("password");
    if(username_tmp){
      this.login_form.username = username_tmp;
    }
    if(password_tmp){
      this.login_form.password = password_tmp;
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
    onLogin(){
      let url = this.getHostUrl() + ':5000/user/login/';
      this.axios.post(url, this.login_form).then((response) => {
        if(response.data != undefined){
          if(response.data.status == '200'){
            if(this.rem_flag){
              localStorage.setItem("username", this.login_form.username);
              localStorage.setItem("password", this.login_form.password);
            }
            this.$router.push('/dashboard');
          }
          else{
            alert("登录失败！");
          }
        }
        else{
          alert("服务器返回错误！");
        }
      })
      .catch((error) => {
        console.log(error);
      });
    },
    jumpRegister(){
      this.$emit('change', 'register');
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
