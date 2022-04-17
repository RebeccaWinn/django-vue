<template>
  <v-container class="app_n" style="margin-top:70px"> 

  <v-card class="pt-4 pb-0">
  <h2 class="text-center mb-4">Recommended Workouts and Tips</h2>
        <v-select
          v-model="selectedCategories"
          :items="categories"
          @change="sortCategories"
          label="Categories"
          dense
          filled
        ></v-select>
    
    </v-card>
    <v-row>
       <v-card
          width="65%"
          class="mx-auto mt-5"
  
        >
      <template >
        <v-col v-for="item in categoryItems"
          :key="item.id"
          class="mt-3 pb-0"
        >

        <a :href="item.link" target="_blank" style="decoration: none;color:black;">

          <h3>
          {{item.title}}
          </h3>
        </a>
        <v-divider class="mt-2 mb-2"></v-divider>
          </v-col>
      </template>
        </v-card>
    </v-row>
  </v-container>
</template>

<script>
  import { getAPI } from '../axios-api'
  export default{
    data:() => ({
      APIData:"",
      items:[],
      title:"",
      categories:['arms','abs','shoulders','legs','back','chest','full-body','tips'],
      selectedCategories:[],
      categoryItems:[],

    }),
    created(){
      this.getItems()
    },
    methods:{
      sortCategories(){
        if(this.selectedCategories.length == 0){
          this.categoryItems = this.items
        }
        else{ 
          this.categoryItems = []
          for(var i = 0; i < this.items.length; i++){
            if(this.selectedCategories.includes(this.items[i].category)){
              this.categoryItems.push(this.items[i])
            }
          }
        }
      },


      getItems(){
        const items = []
        getAPI.get('/scraping/')
        .then(response => {
          console.log('APi data recieved')
          this.APIData = response.data.data
          console.log(this.APIData)
          for (let i = 0; i < this.APIData.length;i++){
            this.title = this.APIData[i].title.replace(/^\[(.+)\]$/,'$1'),
            this.title= this.title.replace(/['"]+/g, '')
            items.push({
              title:this.title,
              link:this.APIData[i].link,
              category:this.APIData[i].category,
              img:this.APIData[i].img,
            })
          }
        })
        .catch(error =>{
          console.log(error)
        })
        this.categoryItems = items
        this.items = items
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