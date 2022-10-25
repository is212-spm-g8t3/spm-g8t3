<template>

	<!-- Authors Table Card -->
	<a-card :bordered="false" class="header-solid h-full" :bodyStyle="{padding: 0,}">
		<template #title>
			<a-row type="flex" align="middle">
				<a-col :span="24" :md="12">
					<h5 class="font-semibold m-0">{{titleName}}</h5>
				</a-col>
				<a-col :span="24" :md="12" style="display: flex; align-items: center; justify-content: flex-end">
					<a-radio-group v-model="statusRadioBtn" size="small">
						<a-radio-button value="all">ALL</a-radio-button>
						<a-radio-button value="active">ATTAINED</a-radio-button>
						<a-radio-button value="inactive">NOT ATTAINED</a-radio-button>
					</a-radio-group>
				</a-col>
			</a-row>
		</template>
		<a-table :columns="columns" :data-source="dataFilteredStatus" :pagination="true">

			<template slot="skillDetails" slot-scope="skillDetails">
				<div class="table-avatar-info">
					<!-- <a-avatar shape="square" :src="Skill_Name.avatar" /> -->
					<div class="avatar-info" style="margin-top: 7px">
						<!-- <h6>{{ Skill_Name }}</h6> -->
						<a @click="showModal" type="dark" icon="plus" style="margin-right: 24px" >
							{{ skillDetails.skillName }}
						</a>


					</div>
				</div>
				<template>
					<div>
						<a-modal centered v-model="visible" title="Skill Details" @ok="handleOk">
							<strong>Skill ID: </strong><p style="display: inline;">{{skillDetails.skillId}}</p>
							<br>
							<strong>Skill Name: </strong><p style="display: inline;">{{skillDetails.skillName}}</p>
							<br>
							<strong>Skill Description: </strong><p style="display: inline;">{{skillDetails.skillDesc}}</p>
							<br>
							<strong>Skill Type: </strong><p style="display: inline;">{{skillDetails.skillType}}</p>
							<br>
							<strong>Last Updated: </strong><p style="display: inline;">{{skillDetails.lastUpdated}}</p>
						</a-modal>
					</div>
				</template>
			</template>

			<template slot="func" slot-scope="func">
				<div class="author-info">
					<h6 class="m-0">{{ func.department }}</h6>
					<p class="m-0 font-regular text-muted">{{ func.job }}</p>
				</div>
			</template>

			<template slot="status" slot-scope="status">
				<a-tag class="tag-status" :class="status == 'active' ? 'ant-tag-success' : 'ant-tag-muted'">
					{{ status == 'active' ? "Attained" : "Not Attained" }}
				</a-tag>
			</template>


			<template slot="cartDetails" slot-scope="cartDetails" >
				<a-button v-on:click="selectSkill(cartDetails.skillId)" 
							:class="cartDetails.isNotAdded == true ? 'ant-tag-mute' : 'ant-tag-primary'">
					{{ cartDetails.isNotAdded == true ? "Modify" : "Select" }}
				</a-button>

			</template>


			<template slot="editBtn" slot-scope="row">
				<a-button type="link" :data-id="row.key">
					<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
						<path class="fill-gray-7" d="M13.5858 3.58579C14.3668 2.80474 15.6332 2.80474 16.4142 3.58579C17.1953 4.36683 17.1953 5.63316 16.4142 6.41421L15.6213 7.20711L12.7929 4.37868L13.5858 3.58579Z"/>
						<path class="fill-gray-7" d="M11.3787 5.79289L3 14.1716V17H5.82842L14.2071 8.62132L11.3787 5.79289Z"/>
					</svg>
				</a-button>
			</template>



		</a-table>
	</a-card>
	<!-- / Authors Table Card -->


</template>

<script>
	export default ({
		props: {
			data: {
				type: Array,
				default: () => [],
			},
			columns: {
				type: Array,
				default: () => [],
			},
			titleName: {
				type: String,
				default: ""
			}
		},
		data() {
			return {
				// Active button for the "Authors" table's card header radio button group.
				statusRadioBtn: 'all',
				visible: false,
			}
		},


		methods: {
			showModal() {
				console.log("opening modal")
				this.visible = true;
				console.log(this.visible)
			},

			selectSkill(skillId){

				//update localStorage variable for skills
				// localStorage.removeItem('selectedSkills');
				//TODO: move this to courses
				// let selectedSkills = JSON.parse(localStorage.getItem('selectedSkills'));
				
				// if (selectedSkills === null){
				// 	// if selected skills is null then initialise selected skills array.
				// 	selectedSkills = [skillId]
				// 	console.log(typeof(selectedSkills))
				// } else if(!selectedSkills.includes(skillId) ){
				// 	console.log(selectedSkills)
				// 	console.log(typeof(selectedSkills))
				// 	selectedSkills.push(skillId)
				// }
				// console.log(selectedSkills)
				// localStorage.setItem('selectedSkills', JSON.stringify(selectedSkills));


				// this.$route.query.roleId
				this.$router.push({
						path: '/select-course?roleId=' + this.$route.query.roleId + "&skillId=" + skillId, 
					});
			},

			handleOk(e) {
			console.log(e);
			this.visible = false;
			}

		},


		computed: {
			dataFilteredStatus: function() {
				if (this.statusRadioBtn != 'all') {
					return this.data.filter(eachData => eachData.status == this.statusRadioBtn)
				}
				return this.data
			},

			getRoleId: function() {

			},
			
		},

		created() {

			//this.getSkillsByRole()
		}
		


	})

</script>