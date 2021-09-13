<template>
  <div>
    <b-container>
      <div class="row">
        <div class="col" ref="main_reader" cols="8">
          <VueShowdown :markdown="content" flavor="github" :extensions="['showdown-katex', special_link_local]" @click.native="performReference" />
        </div>
        <div class="col" v-if="show_reference" ref="ref_reader" cols="5">
          <template v-for="(reference, index) in content_references">
            <VueShowdown :key="index" :markdown="reference" flavor="github" :extensions="['showdown-katex', special_link_local]" />
          </template>
        </div>
      </div>
      <b-button @click="onRefer" >参考</b-button>
    </b-container>
  </div>
</template>

<script>
import MarkdownItVue from "markdown-it-vue";
import { VueShowdown } from 'vue-showdown';
import 'showdown-katex';
import "markdown-it-vue/dist/markdown-it-vue.css";

const special_link = [{
    type: 'lang',
    regex: /\[(.*?)\]\((.*?)\)/g,
    replace: function(wholematch, tag, uuid) {
      var result = '<a href=' + uuid + ' onclick="return false;" class="reference"';
      result += '>' + tag + '</a>';
      return result;
    }
}];

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
      content:"## 5.1 线性方程组的直接解法\n\
### 5.1.1 线性方程组问题\n\
在工程问题中，线性方程组描述了变量之间最基本的关系。线性方程在各个科学分支中无处不在，例如弹性力学、电阻网络、曲线拟合等。线性方程构成了线性代数的核心并时常作为 优化问题的约束条件。由于许多优化算法的迭代过程非常依赖线性方程组的解，所以它也是许 多优化算法的基础。下面我们以一个例子来说明，线性方程组如何解决上面的问题。\n\
**例5.1.1.** *(*三点测距问题*)*三角测量是一种确定点位置的方法，给定距离到已知控制点*(*锚点*)*，三边测量可以应用于许多不同的领域，如地理测绘、地震学、导航(例如 *GPS* 系统)等。 在图*5.2*中，三个测距点 $$a_1, a_2, a_3 \\in \\mathbb{R}^2$$ 的坐标是已知的，并且从点 $$\\textbf{x} = (x_1, x_2)^T$$ 到测距点的距离为 $$d_1, d_2, d_3$$，$$\\textbf{x}$$ 的未知坐标与距离测量有关，可以由下面非线性方程组描述\n\
```latex\n\
||\\textbf{x}−\\textbf{a}_1||_2^2 =d_1^2, ||\\textbf{x}−\\textbf{a}_2||_2^2 =d_2^2, ||\\textbf{x}−\\textbf{a}_3||_2^2 =d^2_3 \\ \\ \\ (5.1)\n\
```\n\
![2](image/2.jpg)",
      content_references: ["## 5.1 线性方程组的直接解法\n\
### 5.1.1 线性方程组问题\n\
在工程问题中，线性方程组描述了变量之间最基本的关系。线性方程在各个科学分支中无处不在，例如弹性力学、电阻网络、曲线拟合等。线性方程构成了线性代数的核心并时常作为 优化问题的约束条件。由于许多优化算法的迭代过程非常依赖线性方程组的解，所以它也是许 多优化算法的基础。下面我们以一个例子来说明，线性方程组如何解决上面的问题。\n\
**例5.1.1.** *(*三点测距问题*)*三角测量是一种确定点位置的方法，给定距离到已知控制点*(*锚点*)*，三边测量可以应用于许多不同的领域，如地理测绘、地震学、导航(例如 *GPS* 系统)等。 在图*5.2*中，三个测距点 $$a_1, a_2, a_3 \\in \\mathbb{R}^2$$ 的坐标是已知的，并且从点 $$\\textbf{x} = (x_1, x_2)^T$$ 到测距点的距离为 $$d_1, d_2, d_3$$，$$\\textbf{x}$$ 的未知坐标与距离测量有关，可以由下面非线性方程组描述\n\
```latex\n\
||\\textbf{x}−\\textbf{a}_1||_2^2 =d_1^2, ||\\textbf{x}−\\textbf{a}_2||_2^2 =d_2^2, ||\\textbf{x}−\\textbf{a}_3||_2^2 =d^2_3 \\ \\ \\ (5.1)\n\
```\n"],
      show_reference: false,
      md_url: "",
      special_link_local: () => special_link
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
      let pred_index = full_host.lastIndexOf(":");
      let pure_host = full_host.substring(0, pred_index);
      return protocol_str + "://" + pure_host;
    },
    loadMd(md_url) {
      console.log(md_url)
      this.axios
        .get(md_url)
        .then(response => {
          if (response.data && response.status == 200) {
            var res = response.data;
            console.log(res);
          }

          this.content = res;
        })
        .catch(error => {
          console.log(error);
        });
    },
    performReference(event) {
      let target = event.target;
      if(target != undefined && target.tagName == "A"){
        if(target.getAttribute("class") == "reference"){
          let word_id = target.getAttribute("href");
          this.getReference(word_id, function(refbook_list){

          });
        }
      }
    },
    onRefer() {
      this.show_reference = true;
      console.log("!111");
    },
    getReference(word_id, callback) {
      let url = this.getHostUrl() + ":5000/read/search?book_id=" + this.uuid + "&word_id=" + word_id;
      this.axios.get(url).then(response => {
        if(response.data && response.status == 200){
          callback(response.data);
        }
      })
    }
  },
  mounted() {
    this.uuid = this.$route.path.split("/")[2];
    this.md_url = this.getHostUrl() + ":5000/file/get_md?book_id=" + this.uuid;
    this.loadMd(this.md_url);
    //this.$refs.myMI.use(require("markdown-it-mathjax"));
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
