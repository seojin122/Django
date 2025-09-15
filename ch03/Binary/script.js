// script.js
document.getElementById("convertBtn").addEventListener("click", function() {
    let binaryValue = "";

    // 체크박스 상태를 읽어서 이진수 문자열 생성
    for (let i = 7; i >= 0; i--) {
        let bitValue = document.getElementById(`bit${i}`).checked ? "1" : "0";
        binaryValue += bitValue;
    }

    // 이진수를 10진수와 16진수로 변환
    let decimalValue = parseInt(binaryValue, 2);
    let hexValue = decimalValue.toString(16).toUpperCase();

    // 결과 출력
    document.getElementById("decimalResult").textContent = decimalValue;
    document.getElementById("hexResult").textContent = hexValue;
});
