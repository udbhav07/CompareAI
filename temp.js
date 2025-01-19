const puppeteer = require('puppeteer');

async function takeScreenshot(url, savePath) {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto(url, { waitUntil: 'networkidle2' });
    await page.screenshot({ path: savePath, fullPage: true });
    await browser.close();
}

// Take screenshots
await takeScreenshot('http://original-website.com', 'original.png');
await takeScreenshot('http://modified-website.com', 'modified.png');
