<template>
    <div>
      <theHeader :inCart="false" :inSellSomething="false"> </theHeader>
      <div class="form-wrapper">
        <div class="form-content">
          <label class="text-center text-4xl">Payment Canceled</label>
          <div class="button-container">
          <NuxtLink to="/">
            <button class="submit-button">Continue shopping</button>

          </NuxtLink>
          <NuxtLink to="/">
            <button class="submit-button">Try Again</button>
          </NuxtLink>
        </div>
        </div>
      </div>
      <br />
      <br />
      <br />
      <br />
      <br />
      <br />
    </div>
  </template>
    <script>
  import { useCartStore } from "~/store/cart";
  import theHeader from "~/components/theHeader.vue";
  
  export default {
    components: {
      theHeader,
    },
    data() {
      return {
        cartStore: useCartStore(),
      };
    },
    async created() {
      console.log("created")

    },
    methods: {

    },
  };
  </script>
  
  <style scoped>
  .form-wrapper {
    display: flex;
    justify-content: center;
  }
  
  .form-content {
    width: 80%;
    max-width: 400px;
    margin-top: 2rem;
    background-color: white;
    padding: 2rem;
    border-radius: 4px;
  }
  
  .form-group {
    margin-bottom: 1rem;
  }
  
  label {
    display: block;
    margin-bottom: 0.5rem;
    color: #047481;
    font-weight: bold;
  }
  
  textarea,
  input {
    width: 100%;
    padding: 0.5rem;
    border-radius: 4px;
    border: 1px solid #ccc;
  }
  button {
    padding: 0.5rem 1rem;
    background-color: #047481;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .uploaded-image {
    max-width: 200px;
    margin-bottom: 1rem;
  }
  
  .submit-button {
    display: block;
    margin-top: 1rem;
    margin-left: auto;
    margin-right: auto;
  }
  
  .row {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: row;
    text-align: center;
  }
  .button-container {
  display: flex;
  justify-content: space-between;
}
  </style>