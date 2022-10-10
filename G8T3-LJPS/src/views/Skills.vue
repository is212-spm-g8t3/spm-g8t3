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
				<a-modal centered v-model="visible" title="Create Skill" @ok="handleOk">
					<p>Some contents...</p>
					<p>Some contents...</p>
					<p>Some contents...</p>
				</a-modal>
			</div>
		</template>
		<!-- / Create Skill Modal Pop up -->

	</div>
</template>

<script>

	import CardSkillTable from '../components/Cards/CardSkillTable' ;
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

			getSkills() {
			const path = 'http://localhost:5000/skills';
			axios.get(path)
				.then((res) => {
					this.skillsData = res.data.data.skills
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
		},
	created() {
    	this.getSkills();
  	},
	})

</script>

<style lang="scss">
</style>