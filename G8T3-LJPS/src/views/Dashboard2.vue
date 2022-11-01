<!-- 
	This is the dashboard page, it uses the dashboard layout in: 
	"./layouts/Dashboard.vue" .
 -->

 <template>
	<div>
		<!-- Title -->
		<a-row :gutter="24">
			<a-col :span="24" class="mb-12">
				<h3 style="margin-left: 12px">My Learning</h3>
			</a-col>
		</a-row>
		<!-- / Title -->

		<!-- Cards -->
		<!-- <a-row :gutter="24" type="flex" align="stretch">
			<a-col :span="24" :xl="8" class="mb-24" v-for="(stat, index) in stats" :key="index">-->

				<!-- My Learning Information Card 1 
				<CardInfo 
					:title="stat.title"
					:description="stat.description"
					:imageURl="stat.imageURl"
				></CardInfo>
				 / My Learning Information Card 1 

			</a-col>
		</a-row>
		< / Cards> -->

		<!-- Title -->
		<a-row :gutter="24">
			<a-col :span="24" class="mb-12">
				<h4 style="margin-left: 12px">Recommended For You</h4>
			</a-col>
		</a-row>
		<!-- / Title -->

		<!-- Table &  Timeline -->
		<a-row :gutter="24" type="flex" align="stretch">
			<!-- Table -->
			<a-col :span="24" :lg="24" class="mb-24">
				
				<!-- Many Roles Card -->
				<CardRoleTableDB2
					:titleName="titleName"
					:data="rolesData"
					:columns="table1Columns"
					style="padding-right: 10px;"
				></CardRoleTableDB2>
				<!-- / Many Roles Card -->
				
			</a-col>
			<!-- / Table -->

		</a-row>
		<!-- / Table & Timeline -->
	</div>
</template>

<script>

		// "Authors" table component.
	import CardRoleTableDB2 from '../components/Cards/CardRoleTableDB2' ;
	import axios from 'axios';

	// Bar chart for "Active Users" card.
	import CardBarChart from '../components/Cards/CardBarChart' ;

	// Line chart for "Sales Overview" card.
	import CardLineChart from '../components/Cards/CardLineChart' ;

	// Counter Widgets
	import WidgetCounter from '../components/Widgets/WidgetCounter' ;

	// "Projects" table component.
	import CardProjectTable from '../components/Cards/CardProjectTable' ;

	// Order History card component.
	import CardOrderHistory from '../components/Cards/CardOrderHistory' ;

	// Information card 1.
	import CardInfo from '../components/Cards/CardInfo' ;

	// Information card 2.
	import CardInfo2 from '../components/Cards/CardInfo2' ;

	// Counter Widgets stats
	const stats = [
		{
			title: 'Front-End Engineer',
			description: 'Front-end engineers path will teach you not only the necessary languages and technologies, but how to think like a front-end engineer, too.',
			imageURl: 'images/front-end-engineer.jpeg'
		},
		{
			title: 'Back-End Engineer',
			description: 'Back-End Engineers path, you will start with programming servers and client-side interfaces, then level up to designing databases.',
			imageURl: 'images/back-end-engineering.jpg'
		},
		{
			title: 'Data Scientist',
			description: 'Analytics is all about using data to answer questions, and you will learn how to analyze data, build dashboards, and deliver impactful reports.',
			imageURl: 'images/data-scientist.jpg'
		}	
	]

	// "Projects" table list of columns and their properties.
	const tableColumns = [
		{
			title: 'COMPANIES',
			dataIndex: 'company',
			scopedSlots: { customRender: 'company' },
			width: 300,
		},
		{
			title: 'MEMBERS',
			dataIndex: 'members',
			scopedSlots: { customRender: 'members' },
		},
		{
			title: 'BUDGET',
			dataIndex: 'budget',
			class: 'font-bold text-muted text-sm',
		},
		{
			title: 'COMPLETION',
			scopedSlots: { customRender: 'completion' },
			dataIndex: 'completion',
		},
	];

	// "Projects" table list of rows and their properties.
	const tableData = [
		{
			key: '1',
			company: {
				name: 'Soft UI Shopify Version',
				logo: 'images/logos/logo-shopify.svg',
			},
			members: [ "images/face-1.jpg", "images/face-4.jpg", "images/face-2.jpg", "images/face-3.jpg", ],
			budget: '$14,000',
			completion: 60,
		},
		{
			key: '2',
			company: {
				name: 'Progress Track',
				logo: 'images/logos/logo-atlassian.svg',
			},
			members: [ "images/face-4.jpg", "images/face-3.jpg", ],
			budget: '$3,000',
			completion: 10,
		},
		{
			key: '3',
			company: {
				name: 'Fix Platform Errors',
				logo: 'images/logos/logo-slack.svg',
			},
			members: [ "images/face-1.jpg", "images/face-2.jpg", "images/face-3.jpg", ],
			budget: 'Not Set',
			completion: {
				label: '100',
				status: 'success',
				value: 100,
			},
		},
		{
			key: '4',
			company: {
				name: 'Launch new Mobile App',
				logo: 'images/logos/logo-spotify.svg',
			},
			members: [ "images/face-1.jpg", "images/face-2.jpg", ],
			budget: '$20,600',
			completion: {
				label: '100',
				status: 'success',
				value: 100,
			},
		},
		{
			key: '5',
			company: {
				name: 'Add the New Landing Page',
				logo: 'images/logos/logo-jira.svg',
			},
			members: [ "images/face-1.jpg", "images/face-4.jpg", "images/face-2.jpg", "images/face-3.jpg", ],
			budget: '$4,000',
			completion: 80,
		},
		{
			key: '6',
			company: {
				name: 'Redesign Online Store',
				logo: 'images/logos/logo-invision.svg',
			},
			members: [ "images/face-1.jpg", "images/face-4.jpg", "images/face-3.jpg", ],
			budget: '$2,000',
			completion: {
				label: 'Cancelled',
				status: 'exception',
				value: 100,
			},
		},
	];

	const roleCols = [
		{
				title: 'Role Name',
				dataIndex: 'JobRoleDetails',
				scopedSlots: { customRender: 'JobRoleDetails'}
		},
		{
				title: 'Role Description',
				dataIndex: 'Job_Role_Description',
				scopedSlots: { customRender: 'Job_Role_Description'}
		}
	]

	export default ({
		components: {
			CardBarChart,
			CardLineChart,
			WidgetCounter,
			CardProjectTable,
			CardOrderHistory,
			CardInfo,
			CardInfo2,
			CardRoleTableDB2,
		},
		data() {
			return {
				rolesData: [],
				table1Columns: roleCols,
				visible: false,
				titleName: "Roles",
				// Associating table data with its corresponding property.
				tableData,

				// Associating table columns with its corresponding property.
				tableColumns,

				// Counter Widgets Stats
				stats,
			}
		},
		methods: {
			showModal() {
			this.visible = true;
			},

			getRoles(){
				const path = 'http://localhost:5000/roles';
				axios.get(path)
					.then((res) => {
						console.log(res.data.data.roles)
						this.rolesData = res.data.data.roles;
						for (let role of this.rolesData){
							role.JobRoleDetails = {}
							role.JobRoleDetails.roleId = role.Job_Role_ID
							role.JobRoleDetails.roleName = role.Job_Role_Name
						}
					})
					.catch((error) => {
						console.error(error);
					});
			},

			handleOk(e) {
			console.log(e);
			this.visible = false;
			},
		},
	created() {
		this.getRoles();
	}
	})

</script>

<style lang="scss">
</style>