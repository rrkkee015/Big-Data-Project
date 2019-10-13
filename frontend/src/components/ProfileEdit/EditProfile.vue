<template>
<div>
	<v-row 
		class="white--text"
		style="display: flex; justify-content: center;"
	>
		<v-col
			cols="12" md="6"
			xs10
			class="d-block"
		>
			<v-row>
				<v-col class="title grey--text">SUBSCRIPTION</v-col>
			</v-row>
			<v-row>
				<v-col cols="3">Subscription State</v-col>
				<v-col cols="1" md="2"></v-col>
				<v-col 
					v-if="profileExpirySubscribeDate" 
					cols="8" 
					md="7" 
					class="margin-p-0"
				>
					<p>Validation 
						<v-btn 
							@click="dialog = true"
							text 
							class="blue--text lowercase"
						>
							Unsubscribe
						</v-btn>
					</p>
					<p>Cancellation scheduled on {{ profileExpirySubscribeDate }}</p>
				</v-col>
				<v-col 
					v-else 
					cols="8" 
					md="7" 
					class="margin-p-0"
				>
					<v-btn 
							@click="subscribe"
							text 
							class="blue--text lowercase"
						>
							Subscribe
						</v-btn>
				</v-col>
			</v-row>
			<hr 
				style="border: 1px solid rgba(255, 255, 255, 0.3); margin: 30px 0;"	
			/>
			<v-row>
				<v-col class="title grey--text">PROFILE</v-col>
			</v-row>
			<v-row>
				<v-col cols="3">E-mail</v-col>
				<v-col cols="1" md="2"></v-col>
				<v-col cols="8" md="7">{{ profileEmail }}</v-col>
			</v-row>
			<v-row>
				<v-col cols="3" style="display: flex; align-items: center;">Gender</v-col>
				<v-col cols="1" md="2"></v-col>
				<v-col cols="8" md="7" style="display: flex; align-items: center;">
					<v-radio-group v-model="profileGender" row>
						<v-radio label="Female" color="white" value="F"></v-radio>
						<v-radio label="Male" color="white" value="M"></v-radio>
					</v-radio-group>
				</v-col>
			</v-row>
			<v-row>
				<v-col cols="3" style="display: flex; align-items: center;">Age</v-col>
				<v-col cols="1" md="2"></v-col>
				<v-col cols="8" md="7">
					<v-text-field
						v-model="profileAge"
						label="age"
					></v-text-field>
				</v-col>
			</v-row>
			<v-row>
				<v-col cols="3" style="display: flex; align-items: center;">Occupation</v-col>
				<v-col cols="1" md="2"></v-col>
				<v-col cols="8" md="7">
					<v-select
						v-model="profileOccupation"
						:items="states"
						menu-props="auto"
						hide-details
						label="Select"
						single-line
					></v-select>
				</v-col>
			</v-row>
			<v-row 
				class="pt-12" 
				style="display: flex; justify-content: center;"
			>
				<v-btn 
					@click="Edit"
					color="#5e5e5e" 
					data-aos="fade-up" 
					data-aos-once="true" 
					data-aos-duration="1500" 
					data-aos-delay="400" 
					style="color:white" 
					text 
				>
					SUBMIT
				</v-btn>
			</v-row>
		</v-col>
		<v-snackbar
      v-model="snackbar"
      color="#E50914"
    >
      Please enter information to change.
      <v-btn
        text
        @click="snackbar = false"
      >
        Close
      </v-btn>
    </v-snackbar>
	</v-row>
	  <v-dialog
    v-model="dialog"
    persistent
    max-width="290"
  >
    <v-card
      style="background-color: rgba(0, 0, 0, 0.7);"  
    >
      <v-card-actions>
        <div class="flex-grow-1"></div>
        <v-btn 
          @click="dialog = false"
          icon
          color="white"
          style="height: 40px; width: 40px;"
        >
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </v-card-actions>
      <v-card-text class="body-1 white--text text-center">
        Would you like to unsubscribe?
      </v-card-text>

      <v-card-actions>
        <div class="flex-grow-1"></div>
        <v-btn
          @click="unsubscribe"
          text
          color="red darken-3"
        >
          OK
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import router from "../../router";

export default {
	data() {
		return {
			dialog: false,
      snackbar : false,
			states: [
				"other", "academic/educator", "artist", "clerical/admin", "college/grad student",
				"customer service", "doctor/health care", "executive/managerial", "farmer",
				"homemaker", "K-12 student", "lawyer", "programmer", "retired", "sales/marketing",
				"scientist", "self-employed", "technician/engineer", "tradesman/craftsman", "unemployed", "writer"
			],
			editAge: 0,
			editGender: '',
			editOccupation: '',
		}
	},
  computed: {
		profileEmail() {
			return this.$store.state.profiles.singleProfile.user.email
		},
		profileExpirySubscribeDate() {
      if (this.$store.state.profiles.singleProfile.expiry_subscribe_date) {
        return this.$store.state.profiles.singleProfile.expiry_subscribe_date.split('T')[0]
      } else {
        return this.$store.state.profiles.singleProfile.expiry_subscribe_date
			}
		},
    profileAge: {
			get() {
				return this.$store.state.profiles.singleProfile.age
			},
			set(value) {
				this.editAge = value
			}
		},
		profileOccupation: {
			get() {
				return this.$store.state.profiles.singleProfile.occupation
			},
			set(value) {
				this.editOccupation = value
			}
		},
		profileGender: {
			get() {
				return this.$store.state.profiles.singleProfile.gender
			},
			set(value) {
				this.editGender = value
			}
		}
	},
	methods: {
		...mapActions('profiles', ['editSingleProfile']),
		Edit() {
			if (this.editAge === 0 && this.editOccupation === '' && this.editGender === '') {
				this.snackbar = true
			} else {
				var params = {
					user: this.$route.params.nickname,
					age: this.editAge,
					occupation: this.editOccupation,
					gender: this.editGender
				}
				if (params.age === 0) {
					delete params.age
				}
				if (params.gender === '') {
					delete params.gender
				}
				if (params.occupation === '') {
					delete params.occupation
				}				
				this.editSingleProfile(params)
				router.push({ name:'profile-detail', params: { nickname: this.$route.params.nickname }})
			}
		},
		subscribe() {
			const params = {
				user: this.$route.params.nickname,
				days: 30
			}
			this.editSingleProfile(params)
		},
		unsubscribe() {
			const params = {
				user: this.$route.params.nickname,
				expiry_subscribe_date: null,
				subscribe: false,
			}
			this.editSingleProfile(params)
			this.dialog = false
		}
	}
}
</script>

<style scoped>
.lowercase {
  font-weight: 300;
  text-transform: lowercase;
	font-size: 1rem;
}
.margin-p-0 > p{
	margin-bottom: 0px;
}
>>> .theme--light.v-input:not(.v-input--is-disabled) input, .theme--light.v-input:not(.v-input--is-disabled) textarea {
	color: white;
}
>>> .theme--light.v-text-field > .v-input__control > .v-input__slot:before {
	border-color : rgba(255, 255, 255, 0.5);
}
>>> .v-text-field.v-input--has-state > .v-input__control > .v-input__slot:before {
	border-color : currentColor;
}
>>> .theme--light.v-label {
	color: white;
}
>>> .theme--light.v-icon {
	color: white;
}
>>> .theme--light.v-select .v-select__selections {
	color: white;
}
>>> .theme--light.v-text-field:not(.v-input--has-state) > .v-input__control > .v-input__slot:hover:before {
	border-color: white;
}
</style>