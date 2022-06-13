<template>
    <h1>
        hello
    </h1>
    <div>
        <p>{{store.store_name}}</p>
        <div class="item" v-for="item in store.items" :key="item.item_id">
            <p>{{item.item_name}}</p>
            <p>{{item.item_description}}</p>
            <p>{{item.item_category}}</p>
            <button @click="modifyItem()">Modificar item</button>
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
            console.log(this.store)
        },
        modifyItem(){
            this.$route.push("/")
        }
    }
}
</script>

<style scoped>
.item{
    border: 2px black solid;
}
</style>