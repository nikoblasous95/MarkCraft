<template>
<div class="grid-container">
    <div class="nav">
      <div id="nav">
        <router-link to="/">Landing</router-link>
      </div>
    </div>
    <div class="main">
        <div class="title">
            <h1>Menu modificador del item {{item.item_name}}</h1>
        </div>
        <form action="" class="form" >
            <label for="item_name" class="name-label">Nombre del item: </label>
            <input type="text" name="item_name" id="item_name" v-model="item.item_name">
            <label for="item_description" class="description-label">Descripcion del item: </label>
            <textarea type="text" name="item_description" id="item_description" v-model="item.item_description"></textarea>
            <label for="item_category" class="category-label">Categoria del item: </label>
            <input type="text" name="item_category" id="item_category" v-model="item.item_category">
            <button class="submit-button" type="submit" @click.prevent="modifyItemFunction()">Modificar item</button>
        </form>
        
    </div>
    <div class="goToItem">
            <button class="submit-button-2" @click="returnBack()">Volver atras</button>
    </div>
</div>
    
</template>


<script>
import { loadItem,modifyItem } from '@/services/api.js'

export default {
name:"adminItemsModify",
    data(){
        return {
            item:{
                item_name:"",
                item_description:"",
                item_category:"",
            }
        }
    },
    mounted(){
        this.loadItemFunction()
    },
    methods:{
        async loadItemFunction(){
            this.item = await loadItem(this.$route.params.item_id)
            console.log(this.item)
            console.log(this.$route.params.item_id)
        },
        async modifyItemFunction(){
            await modifyItem(this.item,this.$route.params.item_id)
        },
         returnBack(){
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
#item_description{
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
#item_category{
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