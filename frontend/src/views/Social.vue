<template>
    <v-container > 
        <v-row style="margin-top:300px">
        <v-col
            v-for="n in 24"
            :key="n"
            cols="4"
        >
            <v-card height="200" width="350"></v-card>
        </v-col>
        </v-row>
    </v-container>

</template>