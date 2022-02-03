<template>
  <v-app id="inspire">
    <v-app-bar app>
      <v-tabs align-with-title>
        <v-tab @click="getCategoryAndProducts()"> <v-icon> mdi-book-open</v-icon> All </v-tab>
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
          <v-icon>mdi-cart </v-icon> Cart
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
                        <v-icon dark> mdi-minus </v-icon>
                      </v-btn>
                      <v-btn class="mx-2" fab dark small color="indigo">
                        <v-icon dark> mdi-plus </v-icon>
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
      responseList: [],
      CategoryAndProducts: [],
      OneCategoryAndProducts: [],
      drawer: null,
      category: 'all',
    };
  },
  components: { 
  },
  mounted() {
    this.getCategoryAndProducts();
    this.getHottestProducts();
    this.getOneCategoryAndProducts();
  },
  methods: {
    getCategoryAndProducts() {
      axios
        .get("/api/products/all/")
        .then((response) => {
          this.CategoryAndProducts = response.data;        
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getHottestProducts() {
      axios
        .get("/api/products/hottest-products/")
        .then((response) => {
          this.CategoryAndProducts = response.data;
        console.log(response.data)
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
