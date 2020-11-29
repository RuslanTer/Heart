<template lang="pug">
  v-toolbar( prominent extended max-height="100px" ).elevation-1
      v-col(lg="2").pt-5
        v-img(width='209', height='56', src="@/assets/logo.svg")

      v-autocomplete(style="width: 100%"
        flat
        hide-no-data
        hide-details
        outlined
        label="Поиск пациента"
        :items="patients_test").pt-4
      v-icon(x-large @click="").pt-6 mdi-microphone
      v-col
        v-list-item.align-content-end
          v-col
            v-list-item-title.title
              | Василий Петров
            v-list-item-subtitle Кардиолог
          v-list-item-avatar
            v-icon(x-large) mdi-account-circle-outline
</template>

<script>
import axios from "axios";

export default {
  name: "ToolBar",

  data() {
    return {
      patients: [],
      patients_test: [],
      valueDeterminate: 50,
    }
  },

  async created() {
    const {data} = await axios.get('http://194.67.116.92:8080/api/patient/', {headers: {}})
    console.log(data)
    this.patients = data
    for (var i=0; i<this.patients.length; i++) {
      this.patients_test.push(this.patients[i].name)
    }

  },

}
</script>

<style scoped>

</style>
