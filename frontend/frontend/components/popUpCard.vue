<template>
  <div class="popup-card">
    <div class="popup-wrapper">
      <v-card class="popup-content">
        <!-- <v-img :src="product.image" class="popup-image"></v-img> -->
        <v-carousel hide-delimiters>
          <v-carousel-item :src="product.image" cover></v-carousel-item>

          <v-carousel-item
          :src="product.image2?product.image2:product.image"
            cover
          ></v-carousel-item>

          <v-carousel-item
          :src="product.image3?product.image3:product.image"
            cover
          ></v-carousel-item>
        </v-carousel>

        <div class="popup-message">
          <div class="text-h6 text-sm-left" style="color: wheat">
            {{ product.description }}
          </div>
          <br>
          <div class="text-h6 text-sm-left" style="color: wheat">
            Price: R{{ product.price }}
          </div>
          <!-- <ul class="popup-list">
              <li class="popup-item">
                <p class="popup-text">{{ message1 }}</p>
              </li>
              <li class="popup-item">
                <p class="popup-text">Whatsapp: <span class="clickable" @click="copyToClipboard(cell)">{{ cell }}</span></p>
                <v-btn class="copy-button" @click="copyToClipboard(cell)">Copy</v-btn>
              </li>
              <li class="popup-item">
                <p class="popup-text">Product Code: <span class="clickable" @click="copyToClipboard(productCode)">{{ productCode }}</span></p>
                <v-btn class="copy-button" @click="copyToClipboard(productCode)">Copy</v-btn>
              </li>
              <li class="popup-item">
                <p class="popup-text">Email: <span class="clickable" @click="copyToClipboard(email)">{{ email }}</span></p>
                <v-btn class="copy-button" @click="copyToClipboard(email)">Copy</v-btn>
              </li>
            </ul> -->
        </div>
        <div class="popup-button" @click="closePopup">Close</div>
        <div class="popup-button" @click="addToCart">Add to Cart</div>
      </v-card>
    </div>
  </div>
</template>
  
  <script>
import { useCartStore } from "~/store/cart";
import { toast } from "vue3-toastify";
import "vue3-toastify/dist/index.css";
export default {
  props: {
    product: Object,
  },
  data() {
    return {
      email: "Joso@me.com",
      message1:
        "To buy this item, please reach out to us on WhatsApp or via email",
      cell: "084 507 3080",
      cartStore: useCartStore(),
    };
  },

  methods: {
    copyToClipboard(text) {
      const el = document.createElement("textarea");
      el.value = text;
      document.body.appendChild(el);
      el.select();
      document.execCommand("copy");
      document.body.removeChild(el);
    },
    addToCart() {
      let result = this.cartStore.addToCart(this.product);
      console.log("cart total: " + this.cartStore.getCartTotal);

      if (result) {
        toast("Product added to cart", {
          autoClose: 500,
        });
      } else {
        toast("Item already in cart", {
          autoClose: 500,
        });
      }
      this.closePopup();
    },
    closePopup() {
      console.log(JSON.stringify(this.product));
      this.$emit("close-popup"); // Emit an event called 'close-popup'
    },
  },
};
</script>
  
  <style scoped>
.popup-card {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: rgba(0, 0, 0, 0.5); /* Semi-transparent background */
}

.popup-wrapper {
  width: 25rem;
  padding: 1rem;
  position: relative;
  background-color: rgba(0, 0, 0, 0.5);
  max-height: 100vh; /* 100% of the viewport height */
  overflow-y: auto; /* Enable vertical scrolling if needed */
}

.popup-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  background-color: rgb(10, 66, 77);
  padding: 1rem;
}

.popup-image {
  width: 100%;
  height: auto;
  background-color: #333333;
}

.popup-message {
  margin-top: 1rem;
}

.popup-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.popup-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.5rem 0;
  elevation: 1;
  background-color: white;
}

.popup-text {
  margin: 0;
}

.clickable {
  cursor: pointer;
  font-weight: bold;
  text-decoration: bold;
}

.copy-button {
  margin-left: 1rem;
  background-color: #047481;
  color: white;
}

.popup-button {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 1rem;
  cursor: pointer;
  text-align: center;
  background-color: #047481;
  color: white;
  font-weight: bold;
  width: 100%;
  height: 3rem;
  box-sizing: border-box;
  border: 2px solid white;
}
</style>
  