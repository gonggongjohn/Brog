<template>
  <div>

    <base-header class="pb-6 pb-8 pt-5 pt-md-8 bg-gradient-success">
<!--       Card stats -->

      <div>
 <button @click = "counter++" style = "font-size:25px;">控制右侧边栏</button>
<div >
    <iframe :src="src" v-if="counter%2" class="act-form"></iframe>
  </div>
 </div>
<!-- https://www.npmjs.com/package/vue-markdown -->
 <vue-markdown>i am a ~~tast~~ **test**. $\eta_1, \eta_2, \cdots, \eta_{n−r}$ </vue-markdown>
 <!-- https://evolly.one/2019/07/01/118-vue-markdown-loader/ -->
<!-- class markdown-body 必须加，否则标签样式会出现问题 -->
  <div class="markdown-body">
    <markdown />
  </div>



    </base-header>



  </div>
</template>

<script>
// 引入 markdown 文件，引入后是一个组件，需要在 components 中注册
import markdown from '@/assets/ApiDocument.md'
// 代码高亮
import 'highlight.js/styles/github.css'
// 其他元素使用 github 的样式
import 'github-markdown-css'
import VueMarkdown from 'vue-markdown'

  export default {
    components: {
      markdown,
      VueMarkdown
      // LineChart,
      // BarChart,
      // BaseProgress,
      // StatsCard,
      // PageVisitsTable,
      // SocialTrafficTable
    },
    data() {
      return {
     src:'/login',
     counter:0
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
    }
    
    },
    mounted() {
    // htmlMsg=this.getBook();

      // this.getBookList();
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
