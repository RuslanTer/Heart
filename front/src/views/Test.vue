<template lang="pug">
  v-content
    tool-bar
    navigation-bar
    router-view
</template>

<script>

import ToolBar from "@/components/ToolBar";
import NavigationBar from "@/components/NavigationBar";
export default {
name: "Test",
  components: {NavigationBar, ToolBar},
  methods:{}
}
</script>

<style scoped>

</style>
