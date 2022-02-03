<template>
  <v-app id="inspire">
    <v-app-bar app>
      <v-tabs align-with-title>
        <v-tab @click="getAllCategoryProducts()"> <v-icon> mdi-book-open</v-icon> All </v-tab>
        <v-tab @click="getOneCategoryAndProducts('noodles')" > <v-icon> mdi-noodles</v-icon> Noodles </v-tab>
        <v-tab @click="getOneCategoryAndProducts('rice')"> <v-icon> mdi-rice</v-icon> Rice </v-tab>
        <v-tab @click="getOneCategoryAndProducts('meat')"> <v-icon> mdi-food-drumstick </v-icon> Meat </v-tab>
        <v-tab @click="getOneCategoryAndProducts('drinks')"> <v-icon> mdi-beer </v-icon> Drinks </v-tab>
        <v-tab @click="getOneCategoryAndProducts('desserts')"> <v-icon> mdi-ice-cream </v-icon> Desserts </v-tab>
        <v-tab @click="getHottestProducts()"> <v-icon> mdi-fire </v-icon> Hottest Products </v-tab>

        <v-spacer></v-spacer>

        <v-tab icon> <v-icon>mdi-account </v-icon> Log In </v-tab>
        <v-tab icon> <v-icon>mdi-credit-card-outline </v-icon> Payment </v-tab>
        <v-tab icon @click="drawer = !drawer">
          <v-icon>mdi-cart </v-icon> Cart({{ cart.length}})
        </v-tab>
      </v-tabs>
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" right fixed temporary height="100%">

    </v-navigation-drawer>

    <v-main class="grey lighten-1">
      <v-container class="overflow-x">
        <template v-for="category in CategoryAndProducts">
            <v-col :key="category.id" cols="12" class="black">
              <strong class="white--text">Category: {{ category.name }}</strong>
            </v-col>
          <v-sheet class="mx-auto" elevation="8" max-width="1785">
            <v-slide-group
              class="pa-4"
              active-class="success"
              show-arrows
            >
              <v-slide-item
                v-for="product in category.products"
                :key="product.id"
                v-slot="{ active, toggle }"
              >
              <v-card class="pa-2" outlined tile>
              <div class="box">
                <p class="text-center">
                  {{ product.name }} - {{ product.price }} EUR
                </p>
              </div>
                <img
                  img :src="product.get_thumbnail"
                  class="`rounded-lg`"
                  height="150"
                  width="250"
                >                
                </img>
                <div class="text-center">
                      <v-btn class="mx-2" fab dark small color="primary">
                        <v-icon dark @click="removeItemFromCart(product)"> mdi-minus </v-icon>
                      </v-btn>
                      <v-btn class="mx-2" fab dark small color="indigo">
                        <v-icon dark @click="addItemIntoCart(product)"> mdi-plus </v-icon>
                      </v-btn>
                </div>
              </v-card>
              </v-slide-item>
            </v-slide-group>
          </v-sheet>
        </template>
      </v-container>
    </v-main>
    <v-footer color="primary lighten-1" padless>
      <v-row justify="center" no-gutters>
        <v-col class="black lighten-1 py-4 text-center white--text" cols="12">
          {{ new Date().getFullYear() }} —
          <strong> Minho's Django - Vue project </strong>
        </v-col>
      </v-row>
    </v-footer>
  </v-app>
</template>

<script>
import axios from "axios";

export default {
  name: "inspire",

  data() {
    return {
      CategoryAndProducts: [],
      drawer: null,
      category: 'all',
      cart: [],
    };
  },
  components: { 
  },
  mounted() {
    this.getAllCategoryProducts();
    this.getHottestProducts();
    this.getOneCategoryAndProducts();
  },
  methods: {
    getAllCategoryProducts() {
      axios
        .get("/api/products/all/")
        .then((response) => {
          this.CategoryAndProducts = response.data;        
        })
        .catch((error) => {
        });
    },
    getHottestProducts() {
      axios
        .get("/api/products/hottest-products/")
        .then((response) => {
          this.CategoryAndProducts = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getOneCategoryAndProducts(category){
      axios
        .get(`/api/products/${category}/`)
        .then((response) => {
          this.CategoryAndProducts = response.data;       
        })
        .catch((error) => {
          console.log(error);
        });
    },
    addItemIntoCart(product){
      var i = 0;
      var found = false;
      var dict = {
        "name": product.name,
        "price": product.price,
        "quantity": 1,
      }
      if (this.cart.length == 0){
        this.cart.push(dict)
        found = true
      } 
      while (i < this.cart.length && found == false){
        if (Object.values(this.cart[i]).indexOf(product.name)>-1){
          this.cart[i].quantity = this.cart[i].quantity + 1 
          found = true
        }
        i ++;
      }
      if (found == false) {
        this.cart.push(dict)
      }
    },
    
    removeItemFromCart(product){
      var i = 0;
      var found = false;

      if (this.cart.length == 0) {
        found = true
      }
      while (i < this.cart.length && found == false){
        if ((Object.values(this.cart[i]).indexOf(product.name)>-1) && this.cart[i].quantity > 0){
          this.cart[i].quantity = this.cart[i].quantity - 1 
          found = true
          if (this.cart[i].quantity == 0){
            this.cart.splice(this.cart[i],1)
          }
        } 
        i ++;
      }
      console.log(this.cart)
      
    },

  },
};
</script>

<style>
.image {
  margin-top: -1.25rem;
  margin-left: -1.25rem;
  margin-right: -1.25rem;
  margin-bottom: -1.25rem;
  border: 5px solid black;
}

.figure {
  padding: 20px;
}
</style>
