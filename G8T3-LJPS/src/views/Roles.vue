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
								<a-select
									mode="multiple"
									style="width: 100%"
									placeholder="Select"
								>
									<a-select-option v-for="(option, index) in skillsOptions" :key="index">
										{{ option }}
									</a-select-option>
								</a-select>
							</a-form-model-item>
						</a-row>
					</a-form-model>
				</a-modal>
			</div>
		</template>
		<!-- / Create Role Modal Pop up -->

		<!-- / Update Role Modal Pop up -->
		<template>
			<div>
				<a-modal centered v-model="isVisibleUpdate" title="Update Role" @cancel="handleCancel">

					<!-- <a-alert v-if="ifExistingRole" type="error" message="That is an existing role! Please enter another role." banner style="margin-bottom:20px;margin-top:0px"/> -->

					<a-form-model layout="vertical" ref="ruleForm" :model="updateForm" :rules="rules">
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

								<a-select
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
								</a-select>
							</a-form-model-item>
						</a-row>
					</a-form-model>
				</a-modal>
									
				<template slot="footer">
					<a-button key="back" @click="handleCancel">
					Cancel
					</a-button>
					<a-button key="submit" type="primary" :loading="loading" @click="handleCreate">
					Create
					</a-button>
				</template>
			</div>
		</template>
		<!-- / Update Role Modal Pop up -->

	</div>
</template>

<script>

// "Authors" table component.
import { FormModel } from 'ant-design-vue';
import Vue from "vue";
import CardRoleTable from '../components/Cards/CardRoleTable';
Vue.use(FormModel);

// "Authors" table list of columns and their properties.
const table1Columns = [
	{
		title: 'NAME',
		dataIndex: 'roleName',
		scopedSlots: { customRender: 'roleName' },
	},
	{
		title: 'DEPARTMENT',
		dataIndex: 'func',
		scopedSlots: { customRender: 'func' },
	},
	{
		title: 'STATUS',
		dataIndex: 'status',
		scopedSlots: { customRender: 'status' },
	},
	{
		title: 'CREATED',
		dataIndex: 'created',
		class: 'text-muted',
	},
	{
		title: '',
		scopedSlots: { customRender: 'editBtn' },
		width: 50,
	},
];

// "Authors" table list of rows and their properties.
const table1Data = [
	{
		key: '1',
		roleName: {
			avatar: 'images/face-2.jpg',
			name: 'Front-End Engineer',
		},
		func: {
			department: 'Technology',
			job: 'Developer',
		},
		status: "Active",
		created: '23/04/18',
	},
	{
		key: '2',
		roleName: {
			avatar: 'images/face-3.jpg',
			name: 'Back-End Engineer',
		},
		func: {
			department: 'Technology',
			job: 'Developer',
		},
		status: "Inactive",
		created: '23/12/20',
	},
	{
		key: '3',
		roleName: {
			avatar: 'images/face-1.jpg',
			name: 'Data Scientist',
		},
		func: {
			department: 'Technology',
			job: 'Analyst',
		},
		status: "Active",
		created: '13/04/19',
	},
	{
		key: '4',
		roleName: {
			avatar: 'images/face-4.jpg',
			name: 'UI/UX Designer',
		},
		func: {
			department: 'Technology',
			job: 'Design',
		},
		status: "Active",
		created: '03/04/21',
	},
	{
		key: '5',
		roleName: {
			avatar: 'images/face-5.jpeg',
			name: 'Business Analyst',
		},
		func: {
			department: 'Technology',
			job: 'Analyst',
		},
		status: "Inactive",
		created: '23/03/20',
	},
	{
		key: '6',
		roleName: {
			avatar: 'images/face-6.jpeg',
			name: 'Project Manager',
		},
		func: {
			department: 'Technology',
			job: 'Manager',
		},
		status: "Active",
		created: '14/04/17',
	},
];


export default ({
	components: {
		CardRoleTable,
	},
	data() {
		return {
			// Associating "Authors" table data with its corresponding property.
			table1Data: table1Data,

			// Associating "Authors" table columns with its corresponding property.
			table1Columns: table1Columns,
			titleName: "Roles",
			ifExistingRole: false,
			ifSuccessfulCreation: false,
			ifErrorCreation: false,
			visible: false,
			loading: false,
			modalLayout: "vertical",
			skillsOptions: ['Skill 1', 'Skill 2', 'Skill 3'],
			form: {
				name: '',
				department: '',
				description: '',
				skills: []
			},
			rules: {
				name: [{ required: true, message: 'Name is required!'}],
				department: [{ required: true, message: 'Department is required!'}],
				description: [{ required: true, message: 'Description is required!'}],
				skills: [{type:'array', required: true, message: 'Please input at least one skill!'}]
			},

			// Update Modal Pop up
			isVisibleUpdate: false,
			updateForm: {
				name: '',
				department: '',
				description: '',
				skills: []
			},
			skillsList: ['Apples', 'Nails', 'Bananas', 'Helicopters'],
			// Update Modal Pop up
		}
	},
	methods: {
		showModal() {
			this.visible = true;
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
					this.visible = false;
				} else {
					console.log('error submit!!');
					return false;
				}
			});
		},

		handleCancel(e) {
			this.visible = false;
			this.$refs.ruleForm.resetFields();
		},

		// Update Modal //

		updateModalRecord(value) {
			console.log(value);
			this.updateForm.name = value.roleName.name;
			this.updateForm.department = value.func.department;
			this.updateForm.description = "Insert description, value.xxx.description";
			this.updateForm.skills = ['Apples', 'Nails'];
			this.isVisibleUpdate = true;
		},

		handleDeselect(value) {
			const index = this.updateForm.skills.indexOf(value);
			if (index > -1) { // only splice array when item is found
				this.updateForm.skills.splice(index, 1); // 2nd parameter means remove one item only
			}
		},

		handleSelect(value) {
			this.updateForm.skills.push(this.filteredOptions[value]);
		},

		// Update Modal //
	},

	computed: {

		// Update Modal //
		filteredOptions() {
			return this.skillsList.filter(o => !this.updateForm.skills.includes(o))
		},

		// Update Modal //
	}
})

</script>

<style lang="scss">
</style>