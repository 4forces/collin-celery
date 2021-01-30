import React, { Component } from 'react';

class UploadForm extends Component {
    constructor(props){
        super(props);
    };

    render() { 
        return (
          <React.Fragment>
            <h2 className="m-3">Upload a File</h2>
            <div className="container d-flex">
              <form method="POST" enctype="multipart/form-data" id="form">
                <input
                  style={{ flex: 6 }}
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
            <div className="container mt-5">
              <a
                href="{% url 'view_files' username=username %}"
                className="btn btn-success mt-3"
              >
                View Uploaded Files
              </a>
            </div>
          </React.Fragment>
        );
    }
}
 
export default UploadForm;