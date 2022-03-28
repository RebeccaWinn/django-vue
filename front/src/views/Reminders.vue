<template>
        <v-container style="margin-top:100px;"> 
        <v-alert v-if="alert == true"
            type="success"
            dismissible
          >{{reminder_alert}}</v-alert>
        <v-card class="pa-4 mb-3">
          <h2  class="text-center">Workout Reminders</h2>
        </v-card>
          <v-row>
            <v-col
              cols="12"
              sm="4"
            >
              <v-sheet
                rounded="lg"
                min-height="268"
                center
                class="pa-5"
              >
              
              <div>Add Custom Reminder</div>
               <v-text-field
                  label="title*"
                  v-model="new_title"
                  required
                ></v-text-field>
                <v-text-field
                  label="description*"
                  v-model="new_description"
                  required
                ></v-text-field>
              
             
                  <v-date-picker v-show="date_open" v-model="new_date" width="100%" mode="dateTime" :timezone="timezone" />
                  <v-btn v-show="date_open" @click="time_open = true; date_open = false">Choose Time</v-btn>
                  <v-time-picker
                        v-show="time_open"
                        v-model="new_time"
                        format="ampm"
                      ></v-time-picker>
                <v-btn @click="postReminder()">Submit</v-btn>


              </v-sheet>
            </v-col>
             <v-dialog
                v-model="dialog"
                persistent
                max-width="600px"
                >
                <v-card>
                    <v-card-title>
                    <span class="text-h5">Edit Reminder</span>
                    </v-card-title>
                    <v-card-text>
                    <v-container>
                        <v-row>
                        
                        <v-col cols="12">
                           <v-text-field
                            label="title*"
                            v-model="updated_title"
                            required
                          ></v-text-field>
                        </v-col>
                        <v-col cols="12">
                            <v-text-field
                            label="description*"
                            v-model="updated_description"
                            required
                          ></v-text-field>
                        </v-col>
                        <v-col cols="12">
                          <v-date-picker v-show="date_open" v-model="updated_date" width="100%" mode="dateTime" :timezone="timezone" />
                          <v-btn v-show="date_open" @click="time_open = true; date_open = false">Choose Time</v-btn>
                          <v-time-picker
                                v-show="time_open"
                                v-model="updated_time"
                                format="ampm"
                              ></v-time-picker>
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
                    <v-btn
                        color="blue darken-1"
                        text
                        @click="updateReminder(id);dialog = false;"
                    >
                        Save
                    </v-btn>
                    </v-card-actions>
                </v-card>
                </v-dialog>
  
            <v-col
              cols="12"
              sm="8"
            >
              <v-sheet
                min-height="70vh"
                rounded="lg"
                
              >   
              <v-card class="pa-5" v-for="reminder in reminders" v-bind:key="reminder.id">
              <v-row>
                <div>
                <v-card-title>{{reminder.title}}</v-card-title>
                <v-card-subtitle>{{reminder.time}}</v-card-subtitle>
                <v-card-text>{{reminder.description}}</v-card-text>
                </div>
                <v-spacer></v-spacer>
                  <v-btn icon @click= "updated_title = reminder.title; updated_description =reminder.description ; dialog = true; id = reminder.id; ">
                  <v-icon>mdi-pencil</v-icon>
                  </v-btn>
                 <v-btn icon>
                    <v-icon @click="deleteReminder(reminder.id);">mdi-delete</v-icon>
                  </v-btn>
              </v-row>

              </v-card>

              </v-sheet>
            </v-col>

          </v-row>

        </v-container>
</template>
<script>

  import{ getAPI } from '../axios-api'
    export default {
      data:() => ({
          new_title:"",
          new_description:"",
          new_date:"",
          new_time:"",
          updated_title:"",
          updated_description:"",
          updated_date:"",
          updated_time:"",
          APIData:"",
          reminders:[],
          events:[],
          alert:false,
          reminder_alert:"",
 
          id:"",
          time_open:false,
          date_open:true,
          dialog: false,
          date:(new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),

          timezone: '',
      }),
      created(){
        this.getReminders()
      },

      methods:{
  
        getReminders(){
           const reminders = []
                getAPI.get('/reminders/')
                .then(response => {
                    console.log('Calendar Events Api has recieved data')
                    this.APIData = response.data
                    for (let i = 0; i < this.APIData.data.length; i++) {
                        reminders.push({
                            id:this.APIData.data[i].id,
                            title:this.APIData.data[i].title,
                            description:this.APIData.data[i].description,
                            time:new Date(this.APIData.data[i].time),
                        })
                    this.checkReminders(new Date(this.APIData.data[i].time),this.APIData.data[i].title,this.APIData.data[i].description)
                  
                    }
                })
                .catch(error => {
                    console.log(error)
                })
                this.reminders = reminders


        },
        checkReminders(time,title,description){
          let d = new Date();
            if (time.getDay() == d.getDay()){
              this.reminder_alert = title + ' : Get to the gym - ' + description 
              this.alert = true
            }
        },


        postReminder(){
          getAPI.post('/reminders/',{
                  title: this.new_title,
                  description: this.new_description,
                  time: this.new_date + " " +this.new_time ,
              }).then(response => {
                  console.log(response)
              }).catch(error => {
                  console.log(error)
              })
              this.new_title=""
              this.new_description=""
              this.new_date=""
              this.new_time=""
            this.getReminders()


        },
        deleteReminder(id){
          getAPI.delete('/reminders/'+id)
                .then(response => {
                    console.log(response);
                })
                .catch(function (error) {
                    console.log(error.response)
                })
            this.getReminders();

        },
    
        updateReminder(id){
           getAPI.patch('/reminders/'+id,{
                  title: this.updated_title,
                  description: this.updated_description,
                  time: this.updated_date + " " +this.updated_time ,
                }).then(response => {
                    console.log(id)
                    console.log(response);
                }).catch(function (error) {
                    console.log(error.response)
                })
                this.getReminders();

        }
      }


    }
</script>