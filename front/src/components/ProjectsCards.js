import Project from './Project';
import axios from 'axios';
import { useEffect, useState } from 'react';



function ProjectsCards(props){

	const [projectCards, setProjectCards] = useState([])
	const config = {headers:{Authorization:`Bearer ${localStorage.getItem('access')}`}}

	const cards = () => {
		console.log('ProjectsCards: cards')
		console.log('config',config)
    	
        axios.get('https://woodworksite.onrender.com/project/', config)
		.then((response) => handelResponse(response))
		}

	const handelResponse = (response) =>{
		console.log('response.data:',response.data)
		setProjectCards(response.data)
	}

	return (
		<>
		<h1>ProjectsCards</h1>
        <button onClick={() => cards()}>getMyDict</button>
		
		<p>{projectCards.map((project, i) =>  {
			return <Project key={i} name={project.name} image={project.image.slice(1)} index={i}/>

		} )}</p>
		</>
	);
}

export default ProjectsCards;
