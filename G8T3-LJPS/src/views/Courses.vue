<!-- 
	This is the tables page, it uses the dashboard layout in: 
	"./layouts/Dashboard.vue" .
 -->

<template>
	<div>
		<!-- Title -->
		<a-row :gutter="24">
			<a-col :span="24" :md="12" class="mb-12">
				<h3 style="margin-left: 12px">Course Management</h3>
			</a-col>
		</a-row>
		<!-- / Title -->

		<!-- Authors Table -->
		<a-row :gutter="24" type="flex">
			<!-- Authors Table Column -->
			<a-col :span="24" class="mb-24">
				<!-- Authors Table Card -->
				<CardRoleTable
					:titleName="titleName"
					:data="table1Data"
					:columns="table1Columns"
					@updateCourse="updateModalCourse"
					:page="tableType"
				></CardRoleTable>
				<!-- / Authors Table Card -->
			</a-col>
			<!-- / Authors Table Column -->
		</a-row>
		<!-- / Authors Table -->

		<!-- Course Modal -->
		<a-modal
			v-model:visible="modal2Visible"
			title="Assign Skills"
			centered
			@ok="modal2Visible = false"
			:loading="loading"
			>
			<template slot="footer">
				<a-button key="back" @click="handleUpdateCancel">
				Cancel
				</a-button>
				<a-button key="submit" type="primary" @click="handleUpdate">
				Update
				</a-button>
			</template>
			<a-select
				:value="existingSkills"
				mode="multiple"
				placeholder="Select skills"
				style="width: 100%"
				:showArrow="true"
				@deselect="handleDeselect"
				@select="handleSelect"
			>
				<a-select-option v-for="(option, index) in filteredOptions" :key="index">
					{{ option }}
				</a-select-option>
			</a-select>
		</a-modal>
		<!-- Course Modal -->


	</div>
</template>

<script>

// "Authors" table component.
import CardRoleTable from '../components/Cards/CardRoleTable' ;
import axios from 'axios';
import { message } from 'ant-design-vue';

const OPTIONS = ['Apples', 'Nails', 'Bananas', 'Helicopters'];
// "Authors" table list of columns and their properties.
const table1Columns = [
	{
		title: 'Name',
		dataIndex: 'Job_Role_Name',
		scopedSlots: { customRender: 'Job_Role_Name' },
	},
	{
		title: 'Category',
		dataIndex: 'Department',
		scopedSlots: { customRender: 'Department' },
	},
	{
		title: 'Type',
		dataIndex: 'type',
		class: 'text-muted',
	},
	{
		title: 'Skills',
		dataIndex: 'Skills',
		scopedSlots: { customRender: 'Skills' },
	},
	{
		title: 'Status',
		dataIndex: 'status',
		scopedSlots: { customRender: 'status' },
	},
	{
		title: 'Actions',
		scopedSlots: { customRender: 'courseAction' },
		width: 50,
	},
];

