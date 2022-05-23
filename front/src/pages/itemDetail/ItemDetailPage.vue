<template>
<div class="gridContainer">
    <div class="nav">
      <div id="nav">
        <router-link to="/">Landing</router-link>
      </div>
    </div>
    <h1>hola</h1>
    <div v-for="item in items" :key="item.item_id"> 
        <p>{{item.item_id}}</p>
        <p>{{item.item_name}}</p>
        </div>
        </div>

   
</template>
<script>
import { loadItem } from "@/services/api.js";
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
    }

}
</script>