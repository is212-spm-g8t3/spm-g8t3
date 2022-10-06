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

		<!-- / Create Role Modal Pop up -->
		<template>
			<div>
				<a-modal centered v-model="visible" title="Create Skill" @ok="handleOk">
					<p>Some contents...</p>
					<p>Some contents...</p>
					<p>Some contents...</p>
				</a-modal>
			</div>
		</template>
		<!-- / Create Role Modal Pop up -->

	</div>
</template>

<script>

	// "Authors" table component.
	import CardSkillTable from '../components/Cards/CardSkillTable' ;
	import axios from 'axios';
	
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
				name: 'Agile Software Development',
			},
			func: {
				department: 'Technology',
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
				department: 'Technology',
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
				department: 'Technology',
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
				department: 'Technology',
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
				department: 'Technology',
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
				department: 'Technology',
				job: 'Development and Implementation',
			},
			status: "active",
			created: '14/04/17',
		},
	];
			
	
	const skillCols = [
		{
			title: 'Skill Name',
			dataIndex: 'Skill_Name',
			scopedSlots: { customRender: 'Skill_Name' },
		},
		{
			title: 'Skill Description',
			dataIndex: 'Skill_Description',
			scopedSlots: { customRender: 'Skill_Description' },
		},
	]


	
	export default ({
		components: {
			CardSkillTable,
		},
		data() {
			return {

				

				skillsData: [], //initialise skills data table
				// Associating "Authors" table data with its corresponding property.
				//table1Data: skillsData,

				// Associating "Authors" table columns with its corresponding property.
				table1Columns: skillCols,
				visible: false,
				titleName: "Skills",

				
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