/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function (flowerbed, n) {
    let i = 0;
    while (i < flowerbed.length) {
        if (flowerbed[i]) {
            i += 2;
            continue;
        }
        if (flowerbed[i - 1]) continue;
        if (flowerbed[i + 1]) {
            i += 3;
            continue;
        }
        // flowerbed[i] = true
        n--;
        i += 2;
    }
    return n <= 0;
};
