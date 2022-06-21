<template>
<div class="gridContainer">
    <div class="nav">
      <div id="nav">
        <router-link to="/">Landing</router-link>
      </div>
    </div>
    <div class="title">
        <h1>
            Añade aqui tu nuevo item
        </h1>
    </div>
    <div class="main">
        <form class="form">
            <label for="itemName" class="name-label">Nombre: </label>
            <input type="text" placeholder="Ingrese el nombre de su item" id="item_name" v-model="item.item_name">
            <label for="itemDescription" class="description-label">Descripcion: </label>
            <textarea type="text" placeholder="Ingrese una pequeña descripcion de su item" id="item_description" v-model="item.item_description"></textarea>
            <label for="itemCategory" class="category-label">Categoria: </label>
            <input type="text" placeholder="Ingrese la categoria de su item" id="item_category" v-model="item.item_category">
            <button class="submit-button" @click.prevent="addItemFunction()">Añadir item a tu lista de items</button>
        </form>

    </div>
</div>
    
</template>

<script>
import  {addItem} from "@/services/api.js"
import { uuid } from 'vue-uuid'; 

export default {
    name:"adminAddItem",
    data(){
        return{
            item:{
                item_id:uuid.v4(),
                item_name:"",
                item_description:"",
                item_category:"",
            }
        }
    },
    methods:{
        async addItemFunction(){
            await addItem(this.item,this.$route.params.store_id )
        },
    },
}
</script>

<style scoped>
.gridContainer {
  width: 100vw;
  min-height: 100vh;
  align-items: center;
  display: grid;
  background: linear-gradient(to bottom, rgb(78, 214, 112), rgb(151, 236, 155));
  grid-template-columns: 0.6fr 1fr 1fr;
  grid-template-rows: 0.1fr 0.1fr 1fr 1fr 1fr ;
  grid-template-areas:
    "nav nav nav"
    "title title title "
    "main main main "
    "main main main "
    "main main main"
    
}
.main{
    grid-area: main;
}
.nav{
    grid-area:nav;
}
.title{
    grid-area: title;
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
#item_name{
    margin: 1em;
    grid-area: email;
    width: 60%;
    height: 30px;
    align-content: center;
    margin: auto;
}
.description-label{
    margin: 1em;
    grid-area: email-label;
    font-size: large;
    font-weight: bold;
}
#item_description{
    margin: 1em;
    grid-area: email;
    width: 60%;
    height: 40px;
    align-content: center;
    margin: auto;
}
.category-label{
    margin: 1em;
    grid-area: email-label;
    font-size: large;
    font-weight: bold;
}
#item_category{
    
    grid-area: email;
     width: 60%;
  height: 25px;
  align-content: center;
  margin: auto;
}
.submit-button{
    padding: 0.5em;
    margin-top: 1em;
    margin: 1.5em;
    grid-area: submit-button;
    border: 1px solid;
    border-color: #31ac4c;
    transition: all 0.2s ;
}
.submit-button:hover{
  transform: scale(1.02); 
}

</style>