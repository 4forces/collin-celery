import './App.css';
import React, { Component } from 'react'
import Navbar from './components/navbar'
import UploadForm from './components/uploadForm'

class App extends Component {
    state = {  }
    render() { 
        return (
          <React.Fragment>
            <Navbar />
            <main className="container">
                <UploadForm />
            </main>
          </React.Fragment>
        );
    }
}
 
export default App;
