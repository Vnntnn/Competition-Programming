/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {
   let P_romise = new Promise(resolve => setTimeout(resolve, millis));
   return P_romise; 
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */