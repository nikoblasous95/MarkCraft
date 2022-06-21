<template>
<div  class="gridContainer">
    <div class="nav">
      <div id="nav">
        <router-link to="/">Landing</router-link>
      </div>
    </div>
    <div class="title">
        <h1>
            Menu de items de {{store.store_name}}
        </h1>
    </div>
    <div class="addButton">
        <button @click="goToAddItem()" class="button">Añadir item</button>
    </div>
    <div class="main">
        <div class="item" v-for="item in store.items" :key="item.item_id">
            <p>{{item.item_id}}</p>
            <p>{{item.item_name}}</p>
            <p>{{item.item_description}}</p>
            <p>{{item.item_category}}</p>
            <button @click="modifyItem(item.item_id)">Modificar item</button>
        </div>
    </div>
    
    
</div>
    
</template>

<script>
import { loadData } from "@/services/api.js";
export default {
    data(){
        return{
            store:{
                
            },
        }
    },
    mounted(){
        this.loadData()
    },
    methods:{
        async loadData(){
            this.store = await loadData(this.$route.params.store_id )
            
        },
        modifyItem(item){
            this.$router.push("/adminItems/"+ this.$route.params.store_id + "/" + item)
        },
        goToAddItem(){
            this.$router.push("/adminAddItems/"+ this.$route.params.store_id )
        }


    }
}
</script>

<style scoped>
.gridContainer{
  width: 100vw;
  min-height: 100vh;
  display: grid;
  background: linear-gradient(to bottom, rgb(78, 214, 112), rgb(151, 236, 155));
  grid-template-columns: 0.5fr 0.5fr 1fr 1fr;
  grid-template-rows: 0.2fr 0.2fr 0.2fr 1fr 1fr;
  grid-template-areas:
    "nav nav nav nav"
    "title title title title"
    "button button button button"
    "main main main main "
    "main main main main";
}
.main{
    grid-area: main;
    display: flex;
    flex-direction: row;
    margin: auto;
}
.store-name{
    grid-area: store-name;
}
.title{
    grid-area: title;
}
.nav{
    grid-area: nav;
}
.addButton{
    grid-area: button;
}
.button{
    align-content: center;
  width: 20%;
  height: 30px;
  margin-top:2em;
  border: 1px solid;
  border-color: #31ac4c;
   transition: all 0.2s ;
}
.button:hover{
     transform: scale(1.05); 
}
.item{
    background: linear-gradient(to bottom, rgb(91, 236, 236), rgb(190, 227, 245));
    margin: 3em;
    padding: 1em;
    border: 2px black solid;
}

</style>