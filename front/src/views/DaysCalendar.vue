<template>
	<div>
		<DaysCalendar/>
	</div>
</template>

<script>
import DaysCalendar from '../components/DaysC.vue';

export default {
  name: 'Calendar',
  
  components: {
    DaysCalendar
  },
};
</script>
<style>
@import url("https://fonts.googleapis.com/css?family=Questrial");

  .app_n{
    font-family: "Questrial";
  }
 </style>