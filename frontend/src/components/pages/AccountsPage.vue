<template>
  <v-container grid-list-md text-center>
    <v-layout justify-center wrap>
      <v-flex xs6>
        <div class="display-2 pa-10">유저 정보</div>
      </v-flex>
      <v-flex xs12>
        <AccountsList />
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import AccountsList from '../AccountsList'

export default {
  components: {
    AccountsList
  }
}
</script>
