<template>
  <v-container style="margin-top:100px"> 
          <v-row>
            <template v-for="n in 4">
              <v-col
                :key="n"
                class="mt-2 white--text"
                cols="12"
              >
                <strong>Category {{ n }}</strong>
              </v-col>
  
              <v-col
                v-for="j in 6"
                :key="`${n}${j}`"
                cols="6"
                md="2"
              >
                <v-sheet height="150"></v-sheet>
              </v-col>
            </template>
          </v-row>
        </v-container>
</template>