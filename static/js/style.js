// js관련 파일입니다.
function submitQuestion() {
    const userInput = document.getElementById('user-input').value.trim();
    const keywords = ['smile', 'eyes_closed', 'winter', 'padded', 'badge'];
    let imageName = 'default_image';

    // 입력된 키워드에 따라 이미지 결정
    keywords.forEach(keyword => {
        if (userInput.toLowerCase().includes(keyword)) {
            imageName = `${keyword}.png`;
        }
    });

    // 교수님 이미지 업데이트
    document.getElementById('professor-img').src = `images/${imageName}`;

    // 백엔드 호출 또는 정적 응답 생성 로직 구현
    document.getElementById('response').innerText = "질문에 따른 응답이 여기에 표시됩니다.";
}

document.getElementById('user-input').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        submitQuestion();
    }
});
