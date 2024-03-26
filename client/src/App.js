import './css/App.css';
import React from 'react';
import Header from './components/Header';
import Main from './components/Main';
import Blogs from './components/Blogs';

const App = () => {
    return (
        <main className="App">
            <Header/>
            <Main/>
            <Blogs/>
        </main>
        );
}

export default App;