export default ({
	components: {
		CardRoleTable,
	},
	data() {
		return {
			// Associating "Authors" table data with its corresponding property.
			table1Data: [],

			// Associating "Authors" table columns with its corresponding property.
			table1Columns: table1Columns,
			titleName: "Courses",
			CoursesSkillsData: [],
			modal2Visible: false,
			skillData: [],
			existingSkills: [],
			selectedCourseId: "",
			tableType: "Course",
			loading: false
		}
	},
	methods: {
		getCoursesSkills() {
			const path = 'http://localhost:5000/getCoursesWithSkills';
			axios.get(path)
				.then((res) => {
					let response = res.data.data
					// console.log(response);
					for (let i = 0; i < response.length; i++) {
						let courseId = response[i].Course_ID;
						let skillData = {
								'skillId': response[i].Skill_ID,
								'skillName': response[i].Skill_Name,
								'skillDescription': response[i].Skill_Description,
								'skillType': response[i].Skill_Type,
								'skillStatus': response[i].Status,
						}
						if (this.CoursesSkillsData[courseId]) {
							this.CoursesSkillsData[courseId].push(skillData);
						}
						else {
							this.CoursesSkillsData[courseId] = [skillData];
						}
					}
					// console.log(this.CoursesSkillsData);
				})
		}
	},
	methods: {
		getCoursesSkills() {
			const path = 'http://localhost:5000/getCoursesWithSkills';
			axios.get(path)
				.then((res) => {
					let response = res.data.data
					// console.log(response);
					for (let i = 0; i < response.length; i++) {
						let courseId = response[i].Course_ID;
						let skillData = {
								'skillId': response[i].Skill_ID,
								'skillName': response[i].Skill_Name,
								'skillDescription': response[i].Skill_Description,
								'skillType': response[i].Skill_Type,
								'skillStatus': response[i].Status,
						}
						if (this.CoursesSkillsData[courseId]) {
							this.CoursesSkillsData[courseId].push(skillData);
						}
						else {
							this.CoursesSkillsData[courseId] = [skillData];
						}
					}
					// console.log(this.CoursesSkillsData);
				})

				.catch((error) => {
					console.error(error);
				});
		},
		// Display Course Table
		async getCourses() {
			await this.getCoursesSkills();
			const path = 'http://localhost:5000/courses';
			axios.get(path)
				.then((res) => {
					let response = res.data.data.courseCatalog
					// console.log(response);

					// Retrieve Courses
					for (let i=0; i<response.length; i++) {
						let courseData = response[i];
						var template = {
							'key' : i,
							'courseId' : courseData.Course_ID,
							'Job_Role_Name' : courseData.Course_Name,
							'description' : courseData.Course_Description,
							'Department' : courseData.Course_Category,
							'status' : courseData.Course_Status,
							'type' : courseData.Course_Type,
							'Skills' : []
						};

						if (this.CoursesSkillsData[courseData.Course_ID]) {
							template['Skills'] = this.CoursesSkillsData[courseData.Course_ID];
						}
						this.table1Data.push(template);
					}
					// console.log(this.table1Data);
				})
				.catch((error) => {
					// eslint-disable-next-line
					console.error(error);
				});
		},

		getAllSkills() {
			const path = 'http://localhost:5000/skills';
			axios.get(path)
				.then((res) => {
					let response = res.data.data.skills
					console.log(response);
					for (let i=0; i < response.length; i++) {
						if (response[i].Status == "Active") {
							this.skillData.push(response[i].Skill_Name)
						}
					}
				})
				.catch((error) => {
					// eslint-disable-next-line
					console.error(error);
				});
		},

		
		async updateModalCourse(value) {
			this.existingSkills = [];
			await this.getAllSkills();
			this.selectedCourseId = value.courseId;
			for (let i=0; i < value.Skills.length; i++) {
				this.existingSkills.push(value.Skills[i].skillName);
			}
			// console.log(this.existingSkills)
			this.modal2Visible = true;
		},

		handleUpdateCancel(e) {
			this.modal2Visible = false;
			this.loading = false;
		},

		handleUpdate(e) {
			this.loading = true;
			const path = 'http://localhost:5000/updateCourseSkills';

			let formData = {
				"updateInfo": {
					"skillsForUpdate": this.existingSkills,
					"courseId": this.selectedCourseId
				}
			};
			console.log(formData);

			axios.post(path, formData,
				{headers:{"Content-Type" : "application/json"}})
				.then((response) => {
					console.log(response);

					// Happy path, success creation
					if (response.data.code == 201) {
						this.handleUpdateCancel();
						message.success(
							response.data.message,
							10,
						);
						setTimeout(function (){
							window.location.reload();
						}, 1000)
					}
				})
				.catch((error) => {
					console.log(error);
					this.loading = false;
				});
		},

		handleSelect(value) {
			this.existingSkills.push(this.filteredOptions[value]);
		},

		handleDeselect(value) {
			const index = this.existingSkills.indexOf(value);
			if (index > -1) { // only splice array when item is found
				this.existingSkills.splice(index, 1); // 2nd parameter means remove one item only
			}
		},
	},
	
	created() {
		this.getCourses();
	},

	computed: {
		filteredOptions() {
			return this.skillData.filter(skill => !this.existingSkills.includes(skill))
		},
	}
})

</script>

<style lang="scss">
</style>