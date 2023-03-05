import React, { useState } from 'react';

import axios, {isCancel, AxiosError} from 'axios';


function Login() {
  const [name, setName] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log('Name:', name, 'Password:', password);
    axios.request({
    		baseURL:'http://127.0.0.1:8000/test/',

    	})
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Name:
        <input type="text" value={name} onChange={(event) => setName(event.target.value)} />
      </label>
      <br />
      <label>
        Password:
        <input type="password" value={password} onChange={(event) => setPassword(event.target.value)} />
      </label>
      <br />
      <button type="submit">Submit</button>
    </form>
  );
}

export default Login












// function Login(props){

// 	return (
// 		<form onSabmit={this}>

//   			<label>
// 			Name:
// 			    <input type="text" name="name" />
//   			</label>

// 			<label>
// 			Password:
// 			    <input type="text" name="password" />
//   			</label>
			
// 			<input type="submit" value="Submit" />
		
// 		</form>
// 	);
// }

// export default Login;
