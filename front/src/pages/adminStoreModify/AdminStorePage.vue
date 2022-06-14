<template>
<div class="grid-container">
    <div class="nav">
      <div id="nav">
        <router-link to="/">Landing</router-link>
      </div>
    </div>
    
    <div class="main">
        <div class="title">
            <h3>Modifica tu tienda aqui</h3>
        </div>
        <form action="modifyStore" class="form">
            <label for="store_name" class="name-label">Nombre de la tienda: </label>
            <input type="text" name="store_name" id="store_name" v-model="store.store_name">
            <label for="store_description" class="description-label">Descripcion de la tienda: </label>
            <textarea  cols="30" rows="10" type="text-area" name="store_description" id="store_description" v-model="store.store_description"></textarea>
            <label for="store_category" class="category-label">Categoria de la tienda: </label>
            <input type="text" name="store_category" id="store_category" v-model="store.store_category">
            <button class="submit-button" type="submit" @click.prevent="modifyStoreFunction()" >Modificar tienda</button>
        </form>
    </div>
    <div class="goToItem">
            <button class="submit-button-2" @click="goToItems()">Menu de items</button>
    </div>
    
</div>

</template>

<script>
import { loadData,modifyStore } from "@/services/api.js"




export default {
    data(){
        return{
            store:{
                store_name:"",
                store_description:"",
                store_category:"",
            },
        }
    },
    mounted(){
    this.loadData()
    },
    methods:{
        async loadData() {
        let storeId = this.$route.params.store_id;
        console.log(storeId)
        this.store = await loadData(storeId);
        console.log(this.store)
    },
    async modifyStoreFunction(){
        await modifyStore(this.store, this.$route.params.store_id)

    },
    goToItems(){
        this.$router.push("/adminItems/"+ this.$route.params.store_id)
    }

    }

}
</script>
<style scoped>
.grid-container {
  width: 100vw;
  min-height: 100vh;
  align-items: center;
  display: grid;
  background: linear-gradient(to bottom, rgb(78, 214, 112), rgb(151, 236, 155));
  grid-template-columns: 0.6fr 1fr 1fr;
  grid-template-rows: 0.1fr 0.1fr 1fr 1fr 1fr ;
  grid-template-areas:
    "nav nav nav"
    "button button button "
    "main main main "
    "main main main "
    "main main main"
    
}
.title{
    font-family:Verdana, Geneva, Tahoma, sans-serif;
    
    
}
.nav{
     
    grid-area: nav;
    margin-bottom:1em;
}
.title{
    grid-area: title;
    margin: auto;
}
.main{
    margin-top: 0em;
    margin: auto;
    align-items: center;
    grid-area: main;
    width: 50%;
    background: linear-gradient(to bottom, rgb(91, 236, 236), rgb(190, 227, 245));
    border: 1px solid rgb(71, 156, 45);
}
.form{
   
    display: flex;
    flex-direction: column;
    margin: 1em;
    
}
.name-label{
    grid-area: email-label;
    margin: 1em;
    font-size: large;
    font-weight: bold;
}
#store_name{
    margin: 1em;
    grid-area: email;
     width: 60%;
  height: 20px;
  align-content: center;
  margin: auto;
}
.description-label{
    margin: 1em;
    grid-area: email-label;
    font-size: large;
    font-weight: bold;
}
#store_description{
    margin: 1em;
    grid-area: email;
     width: 60%;
  height: 40px;
  align-content: center;
  margin: auto;
}
.goToItem{
grid-area: button;
align-content: center;
display: flex;
}
.category-label{
    margin: 1em;
    grid-area: email-label;
    font-size: large;
    font-weight: bold;
}
#store_category{
    margin: 1em;
    grid-area: email;
     width: 60%;
  height: 25px;
  align-content: center;
  margin: auto;
}

.submit-button{
    margin: 1em;
    grid-area: submit-button;
    border: 1px solid;
    border-color: #31ac4c;
    transition: all 0.2s ;
}
.submit-button:hover{
  transform: scale(1.02); 
}

.submit-button-2{
    font-size: large;
    font-weight: bold;
    width: 50%;
    margin: auto;
    margin-bottom: 2em;
    grid-area: submit-button;
    border: 1px solid;
    border-color: #c05e0f;
    transition: all 0.2s ;
    width: 50%;
}
.submit-button-2:hover{
  transform: scale(1.02); 
}

</style>