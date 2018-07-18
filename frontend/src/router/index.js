import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/components/home/home';
import About from '@/components/about/about';
import Status from '@/components/status/status';
import Contest from '@/components/contest/contest';
import User from '@/components/user/user';
import Login from '@/components/signin/login';
import Signup from '@/components/signin/signup';
import Signout from '@/components/signin/signout';
import NotFound from '@/components/global/404';
import ProblemList from '@/components/problem/app';
import ProblemDetail from '@/components/problem/detail/app';
import ProblemDescription from '@/components/problem/detail/description';
import ProblemEditor from '@/components/problem/detail/editor';
import ProblemDiscussion from '@/components/problem/detail/discussion';

Vue.use(Router);

export default new Router({
	mode: 'history',
	routes: [
		{
			path: '',
			redirect: {
				name: 'Home',
			},
		},
		{
			path: '/home',
			name: 'Home',
			component: Home,
		},
		{
			path: '/login',
			name: 'Login',
			component: Login,
		},
		{
			path: '/status',
			name: 'Status',
			component: Status,
		},
		{
			path: '/contest',
			name: 'Contest',
			component: Contest,
		},
		{
			path: '/user',
			name: 'User',
			component: User,
		},
		{
			path: '/about',
			name: 'About',
			component: About,
		},
		{
			path: '/signup',
			name: 'Signup',
			component: Signup,
		},
		{
			path: '/signout',
			name: 'Signout',
			component: Signout,
		},
		{
			path: '/problem',
			name: 'Problem',
			component: ProblemList,
		},
		{
			path: '/problem/:slug',
			component: ProblemDetail,
			children: [
				{
					path: 'description',
					name: 'ProblemDetailDescription',
					component: ProblemDescription,
				},
				{
					path: 'editor',
					name: 'ProblemDetailEditor',
					component: ProblemEditor,
				},
				{
					path: 'discussion',
					name: 'ProblemDetailDiscussion',
					component: ProblemDiscussion,
				},
			],
		},
		{
			path: '*',
			name: '404',
			component: NotFound,
		},
	],
});
