<template lang="pug">
  v-navigation-drawer( permanent  left v-model="drawer" app mini-variant width="100%")
    v-spacer
    template(v-slot:append)

      v-avatar
        v-btn(icon :to="{name: 'home'}")
          v-icon(x-large color="red" ) mdi-heart-pulse
      v-avatar.mt-5
        v-btn(icon)
          v-icon(x-large) mdi-folder
      v-avatar.mt-5
        v-btn(icon)
          v-icon(x-large) mdi-chat-processing-outline
      v-avatar.mt-5
        v-btn(icon)
          v-icon(x-large) mdi-tune-vertical
</template>

<script>
export default {
  name: "NavigationBar",
  data () {
    return {
      drawer: true,
    }
  },
}
</script>

<style scoped>

</style>
