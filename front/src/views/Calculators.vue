<template>
<v-container class="app_n" style="margin-top:140px">
<v-row>
 
  
  <v-card  width="850" class="pa-5 mx-auto">
  <h2 class="text-center">Macro Calculator</h2>
  <v-form
    ref="form"
  >
  <v-card-title>Maintenance Calories</v-card-title>
    <v-col
      class="d-flex"
      cols="12"
      sm="12">
      <v-select
        :items="activity"
        label="Activity"
        item-text="title"
        v-model="activity_selected"
      ></v-select>
    </v-col>
    <v-text-field
      class="ml-4"
      v-model="macro_weight"
      label="Weight (in lbs)"
      required
    ></v-text-field>
    <v-card-text>{{kinobody_formula + " calories"}}</v-card-text>
    <v-card-title>Set goal</v-card-title>
    <v-col
      class="d-flex"
      cols="12"
      sm="12">
      <v-select
        :items="goals"
        label="Goals"
        item-text="title"
        v-model="goal_selected"
      ></v-select>
    </v-col>
    <v-card-text>{{kinobody_formula + " calories (maintenance)"}}</v-card-text>
    <v-card-text > {{cal_cut  + " calories (cut)"}}</v-card-text>
    <v-card-title>Calculated Macros</v-card-title>
    <v-col
      class="d-flex"
      cols="12"
      sm="12">
      <v-select
        :items="macros_split"
        label="Macros split"
        item-text="name"
        v-model="macros_selected"
      ></v-select>
    </v-col>
    <v-template  > 
      <h4 class="pl-4">Protein</h4><v-card-text v-model="protein">{{protein + " grams"}}</v-card-text> 
      <h4 class="pl-4">Fats</h4> <v-card-text v-model="fats">{{fats + " grams"}}</v-card-text>
      <h4 class="pl-4">Carbs </h4> <v-card-text v-model="carbs">{{carbs + " grams"}}</v-card-text>
    </v-template>
    <v-btn class="mt-5 mb-5" @click="calculate_macros()">Calculate</v-btn>
  </v-form>
  
  </v-card>
    <v-card width="250" height="100%" class="ml-4 pa-5 mx-auto">
      <v-card-title>BMI Calculator</v-card-title>
      <v-form
        ref="form"
      >
        <v-text-field
          v-model="weight"
          label="Weight (in lbs)"
          required
        ></v-text-field>

        <v-text-field
          v-model="height"
          label="Height (in inches)"
          required
        ></v-text-field>
        <input type="text" max-height="200" v-model="result"/><br>
        <v-btn class="mt-5 mb-5" @click="calculate()">Calculate</v-btn>
      </v-form>
      </v-card>
      <v-spacer></v-spacer>
    </v-row>
  </v-container>
</template>
<script>
  export default {
    data: () => ({
        weight: '',
        height: '',
        result:0,
        macros_split:[
          {
            name: '20% fats', 
            fat: 0.2

          },
          {
            name: '25% fats (default)', 
            fat: 0.25, 

          }, 
          {
            name: '30% fats', 
            fat: 0.30

          },
          {
            name: '(p: 35%, f: 30%, c: 35%)', 
            fat: 0.30
          },
          {
            name: '(p: 35%, f: 25%, c: 40%)', 
            fat: 0.30
          }
        ],
        goals:[ 
              {
                title:'Light Cut (-10%)',
                value:0.9
              },
              {
                title:'Normal Cut -(20%)',
                value:0.8
              },
              {
                title:'Maximum Cut -(25%)',
                value:0.75
              },
              {
                title:'Maintenance',
                value:1
              },
              {
                title:'Lean Bulk(+10%)',
                value:1.1
              }
            ],
        activity:[
            {
              title:'Sedentary',
              value:13,
              val:1.2
            },
            {
              title:'Lightly Active',
              value:15,
              val:1.35
            },
            {
              title:'Active',
              value:15.5,
              val:1.55
            },
            {
              title:'Very Active',
              value:16,
              val:1.75
            },
          
        ],
        macro_weight:0,
        macro_goals:[],
        activity_selected:0,
        goal_selected:0,
        macros_selected:0,
        macro_splits:0,
        fats:0,
        protein:0,
        carbs:0,

       
   
    }),
    computed:{


      cal_cut(){
        console.log(this.kinobody_formula)
       let k = this.goal_selected * this.kinobody_formula
       return k
      },

      kinobody_formula(){
        let l = this.activity_selected* this.macro_weight
        return l
      }
      
    },

    methods: {
        calculate_macros: function(){
          let weight = this.macro_weight/2.205
          let cals_temp = 0;
          console.log(weight+"here")

          if(this.macros_selected == "20% fats"){
            this.protein = weight * 2
            this.fats = this.cal_cut * 0.2 / 9
  
          }
          else if(this.macros_selected == "25% fats (default)"){
            this.protein = weight * 2.5
            this.fats = this.cal_cut * 0.25 / 9
      
          }
          else if(this.macros_selected == "30% fats"){
            this.protein = weight * 3
            this.fats = this.cal_cut * 0.3/9

          }
          else if(this.macros_selected == "(p: 35%, f: 30%, c: 35%)"){
            this.protein = 0.35 * this.cal_cut/4;
            this.fats = this.cal_cut * 0.3 / 9
          }
          else if(this.macros_selected== "(p: 35%, f: 25%, c: 40%)"){
            this.protein = 0.35 * this.cal_cut/4
            this.fats = 0.25 * this.cal_cut/9
          }

          this.protein = Math.round(this.protein)
          this.fats = Math.round(this.fats)
          cals_temp = (this.protein *4) + ( this.fats *9)
          this.carbs = (this.cal_cut - cals_temp)/4

        },
        calculate: function() {
            var weight = parseInt(this.weight) * 703;
            var height = parseInt(this.height);
            var bmi = weight / (height * height)
            if(bmi < 24) {
                this.result = 'Low: ' + bmi.toFixed(2) + ' kg/m2';
            }
            else if (bmi >=25 && bmi <28 ) {
                this.result = 'Moderate: ' + bmi.toFixed(2) + ' kg/m2';
            }
            else if (bmi >=28 ) {
                this.result = 'High: ' + bmi.toFixed(2) + ' kg/m2';
            }
        },

    },
  }
</script>
<style>
@import url("https://fonts.googleapis.com/css?family=Questrial");

  .app_n{
    font-family: "Questrial";
  }
 </style>