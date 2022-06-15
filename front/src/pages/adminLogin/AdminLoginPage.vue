<template>
    <div class="grid-container">
        <div class="nav">
            <div id="nav">
                <router-link to="/">Landing</router-link>

            </div>
        </div>
        <div class="title">
            <h1>Logeate para acceder al menu usuario de tu tienda</h1>
        </div>
        <div class="main">
            <form class="form">
                <label for="email" class="email-label">Email:</label>
                <input type="text" name="email" id="email" placeholder="Introduce aqui tu email"
                    v-model="this.log.email">
                <label for="phone" class="phone-label">Telefono:</label>
                <input type="text" name="phone" id="phone" placeholder="Introduce aqui tu telefono"
                    v-model="this.log.phone">
                <button type="submit" class="submit-button" @click.prevent="sendInfo()">Admin login</button>
            </form>
        </div>

    </div>

</template>

<script>
import { adminLogin } from '@/services/api.js';

export default {
    name: "adminLogin",
    data() {
        return {
            store_id: JSON.parse(localStorage.getItem('autorizacion')),
            log: {
                email: "",
                phone: ""
            }
        }
    },
    methods: {
        async sendInfo() {
            await adminLogin(this.log)

            this.$router.push("/")
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
    background: linear-gradient(to bottom, rgb(91, 236, 236), white);
    grid-template-columns: 0.6fr 1fr 1fr;
    grid-template-rows: 0.2fr 0.2fr 1fr;
    grid-template-areas:
        "nav nav nav"
        "title title title "
        "main main main "
        "main main main "

}

.nav {
    grid-area: nav;
    margin: auto;
}

.title {
    grid-area: title;
    margin: auto;
}

.main {
    margin-top: 2em;
    margin: auto;
    align-items: center;
    grid-area: main;
    width: 50%;
    background: linear-gradient(to bottom, rgb(78, 214, 112), rgb(151, 236, 155));
    border: 1px solid rgb(71, 156, 45);
}

.form {

    display: flex;
    flex-direction: column;
    margin: 1em;
    /* grid-template-columns: 1fr 1fr 1fr 1fr ;
    grid-template-rows: 0.2fr 0.3fr 1fr 1fr;
    grid-template-areas:
    "email-label email-label email-label email-label"
    "email email email email"
    "phone-label phone-label phone-label phone-label"
    "phone phone phone phone"
    "submit-button submit-button submit-button submit-button"; */
}

.email-label {
    grid-area: email-label;
    margin: 1em;
    font-size: large;
    font-weight: bold;
}

#email {
    margin: 1em;
    grid-area: email;
    width: 60%;
    height: 20px;
    align-content: center;
    margin: auto;
}

.phone-label {
    margin: 1em;
    grid-area: email-label;
    font-size: large;
    font-weight: bold;
}

#phone {
    margin: 1em;
    grid-area: email;
    width: 60%;
    height: 20px;
    align-content: center;
    margin: auto;
}

.submit-button {
    width: 60%;
    height: 20px;
    align-content: center;
    margin: auto;
    margin-top: 2em;
    grid-area: submit-button;
    border: 1px solid;
    border-color: #31ac4c;
    transition: all 0.2s;
}

.submit-button:hover {
    transform: scale(1.02);
}
</style>