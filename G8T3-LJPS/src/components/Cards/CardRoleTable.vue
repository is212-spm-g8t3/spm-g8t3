<template>

	<!-- Authors Table Card -->
	<a-card :bordered="false" class="header-solid h-full" :bodyStyle="{padding: 0,}">
		<template #title>
			<a-row v-if="page == 'Course'"type="flex" align="middle">
				<a-col :span="24" :md="12">
					<h5 class="font-semibold m-0">{{titleName}}</h5>
				</a-col>
				<a-col :span="24" :md="12" style="display: flex; align-items: center; justify-content: flex-end">
					<a-input-search
						v-model:value="search"
						placeholder="Search"
						style="width: 200px; margin-right: 20px"
					/>

					<a-radio-group v-model="statusRadioBtn" size="small">
						<a-radio-button value="All">ALL</a-radio-button>
						<a-radio-button value="Active">Active</a-radio-button>
						<a-radio-button value="Pending">Pending</a-radio-button>
						<a-radio-button value="Retired">Retired</a-radio-button>
					</a-radio-group>
				</a-col>
			</a-row>
			<a-row v-else type="flex" align="middle">
				<a-col :span="24" :md="12">
					<h5 class="font-semibold m-0">{{titleName}}</h5>
				</a-col>
				<a-col :span="24" :md="12" style="display: flex; align-items: center; justify-content: flex-end">
					<a-input-search
						v-model:value="search"
						placeholder="Search for Name"
						style="width: 200px; margin-right: 20px"
					/>
					
					<a-radio-group v-model="statusRadioBtn" size="small">
						<a-radio-button value="All">ALL</a-radio-button>
						<a-radio-button value="Active">ACTIVE</a-radio-button>
						<a-radio-button value="Inactive">INACTIVE</a-radio-button>
					</a-radio-group>
				</a-col>
			</a-row>
		</template>
		<a-table :columns="columns" :data-source="dataFilteredStatus" :pagination="true">

			<template slot="Job_Role_Name" slot-scope="Job_Role_Name">
				<div class="table-avatar-info">
					<a-avatar shape="square" style="background-color: #595959;"> {{Job_Role_Name.match(/\b(\w)/g).join('')}}</a-avatar>
					<!-- <a-avatar shape="square" :src="roleName.avatar" /> -->
					<div class="avatar-info" style="margin-top: 7px">
						<h6>{{ Job_Role_Name }}</h6>
					</div>
				</div>
			</template>
			
			<template v-if="page=='skills'" slot="roleName" slot-scope="roleName">
				<div class="table-avatar-info">
					<!-- <a-avatar shape="square" style="background-color: #595959;"> {{roleName.name.match(/\b(\w)/g).join('')}}</a-avatar> -->
					<!-- <a-avatar shape="square" :src="roleName.avatar" /> -->
					<div class="avatar-info" style="margin-top: 7px">
						<h6>{{ roleName.name }}</h6>
					</div>
				</div>
			</template>

			<template slot="Department" slot-scope="Department">
				<div class="author-info">
					<h6 class="m-0">{{ Department }}</h6>
					<!-- <h6 class="m-0">{{ func.type }}</h6>
					<p class="m-0 font-regular text-muted">{{ func.job }}</p> -->
				</div>
			</template>

			<template v-if="page=='skills'" slot="func" slot-scope="func">
				<div class="table-avatar-info">
					<!-- <a-avatar shape="square" style="background-color: #595959;"> {{roleName.name.match(/\b(\w)/g).join('')}}</a-avatar> -->
					<!-- <a-avatar shape="square" :src="roleName.avatar" /> -->
					<div class="avatar-info" style="margin-top: 7px">
						<h6>{{ func.type }}</h6>
					</div>
				</div>
			</template>

			<template slot="status" slot-scope="status">
				<a-tag v-if="page == 'Course'" class="tag-status" :class="status == 'Active' ? 'ant-tag-success' : 'ant-tag-muted'">
					{{ status == 'Active' ? "ACTIVE" : status == 'Pending' ? 'PENDING' : 'Retired' }}
				</a-tag>

				<a-tag v-else class="tag-status" :class="status == 'Active' ? 'ant-tag-success' : 'ant-tag-muted'">
					{{ status == 'Active' ? "ACTIVE" : "INACTIVE" }}
				</a-tag>
			</template>

			<template slot="Skills" slot-scope="Skills">
				<div class="author-info">
					<h6 class="m-0">{{ Skills.length }}</h6>
				</div>
			</template>

			<!-- <template slot="Type" slot-scope="type">
				<div class="author-info">
					<h6 class="m-0">{{ Skills.length }}</h6>
				</div>
			</template> -->

			<!-- Skill.vue -->
			<template slot="actionSkill" slot-scope="row">
				
				<a-button style="margin-right: 10px;" :data-id="row.key" @click="updateRoles(data[row.key])">
					Edit
				</a-button>
				
			</template>
			<!-- Skill.vue -->

			<template slot="action" slot-scope="row">
				<!-- <span>
					<a-icon type="eye" :style="{ color: '#87d068' }"/>
					<a-icon type="edit" :style="{ color: '#1890FF' }"/>
					<a-icon type="delete" :style="{color: '#F5222D'}" />
				</span> -->
				<!-- <span>
					<a-button shape="circle"  icon="edit"/>
					<a-button shape="circle"  icon="delete"  :style="{color: '#F5222D'}"/>
				</span> -->

				<div :style="{'display': 'flex'}">
					<a-button type="default" :data-id="row.key" @click="updateRoles(row)">
						Edit
					</a-button>
					<a-button class="deleteBtn" :style="{'border-color': '#ff4d4f', 'color': '#ff4d4f', 'margin-left': '10px'}" :data-id="row.key" @click="deleteRole(data[row.key])">
						Delete
					</a-button>
				</div>
			</template>

			<!-- Courses.vue -->
			<template slot="courseAction" slot-scope="row">
				<a-button type="default" :data-id="row.key" @click="updateModalCourse(data[row.key])">
					Edit Skills
				</a-button>
			</template>
			<!-- Courses.vue -->
			
			<div slot="expandedRowRender" slot-scope="record" style="margin: 0">
				{{ record.description }}<br><br>
				<div v-if="page=='roles'">

					<h6>SKILLS</h6>
					<ul>
						<li v-for="(each_skill, index) in record.Skills" :key="index">{{each_skill.Skill_Name}}</li>
					</ul>
				</div>
			</div>

		</a-table>
	</a-card>
	<!-- / Authors Table Card -->

