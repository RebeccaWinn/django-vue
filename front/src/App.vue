<template>
  <v-app>
      <v-app-bar
      app
      color="white"
      flat 
      >
      <v-container class="py-0 fill-height mt-8 mb-8">
        <v-row>
          <v-avatar
          class="mr-10"
          color="indigo"
          size="32"
          >
          <v-btn id="no-background-hover" icon rounded elevation="0" to="/" color="white" >
            <v-icon dark>
              mdi-account-circle
            </v-icon>
          </v-btn>
        </v-avatar>

          <v-btn
          v-for="link in links"
              :key="link"
              text
              @click="page = link"
              >
              <router-link class="black--text" :to="'/' + link">{{ link }}</router-link>
            </v-btn>
            
            <v-spacer></v-spacer>
            
            <v-responsive max-width="260">
              <v-text-field
              dense
              flat
              hide-details
              rounded
              solo-inverted
              ></v-text-field>
            </v-responsive>
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
 a{
  text-decoration:none;    
  color:black;
 }
 no-background-hover::before {
   background-color: transparent !important;
}
 </style>