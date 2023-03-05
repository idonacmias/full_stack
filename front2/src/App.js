import React from 'react';
import './App.css';
import ProjectsCards from './components/ProjectsCards';
import Login from './components/Login';

function App() {
  const cards = [{name:'bob', photo:'/myPhoto.jpeg'}, {name:'bob2', photo:'/myPhoto.jpeg'}, {name:'bob3', photo:'/myPhoto.jpeg'}];
  const test = [{'a':'a'}];
  
  return (

    <div className="App">
      <Login/>
      {/*<ProjectsCards cards={cards}/>*/}

    </div>
  );
}

export default App;
