<template class="app_n">
    <v-container style="margin-top:100px">
        <v-alert v-if="alert == true"
            type="success"
            dismissible
        >{{added_alert}}</v-alert>
        <v-row class="mt-5">
        <v-col cols="2">
            <v-sheet rounded="lg">
            <v-list color="transparent"> <v-row justify="center">
                <v-dialog
                v-model="dialog"
                persistent
                max-width="600px"
                >
                <template v-slot:activator="{ on, attrs }">
                    <v-btn
                    color="primary"
                    dark
                    v-bind="attrs"
                    v-on="on"
                    >
                    Add Workout
                    </v-btn>
                </template>
                <v-card>
                
                    <v-card-title>
                    <span class="text-h5">Add workout</span> 
                    </v-card-title>
                    <v-card-text>
                    <v-container>
                        <v-row>
                        
                        <v-col cols="12">
                            <v-select
                            label="Workout*"
                            :items="['Shoulders', 'Biceps/Triceps', 'Back', 'Chest', 'Glutes', 'Quads', 'Cardio']"
                            required
                            v-model="workout"
                            ></v-select>
                        </v-col>
                        <v-col cols="12">
                            <v-text-field
                            label="day*"
                            v-model="new_start"
                            required
                            ></v-text-field>
                        </v-col>
                        <v-col cols="12">
                            <v-text-field
                            v-model="reminder"
                            label="Reminder for self*"
                            ></v-text-field>
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
                        @click="updateWorkout(selectedEvent.id);dialog = false; update=false; workout='';"
                    >
                        Save
                    </v-btn>
                    <v-btn v-if="update==false"
                        color="blue darken-1"
                        text
                        @click="addWorkout();dialog = false;"
                    >
                        Save
                    </v-btn>
                    </v-card-actions>
                </v-card>
                </v-dialog>
            </v-row>
              
                <v-switch class="pt-4 ma-3"
                    v-model="automatic_reminder"
                    label="Automatic reminders"
                    color="primary"
                    hide-details
                ></v-switch>
      
            </v-list>
            </v-sheet>
        </v-col>

        <v-col>
            <v-sheet
            min-height="70vh"
            rounded="lg"
            >
            <v-row class="fill-height">
            <v-col>
                <v-sheet height="64">
                <v-toolbar
                    flat
                >
                    <v-btn
                    outlined
                    class="mr-4"
                    color="grey darken-2"
                    @click="setToday"
                    >
                    Today
                    </v-btn>
                    <v-btn
                    fab
                    text
                    small
                    color="grey darken-2"
                    @click="prev"
                    >
                    <v-icon small>
                        mdi-chevron-left
                    </v-icon>
                    </v-btn>
                    <v-btn
                    fab
                    text
                    small
                    color="grey darken-2"
                    @click="next"
                    >
                    <v-icon small>
                        mdi-chevron-right
                    </v-icon>
                    </v-btn>
                    <v-toolbar-title v-if="$refs.calendar">
                    {{ $refs.calendar.title }}
                    </v-toolbar-title>
                    <v-spacer></v-spacer>
                    <v-menu
                    bottom
                    right
                    >
                    <template v-slot:activator="{ on, attrs }">
                        <v-btn
                        outlined
                        color="grey darken-2"
                        v-bind="attrs"
                        v-on="on"
                        >
                        <span>{{ typeToLabel[type] }}</span>
                        <v-icon right>
                            mdi-menu-down
                        </v-icon>
                        </v-btn>
                    </template>
                    <v-list>
                        <v-list-item @click="type = 'day'">
                        <v-list-item-title>Day</v-list-item-title>
                        </v-list-item>
                        <v-list-item @click="type = 'week'">
                        <v-list-item-title>Week</v-list-item-title>
                        </v-list-item>
                        <v-list-item @click="type = 'month'">
                        <v-list-item-title>Month</v-list-item-title>
                        </v-list-item>
                        <v-list-item @click="type = '4day'">
                        <v-list-item-title>4 days</v-list-item-title>
                        </v-list-item>
                    </v-list>
                    </v-menu>
                </v-toolbar>
                </v-sheet>
                <v-sheet height="600">
                <v-calendar
                    ref="calendar"
                    v-model="focus"
                    color="primary"
                    :events="events"
                    :event-color="getEventColor"
                    :type="type"
                    @click:event="showEvent"
                    @click:more="viewDay"
                    @click:date="add"
                    @change="getEvents"
                ></v-calendar>
                <v-menu
                    v-model="selectedOpen"
                    :close-on-content-click="false"
                    :activator="selectedElement"
                    offset-x
                >
                    <v-card
                    color="grey lighten-4"
                    min-width="350px"
                    flat
                    >
                    <v-toolbar
                        :color="selectedEvent.color"
                        dark
                    >
                        <v-btn icon
                            @click= "workout=selectedEvent.name;update= true; dialog = true; new_start = selectedEvent.start"
                         >

                        <v-icon>mdi-pencil</v-icon>
                        </v-btn>
                        <v-toolbar-title v-html="selectedEvent.name"></v-toolbar-title>
                        <v-spacer></v-spacer>
                        <v-btn icon>
                        <v-icon>mdi-heart</v-icon>
                        </v-btn>
                        <v-btn icon>
                        <v-icon @click="deleteWorkout(selectedEvent.id); selectedOpen = false;">mdi-delete</v-icon>
                        </v-btn>
                    </v-toolbar>
                    <v-card-text>
                        <span v-html="selectedEvent.details"></span>
                    </v-card-text>
                    <v-card-actions>
                        <v-btn
                        text
                        color="secondary"
                        @click="selectedOpen = false"
                        >
                        Cancel
                        </v-btn>
                    </v-card-actions>
                    </v-card>
                </v-menu>
                </v-sheet>
            </v-col>
            </v-row>
            </v-sheet>
        </v-col>
        </v-row>
    </v-container>
