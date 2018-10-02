<template>
    <div>
        <input v-model="login" type="text" placeholder="Login"/>
        <input v-model="password" type="password" placeholder="Password"/>
        <button @click="setLogin">Enter</button>
        <br>
        <!--{{login}} - {{password}}-->
    </div>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Login",
        data() {
            return {
                login: '',
                password: '',
            }
        },
        methods:{
            setLogin(){
                $.ajax({
                    url:'http://127.0.0.1:8000/auth/token/create',
                    type:"POST",
                    data:{
                      username: this.login,
                      password: this.password
                    },
                    success: (responce) => {
                        console.log(responce.data.attributes.auth_token)
                        alert('Thanks for registry!')
                        sessionStorage.setItem("auth_token",responce.data.attributes.auth_token)
                       // console.log(responce)
                        this.$router.push({name:'home'})
                    },
                    error:(responce) =>{
                        if (responce.status == 400){
                            alert('Login or password not correct!')
                        }
                       // console.log(responce)
                    }
                })
            },
        }
    }
</script>

<style scoped>

</style>
