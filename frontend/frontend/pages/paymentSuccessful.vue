<template>
  <div>
    <theHeader :inCart="false" :inSellSomething="false"> </theHeader>
    <div class="form-wrapper">
      <div class="form-content">
        <label class="text-center text-4xl">Payment Succesful</label>
        <label class="text-center text-2xl"
          >Check your email for the receipt</label
        >
        <NuxtLink to="/">
          <button class="submit-button">Continue shopping</button>
        </NuxtLink>
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
import config from "~/config";
import axios from "axios";

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
    await this.submitPurchase();
    // setTimeout(() => {this.$router.push("/");}, 20000)
  },
  methods: {
    async submitPurchase() {
      try {
        let buyerInfo = this.cartStore.getbuyerInfo;

        if (Object.keys(buyerInfo) == 0){return}

        // add shipping fee
        buyerInfo["shipping_fee"] = this.cartStore.getShippingFee;

        // this.cartStore.clearCart();
        let endpoint = config.apiUrl + config.soldItemsExt;
        let response = await axios.post(endpoint, buyerInfo, {
          headers: {
            "Content-Type": "application/json",
          },
        });

        this.cartStore.clearAll();

        console.log(response);
      } catch (error) {
        console.log(error);
      }
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
</style>