</template>

<script>
    import{ getAPI } from '../axios-api'
    export default {
        name:'DaysCalendar',
        data: () => ({
            automatic_reminder:true,
            APIData:[],
            drawer: null,
            update:false,
            page:'Calendar',
            focus: '',
            type: 'month',
            typeToLabel: {
                month: 'Month',
                week: 'Week',
                day: 'Day',
                '4day': '4 Days',
            },
            alert:false,
            added_alert:"",
            selectedEvent: {},
            selectedElement: null,
            selectedOpen: false,
            events: [],
            colors: ['blue', 'indigo', 'deep-purple', 'cyan', 'green', 'orange', 'grey darken-1'],
            names: ['Shoulders', 'Biceps/Triceps', 'Back', 'Chest', 'Glutes', 'Quads', 'Cardio'],  
            workout: "",
            new_start: "",
            new_date: [],
            day_new:"",
            month_new:"",
            reminder:"reminder",
            dialog:false,
            checkreminders:[],
        }),
    
        mounted () {
            this.$refs.calendar.checkChange()
            this.getEvents()
        },

        created(){
            this.getEvents()
        },

        methods: {
            viewDay ({ date }) {
                this.focus = date
                this.type = 'day'
            },
            add({date}){
                this.workout = ""
                console.log(date)
                this.new_date= date.split("-")
                this.day_new = this.new_date[2]
                if(this.day_new[0] == "0"){
                    this.day_new = this.day_new.slice(1)
                }
                this.month_new = this.new_date[1]
                if(this.month_new[0] == "0"){
                    this.month_new = this.month_new.slice(1)
                }
                this.new_start = new Date(this.month_new+'/'+this.day_new+'/'+this.new_date[0])      
                this.dialog = true
            },
            getEvents(){
                const events = []
                getAPI.get('/events/')
                .then(response => {
                    console.log('Calendar Events Api has recieved data')
                    this.APIData = response.data
                    for (let i = 0; i < this.APIData.data.length; i++) {
                        const start_time = this.APIData.data[i].start.replace('T', ' ');
                        const end_time = this.APIData.data[i].end.replace('T', ' ');
                        events.push({
                            id:this.APIData.data[i].id,
                            name: this.APIData.data[i].name,
                            start: new Date(start_time),
                            end: new Date(end_time),
                            color: this.colors[this.rnd(0, this.colors.length - 1)],
                        })
                    }
                this.events = events

                })
                .catch(error => {
                    console.log(error)
                })
            },
         
            getEventColor (event) {
                return event.color
            },
            setToday () {
                this.focus = ''
            },
            prev () {
                this.$refs.calendar.prev()
            },
            next () {
                this.$refs.calendar.next()
            },
            showEvent ({ nativeEvent, event }) {
                const open = () => {
                this.selectedEvent = event
                this.selectedElement = nativeEvent.target
                requestAnimationFrame(() => requestAnimationFrame(() => this.selectedOpen = true))
                }

                if (this.selectedOpen) {
                this.selectedOpen = false
                requestAnimationFrame(() => requestAnimationFrame(() => open()))
                } else {
                open()
                }

                nativeEvent.stopPropagation()
            },
            addWorkout (){
                getAPI.post('/events/',{
                    name: this.workout,
                    start: this.new_start,
                    end: this.new_start,
                }).then(response => {
                    this.getEvents()
                    console.log(response.data.data.id)
                    if(this.automatic_reminder == true) {
                        getAPI.post('/reminders/',{
                            title: this.workout +' reminder',
                            description: 'automatic reminder',
                            time: new Date(this.new_start),
                            event_id :response.data.data.id
                            
                        }).then(res => {
                            console.log(res)
                        }).catch(error => {
                            console.log(error)
                        })
                    }
                    
                    console.log(response)
                    this.added_alert= this.workout +" workout added to Calendar"
                    this.alert = true
                    this.new_start = ""
                    this.workout = ""
                }).catch(error => {
                    console.log(error)
                })
               
            },
    
            deleteWorkout(id_selected){
                getAPI.delete('/events/'+id_selected)
                    .then(response => {
                        this.getEvents();
                        console.log(response);
                    })
                    .catch(function (error) {
                        console.log(error.response)
                })
                getAPI.get('/reminders/')
                .then(response => {
                        console.log("reminders"+response.data.data)
                    for(let i = 0; i < response.data.data.length; i++) {
                        if (response.data.data[i].event_id == id_selected){
                            getAPI.delete('/reminders/'+ response.data.data[i].id)
                            .then(response => {
                                console.log("reminders"+response);
                            })
                            .catch(function (error) {
                                console.log(error.response)
                            })
                        }
                    }
                })
                .catch(error => {
                    console.log(error)
                })
            
             
            },
            updateWorkout(id){
                getAPI.patch('/events/'+id,{
                    name: this.workout,
                    start: this.new_start,
                    end: this.new_start,
                }).then(response => {
                    this.getEvents();
                    console.log(id)
                    console.log(response);
                }).catch(function (error) {
                    console.log(error.response)
                })
            },
            rnd (a, b) {
                return Math.floor((b - a + 1) * Math.random()) + a
            },

        }
    }
</script>
<style>

@import url('https://fonts.googleapis.com/css2?family=Oswald&display=swap');
  .app_n{
    font-family: 'Oswald', sans-serif;
  }
 </style>