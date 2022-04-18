<template>
  <v-app>
      <v-app-bar
      app
      color="white"
      flat 
      height="85%"
      >
      <v-container class="py-0 fill-height mt-5 mb-5">
        <v-row >
        <v-img src="./assets/logo_fi.png" style="max-width:65px;"></v-img>
        <h2 class="mt-5 ml-3 app_n" >Workout Planner</h2>
            <v-spacer></v-spacer>

          <v-btn class="mt-5"
          v-for="link in links"
              :key="link" 
              text
              @click="page = link"
              >
              <router-link class="black--text" :to="'/' + link">{{ link }}</router-link>
            </v-btn>
            
          <v-avatar
          class="mr-10 mt-5 ml-5"
          color="cyan darken-1"
          size="32"
          >
          <v-btn id="no-background-hover" icon rounded elevation="0" to="/" color="white" >
            <v-icon dark>
              mdi-account-circle
            </v-icon>
          </v-btn>
        </v-avatar>
            

          </v-row>
        </v-container>
      </v-app-bar>
    <v-img src="./assets/gym.jpg">
    
    <router-view>
    </router-view>
 
  </v-img>
  </v-app>

</template>

<script>
 export default {
    data() {
      return {
        page:"home",
        links: [
          'Calendar',
          'Reminders',
          'Recommended',
          'Social',
          'Calculators'
          ],
      }
    }
 }
</script>
<style>
@import url("https://fonts.googleapis.com/css?family=Questrial");
 a{
  text-decoration:none;    
  color:black;
 }
 no-background-hover::before {
   background-color: transparent !important;
}

  .app_n{
    font-family: "Questrial";
  }
 </style>