import React from 'react'

export const LoadingButtonComponent = () => {
  return (
    <>

        <button class="btn btn-iq" type="button" disabled>
            <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
            Loading...
        </button>

    </>
  )
}
