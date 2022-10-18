<!-- 
	This is the dashboard page, it uses the dashboard layout in: 
	"./layouts/Dashboard.vue" .
 -->

<template>
	<div>


		<!-- Title -->
		<a-row :gutter="24">
			<a-col :span="24" class="mb-12">
				<h4 style="margin-left: 12px">Courses recommended For You</h4>
			</a-col>
		</a-row>
		<!-- / Title -->

		<!-- Table & Timeline -->
		<a-row type="flex" :gutter="[24,24]" align="stretch" style="padding-left: 7px; padding-right: 7px">

		<!-- Project Column -->
		<a-col :span="24" :md="6" v-for="index in correctCourseList" :key="index">

			<!-- Project Card -->
			<a-card class="card-project">
				<img
				slot="cover"
				alt="example"
				src="/images/ux-ui.png"
				v-on:click="selectCourse()"
				/>
				<div class="card-tag">{{index.Course_Category}} {{index.Course_ID}} </div>
				<h5 v-on:click="selectCourse()">{{index.Course_Name}} </h5>
				<p>
					{{index.Course_Description}}
				</p>
			</a-card>
			<!-- / Project Card -->

		</a-col>
		<!-- / Project Column -->

		</a-row>

		<!-- / Table & Timeline -->
	</div>
</template>

<script>
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

	export default ({
		components: {
			CardBarChart,
			CardLineChart,
			WidgetCounter,
			CardProjectTable,
			CardOrderHistory,
			CardInfo,
			CardInfo2,
		},
		data() {
			return {

				// Associating table data with its corresponding property.
				tableData,

				// Associating table columns with its corresponding property.
				tableColumns,

				// Counter Widgets Stats
				stats,
				correctCourseList: [],
				allCourse:[],
				skill: "",
				// Active button for the "Projects" table's card header radio button group.
				projectHeaderBtns: 'all',
			}
		},
		methods: {
			showModal() {
			this.visible = true;
			},

			getCourse(){
				console.log(this.$route.query.roleId +"haha" + this.$route.query.skillId)

				const url = "http://localhost:5000/skills" 
				axios.get(url)
					.then((res) => {
						console.log(res.data.data.skills)
						let allSkills = res.data.data.skills;
						for(let i=0; i< allSkills.length; i++){
							var skill= allSkills[i];
							if(skill.Skill_ID == this.$route.query.skillId){
								this.skill = skill.Skill_Name;
								console.log(this.skill +'haha')
							}
							console.log(skill.Skill_ID)
						}
						
					})
					.catch((error) => {
						console.error(error);
					});

			},

			getCourses(){
				const course_url = "http://localhost:5000/courses"
				axios.get(course_url)
					.then((res) => {
						// console.log(res.data.data.courseCatalog)

						this.allCourse = res.data.data.courseCatalog
						// console.log(this.allCourse)
						for(let i=0; i < this.allCourse.length; i++){
							var course = this.allCourse[i]
							if(this.skill==course.Course_Category && course.Course_Status == "Active"){
								this.correctCourseList.push(this.allCourse[i])
							}
						}
						// console.log(this.correctCourseList)
						
					})
					.catch((error) => {
						console.error(error);
					});
			},


			selectCourse(){
				console.log("Hello!")
				let text;
  				if (confirm("Confirm course selection?") == true) {
					text = "Selection confirmed!";
					alert(text)
				} else {
					text = "You canceled!";
					alert(text)
  				}
			},
			handleOk(e) {
			console.log(e);
			this.visible = false;
			},
		},
	created() {
		this.getCourse();
		this.getCourses();
		// console.log(this.$route.query.roleId +"haha" + this.$route.query.skillId)
	},
	})

</script>

<style lang="scss">
</style>