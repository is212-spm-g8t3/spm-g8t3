

<!-- 
	This is the tables page, it uses the dashboard layout in: 
	"./layouts/Dashboard.vue" .
 -->

 <template>
	<div>
		<a-alert v-if="ifSuccessfulCreation" message="New role has been created successfully!" type="success" show-icon class="mb-15" closable/>
		<a-alert v-if="ifErrorCreation" message="There was an error in the creation of  the role. Please contact IT for help." type="error" show-icon class="mb-15" closable/>
		
		<!-- Title -->
		<a-row :gutter="24">
			<a-col :span="24" :md="12" class="mb-12">
				<h3 style="margin-left: 12px">Role Management</h3>
			</a-col>
			<a-col :span="24" :md="12" class="mb-12" style="display: flex; align-items: center; justify-content: flex-end">
				<!-- style="margin-right: 24px" -->
				<a-button @click="showModal" type="dark" icon="plus">
					Create
				</a-button>
			</a-col>
		</a-row>
		<!-- / Title -->

		<a-row :gutter="24" type="flex">

			<a-col :span="24" class="mb-24">

				<CardRoleTable
					:titleName="titleName"
					:data="rolesData"
					:columns="tableColumns"
					page="roles"
					@updateRecord="updateModalRecord"
				>
				</CardRoleTable>
			</a-col>

		</a-row>

		<!-- / Create Role Modal Pop up -->
		<template>
			<div>
				<a-modal centered v-model="visible" title="Create Role" @cancel="handleCancel">

					<a-alert v-if="ifExistingRole" type="error" message="That is an existing role! Please enter another role." banner style="margin-bottom:20px;margin-top:0px"/>
					
					<template slot="footer">
						<a-button key="back" @click="handleCancel">
						Cancel
						</a-button>
						<a-button key="submit" type="primary" :loading="loading" @click="handleCreate">
						Create
						</a-button>
					</template>

					<a-form-model layout="vertical" ref="ruleForm" :model="form" :rules="rules">
						<Alert 
							type="error"
							:message="createErrorMessage" 
							:visible="createErrorVisible"
							:closable="false"></Alert>
						<a-row :gutter="16">
							<a-col :span="12">
								<a-form-model-item slot="" label="Role Name" prop="name">
									<a-input v-model="form.name" placeholder="E.g. Software Developer" />
								</a-form-model-item>
							</a-col>
							<a-col :span="12">
								<a-form-model-item label="Department" prop="department">
									<a-input v-model="form.department" placeholder="E.g. Technology" />
								</a-form-model-item>
							</a-col>
						</a-row>

						<a-row>
							<a-form-model-item label="Role Description" prop="description">
								<a-input v-model="form.description" type="textarea" />
							</a-form-model-item>
						</a-row>
						<a-row>
							<a-form-model-item label="Skills" prop="skills">
									<!-- @value="form.skills" -->
									<!-- @change="handleSkillsChange" -->
								<a-select
									v-model="form.skills"
									show-search
									mode="multiple"
									style="width: 100%"
									placeholder="Select Skill"
									:filter-option="filterOption"
								>
									<!-- :default-value="[3,2]" -->
									<a-select-option v-for="option in skillsData" :key="option.Skill_ID" :value="option.Skill_ID">
										{{ option.Skill_Name }}
									</a-select-option>
								</a-select>
							</a-form-model-item>
						</a-row>
						<a-row>
							<a-form-model-item label="Status" prop="status">
								<a-radio-group v-model="form.status">
									<a-radio-button value="Active">Active</a-radio-button>
									<a-radio-button value="Inactive">Inactive</a-radio-button>
								</a-radio-group>
							</a-form-model-item>
						</a-row>
					</a-form-model>
				</a-modal>
			</div>
		</template>
		<!-- / Create Role Modal Pop up -->

		<!-- <a-alert v-if="ifExistingRole" type="error" message="That is an existing role! Please enter another role." banner style="margin-bottom:20px;margin-top:0px"/> -->
		
		<!-- / Update Role Modal Pop up -->
		<template>
			<div>
				<a-modal centered v-model="isVisibleUpdate" title="Update Role" @cancel="handleCancel">

					<a-form-model layout="vertical" ref="ruleForm" :model="updateForm" :rules="rules">

						<Alert 
							type="error"
							:message="updateErrorMessage" 
							:visible="updateErrorVisible"
							:closable="false"></Alert>

						<a-row :gutter="16">
							<a-col :span="12">
								<a-form-model-item slot="" label="Role Name" prop="name">
									<a-input v-model="updateForm.name" placeholder="E.g. Software Developer" />
								</a-form-model-item>
							</a-col>
							<a-col :span="12">
								<a-form-model-item label="Department" prop="department">
									<a-input v-model="updateForm.department" placeholder="E.g. Technology" />
								</a-form-model-item>
							</a-col>
						</a-row>

						<a-row>
							<a-form-model-item label="Role Description" prop="description">
								<a-input v-model="updateForm.description" type="textarea" />
							</a-form-model-item>
						</a-row>
						<a-row>
							<a-form-model-item label="Skills" prop="skills">

								<!-- <a-select
									:value="updateForm.skills"
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
								</a-select> -->

								<a-select
									v-model="updateForm.skills"
									mode="multiple"
									placeholder="Select Skills"
									style="width: 100%"
									show-search
									:filter-option="filterOption"
									@change="checkSkills()"
								>
									<!-- :default-value="[3,2]" -->
									<a-select-option v-for="option in skillsData" :key="option.Skill_ID" :value="option.Skill_ID">
										{{ option.Skill_Name }}
									</a-select-option>
								</a-select>
							</a-form-model-item>
						</a-row>
						<a-row>
							<a-form-model-item label="Status" prop="status">
								<a-radio-group v-model="updateForm.status">
									<a-radio-button value="Active">Active</a-radio-button>
									<a-radio-button value="Inactive">Inactive</a-radio-button>
								</a-radio-group>
							</a-form-model-item>
						</a-row>
					</a-form-model>

					<template slot="footer">
						<a-button key="back" @click="handleCancel">
						Cancel
						</a-button>
						<a-button key="submit" type="primary" :loading="loading" @click="handleUpdate">
						Update
						</a-button>
					</template>
				</a-modal>
									
				
			</div>
		</template>
		<!-- / Update Role Modal Pop up -->

	</div>
