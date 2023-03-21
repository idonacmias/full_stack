import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

import App from './App';
import Login from './components/Login';
import ProjectsCards from './components/ProjectsCards';
import NavBar from './components/NavBar';
import Test from './components/test';

import reportWebVitals from './reportWebVitals';

import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <NavBar/> 

      <Routes>
         <Route path="/" element={<App />} />
         <Route path="/login" element={<Login />} />
         <Route path="/ProjectsCards" element={<ProjectsCards />} />
         <Route path="/ProjectsCards/:id" element={<ProjectsCards />} />
         <Route path="/test" element={<Test/>} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
