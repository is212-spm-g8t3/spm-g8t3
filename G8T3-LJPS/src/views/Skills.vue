<!-- 
	This is the tables page, it uses the dashboard layout in: 
	"./layouts/Dashboard.vue" .
 -->

<template>
	<div>
		<!-- Title -->
		<a-row :gutter="24">
			<a-col :span="24" :md="12" class="mb-12">
				<h3 style="margin-left: 12px">Skill Management</h3>
			</a-col>
			<a-col :span="24" :md="12" class="mb-12" style="display: flex; align-items: center; justify-content: flex-end">
				<a-button @click="showModal" type="dark" icon="plus" style="margin-right: 24px">
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

		<!-- / Create Skill Modal Pop up -->
		<template>
			<div>
				<a-modal centered v-model="visible" title="Create Skill" @cancel="handleCancel">

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
								<a-form-model-item slot="" label="Name" prop="name">
									<a-input v-model="form.name" placeholder="E.g. Critical Thinking" />
								</a-form-model-item>
							</a-col>
							<a-col :span="12">
								<a-form-model-item label="Type" prop="type">
									<a-select
										v-model:value="form.type"
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
								<a-input v-model="form.description" type="textarea" />
							</a-form-model-item>
						</a-row>
						<a-row>
							<a-form-model-item label="Status" prop="status">
								<a-radio-group v-model:value="form.status">
									<a-radio-button value="active">Active</a-radio-button>
									<a-radio-button value="inactive">Inactive</a-radio-button>
								</a-radio-group>
							</a-form-model-item>
						</a-row>
					</a-form-model>
				</a-modal>
			</div>
		</template>
		<!-- / Create Skill Modal Pop up -->

	</div>
</template>

<script>

	import CardSkillTable from '../components/Cards/CardSkillTable' ;
	import axios from 'axios';
	
			
	
	const skillCols = [
		{
			title: 'Skill Name',
			dataIndex: 'Skill_Name',
			scopedSlots: { customRender: 'Skill_Name' },
		},
		{
			title: 'Type',
			dataIndex: 'func',
			scopedSlots: { customRender: 'func' },
		},
	]


	// "Authors" table list of rows and their properties.
	const table1Data = [
		{
			key: '1',
			roleName: {
				avatar: 'images/face-2.jpg',
				name: 'Agile Software Development',
			},
			func: {
				skill: 'Technology',
				job: 'Design and Architecture',
			},
			status: "active",
			created: '23/04/18',
		},
		{
			key: '2',
			roleName: {
				avatar: 'images/face-3.jpg',
				name: 'Cloud Computing',
			},
			func: {
				skill: 'Technology',
				job: 'Development and Implementation',
			},
			status: "inactive",
			created: '23/12/20',
		},
		{
			key: '3',
			roleName: {
				avatar: 'images/face-1.jpg',
				name: 'Data Analytics',
			},
			func: {
				skill: 'Technology',
				job: 'Business Development',
			},
			status: "active",
			created: '13/04/19',
		},
		{
			key: '4',
			roleName: {
				avatar: 'images/face-4.jpg',
				name: 'Data Visualisation',
			},
			func: {
				skill: 'Technology',
				job: 'Development and Implementation',
			},
			status: "active",
			created: '03/04/21',
		},
		{
			key: '5',
			roleName: {
				avatar: 'images/face-5.jpeg',
				name: 'Software Design',
			},
			func: {
				skill: 'Technology',
				job: 'Design and Architecture',
			},
			status: "inactive",
			created: '23/03/20',
		},
		{
			key: '6',
			roleName: {
				avatar: 'images/face-6.jpeg',
				name: 'Quality Assurance',
			},
			func: {
				skill: 'Technology',
				job: 'Development and Implementation',
			},
			status: "active",
			created: '14/04/17',
		},
	];
	
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
				ifExistingRole: false,
				ifSuccessfulCreation: false,
				ifErrorCreation: false,
				loading: false,
				modalLayout: "vertical",
				form: {
					name: '',
					type: '',
					description: '',
					status: '',
				},
				rules: {
					name: [{ required: true, message: 'Name is required!'}],
					type: [{ required: true, message: 'Type is required!'}],
					description: [{ required: true, message: 'Description is required!'}],
					status: [{required: true, message: 'Status is required!'}]
				},
				options: [
					{
						value: 'softskill',
						label: 'Soft Skill',
					}, 
					{
						value: 'hardskill',
						label: 'Hard Skill',
					}, 
				],
			}
		},
		methods: {
			showModal() {
			this.visible = true;
			},

			getSkills() {
			const path = 'http://localhost:5000/skills';
			axios.get(path)
				.then((res) => {
					console.log(res.data.data.skills)
					this.skillsData = res.data.data.skills;
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
			handleCreate(e) {
				console.log(e);
				// Perform check with database whether role is in database
				// If not, add to database
				// this.loading = false and this.visible = false
				// Show green alert bar if added successfully

				this.$refs.ruleForm.validate(valid => {
					// Form validation: Success
					if (valid) {
						this.loading = true;
						this.visible = false;

						console.log(this.form)
					} 

					// Form validation: Fail
					else {
						console.log('error submit!!');
						return false;
					}
				});
			},

			handleCancel(e) {
				this.visible = false;
				this.$refs.ruleForm.resetFields();
			},

			//TODO: Show skills related to selected role.

			//TODO: Show attained and not attained skills. (show status)
		},
	created() {
    	this.getSkills();
  	},
	})

</script>

<style lang="scss">
</style>