</template>

<script>
import structuredClone from '@ungap/structured-clone';

export default ({
	props: {
		data: {
			type: Array,
			default: () => [],
		},
		columns: {
			type: Array,
			default: () => [],
		},
		titleName: {
			type: String,
			default: ""
		},
		page: {
			type: String,
			default: ""
		}
	},
	created(){
		console.log(this.data)
	},
	data() {
		return {
			// Active button for the "Authors" table's card header radio button group.
			statusRadioBtn: 'All',
			colorList: [],
			search: '',
		}
	},

	computed: {
		dataFilteredStatus: function() {
			if (this.statusRadioBtn != 'All') {
				if(this.page == "roles"){
					return this.data.filter(eachData => eachData.Status == this.statusRadioBtn)
				}
				return this.data.filter(eachData => eachData.status == this.statusRadioBtn)

			}
			if (this.search != '') {
				return this.data.filter(eachData => 
					eachData.Job_Role_Name.toLowerCase().includes(this.search.toLowerCase()) 
					|| eachData.Department.toLowerCase().includes(this.search.toLowerCase())); 
				}
			return this.data

		}
	},

	methods: {
		updateRoles(currentRowData) {
			this.$emit('updateRecord', structuredClone(currentRowData))
		},

		// For Courses.vue
		updateModalCourse(currentRowData) {
			this.$emit('updateCourse', structuredClone(currentRowData))
		},

		// For Skill.vue
		deleteSkill(currentRowData) {
			console.log(currentRowData);
		},

		// For Roles.vue
		deleteRole(currentRowData) {
			console.log(currentRowData);
		}
	},
})

</script>

<style scoped>
	.deleteBtn :hover {
		background-color: #ff4d4f;
		color: white;
	}

	.editIcon :hover {
		color: #1890FF;
		cursor: pointer;
	}

	.deleteIcon :hover {
		color: #F5222D;
		cursor: pointer;
	}
</style>