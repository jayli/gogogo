
const puppeteer = require('puppeteer');

(async function(){
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  browser.on('targetchanged', async () => {
    console.log(browser.target().url())
  })
  page.on('request', (req) => {
    console.log(req.url())
  })
  page.on('load', async () => {
    console.log(page.target().url() + ' page loaded')
    if (/^https:\/\/login\.taobao\.com/ig.test(page.target().url())) {
      console.log('login')
      let userNameInput = await page.mainFrame().$('#fm-login-id')
      let passWordInput = await page.mainFrame().$('#fm-login-password')
      let loginButton = await page.mainFrame().$('button.password-login')

      await userNameInput.type("", {delay: 100})
      await passWordInput.type("", {delay: 100})
      await loginButton.click()
      console.log('------------------------------------')
      page.evaluate(() => {
        window.open('https://www.taobao.com')
      })

    }

    if (/^https:\/\/www\.taoboa\.com/ig.test(page.target().url())) {
      console.log(browser.target().url())
      let el = await page.mainFrame().$('.J_Service')
      console.log('----------------')
      let txt = await el.evaluate((el) => {
        return el.innerHTML
      })
      console.log(txt)
      await browser.close();
    }
  })

  await page.goto('https://login.taobao.com/member/login.jhtml?f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F');



})()

// https://login.taobao.com/member/login.jhtml?f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F
