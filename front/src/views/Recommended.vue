<template>
  <v-container style="margin-top:70px"> 

  <v-card class="pt-4 pb-0">
  <h2 class="text-center">Recommended Workouts and Tips</h2>

      <v-col
        cols="12"
        sm="12"
      >
        <v-select
          v-model="selectedCategories"
          :items="categories"
          @change="sortCategories"
          label="Categories"
          multiple
          outlined
        ></v-select>

      </v-col>
    </v-card>
    <v-row>
      <template >
        <v-col v-for="item in categoryItems"
          :key="item.id"
          cols="6"
          md="4"
          class="mt-5 pb-0"

        >
        <v-card
          
          class="mx-auto"
          max-width="500"
        >
        <a :href="item.link" target="_blank">
          <v-img
            src="../assets/gym2.jpg"
            height="200px"
          ></v-img>

          <v-card-title>
          {{item.title}}
          </v-card-title>
        </a>
        </v-card>
          </v-col>
      </template>
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
      categories:['arms','abs','shoulders'],
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