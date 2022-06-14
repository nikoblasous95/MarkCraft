<template>
<div class="gridContainer">
    <div class="nav">
      <div id="nav">
        <router-link to="/">Landing</router-link>
      </div>
    </div>
    <div class="shop">
        <button class="shopButton" @click=" openShopCart()">
          🛒
        </button>
        <button @click="adminMenu()" v-if="autorization">Herramienta</button>
      </div>
    <div class="filters">
      <input class="inputFilter" type="text" placeholder="Escribe aqui tu busqueda" v-model="filterBySearch">
    </div>
    <div class="image">
     <img src="@/assets/img/bilbo.png" alt="logo prueba">
    </div>
    <div class="main">
      <div class="store">
        <h1>{{store.store_name}}</h1>
        <h4>{{store.store_description}}</h4>
        <div class="items">
        <div  class="item" v-for=" (item,index) in filteredItems || []" :key="index">
          <div @click="openItemDetail(item)">
            <img class="itemImage" src="@/assets/img/pexel.png" alt="imagen prueba"> 
            <p>{{item.item_name}}</p>
            <p>{{item.item_description}}</p>
            <p>{{item.item_category}}</p>
           </div>
          <div>
            <button @click="addItem(item)">añadir al carrito</button>
          </div>

          
          </div>
          </div>
        </div>
    </div>
  
  </div>
</template>

<script>
import { loadData } from "@/services/api.js";
import {addItemToCart} from "@/services/shopingCart.js";
export default {
  name: "storeDetail",
  data() {
    return {
      store:{},
      filterBySearch:"",
      autorization:false,
    };
  },
    created() {
      this.loadData();
      
    },
    mounted(){
    this.autorizationFunction()
    },
  computed: {
    filteredItems(){
      let result = []
      let store = this.store
      for (let item of store.items){
        console.log(item)
        if (this.isStoreInFilter(item)){
          result.push(item)
        }
      }
      return result
    }
  },
  methods: {
    async loadData() {
      let storeId = this.$route.params.id;
      this.store = await loadData(storeId);
    },
    openItemDetail(item) {
      console.log(item)
      this.$router.push("/storeDetail/"+ this.$route.params.id +"/"+ item.item_id);
    },
    autorizationFunction(){
      let getLocalStorage =  JSON.parse(localStorage.getItem('autorizacion'))
      let autorizacion = getLocalStorage.store_id
      
      console.log(this.store.store_id)
      if (autorizacion == this.store.store_id){
        this.autorization = true
      }
    },
    addItem(item){
      addItemToCart(item)
      
    },
    isStoreInFilter(item){
      let seller =item.item_name.toLowerCase()
      console.log(seller)
      // let description = item.item_description.toLowerCase()
      // let itemCategory = item.item_category.toLowerCase()

      if (this.filterBySearch === ""){
        return true
      }
      if (seller.includes(this.filterBySearch)){
        return true
      }
      else {
        return false
      }
    },
     openShopCart() {
      this.$router.push("/shopCart");
    },
    adminMenu(){
      this.$router.push("/adminStore/" + this.store.store_id );
    }

   
  },
};
</script>
<style scoped>
.items{
 
  width: 100%;
  height: 100%;
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
  justify-content: center;
}
.itemImage{
  width: 40%;
  height: 40%;
}
.image{
  grid-area: image;
  width: 100%;
  height: 100%;
 
}
.inputFilter{
  width: 60%;
  height: 25px;
  align-content: center;
}
.main{
  grid-area: main;
  padding: 0;
  margin: 0;
 
}
.filters{
  grid-area: filters;
  width: 100%;
  height: 100%;
  /* background-color: rgb(208, 245, 245); */
  padding-top: 2em;
}
.shop{
  grid-area: shop;
 padding-top: 2em;
 
}
.shopButton{
  align-content: center;
  width: 30%;
  height: 30px;
  
}
.gridContainer{
  width: 100vw;
  min-height: 100vh;
  display: grid;
  background: linear-gradient(to bottom, rgb(91, 236, 236), white);
  grid-template-columns: 0.5fr 0.5fr 1fr 1fr;
  grid-template-rows: 0.2fr 0.3fr 1fr 1fr;
  grid-template-areas:
    "nav nav nav nav"
    "filters filters filters shop"
    "image main main main "
    "image main main main "
    "image main main main";
}
.nav {
  grid-area: nav;
 
  width: 100%;
  height: 100%;
}
.item{
  padding-top: 5px;
  width: 20%;
  background-color: rgb(255, 255, 255);
  flex-direction: row;
  margin: 5px;
}
.store{
  margin: 0px;
  padding: 0;
  width: 100%;
  
}
 

</style>