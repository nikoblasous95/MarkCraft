<template>
  <div class="grid-container">
    <div class="nav">
      <div id="nav">
        <router-link to="/">Landing</router-link>
        
      </div>
    </div>
    <div class="filters">
      <input  class="inputFilter" name="filterBySearch" v-model="filterBySearch" placeholder="Escribe aqui tu busqueda">
      
      </div>
    <div class="landing">
      <div class="stores" v-for="store in filteredStores" :key="store.store_id" >
        <div class="store" @click="openStoreDetail(store)">
          <img src="@/assets/img/logo.png" alt="Foto prueba" class="image" />
          
          <p>{{ store.store_name }}</p>
          <p>{{ store.store_description }}</p>
          <p>{{ store.seller_name }}</p>
          <p v-for="item in store.items" :key="item.item_id">
          <ul class="itemsCategory">
            <li>{{ item.item_category }}</li>
          </ul>
          
          </p>
          
        </div>
      </div>
    </div>

    
    <div class="footer"></div>
  </div>
</template>

<script>


export default {
  name: "landing",
  data() {
    return {
      storesList: [],
      categorySelector: "",
      filterBySearch:"",
    };
  },
  mounted() {
    this.loadData();
  },
  computed: {
    filteredStores(){
      let result = []
      for (let store of this.storesList){
        if (this.isStoreInFilter(store)){
          result.push(store)
        }
      }
      return result
    }
  },
  methods: {
    async loadData() {
      const settings = {
        methods: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      };
      let endpoint = "http://localhost:5000/api/stores";
      let response = await fetch(endpoint, settings);
      let loadData = await response.json();
      this.storesList = loadData;
    },
    openStoreDetail(store) {
      this.$router.push("/storeDetail/" + store.store_id);
    },
    itemFilter(store){
      for (let item of store.items){
        return item.item_category.toLowerCase()
      }
    },
    isStoreInFilter(store){
      let categoria = store.store_category.toLowerCase()
      let seller = store.seller_name.toLowerCase()
      let description = store.store_description.toLowerCase()
      let itemCategory = this.itemFilter(store)

      if (this.filterBySearch === ""){
        return true
      }
      if (categoria.includes(this.filterBySearch) ||
       seller.includes(this.filterBySearch) ||
       description.includes(this.filterBySearch)||
       itemCategory.includes(this.filterBySearch)){
        return true
      }
      else {
        return false
      }
    }
  },
};
</script>

<style scoped>
.stores {
  width: 20%;
  border: 2px rgb(221, 209, 209) solid;
  background-color: rgb(212, 245, 220);
  flex-direction: row;
  margin: 5px;
}


.image {
  width: 40%;
}
.grid-container {
  width: 100vw;
  min-height: 100vh;
  display: grid;
  background: linear-gradient(to bottom, rgb(91, 236, 236), white);
 grid-template-columns: 0.6fr 1fr 1fr;
  grid-template-rows: 0.2fr 0.3fr 1fr 1fr;
  grid-template-areas:
    "nav nav nav"
    "filters filters filters "
    "main main main "
    "main main main "
    "main main main";
}
.inputFilter{
  width: 40%;
  height: 25px;
  align-content: center;
}
.store p {
  padding: 0%;
  margin: 5%;
}
.filters{
  grid-area: filters;
  width: 100%;
  height: 100%;
  /* background-color: rgb(208, 245, 245); */
  padding-top: 2em;
}


.nav {
  grid-area: nav;
  /* background-color: rgb(197, 223, 224); */
  width: 100%;
  height: 100%;
}
.landing {
  grid-area: main;
  /* background-color: rgb(217, 255, 255); */
  width: 100%;
  width: 100%;
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
  justify-content: center;
  color: #153266;
  
}
.menu {
  grid-area: sidebar;
  background-color: rgb(208, 245, 245);
  width: 100%;
  height: 100%;
  padding-top: 20%;
}
.footer {
  grid-area: footer;
  background-color: rgb(208, 245, 245);
  width: 100%;
  height: 100%;
}

</style>