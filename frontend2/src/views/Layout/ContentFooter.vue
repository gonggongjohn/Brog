<template>
  <footer class="footer px-4">
    <b-row align-v="center" class="justify-content-lg-between">
      <b-col lg="6">
        <div class="copyright text-center text-lg-left text-muted">
          © {{year}} <a href="https://gonggongjohn.github.io/ckas-website/" class="font-weight-bold ml-1" target="_blank">Brog</a>
        </div>
      </b-col>
      <b-col lg="6">
        <b-nav align="center" class="nav-footer justify-content-lg-end">
          <b-nav-item href="https://gonggongjohn.github.io/ckas-website/" target="_blank" >
                Brog
              </b-nav-item>

          <b-nav-item href="https://gonggongjohn.github.io/ckas-website/" target="_blank">
           About Us
          </b-nav-item>


        </b-nav>
      </b-col>
    </b-row>
  </footer>
</template>
<script>
export default {
  data() {
    return {
      year: new Date().getFullYear()
    };
  }
};
</script>
<style></style>
