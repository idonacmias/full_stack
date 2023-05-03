import React, { useState } from 'react';

import axios from 'axios'; //{isCancel, AxiosError}

import serverBaseUrl from '../setting'



function Logout() {

	const handleLogout = () => {
		console.log('handleLogout')
		console.log(localStorage)
    localStorage.setItem('access', '')
   		
    }

	return (
			<button onClick={() => handleLogout()}>Logout</button>
 		);
}


export default Logout
