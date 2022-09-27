<!-- 
	This is the tables page, it uses the dashboard layout in: 
	"./layouts/Dashboard.vue" .
 -->

<template>
	<div>
		<!-- Title -->
		<a-row :gutter="24">
			<a-col :span="24" :md="12" class="mb-12">
				<h3 style="margin-left: 12px">Role Management</h3>
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
				<a-modal centered v-model="visible" title="Create Role" @ok="handleOk">
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
	import CardRoleTable from '../components/Cards/CardRoleTable' ;
	
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
			status: "active",
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
			status: "inactive",
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
			status: "active",
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
			status: "active",
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
			status: "inactive",
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
			status: "active",
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
				visible: false,
				titleName: "Roles"
			}
		},
		methods: {
			showModal() {
			this.visible = true;
			},
			handleOk(e) {
			console.log(e);
			this.visible = false;
			},
		},
	})

</script>

<style lang="scss">
</style>