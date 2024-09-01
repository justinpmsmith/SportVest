<template>
  <div class="site-wrapper bg-main">
    <div class="content-wrapper flex-grow">
      <slot></slot>
    </div>

    <footer class="bg-teal-700">
      <div class="row">
        <NuxtLink to="/">
          <h2 class="text-white text-center mx-8"><b><u>Home</u></b></h2>
        </NuxtLink>
        <!-- /contactUs -->
        <!-- /paymentSuccessful -->
        <NuxtLink to="/contactUs">
          <h2 class="text-white text-center mx-8"><b><u>Contact Us</u></b></h2>
        </NuxtLink>
        <NuxtLink to="/about">
          <h2 class="text-white text-center mx-8"><b><u>About Us</u></b></h2>
        </NuxtLink>
      </div>
      <img src="../assets/static/slogan1.jpeg" class="footer-image" />
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
.row {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: row;
  text-align: center;
}
</style>
