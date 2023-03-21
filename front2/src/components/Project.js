// import {Link} from "react-router-dom";


function Project(props){
	return (
		<>

		<>Project card {props.index}</>
		<a href	='/ProjectsCards/{props.id}'>
			<>{props.name}</>
        	<img src={process.env.PUBLIC_URL + props.photo} alt="project" />
		</a>
		<br/>		

		</>
	);
}

export default Project;
