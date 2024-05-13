// js관련 파일입니다.
function submitQuestion() {
    const userInput = document.getElementById('user-input').value.trim();
    const chatHistory = document.getElementById('chat-history');
    let imageName = 'default_image.png'; // 기본 이미지 이름 설정

    // 사용자 메시지 말풍선 추가
    let userBubble = document.createElement('div');
    userBubble.classList.add('chat-message', 'user-message');
    userBubble.innerText = userInput;
    chatHistory.appendChild(userBubble);

    /*
    // 이미지 파일명 키워드 리스트
    const imageKeywords = ['웃는', '정색', '눈감은', '행복', '활짝웃는', '화난', '피곤한', '기쁜']; // 실제 이미지 파일 이름에 맞춰 조정 필요

    // 사용자 입력에서 이미지 파일명 키워드를 찾아 매칭되는 이미지로 변경
    imageKeywords.forEach(keyword => {
        if (userInput.includes(keyword)) {
            imageName = `${keyword}.png`; // 예시, 실제 경로는 파일명에 맞춰서 조정
        }
    });

    // 교수님 이미지 업데이트
    document.getElementById('professor-img').src = `images/${imageName}`;
    */

    // 백엔드 호출 또는 정적 응답 생성 로직 구현
    setTimeout(() => {
        let professorResponse = "교수님 응답";
        let professorBubble = document.createElement('div');
        professorBubble.classList.add('chat-message', 'professor-message');
        professorBubble.innerText = professorResponse;
        chatHistory.appendChild(professorBubble);
    }, 1000);

    // 입력창 초기화
    document.getElementById('user-input').value = '';
}

document.getElementById('user-input').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        submitQuestion();
    }
});

