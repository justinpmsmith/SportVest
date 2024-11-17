<template>
  <div>
    <theHeader :inCart="false" :inSellSomething="false"> </theHeader>
    <h1 class="text-white text-4xl text-center my-8">Checkout</h1>
    <div v-if="formStep == 0">
      <div class="form-wrapper">
        <form @submit.prevent="next" class="form-content">
          <label
            >Would you like to collect your order(Arrangments will be made for
            collection in White River Mpumalanga) or have it delivered through
            PUDO(Powered by The Delivery Guy)?</label
          >
          <div class="radio-group">
            <ul>
              <li>
            <label for="collection">Collection (free)</label>
            <input
              type="radio"
              id="collection"
              name="delivery"
              v-model="this.collection"
              :value="true"
            />
          </li>
          <li>

            <label for="delivery">Delivery ({{ shippingFee }})</label>
            <input
              type="radio"
              id="delivery"
              name="delivery"
              v-model="this.collection"
              :value="false"
            />
          </li>
        </ul>

          </div>
          <button class="submit-button" type="submit">Next</button>
        </form>
      </div>
      <br />
      <br />
      <br />
    </div>

    <div v-if="formStep == 1 && !collection">
      <div class="form-wrapper">
        <form @submit.prevent="submitDeliveryForm" class="form-content">
          <div class="form-group">
            <label for="name">Name:</label>
            <input type="text" id="name" v-model="name" />
          </div>
          <div class="form-group">
            <label for="surname">Surname:</label>
            <input type="text" id="surname" v-model="surname" />
          </div>
          <div class="form-group">
            <label for="address">Address of PUDO nearest to you:</label>
            <input type="text" id="address" v-model="address" />
          </div>
          <div class="form-group">
            <label for="postal">Postal Code:</label>
            <input type="number" id="postal" v-model="postal" />
          </div>
          <div class="form-group">
            <label for="cell">Cell:</label>
            <input type="tel" id="cell" v-model="cell" />
          </div>
          <div class="form-group">
            <label for="email">Email Address:</label>
            <input type="email" id="email" v-model="email" />
          </div>
          <div class="button-group">
            <button class="submit-button" @click="previous">Previous</button>

            <button class="submit-button" type="submit">Next</button>
          </div>
        </form>
      </div>
      <br />
      <br />
      <br />
    </div>

    <div v-if="formStep == 1 && collection">
      <div class="form-wrapper">
        <form @submit.prevent="submitCollectionForm" class="form-content">
          <div class="form-group">
            <label for="name">Name:</label>
            <input type="text" id="name" v-model="name" />
          </div>
          <div class="form-group">
            <label for="surname">Surname:</label>
            <input type="text" id="surname" v-model="surname" />
          </div>
          <div class="form-group">
            <label for="cell">Cell:</label>
            <input type="tel" id="cell" v-model="cell" />
          </div>
          <div class="form-group">
            <label for="email">Email Address:</label>
            <input type="email" id="email" v-model="email" />
          </div>
          <div class="button-group">
            <button class="submit-button" @click="previous">Previous</button>

            <button class="submit-button" type="submit">Next</button>
          </div>
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
          <label class="text-center">R{{ orderTotal }}</label>
          <label class="text-md-center"
            >Thank you for your support. Please note due to the nature of the business, all items are non-refundable.</label
          >

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
                :value="baseUrl + cancelUrl"
              />
              <!-- <input type="hidden" name="notify_url" value="https://www.example.com/notify"> -->
              <input type="hidden" name="amount" :value="orderTotal" />
              <input type="hidden" name="item_name" value="Sportvest Order" />
              <input type="hidden" name="email_address" :value="email" />
              <!-- <input type="hidden" name="signature" :value="signature" /> -->

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
import { toast } from "vue3-toastify";
import CryptoJS from "crypto-js";

import config from "~/config";

