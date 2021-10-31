// curl

const https = require('https');

(async () => {

  https.get("https://jsonbin.org/me/urls", {
    method: "GET",
    headers: {
      "authorization": 'token bb2fbb2f-1b6f-4b2f-bb66-6ba7e9f412e4'
    }
  }, (res) => {
    console.log(res.statusCode)
    res.setEncoding('utf8')
    let rawData = '';
    res.on('data', chunk => { rawData += chunk; })
    res.on('end', () => {
      console.log('--- response end ---')
      console.log(rawData)
    })
  })

})()


