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
					@updateRecord="updateModalRecord"
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

						<a-row>
							<a-form-model-item label="Description" prop="description">
								<a-input v-model="updateForm.description" type="textarea" />
							</a-form-model-item>
						</a-row>

						<a-row>
							<a-form-model-item label="Status" prop="status">
								<a-radio-group v-model:value="updateForm.status">
									<a-radio-button value="Active">Active</a-radio-button>
									<a-radio-button value="Inactive">Inactive</a-radio-button>
								</a-radio-group>
							</a-form-model-item>
						</a-row>
						
						<a-alert v-if="isUpdateError" :message="updateErrorMsg" type="error" show-icon closable />
					</a-form-model>
				</a-modal>
			</div>
		</template>
		<!-- / Update Course Modal Pop up -->
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
		title: 'NAME',
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
		class: 'text-muted',
	},
	{
		title: 'STATUS',
		dataIndex: 'status',
		scopedSlots: { customRender: 'status' },
	},
	{
		title: '',
		scopedSlots: { customRender: 'action' },
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
			visible: false,
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
		// Display Course Table
		getCourses() {
			const path = 'http://localhost:5000/courses';
			axios.get(path)
				.then((res) => {
					let response = res.data.data.courseCatalog
					// console.log(response);

					// Retrieve Courses
					for (let i=0; i<response.length; i++) {
						let courseData = response[i];
						var template = {};
						template.key = i;
						template.courseId = courseData.Course_ID;
						template.Job_Role_Name = courseData.Course_Name;
						template.description = courseData.Course_Description;
						template.Department = courseData.Course_Category;
						template.status = courseData.Course_Status;
						template.type = courseData.Course_Type;
						
						// async let skillsData = this.getSkills(courseData.Course_Name);
						// console.log(skillsData);
						// if (skillsData) {
						// 	if (skillsData.data.code == 200) {
						// 		template.Skills = skillsData.data.data.courseSkills;
						// 	}
						// }
						// console.log(skillsData);
						this.table1Data.push(template);
					}
					console.log(this.table1Data);
					
				})
				.catch((error) => {
					// eslint-disable-next-line
					console.error(error);
				});
		},
		// Display Course Table

		handleOk(e) {
			console.log(e);
			this.visible = false;
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

			let formData = JSON.stringify({
				"skillsForUpdate": this.existingSkills,
				"courseId": this.selectedCourseId
			});
			console.log(formData);

			axios.post(path, {
				"updateInfo": formData,
			})
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

	},
	
	created() {
		this.getCourses();
	},
})

</script>

<style lang="scss">
</style>