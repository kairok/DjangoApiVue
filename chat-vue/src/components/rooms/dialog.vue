<template>
    <mu-col span="8" xl="9" >
        <mu-container class="dialog2">
            <mu-row v-for="dialog in dialogs"
                    direction="column"
                    justify-content="start"
                    align-items="end">
                <p><strong>{{dialog.user.username}}</strong></p>
                <p>{{dialog.text}}</p>
                <span>{{dialog.date}}</span>
            </mu-row>
            </mu-container>
        <mu-container>
            <mu-row  align-items="end">
                <mu-text-field v-model="form.textarea" multi-line :rows="4" full-width
                placeholder="Введите текст"
                ></mu-text-field>
                 <mu-button  class="btnsend" round color="success">Отправить</mu-button>
            </mu-row>
        </mu-container>

    </mu-col>
</template>

<script>
     import $ from 'jquery'


    export default {
        name: "Dialog",
        props: {
            id:'',
        },

        data() {
            return {
                dialogs: '',
                form: {
                    textarea:''
                }
            }
        },
        created() {
             $.ajaxSetup({
                      headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
                  });
          this.loadDialog()
        },
        methods: {
            loadDialog(){
                 $.ajax({
                    url: 'http://127.0.0.1:8000/api/v1/chat/dialog/',
                    type: "GET",
                     data: {
                        room: this.id
                     },
                    success: (responce)=> {
                        this.dialogs = responce.data.data
                        console.log(responce)
                    }
                })
            }
        }
    }
</script>

<style scoped>
     .btnsend {
        margin: 10px 0 0 45px;
    }
    .dialog2 {
        border: 1px solid #000;
    }

</style>
