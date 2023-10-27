<template>
    <div>
      <productsList :category="'Golf'"></productsList>
    </div>
    
</template>

<script>
import productsList from '../../components/productsList.vue';

export default {
    components: {
        productsList
    },

    data() {
    return {
      products: []
    };
  },
}
</script>