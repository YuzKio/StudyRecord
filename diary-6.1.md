# 算法

## 1、剑指Offer 03. 数组中的重复数字

https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/

* **用map**

  ```javascript
  var findRepeatNumber = function(nums) {
      const len = nums.length;
      let map = new Map();
      for(let i = 0; i < len; i ++) {
          map.set(nums[i], 0);
      }
      for(let i = 0; i < len; i ++) {
          let tmp = map.get(nums[i]) + 1;
          if(tmp >= 2) return nums[i];
          else map.set(nums[i], tmp);
      }
      return;
  }
  ```

* **不用map**

  每个for中都把数字交换到它们对应的位置，如果交换到的位置已经有数了，就说明是重复的。

  原数组：**[2, 3, 1, 0, 2, 5, 3]**

  第一个for循环开始（i=0）：

  第一次交换：cur = 2， **[1, 3, 2, 0, 2, 5, 3]**， cur = 1

  第二次交换：cur = 1， **[3, 1, 2, 0, 2, 5, 3]**， cur = 3

  第三次交换：cur = 3， **[0, 1, 2, 3, 2, 5, 3]**， cur = 0

  第二个for循环开始（i=1）：……

  ```javascript
  var findRepeatNumber = function(nums) {
      for(let i = 0; i < nums.length; i ++) {
          let cur = nums[i];
          while(cur != i) {
              if(cur != nums[cur]) {
                  let tmp = cur;
                  nums[i] = nums[cur];
                  nums[cur] = tmp;
                  cur = nums[i];
              } else {
                  return cur;
              }
          }
      }
      return -1;
  }
  ```

  

## 2、剑指Offer 20.表示数值的字符串

https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/

* **不用库函数，不用正则**

  从头开始，cursor后移，判断是否有非法模式：

  * 跳过开头所有的空格。
  * 然后进行**有符号数的判断**。就是说如果是有符号的话，光标就后移一位。把移动后/没有符号/有非法符号的整数进一步进行无符号数的判断。
  * 再进行**无符号数的判断**。无符号数应该所有数都在0~9之间。如果第一位是非法的话，直接就根据第一位判断为false，光标不再后移（也就是不再对之后的字符串进行判断）；如果第一位合法，保存这个下标，然后光标一直往后移动，一直到当前所指不在0~9之间，这时返回对第一位合法性的判断。也就是说，如果第一位不是非法字符，则遇到特殊符号之前的这一串字符串都是合法的字符！
  * 这时候应该对遇到特殊符号之前的字符串保存它的合法性。
  * 然后进入到对**特殊符号的判断**。
    * 如果这个符号是小数点，我们要判断这之后的数是不是合法的。小数点后的合法是指，如果小数点前有数，小数点后应该是***空（“”）***或者是***无符号数***。如果小数点之后判断是无符号数，就把inValid置为true。如果判断不是无符号数的话，也先保留，因为它可能也是正确的（比如“3.”）。
    * 如果这个符号是e/E，如果之前的字符串是合法的话，再判断之后的字符串是否合法。合法是指，他可以是有符号的整数。
  * 跳过结尾的所有空格。
  * 如果这个字符串是合法的数值，那么最后的光标应该指向undefined，也就是越界了；如果光标还在字符串内，说明这不是合法的数值。

  ```javascript
  const isNumber = (s) => {
      let cursor = 0; // 扫描字符的光标
      let isValid; // 当前扫描时是否有效
      
      const scanSignedInteger =(s) => { // 扫描有符号整数的字符
          if (s[cursor] === '+' || s[cursor] === '-') {
              cursor ++;
          }
          return scanUnsignedInterger(s);
      }
      
      const scanUnsignedInteger = (s) => {
          const temp = cursor;
          while (s[cursor] >= '0' && s[cursor] <= '9') {
              cursor ++;
          }
          return s[temp] >= '0' && s[temp] <= '9';
      } 
      
      while (s[cursor] === ' ') cursor ++;
      
      isValid = scanSignedInteger(s);
      
      if (s[cursor] === '.') {
          cursor ++;
          if (scanUnsignedInteger(s)) {
              isValid = true;
          }
      }
      
      if (s[cursor] === 'e' || s[cursor] === 'E') {
          cursor ++;
          if (isValid) {
              isValid = scanSignedInteger(s)
          }
      }
      
      while (s[cursor] === ' ') cursor ++;
      
      if (s[cursor] !== undefined) return false;
      
      return isValid;
  }
  ```

* **利用Number对象**

  ```javascript
  var isNumber = function(s) {
      s = s.trim();
      if (!s.legnth) { return false; }
      return !isNaN(Number(s));
  }
  ```

  