</template>

<script>
	import Vue from "vue";
	import axios from 'axios';
	import CardRoleTable from '../components/Cards/CardRoleTable' ;
	import Alert from '../components/Alert/Alert' ;
	import { FormModel } from 'ant-design-vue';
	Vue.use(FormModel);
	
	const tableColumns = [
		{
			title: 'NAME',
			dataIndex: 'Job_Role_Name',
			scopedSlots: { customRender: 'Job_Role_Name' },
		},
		{
			title: 'DEPARTMENT',
			dataIndex: 'Department',
			scopedSlots: { customRender: 'Department' },
		},
		{
			title: 'STATUS',
			dataIndex: 'Status',
			scopedSlots: { customRender: 'status' },
		},
		{
			title: 'SKILLS COUNT',
			dataIndex: 'Skills',
			scopedSlots: { customRender: 'Skills' },
			align: "center"
		},
		{
			title: 'ACTIONS',
			scopedSlots: { customRender: 'action' },
			width: 50,
			align: "center"
		},
	];

	
	export default ({
		components: {
			CardRoleTable,
			Alert
		},
		data() {
			return {
				rolesData: [],

				// Associating "Authors" table columns with its corresponding property.
				tableColumns: tableColumns,
				titleName: "Roles",
				ifExistingRole: false,
				ifSuccessfulCreation: false,
				ifErrorCreation: false,
				visible: false,
				loading: false,
				modalLayout: "vertical",
				skillsData: [], // Make ID tagged to skills
				form: {
					name: '',
					department: '',
					description: '',
					skills: [],
					status: ""
				},
				rules: {
					name: [{ required: true, message: 'Name is required!'}],
					department: [{ required: true, message: 'Department is required!'}],
					description: [{ required: true, message: 'Description is required!'}],
					skills: [{type:'array', required: true, min: 1, message: 'Please input at least one skill!'}]
				},
				createErrorVisible: false,
				createErrorMessage: "",

				isVisibleUpdate: false,
				updateForm: {
					id: 0,
					name: '',
					department: '',
					description: '',
					status: '',
					skills:[]
				},
			
				updateErrorVisible: false,
				updateErrorMessage: "",
			}
		},
		created(){
			this.getAllSkills();
			this.getRolesData();
			console.log(this.rolesData)
		},
		methods: {
			checkSkills(){
				console.log(this.updateForm)
			},
			showModal() {
				this.visible = true;
			},

			getRolesData(){
				const path = 'http://localhost:5000/getRolesWithSkills';
				axios.get(path)
					.then((res) => {
						this.rolesData = [];
						console.log(res.data)
						var allData = res.data.data
						var sortedData = {}
						for(var each_row of allData){
							if(!sortedData.hasOwnProperty(each_row.Job_Role_ID)){
								sortedData[each_row.Job_Role_ID] = {
									"key": each_row.Job_Role_ID,
									"Job_Role_ID": each_row.Job_Role_ID,
									"Job_Role_Name": each_row.Job_Role_Name,
									"description": each_row.Job_Role_Description,
									"Department": each_row.Department,
									"Status": each_row.Status,
									"Skills": [{
											"Skill_ID": each_row.Skill_ID,
											"Skill_Name": each_row.Skill_Name
										}
									]
								}
							} else {
								sortedData[each_row.Job_Role_ID]["Skills"].push(
									{
										"Skill_ID": each_row.Skill_ID,
										"Skill_Name": each_row.Skill_Name
									}
								)
							}
						}
						console.log(sortedData)

						Object.values(sortedData).forEach(val => {
							this.rolesData.push(val)
						});
					})
					.catch((error) => {
						console.log(error);
						console.error(error.response.data);
					});
			},

			handleCreate(e) {
				console.log(e);
				// Perform check with database whether role is in database
				// If not, add to database
				// this.loading = false and this.visible = false
				// Show green alert bar if added successfully

				this.$refs.ruleForm.validate(valid => {
					if (valid) {
						this.loading = true;

						const path = 'http://localhost:5000/createRole';
						axios.post(path, this.form, 
							{headers:{"Content-Type" : "application/json"}})
						.then((res) => {
							console.log(res)
							this.getRolesData();
      						this.$message.success('Role created successfully!');
							this.handleCancel();
							this.visible = false;
						})
						.catch((error) => {
							// eslint-disable-next-line
							console.log(error);
							console.error(error.response.data);
							this.createErrorVisible = true;
							this.createErrorMessage = error.response.data.message;
						});
						this.loading = false;

					} else {
						console.log('error submit!!');
						return false;
					}
				});
			},

			handleUpdate(e) {
				console.log(e);
				// Perform check with database whether role is in database
				// If yes, update database
				// this.loading = false and this.visible = false
				// Show green alert bar if added successfully

				this.$refs.ruleForm.validate(valid => {
					if (valid) {
						this.loading = true;
						console.log(this.updateForm)

						const path = 'http://localhost:5000/updateRole';
						axios.post(path, this.updateForm, 
							{headers:{"Content-Type" : "application/json"}})
						.then((res) => {
							console.log(res)
							// for(var each_row in this.rolesData){
							// 	if(each_row["key"] == this.updateForm.id){
							// 		each_row["Job_Role_Name"] = this.updateForm.name
							// 		each_row["Department"] = this.updateForm.department
							// 		each_row["description"] = this.updateForm.description
							// 		each_row["Status"] = this.updateForm.status
							// 		console.log(this.updateForm.skills)
							// 		each_row["Skills"] = this.updateForm.skills
							// 	}
							// }

							// console.log(this.rolesData)
							this.getRolesData();

      						this.$message.success('Role updated successfully!');
							this.handleCancel();
							// this.isVisibleUpdate = false;
						})
						.catch((error) => {
							// eslint-disable-next-line
							console.log(error);
							console.error(error.response.data);
							this.updateErrorVisible = true;
							if(error.hasOwnProperty("response")){
								// this.$message.error('Error updating role. Please contact support.');
								this.updateErrorMessage = error.response.data.message;
							} else {
								this.updateErrorMessage = 'Error updating role. Please contact support.';
							}

						});
						this.loading = false;

					} else {
						console.log('error submit!!');
						return false;
					}
				});
			},

			handleCancel() {
				this.visible = false;
				this.isVisibleUpdate = false;
				this.createErrorVisible = false;
				this.createErrorMessage = "";
				this.updateErrorVisible = false;
				this.updateErrorMessage = "";
				// this.form.skills = [];
      			this.$refs.ruleForm.resetFields();
      			// this.$refs.formUpdate.resetFields();
			},

			getAllSkills(){
				const path = 'http://localhost:5000/skills';
				axios.get(path)
					.then((res) => {
						this.skillsData = res.data.data.skills
						console.log(this.skillsData)
					})
					.catch((error) => {
						// eslint-disable-next-line
						console.error(error);
					});
			
			},

			filterOption(input, option) {
				return (
					option.componentOptions.children[0].text.toLowerCase().indexOf(input.toLowerCase()) >= 0
				);
			},

			// Edit Roles

			// handleSkillsChange(value){
			// 	// console.log(`selected ${value}`);
			// 	console.log(value);
			// 	this.form.skills = value;
			// },

			updateModalRecord(value) {
				console.log(value);
				this.updateForm.id = value.Job_Role_ID
				this.updateForm.name = value.Job_Role_Name;
				this.updateForm.department = value.Department;
				this.updateForm.description = value.description;
				this.updateForm.skills = [];
				for(var each_skill of value.Skills){
					this.updateForm.skills.push(each_skill.Skill_ID);
				}
				this.updateForm.status = value.Status
				this.isVisibleUpdate = true;
			},

			// handleDeselect(value) {
			// const index = this.updateForm.skills.indexOf(value);
			// if (index > -1) { // only splice array when item is found
			// 	this.updateForm.skills.splice(index, 1); // 2nd parameter means remove one item only
			// }
			// },

			// handleSelect(value) {
			// this.updateForm.skills.push(this.filteredOptions[value]);
			// },

	},

	computed: {

			// Update Modal //
			// filteredOptions() {
			// 	return this.skillsList.filter(o => !this.updateForm.skills.includes(o))
			// },
		},
	})

</script>

<style lang="scss">
</style>