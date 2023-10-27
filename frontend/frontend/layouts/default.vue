<template>
  <div class="site-wrapper bg-main">
    <nav class="flex flex-col md:flex-row items-center justify-center"> <!-- Center the logo and buttons -->
      <div class="logo-container">
        <NuxtLink to="/">
          <img src="../assets/static/logo.png" alt="Home" class="logo-image" />
        </NuxtLink>
      </div>

      <div class="button-container mt-4">
        <NuxtLink
          to="/sellSomething"
          class="py-3 px-6 bg-gray-800 text-white rounded-md whitespace-nowrap font-bold nav-links"
        >
          Sell Something
        </NuxtLink>

        <NuxtLink
          to="/sellSomething"
          class="py-3 px-6 bg-gray-800 text-white rounded-md whitespace-nowrap font-bold nav-links"
        >
          Go To Cart
        </NuxtLink>
      </div>
    </nav>
    <div class="content-wrapper flex-grow">
      <slot></slot>
    </div>

    <footer class="bg-teal-700">
      <img src="../assets/static/slogan.jpeg" class="footer-image" />
    </footer>
  </div>
</template>

<style scoped>
.site-wrapper {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center; /* Vertically center the content */
  align-items: center; /* Horizontally center the content */
}

.logo-container {
  display: flex;
  justify-content: center; /* Center the logo horizontally */
}

.logo-image {
  width: 40%;
  height: auto;
  margin-left: 32%;
}

.button-container {
  display: flex;
  justify-content: center; /* Center the buttons horizontally */
  align-items: center;
  margin-top: 1rem;
}

.nav-links {
  display: flex;
  align-items: center;
  margin-right: 1rem;
}

.footer-image {
  width: 100%;
  height: auto;
}

.content-wrapper {
  background-color: inherit;
}
</style>
