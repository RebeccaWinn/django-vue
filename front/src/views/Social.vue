<template>
    <v-container class="app_n" style="margin-top:100px"> 
      
        <v-dialog
            v-model="dialog"
            persistent
            max-width="600px"
        >
            <template v-slot:activator="{ on, attrs }">
              <v-card class="pt-4 mb-4">
                <h2  class="text-center">Social Page</h2>
                <v-btn
                color="primary"
                dark
                v-bind="attrs"
                v-on="on"
                class="ml-4 mb-2"
                >
                Add Post
                </v-btn>
            </v-card>
            </template>
            <v-card>
            
                <v-card-title>
                <span class="text-h5">Add Post</span> 
                </v-card-title>
                <v-card-text>
                <v-container>
                    <v-row>
                    <v-col cols="12">
                        <v-text-field
                            label="title*"
                            v-model="new_title"
                            required
                        >
                        </v-text-field>
                    </v-col>
                    <v-col cols="12">
                        <v-textarea
                        outlined
                        label="description*"
                        v-model="new_description"
                        required
                        ></v-textarea>
                    </v-col>
                    </v-row>
                </v-container>
                <small>*indicates required field</small>
                </v-card-text>
                <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                    color="blue darken-1"
                    text
                    @click="dialog = false"
                >
                    Close
                </v-btn>
                <v-btn v-if="update==true"
                    color="blue darken-1"
                    text
                    @click="updatePost(id);dialog = false; update=false;;"
                >
                    Save
                </v-btn>
                <v-btn v-if="update==false"
                    color="blue darken-1"
                    text
                    @click="addPost();dialog = false;"
                >
                    Save
                </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
          <v-row>
            <template>
              <v-col v-for="post in posts"
                :key="post.id"
                cols="6"
                md="4"
              >
              <v-card
                class=" pa-4"
                width="500"
                >
                <v-row>
                    <div class="ma-2">
                        <v-row class="pl-2 mt-2" >
                       <v-avatar
    
                            color="indigo"
                            size="32"
                            >
                        <v-btn id="no-background-hover" icon rounded elevation="0" to="/" color="white" >
                            <v-icon dark>
                            mdi-account-circle
                            </v-icon>
                        </v-btn>
                        </v-avatar>
                        <p class="ml-3 mt-1"> User Name</p>
                        </v-row>
                        <v-card-title class="mt-1 mb-5"> {{post.title}}</v-card-title>
                        <v-card-subtitle style="font-size:15px;">{{post.description}}</v-card-subtitle>
                    </div>
                    <v-spacer></v-spacer>
                    <v-btn icon @click= "update = true; id = post.id; new_title = post.title; new_description = post.description ; dialog = true;">
                        <v-icon>mdi-pencil</v-icon>
                    </v-btn>

                    <v-btn icon>
                        <v-icon @click="deletePost(post.id);">mdi-delete</v-icon>
                    </v-btn>
                </v-row>
              </v-card>
            </v-col>
            </template>
          </v-row>
    </v-container>

</template>

<script>
    import{ getAPI } from '../axios-api'
    export default {
        data: () => ({
          new_title:"",
          new_description:"",
          updated_title:"",
          updated_description:"",
          posts:[],
          update:false,
          dialog:false,
          APIData:[],
          id:""

        }),
        created(){
            this.getPosts()
        },
        methods:{
            getPosts(){
                const posts = [];
                getAPI.get('/posts/')
                .then(response =>{
                    console.log("recieved posts data")
                    this.APIData = response.data
                    console.log(this.APIData.data)
                    for(let i = 0; i < this.APIData.data.length; i++){
                        posts.push({
                            id:this.APIData.data[i].id,
                            title:this.APIData.data[i].title,
                            description: this.APIData.data[i].description
                        })
                    }
                    this.posts = posts
                }).catch(error =>{
                    console.log(error)
                })
            },
            addPost(){
                getAPI.post('/posts/',{
                        title: this.new_title,
                        description: this.new_description,
                    }).then(response => {
                        this.getPosts();
                        console.log(response)
                    }).catch(error => {
                        console.log(error)
                    })
                    this.new_title=""
                    this.new_description=""

            },
            deletePost(id){
                getAPI.delete('/posts/'+id)
                        .then(response => {
                            console.log(response);
                            this.getPosts();
                        })
                        .catch(function (error) {
                            console.log(error.response)
                        })
            },
        
            updatePost(id){
                getAPI.patch('/posts/'+id,{
                        title: this.new_title,
                        description: this.new_description,
                        }).then(response => {
                            this.getPosts();
                            console.log(id)
                            console.log(response);
                        }).catch(function (error) {
                            console.log(error.response)
                        })
                        this.new_title = ""
                        this.new_description = ""

            }
        }

    }
</script>
<style>
@import url("https://fonts.googleapis.com/css?family=Questrial");

  .app_n{
    font-family: "Questrial";
  }
 </style>