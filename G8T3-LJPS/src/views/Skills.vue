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
				<CardRoleTable
					:titleName="titleName"
					:data="table1Data"
					:columns="table1Columns"
				></CardRoleTable>
				<!-- / Authors Table Card -->

			</a-col>
			<!-- / Authors Table Column -->

		</a-row>
		<!-- / Authors Table -->

		<!-- / Create Role Modal Pop up -->
		<template>
			<div>
				<a-modal centered v-model="visible" title="Create Skill" @cancel="handleCancel" >
					
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
									<a-radio-button value="Active">Active</a-radio-button>
									<a-radio-button value="Inactive">Inactive</a-radio-button>
								</a-radio-group>
							</a-form-model-item>
						</a-row>
						<a-alert v-if="ifExistingRole" message="The skill that you have entered already exists!" type="error" show-icon />

					</a-form-model>
				</a-modal>
			</div>
		</template>
		<!-- / Create Role Modal Pop up -->

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
			dataIndex: 'roleName',
			scopedSlots: { customRender: 'roleName' },
		},
		{
			title: 'Type',
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
			// Display Skill Table
			getSkills() {
				const path = 'http://localhost:5000/skills';
				axios.get(path)
					.then((res) => {
						let response = res.data.data.skills
						// console.log(response);
						for (let i=0; i<response.length; i++) {
							var template = {
								key: '',
								roleName: {
									avatar: 'images/face-6' + '.jpeg',
									name: '',
								},
								description : '',
								func: {
									type: '',
								},
								status: '',
								created: '',
							}
							let skillData = response[i];
							template.key = i;
							template.roleName.name = skillData.Skill_Name;
							template.roleName.avatar = `images/face-${i}.jpg`;
							template.description = skillData.Skill_Description;
							template.func.job = skillData.Skill_Type;
							template.status = skillData.Status;
							template.created = new Date(skillData.Created_Date).toLocaleDateString();
							this.table1Data.push(template);
						}
					})
					.catch((error) => {
						// eslint-disable-next-line
						console.error(error);
					});
			},
			// Display Skill Table

			showModal() {
				this.visible = true;
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

						console.log(this.form)

						const path = 'http://localhost:5000/skills/addNewSkill';

						let formData = JSON.stringify(this.form);

						axios.post(path, {
							"skillFormData": formData,
						})
							.then((response) => {
								console.log(response);

								// Happy path, success creation
								if (response.data.code == 201) {
									message.success(response.data.message, 10);
									this.handleCancel();
									window.location.reload();
								}
							})
							.catch((error) => {
								console.log(error);
								this.ifExistingRole = true;
								this.loading = false;
							});
					} 

					// Form validation: Fail
					else {
						console.log('error submit!!');
						return false;
					}
				});
			},

			closeModal() {
				this.visible = false;
			},

			handleCancel(e) {
				this.visible = false;
				this.ifExistingRole = false;
				this.$refs.ruleForm.resetFields();
			},
		},
		
		created() {
    		this.getSkills();
  		},
	})

</script>

<style lang="scss">
</style>