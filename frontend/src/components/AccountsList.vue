<template>
  <v-data-table
    :headers="headers"
    :items="accountList"
    :items-per-page="10"
    class="elevation-1"
    show-expand
  >
  </v-data-table>
</template>

<script>

export default {
  props: {
    accountList: {
      type:Array,
      default: () => new Array()
    }
  },
  data() {
    return {
      headers: [
        { text: 'user', value: 'user' },
        { text: 'username', value: 'username' },
        { text: 'age', value: 'age' },
        { text: 'occupation', value: 'occupation' },
        { text: 'gender', value: 'gender' },
      ]
    }
  }
}
</script>