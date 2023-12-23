<template>
  <theHeader :inCart="false" :inSellSomething="false"> </theHeader>
  <h1 class="text-white text-4xl text-center my-8">Checkout</h1>

  <div v-if="formStep == 1">
    <div class="form-wrapper">
      <form @submit.prevent="submitForm" class="form-content">
        <div class="form-group">
          <label for="name">Name:</label>
          <input type="text" id="name" v-model="name" />
        </div>
        <div class="form-group">
          <label for="address">PAXI or Postnet nearest to you:</label>
          <input type="text" id="address" v-model="address" />
        </div>
        <div class="form-group">
          <label for="postal">Postal Code:</label>
          <input type="number" id="postal" v-model="postal" />
        </div>
        <div class="form-group">
          <label for="cell"
            >Cell Number (to keep in touch regarding delivery):</label
          >
          <input type="number" id="cell" v-model="cell" />
        </div>
        <div class="form-group">
          <label for="email"
            >Email Address (where we will send the receipt):</label
          >
          <input type="email" id="email" v-model="email" />
        </div>
        <button class="submit-button" type="submit">Next</button>
      </form>
    </div>
  </div>

  <div v-if="formStep == 2">hello world</div>

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
      formStep: 1,
      name: "",
      address: "",
      postal: "",
      cell: "",
      email: "",
    };
  },
  methods: {
    submitForm() {
      if (this.validateForm()) {
        let info = {
          name: this.name,
          address: this.address,
          postal: this.postal,
          cell: this.cell,
          email: this.email,
        };
        this.cartStore.addBuyerInfo(info);
        console.log("info");
        console.log(info);
        this.formStep++;
        this;
      } else {
        alert("Please fill in all the fields");
      }
    },
    validateForm() {
      if (this.name == "") {
        return false;
      } else if (this.address == "") {
        return false;
      } else if (this.cell == "") {
        return false;
      } else if (this.postal == "") {
        return false;
      } else if ((this.email = "")) {
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

.selling-process p {
  /* Adjust text color */
}
.selling-process li {
  margin-bottom: 0.5rem;
}
</style>