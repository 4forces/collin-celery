import React, { Component } from 'react'


class Navbar extends Component {
    render() { 
        return ( 
            <nav className="navbar navbar-expand-lg navbar-light bg-light">
                <div className="container-fluid">
                    <a className="navbar-brand" href="#"><i className="far fa-file-alt align-center ml-2"></i><i className="fas fa-check-double mr-2"></i>  File Sensitivity Checker</a>
                    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                        <span className="navbar-toggler-icon"></span>
                    </button>
                    <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
                        <div className="navbar-nav">
                            <a className="nav-link active" aria-current="page" href="#">Home</a>
                            <a className="nav-link" href="/accounts/login">Log In</a>
                            <a className="nav-link" href="/accounts/logout">Log Out</a>
                            <a className="nav-link" href="/accounts/signup">Register</a>
                        </div>
                    </div>
                </div>
            </nav>
        );
    }
}
 
export default Navbar;