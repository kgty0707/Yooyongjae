// js관련 파일입니다.
function submitQuestion() {
    const url = 'http://localhost:8000/send_query';
    const modelType = document.getElementById('model-select').value;
    const userInput = document.getElementById('user-input').value;
    const sendButton = document.getElementById('send-button');
    const spinner = document.getElementById('spinner');
    const userQuestionDiv = document.getElementById('user-question');

    if (userInput.trim() === "") {
        alert("질문을 입력하세요.");
        return;
    }

    const data = {
        model_type: modelType,
        query: userInput
    };

    // 사용자 질문을 핑크색 말풍선에 표시
    userQuestionDiv.innerHTML = userInput;

    // 전송 버튼 비활성화 및 스피너 표시
    sendButton.disabled = true;
    spinner.style.display = 'block';

    // 백엔드에 데이터 전송
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        // 응답 데이터 처리
        document.getElementById('professor-response').innerHTML = data.answer;
        const pictureUrl = '/static/images/' + encodeURIComponent(data.picture);
        document.getElementById('professor-img').src = pictureUrl;

        // 전송 버튼 활성화 및 스피너 숨김
        sendButton.disabled = false;
        spinner.style.display = 'none';
    })
    .catch(error => {
        console.error('Error:', error);

        // 전송 버튼 활성화 및 스피너 숨김
        sendButton.disabled = false;
        spinner.style.display = 'none';
    });
}


/*
function submitQuestion() {
    const userInput = document.getElementById('user-input').value.trim();
    const modelSelect = document.getElementById('model-select').value;
    const chatResponse = document.getElementById('chat-response');
    const sendButton = document.getElementById('send-button');

    if (!userInput) {
        alert("질문을 입력하세요.");
        return;
    }

    // 사용자 메시지 말풍선 추가
    let userBubble = document.createElement('div');
    userBubble.classList.add('chat-message', 'user-message');
    userBubble.innerText = userInput;
    chatResponse.appendChild(userBubble);

    // 전송 버튼 비활성화 및 스피너 추가
    sendButton.disabled = true;
    let spinner = document.createElement('div');
    spinner.classList.add('spinner');
    chatResponse.appendChild(spinner);

    // 서버로 요청 보내기
    fetch('/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ input_text: userInput, model_type: modelSelect })
    })
    .then(response => response.json())
    .then(data => {
        chatResponse.removeChild(spinner);
        
        let professorImage = data.image_url;
        let professorResponse = data.response;

        // 교수님 이미지 업데이트
        document.getElementById('professor-img').src = professorImage;

        // 교수님 응답 말풍선 추가
        let professorBubble = document.createElement('div');
        professorBubble.classList.add('chat-message', 'professor-message');
        professorBubble.innerText = professorResponse;
        chatResponse.appendChild(professorBubble);

        // 전송 버튼 활성화
        sendButton.disabled = false;
    })
    .catch(error => {
        console.error('Error:', error);
        chatResponse.removeChild(spinner);
        sendButton.disabled = false;
    });

    // 입력창 초기화
    document.getElementById('user-input').value = '';
}

document.getElementById('user-input').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        submitQuestion();
    }
});
*/

/*
function submitQuestion() {
    const userInput = document.getElementById('user-input').value.trim();
    const chatHistory = document.getElementById('chat-history');
    let imageName = 'default_image.png'; // 기본 이미지 이름 설정

    // 사용자 메시지 말풍선 추가
    let userBubble = document.createElement('div');
    userBubble.classList.add('chat-message', 'user-message');
    userBubble.innerText = userInput;
    chatHistory.appendChild(userBubble);

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

*/