import React from 'react';
import './Login.css';
import 'bootstrap/dist/css/bootstrap.css';

const Login = () => {

    
  
    return (
      <div>
    
            <div className="box"> 
                <div className="image"><img src="https://cdni.iconscout.com/illustration/premium/thumb/man-working-on-his-laptop-on-the-sofa-at-home-2511605-2131717.png" alt=""/></div>
            </div>
            <div className="heading">
                <h1>WELCOME BACK</h1>
                <p>Sign in to Continue</p>
        </div>

    
    
        <form onSubmit>
            <div className="mb-3">
              <label htmlfor="exampleInputEmail1" id="email1" className="form-label" >Email</label>
              <input type="email" className="form-control border border-dark" id="exampleInputEmail1" aria-describedby="emailHelp"/>
            </div>
            <div className="mb-3">
              <label htmlfor="exampleInputPassword1" id="pass1" className="form-label">Password</label>
              <input type="password" className="form-control border border-dark" id="exampleInputPassword1"/>
            </div>
            <div className="mb-3 form-check">
              <input type="checkbox" className="form-check-input border border-dark"  id="exampleCheck1"/>
              <label className="form-check-label "  htmlfor="exampleCheck1">Remember me</label><span><a className="link-opacity-50-hover link-underline link-underline-opacity-0"styles="color:black" id="forgetpass"  href="#">Forget Password?</a></span>
              </div>
              <button type="submit " className="btn btn-dark ">Submit</button>
          </form>

                <div className="mb-3">
                    <p>Don't Have a Acoount?<a className="link-opacity-50-hover link-underline link-underline-opacity-0" id="register"  href="#">Register Here</a></p>
                </div>




          <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe" crossorigin="anonymous"></script>
      </div>
    );
  };
  
  


export default Login