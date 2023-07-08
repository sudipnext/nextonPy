const axios = require('axios')
const puppeteer = require('puppeteer')
const url = 'https://www.tiktok.com/@dimerci91'

    axios(url)
    .then(response => {
        const html = response.data;
        console.log(html)
    })
    .catch(console.error)

