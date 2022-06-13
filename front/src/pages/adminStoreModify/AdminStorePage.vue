<template>
<h1>hello
    
</h1>
    <form action="">
        <label for="store_name">Nombre de la tienda: </label>
        <input type="text" name="store_name" id="store_name" v-model="store.store_name">
        <label for="store_description">Descripcion de la tienda: </label>
        <input type="text" name="store_description" id="store_description" v-model="store.store_description">
        <label for="store_category">Categoria de la tienda: </label>
        <input type="text" name="store_category" id="store_category" v-model="store.store_category">
        <button type="submit" @click.prevent="modifyStoreFunction()" >Modificar tienda</button>
    </form>
    <button @click="goToItems()">Menu de items</button>
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