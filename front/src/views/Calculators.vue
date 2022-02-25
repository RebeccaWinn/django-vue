<template>
<v-container style="margin-top:140px">
<v-row>
  <v-card width="500" class="pa-5 mx-auto">
  <v-card-title>BMI Calculator</v-card-title>
  <v-form
    ref="form"
    v-model="valid"
  >
    <v-text-field
      v-model="weight"
      label="Weight (in kg)"
      required
    ></v-text-field>

    <v-text-field
      v-model="height"
      label="Height (in cm)"
      required
    ></v-text-field>
    <input type="text" max-height="200" v-model="result"/><br>
    <v-btn class="mt-5 mb-5" @click="calculate()">Calculate</v-btn>
  </v-form>
  </v-card>
  <v-spacer></v-spacer>
  
  <v-card  width="500" class="pa-5 mx-auto">
  <v-card-title>Macro Calculator</v-card-title>
  <v-form
    ref="form"
    v-model="valid"
  >
    <v-text-field
      v-model="weight"
      label="Weight (in kg)"
      required
    ></v-text-field>

    <v-text-field
      v-model="height"
      label="Height (in cm)"
      required
    ></v-text-field>
    <input type="text" max-height="200" v-model="result"/><br>
    <v-btn class="mt-5 mb-5" @click="calculate()">Calculate</v-btn>
  </v-form>
  
  </v-card>

</v-row>
  </v-container>
</template>
<script>
  export default {
    data: () => ({
        weight: '',
        height: '',
        result:''
    }),

    methods: {
        calculate: function() {
            var weight = parseInt(this.weight);
            var height = parseInt(this.height) / 100;
            var bmi = weight / (height * height)
            if(bmi < 25) {
                this.result = 'Low: ' + bmi.toFixed(2) + ' kg/m2';
            }
            else if (bmi >=25 && bmi <30 ) {
                this.result = 'Moderate: ' + bmi.toFixed(2) + ' kg/m2';
            }
            else if (bmi >=30 ) {
                this.result = 'High: ' + bmi.toFixed(2) + ' kg/m2';
            }
        }
    },
  }
</script>