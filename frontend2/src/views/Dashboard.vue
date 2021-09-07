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

      </b-row>

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

      };
    },
    methods: {

    },
    mounted() {
    }
  };
</script>
<style>
.el-table .cell{
  padding-left: 0px;
  padding-right: 0px;
}
</style>
