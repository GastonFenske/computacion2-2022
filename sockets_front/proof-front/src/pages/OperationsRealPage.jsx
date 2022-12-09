import React, { useEffect, useState } from 'react'
import { Navbar } from '../components/navbar'
// import { getNewInfo } from '../helpers/getNewInfo'
import io from 'socket.io-client'


// const socket = io('http://127.0.0.1:8000')

export const OperationsRealPage = () => {

    const [msj, setMsj] = useState('nada')
    const [messages, setMessages] = useState([])

    const getInfo = () => {
        // console.log('Entra al get info')
        // const msj = await getNewInfo()

        const socket = io('http://127.0.0.1:8000')



        socket.on('message', (message) => {
            console.log(message, 'message que llega desde el server asyncio')
            setMessages([...messages, message])
            setMsj(message)
            // disconnect socket
            // socket.disconnect()
        })

        socket.on('server:newVeil', (message) => {
          console.log(message, 'vela nueva')
          setMessages([...messages, message])
          setMsj(message)
        })

        return socket

        // console.log(msj, 'El mensaje que llega')
        // setMessages([...messages, msj])
        // setMsj(msj)
    }

    const disconnectSocket = () => {
      socket.disconnect()
    }

    useEffect(() => {
      
        const socket = getInfo()

        // const socket = io('http://127.0.0.1:8000')

    //     socket.on('message', (message) => {
    //         console.log(message, 'message')
    //         setMessages([...messages, message])
    //         setMsj(message)
    //     })
    
      return () => {
        socket.disconnect()
      }

    }, [])
    

  return (
    <>
        <Navbar />
        <div className='container mt-6 text-light'>
             <h1>Operations en real time</h1>
             <p>
                Recibido: {msj}
                {/* Lista completa: {messages} */}
             </p>
        </div>
    </>
  )
}
