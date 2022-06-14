<template>
  <div class="grid-container">
    <div class="nav">
      <div id="nav">
        <router-link to="/">Landing</router-link>
      </div>
    </div>
    <div class="title">
      <h1>Tu lista de Items </h1>
      <button @click="buyItems">Comprar</button>
      <div>
      <input name="email" class="email" id="email" placeholder="Introduce aqui tu email y pulsa enter" v-model="this.info.email" v-show="visualizacion" >
      <button v-show="visualizacion" @click="sendInfo()">Recibir email</button>
    </div>
    </div>
    <div class="items">
      
      <div class="container" v-if="isLoading">
        <div class="ring"></div>
      </div>
      <div v-for="(item,index) in items" :key="index" class="item">
        <img src="@/assets/img/pexel.png" alt="" class="image">
        <p>{{item.item_name}}</p>
        <p>{{item.item_description}}</p>
        <button @click="removeItem(item)">Eliminar item</button>
      </div>
    </div>
    
    
  </div>
    
    
</template>

<script>
import { cartItems } from '@/services/shopingCart.js';
import { sendData } from '@/services/api.js';



export default{
    name:"ShopCart",
    data(){
        return{
            items: [],
            numberOfItems : 0,
            visualizacion : false,
            isLoading: false,
            info : {
              allItems: [],
              email : "",
            }
        }
    },
    computed:{
      
    },
    mounted() {
    this.cartItems()
  },
    methods:{
        cartItems(){
         this.items = cartItems()
        },
        removeItem(item){
        this.items.splice(this.items.indexOf(item),1)
        },
        buyItems(){
          this.visualizacion = true

        },
        isValidInfoForm() {
      if (this.info.email === "" ||
          this.info.allItems === ""
      ){
        return false;
      } else {
        return true;
      }
    },
      async sendInfo() {
        this.info.allItems = this.items
      if (!this.isValidInfoForm()) {
        alert("SE DEBE RELLENAR EL EMAIL");
        return;
      }
      this.isLoading= true
      await sendData(this.info);
      this.isLoading = false;
      this.visualizacion = false
    },
        
        
}
}
</script>
<style scoped>
.grid-container{
width: 100vw;
  min-height: 100vh;
  display: grid;
  background: linear-gradient(to bottom, rgb(91, 236, 236), white);
  grid-template-columns: 1fr 1fr 1fr;
  grid-template-rows: 0.4fr 0.5fr 1fr 1fr 0.5fr;
  grid-template-areas:
    "nav nav nav"
    "title title title "
    "items items items "
    "items items items"
    "email-container email-container email-container";
}
.title{
  grid-area: title;
}
.email{
  width: 40%;
  margin-top: 10px;
  height: 1.5em;
  text-align: center;
 
}
.image{
  width: 50%;
  padding-top: 5px;
}
.nav{
  grid-area: nav;
}
.email-container{
  grid-area: email-container;
  width:100%;
  height: 25%;
  
  
}

.items{
  grid-area:items;
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
  justify-content: center;
}
.item{
  width: 20%;
  border: 2px rgb(221, 209, 209) solid;
  background-color: rgb(212, 245, 220);
  flex-direction: row;
  margin: 5px;
}
.container{
  position:fixed;
  width:100%;
  display:flex;
  justify-content: center;
  align-items: center;
}
.container .ring{
  position:relative;
  width:150px;
  height: 150px;
  margin: -30px;
  border-radius:50%;
  border: 4px solid transparent;
  border-top: 4px solid #04115a;
  animation: animate 4s linear infinite;
}
@keyframes animate {
  0%{
      transform: rotate(0deg)
  }
  100%{
      transform: rotate(360deg)
  }
}
.container .ring::before{
  content:"";
  position:absolute;
  top: 12px;
  right: 12px;
  border-radius: 50%;
  width:15px;
  height:15px;
  background: #070136;
  box-shadow: 0 0 0 15px #00000033,
  0 0 0 10px #00000022,
  0 0 0 20px #00000011,
  0 0  20px #000000,
  0 0 50px #000000;
}
</style>