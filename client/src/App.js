import './css/App.css';
import React from 'react';
import Header from './components/Header';
import Main from './components/Main';

class App extends React.Component {
    render() {
        return (
            <main className="App">
              <Header/>
              <Main/>
            </main>
          );
    }
}

export default App;
