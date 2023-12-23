<template>
  <div class="site-wrapper bg-main">

    <div class="content-wrapper flex-grow">
     
      <slot></slot>
    </div>

    <footer class="bg-teal-700">
      <img src="../assets/static/slogan.jpeg" class="footer-image" />
    </footer>
  </div>
</template>




<style scoped>


.footer-image {
  width: 100%;
  height: auto;
}

.content-wrapper {
  background-color: inherit;
}
</style>
