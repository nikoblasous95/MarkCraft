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
    <h1>hola</h1>
    <div v-for="item in items" :key="item.item_id"> 
        <p>{{item.item_id}}</p>
        <p>{{item.item_name}}</p>
        <p>{{item.item_description}}</p>
        <button @click="addItem(item)">Añadir al carrito</button>
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
            items : [{}],
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
        let itemId = this.$route.params.id;
        console.log(itemId)
        this.items = await loadItem(itemId);
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