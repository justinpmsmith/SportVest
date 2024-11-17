<template>
  <div>
    <theHeader :inCart="false" :inSellSomething="true"> </theHeader>
    <h1 class="text-white text-4xl text-center my-8">Contact Us</h1>

  
    <div class="form-wrapper">
      <form @submit.prevent="submitForm" class="form-content">
        <div class="form-group">
          <label for="name">Name:</label>
          <input id="name" v-model="name" />
        </div>
        <div class="form-group">
          <label for="surname">Surname:</label>
          <input id="surnname" v-model="surname" />
        </div>
        <div class="form-group">
          <label for="cell">Cell Number:</label>
          <input type="tel" id="cell" v-model="cell" />
        </div>
        <div class="form-group">
          <label for="email">Email Address:</label>
          <input type="email" id="email" v-model="email" />
        </div>
        <div class="form-group">
          <label for="message">Message:</label>
          <textarea id="message" v-model="message"></textarea>
        </div>
        <button class="submit-button" type="submit">Submit</button>
      </form>
    </div>
    <br />
  </div>
  </template>
    
    <script>
  import axios from "axios";
  import { useCartStore } from "~/store/cart";
  import theHeader from "~/components/theHeader.vue";
  import { toast } from "vue3-toastify";
  import "vue3-toastify/dist/index.css";
  import config from "~/config";
  
  export default {
    components: {
      theHeader,
    },
    data() {
      return {
        cartStore: useCartStore(),
        message: "",
        cell: "",
        email: "",
        toastId: null,
        name:"",
        surname: "",
      };
    },
  
    methods: {

      async submitForm() {
        // Display a toast message at the beginning
  
        try {
          if (this.validateForm()) {
            this.toastId = toast("Uploading product information");
         
            var extension = config.contactUsExt;
            var api = config.apiUrl;
            var endpoint = api + extension;
  
            const formData = new FormData();
            formData.append("message", this.message);
            formData.append("cell", this.cell);
            formData.append("email", this.email);
            formData.append("name", this.name + " " + this.surname);

            console.log("form: " )
            console.log(formData);

  
  
            const timeoutPromise = new Promise((_, reject) =>
              setTimeout(() => reject(new Error("Request timed out")), 30000)
            );
  
            const response = await Promise.race([
              axios.post(endpoint, formData),
              timeoutPromise,
            ]);
  
            console.log(
              "########################## response: " + response.data.message
            );
  
            this.message = "";
            this.cell = "";
            this.email = "";
            this.name = "";
            this.surname = "";
  
            if (response.data.message === "success") {
              alert(
                "Messaged submitted"
              );
            } else {
              alert(
                "There was an issue uploading your product. Please try again."
              );
            }
          } else {
            return;
          }
        } catch (error) {
          console.error(error);
          alert("There was an issue submitting your message");
        } finally {
          // Close the toast once the method execution is completed
          toast.clearAll(this.toastId);
          this.toastId = null;
        }
      },
      validateForm() {
        if (this.message == "") {
          alert("Please fill in the message field");

          return false;
        } else if (this.cell == "" && this.email == "") {
          alert("Please fill in either cell number or email");

          return false;
        } else if (this.name == "" || this.surname == "") {
          alert("Please fill name and surname");

          return false;
        }
        return true;
      },
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
  
  .selling-process {
    /* Add styles to center the content horizontally */
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    text-align: center;
  }
  
  .selling-process h2 {
    /* Add styles to restore the numbered bullets */
    text-align: center;
    font-weight: bold;
    margin-bottom: 1rem;
  }
  
  .selling-process ol {
    /* Add styles to restore the numbered bullets */
    text-align: left;
    list-style-type: decimal;
    padding-left: 2rem;
    margin-bottom: 1rem;
    color: white;
  }
  

  .selling-process li {
    margin-bottom: 0.5rem;
  }
  </style>
    