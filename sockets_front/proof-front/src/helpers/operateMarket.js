export const operateMarket = async (market) => {

    const url = 'http://127.0.0.1:1234/api/trade'
    const resp = await fetch(url,
        {
            method: 'POST',
            body: JSON.stringify({'market': market})
        }
    )
    const data = await resp.json();
}