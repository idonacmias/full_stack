// import {Link} from "react-router-dom";


function Project(props){
	return (
		<>

		<>Project card {props.index}</>
		<>{props.name}</>
		<br/>		
		<img src={props.image} alt={props.name} />

		</>
	);
}

export default Project;
