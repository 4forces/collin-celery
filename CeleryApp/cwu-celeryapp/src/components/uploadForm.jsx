import React, { Component } from 'react';

class UploadForm extends Component {
  constructor(){
    super();
    this.state = {
      uploadfile: null,
      sensitivity: 0
    }
    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
    this.getCookie = this.getCookie.bind(this)
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

  handleChange=e=>
    this.setState({
      uploadfile: e.target.files[0],
      sensitivity: 0
  });

  handleSubmit(e){
    e.preventDefault()
    let csrftoken = this.getCookie('csrftoken')
    let formData = new FormData();
    formData.append('uploadfile', this.state.uploadfile);
    formData.append('sensitivity', this.state.sensitivity);

    let url = "http://127.0.0.1:8000/api/api-create/";
    fetch(url,{
      method: 'POST',
      headers:{
        'X-CSRFToken': csrftoken,
      },
      body: formData
    }).then((response) => response.json())
      .then((result) => {
        console.log('Success:', result);
        window.location.reload();
      })
      .catch((error) => {
        console.log("Error:", error)
      })
  }

  render() {
    return (
      <React.Fragment>
        <h2 className="m-3">Upload a File</h2>
        <div className="container d-flex">
          <form onSubmit={this.handleSubmit} id="form">
            <input
              onChange={this.handleChange}
              className="form-control my-2"
              id="uploadField"
              type="file"
              name="uploadField"
            ></input>
            <button
              style={{ flex: 1 }}
              className="btn btn-outline-primary mt-3"
              type="submit"
            >
              Upload File
            </button>
          </form>
        </div>
        <div className="container">
          <a
            className="btn btn-success mt-3"
            data-bs-toggle="collapse"
            href="#collapseExample"
            role="button"
            aria-expanded="false"
            aria-controls="collapseExample"
          >
            View Uploaded Files
          </a>
        </div>
      </React.Fragment>
    );
  }
}
 
export default UploadForm;