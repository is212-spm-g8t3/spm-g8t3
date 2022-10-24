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

		<!-- / Update Course Modal Pop up -->
		<template>
			<div>
				<a-modal centered v-model="isVisibleUpdate" title="Update Skill" @cancel="handleCancel">
									
					<template slot="footer">
						<a-button key="back" @click="handleUpdateCancel">
						Cancel
						</a-button>
						<a-button key="submit" type="primary" :loading="loading" @click="handleUpdate">
						Update
						</a-button>
					</template>

					<a-form-model layout="vertical" ref="ruleUpdateForm" :model="updateForm" :rules="rules">
						<a-row :gutter="16">
							<a-col :span="12">
								<a-form-model-item slot="" label="Name" prop="name">
									<a-input v-model="updateForm.name" placeholder="E.g. Critical Thinking" />
								</a-form-model-item>
							</a-col>
							<a-col :span="12">
								<a-form-model-item label="Type" prop="type">
									<a-select
										v-model:value="updateForm.type"
										show-search
										placeholder="Select skill type"
										:options="options"
									>
									</a-select>
								</a-form-model-item>
							</a-col>
						</a-row>

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
import { SlowBuffer } from 'buffer';
	
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
			ifExistingRole: false,
			ifSuccessfulCreation: false,
			ifErrorCreation: false,
			loading: false,
			modalLayout: "vertical",
			rules: {
				name: [{ required: true, message: 'Name is required!'}],
				type: [{ required: true, message: 'Type is required!'}],
				description: [{ required: true, message: 'Description is required!'}],
				status: [{required: true, message: 'Status is required!'}]
			},
			options: [
				{
					value: 'Soft Skill',
					label: 'Soft Skill',
				}, 
				{
					value: 'Hard Skill',
					label: 'Hard Skill',
				}, 
			],

			// Update Modal Pop up
			isVisibleUpdate: false,
			updateForm: {
				id: 0,
				name: '',
				type: '',
				description: '',
				status: ''
			},
			isUpdateError: false,
			updateErrorMsg: 'Default Error Message'
			// Update Modal Pop up
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

		handleCancel(e) {
			this.visible = false;
			this.ifExistingRole = false;
			this.$refs.ruleForm.resetFields();
		},

		// Update Modal //

		updateModalRecord(value) {
			// console.log(value);
			this.updateForm.id = value.skillID;
			this.updateForm.name = value.Job_Role_Name;
			this.updateForm.type = value.Department;
			this.updateForm.description = value.description;
			this.updateForm.status = value.status
			this.isVisibleUpdate = true;
		},

		handleUpdate(e) {
			// Perform check with database whether role is in database
			// If not, add to database
			// this.loading = false and this.visible = false
			// Show green alert bar if added successfully

			this.$refs.ruleUpdateForm.validate(valid => {
				// Form validation: Success
				if (valid) {
					this.loading = true;

					console.log(this.updateForm)

					const path = 'http://localhost:5000/skills/updateSkill';

					let formData = JSON.stringify(this.updateForm);

					axios.post(path, {
						"skillFormData": formData,
					})
						.then((response) => {
							console.log(response);

							// Happy path, success creation
							if (response.data.code == 201) {
								message.success(response.data.message, 10);
								this.handleUpdateCancel();
								location.reload();
							}

						})
						.catch((error) => {
							console.log(error);
							console.log("error error");
							this.updateErrorMsg = error.response.data.message
							console.log(this.updateErrorMsg)
							this.isUpdateError = true;
							this.loading = false;
						});
				} 

				// Form validation: Fail
				else {
					console.log('There is an error when submitting the form');
					return false;
				}
			});
		},

		handleUpdateCancel(e) {
			this.isVisibleUpdate = false;
		},

	},
	
	created() {
		this.getCourses();
	},
})

</script>

<style lang="scss">
</style>