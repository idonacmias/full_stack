import Project from './Project';
import axios from 'axios';
import { useEffect, useState } from 'react';



function ProjectsCards(props){

	const [projectCards, setProjectCards] = useState({})
	const config = {headers:{Authorization:`Bearer ${localStorage.getItem('access')}`}}

	const cards = () => {
		console.log('ProjectsCards: cards')
		console.log('config',config)
    	
        axios.get('http://localhost:8000/project/10/', config)
		.then((response) => handelResponse(response))
		}

	const handelResponse = (response) =>{
		console.log('response.data:',response.data)
		setProjectCards(response.data)
		projectCards.image = projectCards.image.slice(1)
		console.log('ProjectCards:',projectCards)
		console.log('ProjectCards.image:', projectCards.image)
	}

	return (
		<>
		<h1>ProjectsCards</h1>
        <button onClick={() => cards()}>getMyDict</button>
		
		<Project key={0} name={projectCards.name} image={projectCards.image} index={0}/>
		{/*<p>{projectCards.map((project, i) =>  {
			return <Project key={i} name={project.name} photo={project.photo} index={i}/>

		} )}</p>*/}
		</>
	);
}

export default ProjectsCards;
