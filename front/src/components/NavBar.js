import {Link} from "react-router-dom";


function NavBar(props){
	return (
		<>
      		<Link to="/">Home page  </Link> 
      		<Link to="/login">Login  </Link> 
      		<Link to="/ProjectsCards">Projects  </Link>
      		{/*<Link to="/PersenalProjectsCards">My projects  </Link> */}
      		{/*<Link to="/test">test  </Link> */}
      		<Link to="/logout">logout  </Link> 

		
		</>
	);
}

export default NavBar;
