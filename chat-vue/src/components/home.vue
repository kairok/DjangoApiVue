<template>
    <mu-container>
        <mu-appbar style="width: 100%;" color="primary">

            Chat vue!
            <mu-button v-if="!auth" @click="gotLogin"  flat slot="right">Enter</mu-button>
            <mu-button v-else @click="logout"  flat slot="right">Exit</mu-button>

        </mu-appbar>
        <mu-row>
                <h1></h1>

        </mu-row>
        <mu-row>
                <room v-if="auth" @openDialog="openDialog"></room>
                 <Dialog v-if="dialog.show" :id="dialog.id"></Dialog>
        </mu-row>

    </mu-container>
</template>

<script>
    import Room from '@/components/rooms/Room'
     import Dialog from '@/components/rooms/dialog'

    export default {
        name: "home",
        components: {
            Room,
            Dialog
        },
        data() {
          return {
              rooms:'',
              dialog: {
                  id: '',
                  show: false
              }
          }
        },
        computed: {
          auth() {
              if (sessionStorage.getItem("auth_token"))  {
                  return true
              }
          }
        },
        methods: {
          gotLogin(){
              this.$router.push({name:"Login"})
          },
            logout(){
              sessionStorage.removeItem('auth_token')
                window.location='/'
            },
            openDialog(id){
                this.dialog.id = id
                this.dialog.show = true
            }
        },

    }
</script>

<style scoped>

</style>
