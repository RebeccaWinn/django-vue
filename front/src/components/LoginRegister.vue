<template>
 <v-container center class="app_n" v-model="dialog" style="width: 50%;padding-top:120px;" persistent max-width="90%" min-width="360px">
          <v-tabs v-model="tab" show-arrows background-color="cyan darken-1" icons-and-text dark grow>
            <v-tabs-slider color="blue lighten-3"></v-tabs-slider>
            <v-tab v-for="i in tabs" :key="i">
              <v-icon large>{{ i.icon }}</v-icon>
              <div class="caption py-1">{{ i.name }}</div>
            </v-tab>
                  <v-tab-item>
                    <v-card class="px-4">
                      <v-card-text>
                        <v-form ref="registerForm" v-model="valid" lazy-validation>
                          <v-row>
                            <v-col cols="12" sm="6" md="6">
                              <v-text-field v-model="firstName" :rules="[rules.required]" label="First Name" maxlength="20" required></v-text-field>
                            </v-col>
                            <v-col cols="12" sm="6" md="6">
                              <v-text-field v-model="lastName" :rules="[rules.required]" label="Last Name" maxlength="20" required></v-text-field>
                            </v-col>
                            <v-col cols="12">
                              <v-text-field v-model="email" :rules="emailRules" label="E-mail" required></v-text-field>
                            </v-col>
                            <v-col cols="12">
                              <v-text-field v-model="password" :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'" :rules="[rules.required, rules.min]" :type="show1 ? 'text' : 'password'" name="input-10-1" label="Password" hint="At least 8 characters" counter @click:append="show1 = !show1"></v-text-field>
                            </v-col>
                            <v-col cols="12">
                              <v-text-field block v-model="verify" :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'" :rules="[rules.required, passwordMatch]" :type="show1 ? 'text' : 'password'" name="input-10-1" label="Confirm Password" counter @click:append="show1 = !show1"></v-text-field>
                            </v-col>
                            <v-spacer></v-spacer>
                            <v-col class="d-flex ml-auto" cols="12" sm="3" xsm="12">
                              <v-btn color="cyan darken-1" class="white--text" x-large block :disabled="!valid" @click="validate">Register</v-btn>
                            </v-col>
                          </v-row>
                        </v-form>
                      </v-card-text>
                    </v-card>
                  </v-tab-item>
                  <v-tab-item>
                      <v-card class="px-4">
                          <v-card-text>
                              <v-form ref="loginForm" v-model="valid" lazy-validation>
                                  <v-row>
                                      <v-col cols="12">
                                          <v-text-field v-model="loginEmail" :rules="loginEmailRules" label="E-mail" required></v-text-field>
                                      </v-col>
                                      <v-col cols="12">
                                          <v-text-field v-model="loginPassword" :append-icon="show1?'eye':'eye-off'" :rules="[rules.required, rules.min]" :type="show1 ? 'text' : 'password'" name="input-10-1" label="Password" hint="At least 8 characters" counter @click:append="show1 = !show1"></v-text-field>
                                      </v-col>
                                      <v-col class="d-flex" cols="12" sm="6" xsm="12">
                                      </v-col>
                                      <v-spacer></v-spacer>
                                      <v-col class="d-flex" cols="12" sm="3" xsm="12" align-end>
                                          <v-btn x-large block :disabled="!valid" class="white--text" color="cyan darken-1" @click="validate"> Login </v-btn>
                                      </v-col>
                                  </v-row>
                              </v-form>
                          </v-card-text>
                      </v-card>
                  </v-tab-item>
              </v-tabs>
        </v-container>
</template>
<script>
export default {
    data: () => ({
        dialog: false,
        tab: 0,
        tabs: [
            {name:"Register", icon:"mdi-account-outline"},
            {name:"Login", icon:"mdi-account"}
        ],
        valid: true,
        
        firstName: "",
        lastName: "",
        email: "",
        password: "",
        verify: "",
        loginPassword: "",
        loginEmail: "",
        loginEmailRules: [
          v => !!v || "Required",
          v => /.+@.+\..+/.test(v) || "E-mail must be valid"
        ],
        emailRules: [
          v => !!v || "Required",
          v => /.+@.+\..+/.test(v) || "E-mail must be valid"
        ],
    
        show1: false,
        rules: {
          required: value => !!value || "Required.",
          min: v => (v && v.length >= 8) || "Min 8 characters"
        },

    })
}


</script>
