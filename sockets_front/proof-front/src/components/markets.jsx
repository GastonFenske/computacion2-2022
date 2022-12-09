import React, { useEffect, useState } from 'react'
import axios from 'axios';
import { getMarkets } from '../helpers/getMarkets';
import { operateMarket } from '../helpers/operateMarket';
import { LoadingComponent } from './LoadingComponent';

export const MarketsComponent = () => {

  const [markets, setMarkets] = useState([])

  const getOpenMarkets = async () => {
    const openMarkets = await getMarkets()
    setMarkets(openMarkets)
  }

  useEffect(() => {

    getOpenMarkets()
  
    // return () => {
    //   second
    // }
  }, [])


  return (
    <>

      {/* if open_markets is empty return LoadingComponent */}

      {
        markets.length === 0 && <LoadingComponent />
      }

      <h3 className='my-4 mt-6 text-light'>
        Mercados abiertos
      </h3>

      <ol className='list-group mb-4 bg-dark'>
        {
          markets.map(market => (
            <li key={market.id} className='list-group-item d-flex justify-content-between align-items-center text-light bg-pro'>
  
              {market.name}
              {/* create a button to operate this market */}

              <button 
                className="btn btn-iq text-light"
                onClick={ () => operateMarket(market.name) }
              >
                Operar
              </button>

            </li>
          ))
        }
      </ol>

    </>
  )
}
