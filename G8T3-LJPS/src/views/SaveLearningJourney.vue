
 <template>
	<div>
		<!-- Title -->
		<a-row :gutter="24">
			<a-col :span="24" :md="12" class="mb-12">
				<h3 style="margin-left: 12px">Learning Journey Confirmation - {{ roleName }}</h3>
			</a-col>
			<a-col :span="24" :md="12" class="mb-12" style="display: flex; align-items: center; justify-content: flex-end">
			</a-col>
		</a-row>
		<!-- / Title -->

        <div>
            <!-- iterate through skills -->
            <a-row v-for="skill of skills">
                <h4>{{skill.skillName}}</h4>
                <a-row v-for="course of courses">
                    <strong>{{course.courseName}}</strong>
                </a-row>
            </a-row>
        </div>

	</div>
</template>

<script>

	// import CardSkillTable from '../components/Cards/CardSelectSkillTable' ;
	import axios from 'axios';
// import { SlowBuffer } from 'buffer';
	
			
	
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
			}

		},
	created() {
    	this.getSkillsByRole();
		this.getRoleName();
  	},
	})

</script>

<style lang="scss">
</style>