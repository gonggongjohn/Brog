<template>
  <div>

    <base-header class="pb-6 pb-8 pt-5 pt-md-8 bg-gradient-success">
<!--       Card stats -->

      <b-row>

        <b-col xl="4" md="6">
          <div>
          <b-card
          title="数据科学与工程的数学基础"
          img-src="/img/books/image_u55.svg"
          img-alt="Image"
          img-top
          tag="article"
          style="max-width: 20rem;"
          class="mb-2"
          align="center">

      <b-button href="#" variant="primary">进入阅读</b-button>
<!--            <b-button href="#" variant="primary">添加到书架</b-button>-->
      </b-card>
      </div>

        </b-col>
        <b-col xl="4" md="6">
          <div>
          <b-card
          title="线性代数"
          img-src="/img/books/image_u69.svg"
          img-alt="Image"
          img-top
          tag="article"
          style="max-width: 20rem;"
          class="mb-2"
          align="center">

      <b-button href="#" variant="primary">进入阅读</b-button>
<!--            <b-button href="#" variantariant="primary">添加到书架</b-button>-->
      </b-card>
      </div>


        </b-col>
        <b-col xl="4" md="6">
          <div>
          <b-card
          title="机器学习"
          img-src="/img/books/image_u77.svg"
          img-alt="Image"
          img-top
          tag="article"
          style="max-width: 20rem;"
          class="mb-2"
          align="center">

      <b-button href="#" variant="primary">进入阅读</b-button>
<!--            <b-button href="#" variantariant="primary">添加到书架</b-button>-->
      </b-card>
      </div>

        </b-col>


        <b-col xl="4" md="6" v-for="(book_item,index) in book_list.slice(1)" :key="book_item.name" >
          <div>
          <b-card
          title=""
          img-src="/img/books/book_logo.png"
          img-alt="Image"
          img-top
          tag="article"
          style="max-width: 20rem;"
          class="mb-2"
          align="center">
            <b-card-text>
      <strong>{{book_item.name}}</strong>
    </b-card-text>

      <b-button v-on:click="onReadingBook(index+1)" variant="primary">进入阅读</b-button>
<!--            <b-button href="#" variantariant="primary">添加到书架</b-button>-->
      </b-card>
      </div>

        </b-col>


      </b-row>


<!--    <div v-html="htmlMsg"></div>-->
    <!-- <div id="info"></div> -->

    </base-header>



  </div>
</template>
<script>


  export default {
    components: {

    },

    data() {
      return {
        // htmlMsg:this.getBook(),
      book_list: [
        {
          uuid:"1" ,
          name: "123",
          contributor: ""
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
      getBook(){
        console.log(this.getHostUrl() )
        var url = this.getHostUrl() + ':5000/file/list_collection/';
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


          // var booknum=book_list_tmp.length;
          // var rownum=parseInt(booknum/3);
          // var colnum=booknum-3*rownum;
          // //生成html格式文本
          // var htmlStr='';
          // var i,j=0;
          // console.log(this.book_list)
          // for(i=0;i<=rownum;i++){
          //   htmlStr+='<div class="row">';
          //   if(i!=rownum){
          //     console.log(i,rownum)
          //     for(j=0;j<3;j++){
          //     htmlStr+='<div class="col-md-6 col-xl-4"><div><article class="card mb-2 text-center" style="max-width: 20rem;"><img src="/img/books/book_logo.png" alt="Image" class="card-img-top"><!----><div class="card-body"><h4 class="card-title">'+book_list_tmp[3*i+j].filename+'</h4><!----><a role="button" tabindex="0" onclick="this.onReading(this.book_list)" target="_self" class="btn btn-primary">进入阅读</a></div><!----><!----></article></div></div>';
          //     }
          //
          //   }else{
          //     for(j=0;j<colnum;j++){
          //       console.log(book_list_tmp[3*i+j].filename)
          //     htmlStr+='<div class="col-md-6 col-xl-4"><div><article class="card mb-2 text-center" style="max-width: 20rem;"><img src="/img/books/book_logo.png" alt="Image" class="card-img-top"><!----><div class="card-body"><h4 class="card-title">'+book_list_tmp[3*i+j].filename+'</h4><!----><a role="button" tabindex="0"  v-on:click="this.onReading(1)" target="_self" class="btn btn-primary">进入阅读</a></div><!----><!----></article></div></div>';
          //
          //
          //     }
          //   }
          //   htmlStr+="</div>";
          // }
          // // window.innerHTML()
          // // return book_list_tmp.length;
          // // console.log(htmlStr)
          // this.htmlMsg=htmlStr;
          // // document.getElementById ("info").innerHTML =htmlStr;
          // return htmlStr;

        }

      });
      },
      onReadingBook(index){
         console.log(this.book_list[index].uuid);
         this.$router.push({path: `/viewer/${this.book_list[index].uuid}`});
      // this.$router.push({path: '/viewer/', query: {uuid: this.book_list[index].uuid}});
    },
       getBookList(){
      var url = this.getHostUrl() + ':5000/file/list_all/';
      this.axios.get(url).then((response) => {
        if(response.data && response.status == 200){
          var book_list_tmp = response.data;
          console.log(book_list_tmp)
          // window.innerHTML()
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
    }

    },
    mounted() {
      this.getBook();
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
</style>
