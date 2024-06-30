<template>
    <div>
      <productsList :category="category"></productsList>
    </div>
  </template>
  
  <script>
  import productsList from '~/components/productsList.vue';
  // const route = useRoute()
  
  export default {
    components: {
        productsList
    },
    data() {
      const route = useRoute();

      return{
      category: route.params.category,

      }
    },
    created() {

    },

}
  </script>

  <!-- <template>
    <div>
      <productsList :category="'all'"></productsList>
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
</script> -->