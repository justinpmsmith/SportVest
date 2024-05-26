<template>
  <div>
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
            <label for="address">Address of Postnet nearest to you:</label>
            <input type="text" id="address" v-model="address" />
          </div>
          <div class="form-group">
            <label for="postal">Postal Code:</label>
            <input type="number" id="postal" v-model="postal" />
          </div>
          <div class="form-group">
            <label for="cell">Cell:</label>
            <input type="number" id="cell" v-model="cell" />
          </div>
          <div class="form-group">
            <label for="email">Email Address:</label>
            <input type="email" id="email" v-model="email" />
          </div>
          <button class="submit-button" type="submit">Next</button>
        </form>
      </div>
      <br />
      <br />
      <br />
    </div>

    <div v-if="formStep == 2">
      <div class="form-wrapper">
        <form class="form-content">
          <label class="text-center text-2xl">Total</label>
          <label class="text-center">R{{ cartTotal }}</label>

          <div class="row">
            <button class="submit-button" @click="previous">Previous</button>

            <form
              action="https://www.payfast.co.za/eng/process"
              method="post"
              class="submit-button"
            >
              <input type="hidden" name="merchant_id" :value="merchantId" />
              <input type="hidden" name="merchant_key" :value="merchantKey" />
              <input
                type="hidden"
                name="return_url"
                :value="baseUrl + successUrl"
              />
              <input
                type="hidden"
                name="cancel_url"
                :value="baseUrl + successUrl"
              />
              <!-- <input type="hidden" name="notify_url" value="https://www.example.com/notify"> -->
              <input type="hidden" name="amount" :value="cartTotal" />
              <input type="hidden" name="item_name" value="Sportvest Order" />
              <button type="submit">Pay Now</button>
            </form>
          </div>
        </form>
      </div>
      <br />
      <br />
      <br />
      <br />
      <br />
      <br />
      <br />
      <br />
      <br />
      <br />
      <br />
    </div>
  </div>
</template>

<script>
import { useCartStore } from "~/store/cart";
import theHeader from "~/components/theHeader.vue";
import config from "~/config";

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
      merchantId: "",
      merchantKey: "",
      cartTotal: 0,
      baseUrl: "https://370b-165-255-36-241.ngrok-free.app",
      successUrl: "/paymentSuccessful",
      cancelUrl: "/paymentCancelled",
    };
  },
  created() {
    this.merchantId = config.merchantId;
    this.merchantKey = config.merchantKey;
    this.cartTotal = this.cartStore.getCartTotal;
  },
  // computed: {
  //   cartTotal() {
  //     let total = this.cartStore.getCartTotal;
  //     return total;
  //   },
  // },
  methods: {
    submitForm() {
      if (this.validateForm()) {
        let total = this.cartStore.getCartTotal;

        let info = {
          name: this.name,
          address: this.address,
          postal: this.postal,
          cell: this.cell,
          email: this.email,
          totalPrice: total,
        };
        this.cartStore.addBuyerInfo(info);
        console.log("info");
        console.log(info);
        this.formStep = 2;
        this;
      } else {
        alert("Please fill in all the fields");
      }
    },
    previous() {
      this.formStep = 1;
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
      } else if (this.email == "") {
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

.row {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: row;
  text-align: center;
}
.radio-group {
  display: flex;
  justify-content: space-between;
}

.radio-group input {
  margin-right: 2vw;
  transform: scale(0.8); /* Adjust the scale factor to make them smaller */
}

/* Optional: Adjust the label size and padding if needed */
.radio-group label {
  font-size: 14px;
  margin-right: 12vw;
  padding-top: 1.5vw;
  /* padding-left: 2px;  */
}
</style>