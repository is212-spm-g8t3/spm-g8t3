<!-- 
	This is the tables page, it uses the dashboard layout in: 
	"./layouts/Dashboard.vue" .
 -->

 <template>
	<div>
		<!-- Title -->
		<a-row :gutter="24">
			<a-col :span="24" :md="12" class="mb-12">
				<h3 style="margin-left: 12px">Skill Selection</h3>
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
				></CardSkillTable>
				<!-- / Authors Table Card -->

			</a-col>
			<!-- / Authors Table Column -->

		</a-row>
		<!-- / Authors Table -->

	</div>
</template>

<script>

	import CardSkillTable from '../components/Cards/CardSelectSkillTable' ;
	import axios from 'axios';
import { SlowBuffer } from 'buffer';
	
			
	
	const skillCols = [
		{
			title: 'SKILL NAME',
			dataIndex: 'Skill_Name',
			scopedSlots: { customRender: 'Skill_Name' },
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
							skill.cartDetails.isNotAdded = false
						}
						console.log(this.skillsData)
					})
					.catch((error) => {
					// eslint-disable-next-line
					console.error(error);
					});
                    
			},

            // getSkills() {
			// const path = 'http://localhost:5000/skills';
			// axios.get(path)
			// 	.then((res) => {
			// 		this.skillsData = res.data.data.skills
			// 		console.log(this.skillsData)
			// 		for (let skill of this.skillsData){
			// 			skill.cartDetails = {}
			// 			skill.cartDetails.skillId = skill.Skill_ID
			// 			skill.cartDetails.isNotAdded = false
			// 		}
			// 		console.log(this.skillsData)
			// 	})
			// 	.catch((error) => {
			// 	// eslint-disable-next-line
			// 	console.error(error);
			// 	});
			// },
			handleOk(e) {
			console.log(e);
			this.visible = false;
			}

			//TODO: Show skills related to selected role.

			//TODO: Show attained and not attained skills. (show status)
		},
	created() {
    	this.getSkillsByRole();
  	},
	})

</script>

<style lang="scss">
</style>