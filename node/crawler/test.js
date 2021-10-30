const puppeteer = require('puppeteer');


(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  page.once('load', () => {
    console.log('page loaded')
    page.keyboard.sendCharacter('ok')
  })
  page.on('request', (req) => {
    console.log(req.url())
  })

  page.waitForSelector('.J_Service').then(async () => {
    let el = await page.mainFrame().$('.J_Service')
    console.log('----------------')
    let txt = await el.evaluate((el) => {
      return el.innerHTML
    })
    console.log(txt)
    await el.screenshot({
      path: 'aaa.png'
    })
  })

  page.on('dialog', async (dialog) => {
    console.log('dialog:', dialog.message())
    await dialog.dismiss()
  })

  await page.evaluate(() => {
    alert(111)
  })

  await page.goto('https://www.taobao.com');


  await browser.close();
})();
