import React, { Component } from 'react';

class FileList extends Component {
    state ={
        value: this.props.value
    }
    
    

    render() {
    let file = this.state.value;
    return (
        <React.Fragment>
        <div className="collapse" id="collapseExample">
            <div className="card card-body" key={this.id}>
            <table className="table mt-3">
                <thead>
                <tr>
                    <th>File Name</th>
                    <th>File Size</th>
                    <th>Sensitivity</th>
                    <th>Upload Date</th>
                    <th>Modified Date</th>
                    <th>Delete File</th>
                </tr>
                </thead>
                <tbody>
                <tr>
                    <td>{file.uploadfile_name}</td>
                    <td>{file.uploadfile_size}</td>
                    <td>{file.sensitivity}</td>
                    <td>{file.created}</td>
                    <td>{file.updated}</td>
                    <td>
                    <button onClick={() => this.props.deleteFile(file.id)} className="btn btn-sm btn-outline-danger">
                        DELETE
                    </button>
                    </td>
                </tr>
                </tbody>
            </table>
            </div>
        </div>
        </React.Fragment>
    );
    }
}
 
export default FileList;