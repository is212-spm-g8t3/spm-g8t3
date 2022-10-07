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

			<template slot="Job_Role_Name" slot-scope="Job_Role_Name">
				<div class="table-avatar-info">
					<!--<a-avatar shape="square" :src="Job_Role_Name.avatar" />-->
					<div class="avatar-info" style="margin-top: 7px">
						<h6>{{ Job_Role_Name }}</h6>
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
				<a-button type="link" :data-id="row.key">
					<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
						<path class="fill-gray-7" d="M13.5858 3.58579C14.3668 2.80474 15.6332 2.80474 16.4142 3.58579C17.1953 4.36683 17.1953 5.63316 16.4142 6.41421L15.6213 7.20711L12.7929 4.37868L13.5858 3.58579Z"/>
						<path class="fill-gray-7" d="M11.3787 5.79289L3 14.1716V17H5.82842L14.2071 8.62132L11.3787 5.79289Z"/>
					</svg>
				</a-button>
			</template>

		</a-table>
	</a-card>
	<!-- / Authors Table Card -->

</template>

<script>

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
		}
	})

</script>