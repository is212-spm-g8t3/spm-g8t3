<template>

	<!-- Authors Table Card -->
	<a-card :bordered="false" class="header-solid h-full" :bodyStyle="{padding: 0,}">
		<template #title>
			<a-row type="flex" align="middle">
				<a-col :span="24" :md="12">
					<h5 class="font-semibold m-0">{{titleName}}</h5>
				</a-col>
				<a-col :span="24" :md="12" style="display: flex; align-items: center; justify-content: flex-end">
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
					<!-- <a-avatar shape="square" style="background-color: #595959;"> {{roleName.name.match(/\b(\w)/g).join('')}}</a-avatar> -->
					<!-- <a-avatar shape="square" :src="roleName.avatar" /> -->
					<div class="avatar-info" style="margin-top: 7px">
						<h6>{{ Job_Role_Name }}</h6>
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

			<template slot="Status" slot-scope="Status">
				<a-tag class="tag-status" :class="Status == 'Active' ? 'ant-tag-success' : 'ant-tag-muted'">
					{{ Status == 'Active' ? "ACTIVE" : "INACTIVE" }}
				</a-tag>
			</template>

			<template slot="Skills" slot-scope="Skills">
				<div class="author-info">
					<h6 class="m-0">{{ Skills.length }}</h6>
				</div>
			</template>

			<template slot="action" slot-scope="row">
				<span>
					<a-icon type="eye" :style="{ color: '#87d068' }"/>
					<a-icon type="edit" :style="{ color: '#1890FF' }"/>
					<a-icon type="delete" :style="{color: '#F5222D'}" />
				</span>
				<!-- <span>
					<a-button shape="circle"  icon="eye" :style="{ color: '#87d068' }"/>
					<a-button shape="circle"  icon="edit"/>
					<a-button shape="circle"  icon="delete"  :style="{color: '#F5222D'}"/>
				</span> -->


				<a-button type="default" :data-id="row.key" @click="updateRoles(data[row.key])">
					Edit
				</a-button>
			</template>

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
		}
	},
	data() {
		return {
			// Active button for the "Authors" table's card header radio button group.
			statusRadioBtn: 'All',
			colorList: []
		}
	},

	computed: {
		dataFilteredStatus: function() {
			if (this.statusRadioBtn != 'All') {
				return this.data.filter(eachData => eachData.status == this.statusRadioBtn)
			}
			return this.data
		}
	},

	methods: {
		updateRoles(currentRowData) {
			this.$emit('updateRecord', structuredClone(currentRowData))
		},
	},
})

</script>