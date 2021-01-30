import './App.css';
import React, { Component } from 'react'
import Navbar from './components/navbar'
import UploadForm from './components/uploadForm'
import FileList from './components/fileList'


class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      fileList: [],
      deleteId: null,
      editing: false,
    };
    this.fetchFiles = this.fetchFiles.bind(this);
    this.getCookie = this.getCookie.bind(this);
    this.deleteItem = this.deleteItem.bind(this);
  }

  getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }

  componentWillMount() {
    this.fetchFiles();
  }

  fetchFiles() {
    console.log("Fetching...");
    fetch("http://127.0.0.1:8000/api/api-list/")
      .then((response) => response.json())
      .then((data) =>
        this.setState({
          fileList: data,
        })
      );
  }

  deleteItem(file_id) {
    let csrftoken = this.getCookie('csrftoken');
    let url = `http://127.0.0.1:8000/api/api-delete/${file_id}`;
    fetch(url, {

      method: 'DELETE',
      headers:{
        'Access-Control-Allow-Origin':'*',
        "content-type": "application/json",
        "x-csrftoken": csrftoken,
      },
    }).then((response) => response.json())
      .then((result) => {
        console.log("Success:", result);
        this.fetchFiles();
      })
      .catch((error) => {
        console.log("Error:", error);
      });
  }

  render() {
    let files = this.state.fileList;
    return (
      <React.Fragment>
        <Navbar />
        <main className="container">
          <UploadForm />
          {files.map((file) => (
            <FileList key={file.id} value={file} deleteFile={this.deleteItem}/>
          ))}
        </main>
      </React.Fragment>
    );
  }
}
 
export default App;
