<template>
	<v-layout wrap>
		<v-card
      @click="goToWithParams('profile-detail', 'Alexander')"
      class="white--text pl-5"
      style="width: 100%; background-color: rgba(0, 0, 0, 0);"
		>
			<v-row>
				<v-col class="pl-0">
					<p class="mb-0">Alexander</p>
					<p class="mb-0 caption">Toy Story / Grumpier Old Men / Father of the Bride Part II</p>
				</v-col>
			</v-row>
		</v-card>
		<v-card
      @click="goToWithParams('profile-detail', 'Kara')"
      class="white--text pl-5"
      style="width: 100%; background-color: rgba(0, 0, 0, 0);"
		>
			<v-row>
				<v-col class="pl-0">
					<p class="mb-0">Kara</p>
					<p class="mb-0 caption">Toy Story / Powder / Twelve Monkeys</p>
				</v-col>
			</v-row>
		</v-card>
		<v-card
      @click="goToWithParams('profile-detail', 'Brian')"
      class="white--text pl-5"
      style="width: 100%; background-color: rgba(0, 0, 0, 0);"
		>
			<v-row>
				<v-col class="pl-0">
					<p class="mb-0">Brian</p>
					<p class="mb-0 caption">Braveheart / Pulp Fiction / Forrest Gump</p>
				</v-col>
			</v-row>
		</v-card>
	</v-layout>
</template>

<script>
import router from "../../router";

export default {
	methods: {
		goToWithParams: function(path, params) {
			router.push({ name: path, params:{ nickname: params} });
		},
	}
}
</script>

<style scoped>
.recommended-profile {
	object-fit: cover;
	border-radius: 50%;
	height: 40px;
	width: 40px;
}
</style>