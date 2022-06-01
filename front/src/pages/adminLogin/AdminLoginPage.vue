<template>
    <h1>hello</h1>
    <form>
        <label for="email">Email</label>
        <input type="text" name="email" id="email" placeholder="Introduce aqui tu email" v-model="this.log.email">
        <label for="phone">Telefono</label>
        <input type="text" name="phone" id="phone" placeholder="Introduce aqui tu telefono" v-model="this.log.phone">
        <button type="submit" @click.prevent="sendInfo()">Admin login</button>
    </form>
</template>

<script>
import { adminLogin } from '@/services/api.js';

export default {
    name:"adminLogin",
    data(){
        return{
            store_id: JSON.parse(localStorage.getItem('autorizacion')) ,
            log:{
                email:"",
                phone:""
            }
        }
    },
    methods:{
        async sendInfo(){
            await adminLogin(this.log)
            
            this.$router.push("/")
        }
    }
}
</script>
