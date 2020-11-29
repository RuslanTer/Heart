<template lang="pug">
  v-card(flat style="background-color: rgba(0,0,0, 0)").elevation-0
    v-row
      v-col(lg="5")
        v-card.elevation-0
          v-card-title.text-style-patient.pt-6 ПЕРСОНАЛЬНЫЕ РЕКОМЕНДАЦИИ
          v-card-text.pt-12  {{rec}}
      v-col(lg="7")
        v-row
          v-col(lg="6" v-for="bol in bols").pt-0
            v-card().elevation-0
              v-card-title {{bol.name}}
              v-card-text
                v-sparkline(:value="[bol.coeff/2, bol.coeff]"
                  :gradient="gradient"
                  :smooth="radius || false"
                  :padding="padding"
                  :line-width="width"
                  :stroke-linecap="lineCap"
                  :gradient-direction="gradientDirection"
                  :fill="fill"
                  :type="type"
                  :auto-line-width="autoLineWidth"
                  auto-draw)
                  template(v-slot:label="item") {{ item.value }}
</template>

<script>
const gradients = [
  ['#222'],
  ['#42b3f4'],
  ['red', 'orange', 'yellow'],
  ['purple', 'violet'],
  ['#00c6ff', '#F0F', '#FF0'],
  ['#f72047', '#ffd200', '#1feaea'],
]

export default {
  name: "Analys",
  props: {
    bols: Array,
    rec: String,
  },
  data: () => ({
    picker: new Date().toISOString().substr(0, 7),
    width: 2,
    radius: 10,
    padding: 8,
    lineCap: 'round',
    gradient: gradients[5],
    gradientDirection: 'top',
    gradients,
    fill: false,
    type: 'trend',
    autoLineWidth: false,
  })
}
</script>

<style scoped>
.text-style-patient {
  font-family: Roboto, sans-serif;
  font-size: 20px;
  font-style: normal;
  font-weight: 500;
  line-height: 14px;
  letter-spacing: 0.02em;
  text-align: left;

}
</style>
