<template>
  <div class="row">
    <div ref="main_reader">
      <b-card no-body class="col-6">
              <canvas v-for="page in pageNum" :id="'canvas' + page" :key="page"></canvas>
      </b-card>
    </div>
    <div ref="ref_reader">
      
    </div>
  </div>
</template>

<script>
import * as PDFJS from 'pdfjs-dist/webpack'

export default {
  name: "Reader",
  data() {
    return {
      uuid: "",
      pdf_url: "",
      pdf_doc: null,
      pageNum: 0,
    };
  },
  mounted() {
    this.uuid = this.$route.query.uuid;
    this.pdf_url = this.getHostUrl() + ':5000/file/get_pdf?book_id=' + this.uuid;
    this.loadPdf(this.pdf_url);
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
    loadPdf(pdf_url){
      let that = this;
      PDFJS.getDocument(pdf_url).promise.then((pdf) => {
        that.pdf_doc = pdf;
        that.pageNum = pdf.numPages;
        that.$nextTick(() => {
          that.renderPage(1);
        });
      });
    },
    renderPage(page_num){
      let that = this;
      this.pdf_doc.getPage(page_num).then((page) => {
        var scale = 1.5
        var viewport = page.getViewport({scale: scale});
        var canvas = document.getElementById('canvas' + page_num);
        var context = canvas.getContext('2d');
        canvas.height = viewport.height;
        canvas.width = viewport.width;
        var renderContext = {
          canvasContext: context,
          viewport: viewport,
        }
        page.render(renderContext);
        console.log(page_num)

        if (that.pageNum > page_num) {
          that.renderPage(page_num + 1)
        }
      });
    }
  }
}
</script>
