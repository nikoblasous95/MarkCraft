<template>
    <h1>
        hello
    </h1>
    <form action="">
        <label for="item_name">Nombre del item: </label>
        <input type="text" name="item_name" id="item_name" v-model="item.item_name">
        <label for="item_description">Descripcion del item: </label>
        <input type="text" name="item_description" id="item_description" v-model="item.item_description">
        <label for="item_category">Categoria del item: </label>
        <input type="text" name="item_category" id="item_category" v-model="item.item_category">
        <button type="submit" @click.prevent="modifyItemFunction()">Modificar item</button>
    </form>
        <button @click="returnBack()">Volver atras</button>
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