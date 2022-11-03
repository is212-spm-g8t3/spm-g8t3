<!-- 
	This is the tables page, it uses the dashboard layout in: 
	"./layouts/Dashboard.vue" .
 -->

 <template>
	<div>
		<!-- Title -->
		<a-row :gutter="24">
			<a-col :span="24" :md="12" class="mb-12">
				<h3 style="margin-left: 12px">Skill Selection - {{ roleName }}</h3>
			</a-col>
			<a-col :span="24" :md="12" class="mb-12" style="display: flex; align-items: center; justify-content: flex-end">
			</a-col>
		</a-row>
		<!-- / Title -->

		<!-- Authors Table -->
		<a-row :gutter="24" type="flex">

			<!-- Authors Table Column -->
			<a-col :span="24" class="mb-24">

				<!-- Authors Table Card -->
				<CardSkillTable
					:titleName="titleName"
					:data="skillsData"
					:columns="table1Columns"
					style="padding-right: 10px"
				></CardSkillTable>
				<!-- / Authors Table Card -->

			</a-col>
			<!-- / Authors Table Column -->

		</a-row>
		<!-- / Authors Table -->

		<a-row :gutter="24" type="flex">
			<a-col :span="24" class="mb-24" style="text-align: right">
				<a-button type="dark" v-on:click="checkout()" >
					Save
				</a-button>
			</a-col>
		</a-row>
	</div>
</template>

<script>

	import CardSkillTable from '../components/Cards/CardSelectSkillTable' ;
	import axios from 'axios';
import { SlowBuffer } from 'buffer';
	
			
	
	const skillCols = [
		{
			title: 'SKILL NAME',
			dataIndex: 'skillDetails',
			scopedSlots: { customRender: 'skillDetails' },
		},
		{
			title: 'SKILL DESCRIPTION',
			dataIndex: 'Skill_Description',
			scopedSlots: { customRender: 'Skill_Description' },
		},
		{
			title: 'STATUS',
			dataIndex: 'status',
			scopedSlots: { customRender: 'status' },
		},
		// if skill is not added, show 'show to cart'
		{
			title: '',
			dataIndex: 'cartDetails',
			scopedSlots: { customRender: 'cartDetails' },
		},
		// {
		// 	title: 'CREATED',
		// 	dataIndex: 'created',
		// 	class: 'text-muted',
		// },
		// {
		// 	title: '',
		// 	scopedSlots: { customRender: 'editBtn' },
		// 	width: 50,
		// },
	]


	
	export default ({
		components: {
			CardSkillTable,
		},
		data() {
			return {

				

				skillsData: [], //initialise skills data table
				table1Columns: skillCols,
				visible: false,
				titleName: "Skills",
				roleName: "",

				
			}
		},
		methods: {
			showModal() {
			this.visible = true;
			},

			getSkillsByRole(){
                //get skills by role ID
				const path = 'http://localhost:5000/skills-by-role?roleId='+this.$route.query.roleId;
				axios.get(path)
					.then((res) => {
						this.skillsData = res.data.data.skills
						console.log(this.skillsData)
						for (let skill of this.skillsData){
							skill.cartDetails = {}
							skill.cartDetails.skillId = skill.Skill_ID

							//check if skill has been added to cart
							let selectedSkillsAndCourses = JSON.parse(localStorage.getItem('selectedSkillsAndCourses'));

							if (!(selectedSkillsAndCourses === null)){
								if (!(skill.Skill_ID in selectedSkillsAndCourses)){
									skill.cartDetails.isNotAdded = false
								}else{
									skill.cartDetails.isNotAdded = true
								}
							}
							

							//for skill details display
							skill.skillDetails = {}
							skill.skillDetails.skillId = skill.Skill_ID
							skill.skillDetails.skillName = skill.Skill_Name
							skill.skillDetails.skillDesc = skill.Skill_Description
							skill.skillDetails.skillType = skill.Skill_Type
							skill.skillDetails.lastUpdated = skill.Created_Date

						}
						console.log(this.skillsData)
					})
					.catch((error) => {
					// eslint-disable-next-line
					console.error(error);
					});
                    
			},
			getRoleName(){
                //get selected role name
				const path = 'http://localhost:5000/roles';
				axios.get(path)
					.then((res) => {
						let roles = res.data.data.roles
						for (let role of roles){
							if (this.$route.query.roleId == role.Job_Role_ID){
								this.roleName = role.Job_Role_Name
								break
							}
						}
						console.log(this.roleName)

					})
					.catch((error) => {
					// eslint-disable-next-line
					console.error(error);
					});
                    
			},

			handleOk(e) {
			console.log(e);
			this.visible = false;
			},

			checkout(){
				//checkout skills and courses
				let sendData = confirm("You are about to save a learning journey. Proceed?");

				if (sendData == false){
					return
				}

				let roleId = this.$route.query.roleId
				let skillId = this.$route.query.skillId

				let selectedSkillsAndCourses = JSON.parse(localStorage.getItem('selectedSkillsAndCourses'));
				let staffInfo = JSON.parse(localStorage.getItem('staffInfo'));
				let staffId = staffInfo['staffId'];

				let payload = { job_role_id: roleId, staff_id: staffId };
				const path = 'http://localhost:5000/learningJourney/createLearningJourney';
				axios.post(path, payload)
					.then((res) => {
						console.log(res)
						//console.log("Learning Journey Successfully created")
						
						
					})
					.catch((error) => {
					// eslint-disable-next-line
					console.error(error);
					});

				//send data to save learning endpoint

				// this.$router.push({
				// 		path: '/save-learning-journey', 
				// 	});

				//save learning journey skills
				for (let skill in selectedSkillsAndCourses){
					console.log(skill)
					let skillPayload = { skill_id: skill, staff_id: staffId, lj_id: 13 };
					let skillPath = 'http://localhost:5000/learningJourney/createLearningJourneySkill';
					axios.post(skillPath, skillPayload)
						.then((res) => {
							console.log("Learning Journey skill Successfully saved")
							
						})
						.catch((error) => {
						// eslint-disable-next-line
						console.error(error);
						});
				}

				//save learning journey courses
				for (let skillId in selectedSkillsAndCourses){
					for (let course of selectedSkillsAndCourses[skillId]){
						let coursePayload = { skill_id: skillId, 
							staff_id: staffId, 
							reg_id: 1, 
							course_id: course, 
							lj_id: 13
						};
						let coursePath = 'http://localhost:5000/learningJourney/createLearningJourneyCourse';
						axios.post(coursePath, coursePayload)
							.then((res) => {
								console.log("Learning Journey course Successfully saved")
								
							})
							.catch((error) => {
							// eslint-disable-next-line
							console.error(error);
							});
					}
					
				}

				alert("Learning Journey successfully created")
				localStorage.removeItem('selectedSkillsAndCourses');
				this.$router.push({
                    path: '/learning-journey'
                });
			},

		},
	created() {
    	this.getSkillsByRole();
		this.getRoleName();
  	},
	})

</script>

<style lang="scss">
</style>