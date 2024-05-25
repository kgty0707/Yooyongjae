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
        console.log(data)
        console.log(data.picture)
        const pictureUrl = '../static/image_data/' + decodeURIComponent(data.picture);
        console.log(pictureUrl)
        document.getElementById('professor-img').src = pictureUrl;
        

        // 전송 버튼 활성화 및 스피너 숨김
        sendButton.disabled = false;
        spinner.style.display = 'none';

        // 입력창 비우기
        document.getElementById('user-input').value = "";
    })
    .catch(error => {
        console.error('Error:', error);

        // 전송 버튼 활성화 및 스피너 숨김
        sendButton.disabled = false;
        spinner.style.display = 'none';
    });
}