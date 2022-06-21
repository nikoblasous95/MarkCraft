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
    </div>
    <div class="image">
      <img class="itemImage" src="@/assets/img/pexel.png" alt="imagen prueba"> 
    </div>
      <div class="main">
       <div class="item-title">
            <h2>{{item.item_name}}</h2>
          </div>
        <div class="item">
          <p>{{item.item_id}}</p>
          <p>{{item.item_description}}</p>
          <p>{{item.item_category}}</p>
          <button @click="addItem(item)">Añadir al carrito</button>
        </div>
        
      </div>
       
      
      
       
    
</div>

   
</template>
<script>
import { loadItem } from "@/services/api.js";
import { addItemToCart } from "@/services/shopingCart.js";
export default{
    name:"ItemDetail",
    data(){
        return {
            item : {},
            itemId : this.$route.params.id,
        };
    },
    mounted(){
        this.loadItems()
    },
    computed:{
        
    },
    methods:{
    async loadItems() {
        let itemId = this.$route.params.item_id;
        console.log(itemId)
        this.item = await loadItem(itemId);
        
    },
    addItem(item){
        console.log(item)
        addItemToCart(item)
    },
    openShopCart() {
      this.$router.push("/shopCart");
    },
   
    }

}
</script>

<style scoped>
.gridContainer{
  width: 100vw;
  min-height: 100vh;
  display: grid;
  background: linear-gradient(to bottom, rgb(91, 236, 236), white);
  grid-template-columns: 0.5fr 0.5fr 1fr 1fr;
  grid-template-rows: 0.2fr 0.3fr 1fr 1fr;
  grid-template-areas:
    "nav nav nav nav"
    "shop shop shop shop"
    "image image main main "
    "image image main main "
    "image image main main";
}
.nav {
  grid-area: nav;
 
  width: 100%;
  height: 100%;
}
.shop{
  grid-area: shop;
  display: flex;
  margin-top: 2em;
  
}
.main{
  grid-area: main;
  padding: 0;
  margin: auto;
  align-items: auto;
 
}
.shopButton{
  align-content: center;
  width: 20%;
  height: 30px;
  margin:auto;
  border: 1px solid;
  border-color: #31ac4c;
   transition: all 0.2s ;
}
.shopButton:hover{
  transform: scale(1.05); 
}
.image{
  grid-area: image;
  margin:2em;
  width: 100%;
  height: 75%;
}
.item-title{
  align-content: center;
}
.itemImage{
  width: 100%;
  height: 100%;
  margin: auto;
}
.item{
  padding: 1.5em;
  border: 2px black solid;
  width: 100%;
  background: linear-gradient(to bottom, #46db66, rgb(161, 252, 173));
  margin: 5px;
    
}


</style>