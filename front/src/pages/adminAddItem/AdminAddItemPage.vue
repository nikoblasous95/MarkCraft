<template>
    <h1>hello</h1>
    <div class="form-container">
        <form >
            <label for="itemName">Nombre: </label>
            <input type="text" placeholder="Ingrese el nombre de su item" v-model="item.item_name">
            <label for="itemDescription">Descripcion: </label>
            <input type="text" placeholder="Ingrese una pequeña descripcion de su item" v-model="item.item_description">
            <label for="itemCategory">Categoria: </label>
            <input type="text" placeholder="Ingrese la categoria de su item" v-model="item.item_category">
            <button @click.prevent="addItemFunction()">Añadir item a tu lista de items</button>
        </form>

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