export default {
  components: {
    theHeader,
  },
  data() {
    return {
      cartStore: useCartStore(),
      formStep: 0,
      name: "",
      surname: "", 
      address: "",
      postal: "",
      cell: "",
      email: "",
      merchantId: "",
      merchantKey: "",
      orderTotal: 0,
      baseUrl: config.domain,
      successUrl: "/paymentSuccessful",
      cancelUrl: "/paymentCancelled",
      collection: null,
      signature: "",
      shippingFee: 70,
    };
  },
  created() {
    this.merchantId = config.merchantId;
    this.merchantKey = config.merchantKey;
    // this.cartTotal = this.cartStore.getCartTotal;
  },
  // computed: {
  //   cartTotal() {
  //     let total = this.cartStore.getCartTotal;
  //     return total;
  //   },
  // },
  methods: {
    next() {

      if (this.collection == null) {
        toast("Please Choose collection or Delivery", {
          autoClose: 500,
        });
        return;
      }

      if (!this.collection) {
        this.cartStore.setShippingFee(this.shippingFee);
      } else {
        this.cartStore.setShippingFee(0);
      }
      this.orderTotal = this.cartStore.getOrderTotal;

      this.formStep += 1;
    },
    submitDeliveryForm() {
      if (this.validateDeliveryForm()) {
        let total = this.cartStore.getOrderTotal;

        this.name = this.name + " " + this.surname;

        let info = {
          name: this.name,
          address: this.address,
          postal: this.postal,
          cell: this.cell,
          email: this.email,
          totalPrice: total,
        };

        this.cartStore.addBuyerInfo(info);
        this.formStep = 2;
        this.generateSignatureFromData();
      } else {
        alert("Please fill in all the fields");
      }
    },
    submitCollectionForm() {
      if (this.validateCollectionForm()) {
        let total = this.cartStore.getOrderTotal;

        this.name = this.name + " " + this.surname;

        let info = {
          name: this.name,
          address: "NA",
          postal: "NA",
          cell: this.cell,
          email: this.email,
          totalPrice: total,
        };

        console.log("buyer info: ")
        console.log(info);
        this.cartStore.addBuyerInfo(info);
        this.formStep = 2;
        this.generateSignatureFromData();
      } else {
        alert("Please fill in all the fields");
      }
    },

    previous() {
      this.formStep -= 1;
    },
    validateDeliveryForm() {
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
    validateCollectionForm() {
      if (this.name == "" || this.surname == "") {
        return false;
      } else if (this.cell == "") {
        return false;
      } else if (this.email == "") {
        return false;
      }
      return true;
    },

    generateSignature(data, passPhrase = null) {
      // Create parameter string
      let pfOutput = "";
      for (let key in data) {
        if (data.hasOwnProperty(key)) {
          if (data[key] !== "") {
            pfOutput += `${key}=${encodeURIComponent(String(data[key]).trim()).replace(
              /%20/g,
              "+"
            )}&`;
          }
        }
      }

      // Remove last ampersand
      let getString = pfOutput.slice(0, -1);
      if (passPhrase !== null) {
        getString += `&passphrase=${encodeURIComponent(
          passPhrase.trim()
        ).replace(/%20/g, "+")}`;
      }

      return CryptoJS.MD5(getString).toString(CryptoJS.enc.Hex);
    },
    generateSignatureFromData() {
      // Create parameter string

      let data = {
        merchant_id: this.merchantId,
        merchant_key: this.merchantKey,
        return_url: this.baseUrl + this.successUrl,
        cancel_url: this.baseUrl + this.cancelUrl,
        amount: this.orderTotal,
        item_name: "Sportvest Order",
        email_address: this.email,
        // cell_number: this.cell,
      };

      console.log(JSON.stringify(data));

      this.signature = this.generateSignature(data, config.passPhrase);
      console.log("signature: " + this.signature);
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
  justify-content: center;
}

.radio-group input {
  /* margin-right: 2vw; */
  /* transform: scale(0.8); Adjust the scale factor to make them smaller */
}

/* Optional: Adjust the label size and padding if needed */
.radio-group label {
  font-size: 1rem;
  /* margin-right: 12vw; */
  padding-top: 2rem;
  /* padding-left: 2px;  */
}
.button-group {
  display: flex;
  justify-content: center;

}
.radio-group {
  display: flex; /* Make radio buttons and labels behave as flex items */
  align-items: center; /* Align labels and radio buttons vertically */
}

.radio-group label {
  /* margin-right: 3rem; Optional spacing between label and radio button */
}
</style>