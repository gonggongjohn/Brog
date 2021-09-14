<template>
  <div>
    <!-- Header -->
    <div class="header bg-gradient-success py-7 py-lg-8 pt-lg-9">
      <b-container class="container">
        <div class="header-body text-center mb-7">
          <b-row class="justify-content-center">
            <b-col xl="5" lg="6" md="8" class="px-5">
              <h1 class="text-white">Brog 书蛙</h1>
              <p class="text-lead text-white">极致流畅的阅读体验，专为您呈现！</p>
            </b-col>
          </b-row>
        </div>
      </b-container>
      <div class="separator separator-bottom separator-skew zindex-100">
        <svg x="0" y="0" viewBox="0 0 2560 100" preserveAspectRatio="none" version="1.1"
             xmlns="http://www.w3.org/2000/svg">
          <polygon class="fill-default" points="2560 0 2560 100 0 100"></polygon>
        </svg>
      </div>
    </div>
    <!-- Page content -->
    <b-container class="mt--8 pb-5">
      <!-- Table -->
      <b-row class="justify-content-center">
        <b-col lg="6" md="8" >
          <b-card no-body class="bg-secondary border-0">
            <b-card-header class="bg-transparent pb-5">
              <div class="text-muted text-center mt-2 mb-4"><small>Sign up with</small></div>
              <div class="text-center">
                <a href="#" class="btn btn-neutral btn-icon mr-4">
                  <span class="btn-inner--icon"><img src="img/icons/common/github.svg"></span>
                  <span class="btn-inner--text">Github</span>
                </a>
                <a href="#" class="btn btn-neutral btn-icon">
                  <span class="btn-inner--icon"><img src="img/icons/common/google.svg"></span>
                  <span class="btn-inner--text">Google</span>
                </a>
              </div>
            </b-card-header>
            <b-card-body class="px-lg-5 py-lg-5">
              <div class="text-center text-muted mb-4">
                <small>Or sign up with credentials</small>
              </div>
              <validation-observer v-slot="{handleSubmit}" ref="formValidator">
                <b-form role="form" @submit.prevent="handleSubmit(onSubmit)">
                  <base-input alternative
                              class="mb-3"
                              prepend-icon="ni ni-hat-3"
                              placeholder="Name"
                              name="Name"
                              :rules="{required: true}"
                              v-model="model.username">
                  </base-input>

                  <base-input alternative
                              class="mb-3"
                              prepend-icon="ni ni-lock-circle-open"
                              placeholder="password"
                              type="password"
                              name="Password"
                              :rules="{required: true, min: 3}"
                              v-model="model.password">
                  </base-input>
                  <div class="text-muted font-italic"><small>password strength: <span
                    class="text-success font-weight-700">strong</span></small></div>

                  <b-form-select v-model="model.major" :options="major_options"></b-form-select>

                  <b-row class=" my-4">
                    <b-col cols="12">
                      <base-input :rules="{ required: { allowFalse: false } }" name=Privacy Policy>
                        <b-form-checkbox v-model="model.agree">
                          <span class="text-muted">I agree with the <a href="#!">Privacy Policy</a></span>
                        </b-form-checkbox>
                      </base-input>
                    </b-col>
                  </b-row>
                  <div class="text-center">
                    <b-button type="submit" variant="primary" class="mt-4">Create account</b-button>
                  </div>
                </b-form>
              </validation-observer>
            </b-card-body>
          </b-card>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>
<script>

  export default {
    name: 'register',
    data() {
      return {
        model: {
          username: '',
          password: '',
          major: 0,
          agree: false
        },
        major_options: [
          {
            value: 0,
            text: '请选择您的专业背景'
          },
          {
            value: 1,
            text: '数据科学'
          },
          {
            value: 2,
            text: '生物学'
          },
          {
            value: 3,
            text: '化学'
          },
          {
            value: 4,
            text: '管理科学'
          }
        ]
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
      onSubmit() {
        // this will be called only after form is valid. You can do an api call here to register users
        let url = this.getHostUrl() + ':5000/user/register/';
        this.axios.post(url, this.model).then((response) => {
          if(response.data != undefined){
            if(response.data.status == '200'){
              if(this.model.agree){
                localStorage.setItem("username", this.model.username);
                localStorage.setItem("password", this.model.password);
              }
              this.$router.push('/login');
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
      }
    }

  };
</script>
<style></style>
