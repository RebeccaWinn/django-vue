<template>
  <v-container style="margin-top:100px"> 

          <v-row>
            <template>
              <v-col v-for="item in items"
                :key="item.id"
                cols="6"
                md="4"

              >
              <v-card
                
                class="mx-auto"
                max-width="500"
              >
              <a :href="item.link" target="_blank">
                <v-img
                  src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
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

    }),
    created(){
      this.getItems()
    },
    methods:{
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
        this.items = items
      }
    }
  }


</script>