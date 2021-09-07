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
            <b-button href="#" variant="primary">添加到书架</b-button>
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
            <b-button href="#" variant="primary">添加到书架</b-button>
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
            <b-button href="#" variant="primary">添加到书架</b-button>
      </b-card>
      </div>

        </b-col>

      </b-row>

    <!-- <div>{{getBookNum()}}</div> -->
    
   <li v-for='num in 10' :key="num">{{ num }}</li>

    </base-header>



  </div>
</template>
<script>


  export default {
    components: {
      // LineChart,
      // BarChart,
      // BaseProgress,
      // StatsCard,
      // PageVisitsTable,
      // SocialTrafficTable
    },
    data() {
      return {

      book_list: [
        {
          uuid:"1" ,
          name: "123",
          contributor: "1234"
        }
      ]
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
      getBookNum(){
        console.log(this.getHostUrl() )
var url = this.getHostUrl() + ':5000/file/list_all/';
      this.axios.get(url).then((response) => {
  if(response.data && response.status == 200){
          var book_list_tmp = response.data;
          console.log("booknum:",book_list_tmp.length)
          // window.innerHTML()
          // return book_list_tmp.length;
          return book_list_tmp.length;

        }

      });
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
