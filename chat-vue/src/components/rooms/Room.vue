<template>
    <mu-col span="4" xl="2" class="room-list">
        <!--${{rooms}}-->
        <div v-for="room in rooms">
                    <h3 @click="openDialog(room.id)">{{room.creater.username}}</h3>
            <small>{{room.date}}</small>

        </div>

    </mu-col>
</template>

<script>
      import $ from 'jquery'


    export default {
        name: "Room",
        data() {
            return {
                rooms: '',
            }
        },

        created(){
                $.ajaxSetup({
                      headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
                  });
                this.loadRoom()
        },
        methods: {
            loadRoom(){
                $.ajax({
                    url: 'http://127.0.0.1:8000/api/v1/chat/room/',
                    type: "GET",
                    success: (responce)=> {
                        this.rooms = responce.data.data
                     //   console.log(responce)
                    }
                })
            },
             openDialog(id) {
                this.$emit("openDialog", id)
              //  console.log(id)
            }

        },
    }
</script>

<style scoped>

    .room-list {
        margin: 0 10px 0 0 ;
        box-shadow: 1px 4px 5px #cccccc;
    }

</style>
