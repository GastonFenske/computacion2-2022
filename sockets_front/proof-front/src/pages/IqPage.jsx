import React, { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { LoadingButtonComponent } from '../components/LoadingButtonComponent';
import { LoadingComponent } from '../components/LoadingComponent';
import { Navbar } from '../components/navbar'

export const IqPage = () => {

    localStorage.setItem("authenticated", false);

    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')

    const [loading, setLoading] = useState(false)

    const [authenticated, setauthenticated] = useState(
        localStorage.getItem(localStorage.getItem("authenticated") || false)
    );

    const navigate = useNavigate();

    const onEmailChange = ({ target }) => {
        setEmail( target.value );
    }

    const onPasswordChange = ({ target }) => {
        setPassword( target.value );
    }

    const onSubmit = async (e) => {
        e.preventDefault();

        setLoading(true);
        
        const url = 'http://127.0.0.1:1234/api/login'
        const resp = await fetch(
            url,
            {
                method: 'POST',
                body: JSON.stringify({
                    email,
                    password
                }),
            }
        )
        const data = await resp.json();

        if ( data.status === 'ok' ) {
            // go to MarketsPage
            localStorage.setItem("authenticated", true);
            navigate('/markets');
        }

    }

    useEffect(() => {
      
        localStorage.setItem("authenticated", false);
    
    //   return () => {
    //     second
    //   }
    }, [
        // every time I change the value of authenticated, this useEffect will be executed
        authenticated
    ])
    

  return (
    <>

        <Navbar />

        <div class="container">

        <div class="row d-flex justify-content-center my-6">
            <div class="bg-forms p-5 rounded col-md-4 col-10">
                <div class="d-flex justify-content-center">
                    <h3>Log In IQ Option</h3>
                </div>
                <form class="pt-3"
                onSubmit={ onSubmit }
                >
                    <div class="mb-3">
                    <label for="exampleInputEmail1" class="form-label">Email</label>
                    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Ingresa tu email" 
                    value={ email }
                    onChange={ onEmailChange }
                    />
                    </div>
                    <div class="mb-3">
                    <label for="exampleInputPassword1" class="form-label">Password</label>
                    <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Ingresa tu password" 
                    value={ password }
                    onChange={ onPasswordChange }
                    />
                    </div>
                    <div class="d-grid pt-3">

                        {
                            // when the user submit show loading button component
                            loading 
                            ?
                             <LoadingButtonComponent />
                            :
                            <button type="submit" class="btn btn-iq"
                                onClick={ onSubmit }
                            >
                                Log In
                            </button>

                        }


                    </div>
                </form>
            </div>
        </div>

        </div>

        {/* <LoadingComponent /> */}

    </>
  )
}
