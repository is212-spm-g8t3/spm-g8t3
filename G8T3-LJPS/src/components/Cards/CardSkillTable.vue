<template>

	<!-- Authors Table Card -->
	<a-card :bordered="false" class="header-solid h-full" :bodyStyle="{padding: 0,}">
		<template #title>
			<a-row type="flex" align="middle">
				<a-col :span="24" :md="12">
					<h5 class="font-semibold m-0">{{titleName}}</h5>
				</a-col>
				<!-- <a-col :span="24" :md="12" style="display: flex; align-items: center; justify-content: flex-end">
					<a-radio-group v-model="statusRadioBtn" size="small">
						<a-radio-button value="all">ALL</a-radio-button>
						<a-radio-button value="active">ATTAINED</a-radio-button>
						<a-radio-button value="inactive">NOT ATTAINED</a-radio-button>
					</a-radio-group>
				</a-col> -->
			</a-row>
		</template>
		<a-table :columns="columns" :data-source="dataFilteredStatus" :pagination="true">

			<template slot="Skill_Name" slot-scope="Skill_Name">
				<div class="table-avatar-info">
					<!-- <a-avatar shape="square" :src="Skill_Name.avatar" /> -->
					<div class="avatar-info" style="margin-top: 7px">
						<h6>{{ Skill_Name }}</h6>
					</div>
				</div>
			</template>

			<template slot="func" slot-scope="func">
				<div class="author-info">
					<h6 class="m-0">{{ func.department }}</h6>
					<p class="m-0 font-regular text-muted">{{ func.job }}</p>
				</div>
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