const puppeteer = require('puppeteer');
const fs = require('fs');
const xlsx = require('xlsx');

const urls = [
    'https://www.amazon.in/Atomberg-Renesa-Motor-Remote-Ceiling/dp/B08Y5QJXSR/ref=sr_1_1?pf_rd_i=976442031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=3871fa3d-4ea9-4d76-af8b-791d782f48f8&pf_rd_r=Q6HKYS7H4WAMCCKJS4MM&pf_rd_s=merchandised-search-7&qid=1704455311&refinements=p_n_condition-type%3A8609960031%2Cp_36%3A99900-&s=kitchen&sr=1-1&th=1',
  'https://www.amazon.in/atomberg-Efficio-Alpha-Delivery-Indicators/dp/B0C2C9HTVJ/ref=pd_bxgy_img_d_sccl_2/257-2884551-4487840?pd_rd_w=8xGTR&content-id=amzn1.sym.2f895d58-7662-42b2-9a98-3a18d26bef33&pf_rd_p=2f895d58-7662-42b2-9a98-3a18d26bef33&pf_rd_r=KKA5G0136XGDDAHDAH2V&pd_rd_wg=1xDOY&pd_rd_r=1b71f9f4-9ac2-4d37-b7e2-5b6b270e0c99&pd_rd_i=B0C2C9HTVJ&th=1',
  'https://www.amazon.in/Pigeon-Pack-Stick-Cookware-2Pc/dp/B07KYPZHJ9/ref=mp_s_a_1_3?qid=1704456043&s=kitchen&sr=1-3&th=1'

];
(async () =>{
    const broswer = await puppeteer.launch();
    const page = await broswer.newPage();

    const productsdata = [];

    for(const url of urls){
        await page.goto(url, {waitUntil: 'domcontentloaded'});

        const productName = await page.$eval('#productTitle', (element) => element.textContent.trim());
        const productPriceElement = await page.$('.a-price-whole');
        const productPrice  =productPriceElement ? await page.evaluate(element => element.textContent.trim(), productPriceElement) : 'N/A';

        productsdata.push({
            name: productName,
            price: productPrice
        })
        console.log('fetched successfully.......')
    }
    await broswer.close();

    const worksheet = xlsx.utils.json_to_sheet(productsdata);
    const excelData = xlsx.write(
        {Sheets: {'Products': worksheet}, SheetNames: ['Products']},
        {bookType: 'xlsx', type: 'buffer'}
    );

    fs.writeFileSync('products.xlsx', excelData);

})();