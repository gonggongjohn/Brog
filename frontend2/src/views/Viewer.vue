<template>
  <div>
    <b-container>
      <div class="row">
        <div class="col" ref="main_reader" cols="8">
          <VueShowdown :markdown="content" flavor="github" :extensions="['showdown-katex', bl]" />
        </div>
        <div class="col" v-if="show_reference" ref="ref_reader" cols="5">
          <markdown-it-vue
            ref="myMI"
            class="md-body"
            :content="content"
            :options="options"
          />
        </div>
      </div>
      <b-button @click="onRefer">刷新页面</b-button>
    </b-container>
  </div>
</template>

<script>
import MarkdownItVue from "markdown-it-vue";
import { VueShowdown } from 'vue-showdown';
import 'showdown-katex';
import "markdown-it-vue/dist/markdown-it-vue.css";

const linkMap = {
  a: 'return false;'
};

const binding_link = Object.keys(linkMap).map(key => ({
  type: 'output',
  regex: new RegExp(`<${key}(.*)>`, 'g'),
  replace: `<${key} click='${linkMap[key]}' $1>`
}));

export default {
  components: {
    MarkdownItVue,
    VueShowdown
  },
  data() {
    return {
      src: "/login",
      counter: 0,
      uuid: "",
      content:
        "# 第五章 矩阵计算问题 \n \
在众多科学与工程学科，如物理、化学工程、统计学、经济学、生物学、信号处理、自动控 制、系统理论、医学和军事工程等中，许多问题都可用数学建模成矩阵方程 $$Ax = b$$. 根据数据向量 $$b \\in \\mathbb{R}^{m \\times 1}$$ 和数据矩阵 $$A \\in \\mathbb{R}^{m \\times n}$$ 的不同，矩阵方程主要有以下三种类型: \
[abddd](1)\
 加粗",
      show_reference: false,
      options: {
        linkAttributes: {
          attrs: {
            target: "_blank",
            rel: "noopener",
            name: "link",
            id: "link",
            onclick: "console.log(this.getAttribute('href'));"
          }
        }
      },
      md_url: "",
      bl: () => binding_link
    }
  },
  methods: {
    getHostUrl() {
      let full_path = window.document.location.href;
      let protocol_index = full_path.indexOf("://");
      let protocol_str = full_path.substring(0, protocol_index);
      let full_path_stripped = full_path.substring(protocol_index + 3);
      let router_path = this.$route.path;
      let host_index = full_path_stripped.indexOf(router_path);
      let full_host = full_path_stripped.substring(0, host_index);
      console.log(full_path);
      let pred_index = full_host.lastIndexOf(":");
      let pure_host = full_host.substring(0, pred_index);
      return protocol_str + "://" + pure_host;
    },
    loadMd(md_url) {
      // this.content = md_url;
      console.log(md_url);
      this.axios
        .get(md_url)
        .then(response => {
          if (response.data && response.status == 200) {
            var res = response.data;
            console.log(res);
            console.log("@#%@#%23532");
          }

          this.content = res;
        })
        .catch(error => {
          console.log(error);
        });
    },
    performReference(event) {
      console.log(event.target);
      console.log("!#535135");
    },
    onRefer() {
      this.show_reference = true;
      console.log("!111");
    },
    getReference(word_id) {
      let url = this.getHostUrl() + ":5000/read/search?book_id=" + this.uuid + "&file_id=" + word_id;
      this.axios.get(url).then(response => {
        if(response.data && response.status == 200){

        }
      })
    }
  },
  mounted() {
    this.uuid = this.$route.path.split("/")[2];
    console.log(this.uuid);
    this.md_url = this.getHostUrl() + ":5000/file/get_md?book_id=" + this.uuid;
    //this.loadMd(this.md_url);
    this.$refs.myMI.use(require("markdown-it-mathjax"));
  },
  updated() {
    console.log(document.getElementsByName("link")[0]);
    let linklist = document.getElementsByName("link");
    if (linklist[0] != undefined) {
      console.log(linklist[0]);
      linklist[0].addEventListener("click", this.performReference(event));
    }
    linklist.forEach(element => {
      console.log("12412");
      element.addEventListener("click", this.performReference(event));
    });

    document.body.addEventListener("click", this.performReference(event));

    let link_list = document.getElementsByTagName("a");
    console.log(link_list);
    link_list.forEach(element => {
      console.log("12412");
      console.log(element);
      element.addEventListener("click", this.performReference(event));
    });
  }
};
</script>
<style>
.el-table .cell {
  padding-left: 0px;
  padding-right: 0px;
}
.act-form {
  width: 300px;
  /* background: #F0AD4E; */
  height: 100%;
  border: none;
  position: absolute;
  right: 0px;
  top: 80px;
}
</style>
