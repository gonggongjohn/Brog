<template>
  <div>
    <markdown-it-vue ref="myMI" class="md-body" :content="content" :options="options" />
  </div>
</template>

<script>
import MarkdownItVue from 'markdown-it-vue'
import 'markdown-it-vue/dist/markdown-it-vue.css'

  export default {
    components: {
      MarkdownItVue
    },
    data() {
      return {
        src:'/login',
        counter:0,
        content: "# 第五章 矩阵计算问题 \n \
在众多科学与工程学科，如物理、化学工程、统计学、经济学、生物学、信号处理、自动控 制、系统理论、医学和军事工程等中，许多问题都可用数学建模成矩阵方程 $Ax = b$. 根据数据向量 $b \\in \\mathbb{R}^{m \\times 1}$ 和数据矩阵 $A \\in \\mathbb{R}^{m \\times n}$ 的不同，矩阵方程主要有以下三种类型: \
[abddd](1) \
 加粗",
        options: {
          linkAttributes: {
            attrs: {
              target: '_blank',
              rel: 'noopener',
              ref: 'link',
              onclick: "console.log(this.getAttribute('href'));"
            }
          }
        }
      };
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
      onClickLink123(){
        console.log("1");
      }
    },
    mounted() {
      this.$refs.myMI.use(require('markdown-it-mathjax'));
    }
  };
</script>
<style>
.el-table .cell{
  padding-left: 0px;
  padding-right: 0px;
}
.act-form{
  width:300px;
  /* background: #F0AD4E; */
  height:100%;border:none;position:absolute;right:0px;top:80px;
}
</style>
