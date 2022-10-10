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
						<a-radio-button value="all">ALL</a-radio-button>
						<a-radio-button value="active">ACTIVE</a-radio-button>
						<a-radio-button value="inactive">INACTIVE</a-radio-button>
					</a-radio-group>
				</a-col>
			</a-row>
		</template>
		<a-table :columns="columns" :data-source="dataFilteredStatus" :pagination="true">

			<template slot="roleName" slot-scope="roleName">
				<div class="table-avatar-info">
					<a-avatar shape="square" :src="roleName.avatar" />
					<div class="avatar-info" style="margin-top: 7px">
						<h6>{{ roleName.name }}</h6>
					</div>
				</div>
			</template>

			<template slot="func" slot-scope="func">
				<div class="author-info">
					<h6 class="m-0">{{ func.department }}</h6>
					<p class="m-0 font-regular text-muted">{{ func.job }}</p>
				</div>
			</template>

			<template slot="status" slot-scope="status">
				<a-tag class="tag-status" :class="status == 'active' ? 'ant-tag-success' : 'ant-tag-muted'">
					{{ status == 'active' ? "ACTIVE" : "INACTIVE" }}
				</a-tag>
			</template>

			<template slot="editBtn" slot-scope="row">
				<a-button type="default" :data-id="row.key" @click="updateRoles(data[row.key-1])">
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
			statusRadioBtn: 'all',
		}
	},

	computed: {
		dataFilteredStatus: function() {
			if (this.statusRadioBtn != 'all') {
				return this.data.filter(eachData => eachData.status == this.statusRadioBtn)
			}
			return this.data
		}
	},

	methods: {
		updateRoles(currentRowData) {
			this.$emit('updateRecord', structuredClone(currentRowData))
		}
	}
})

</script>