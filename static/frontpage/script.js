// Chat Box Functionality
const chatButton = document.getElementById('chatButton');
const chatContainer = document.getElementById('chatContainer');
const closeChat = document.getElementById('closeChat');
const chatInput = document.getElementById('chatInput');
const sendMessage = document.getElementById('sendMessage');
const chatMessages = document.getElementById('chatMessages');

// FAQ responses
const faqResponses = {
    'horário': 'Nossa escola funciona de segunda a sexta, das 7h às 17h.',
    'matrícula': 'Para matrículas, visite nossa secretaria com RG, CPF, comprovante de residência e histórico escolar.',
    'mensalidade': 'As mensalidades variam conforme o ano escolar. Entre em contato pelo telefone (11) 5555-5555 para mais informações.',
    'uniforme': 'O uniforme é obrigatório e pode ser adquirido na loja da escola.',
    'calendário': 'O calendário escolar está disponível no Portal do Aluno ou na secretaria.',
    'férias': 'As férias de julho serão do dia 15 ao dia 31. As férias de fim de ano começam em 15 de dezembro.',
    'contato': 'Você pode nos contatar pelo telefone (11) 5555-5555 ou pelo email contato@escolanovosaber.com.br',
    'endereço': 'Estamos localizados na Av. da Educação, 1000 - São Paulo/SP',
    'prova': 'As provas bimestrais ocorrem na última semana de cada bimestre.'
};

chatButton.addEventListener('click', () => {
    chatContainer.style.display = 'block';
});

closeChat.addEventListener('click', () => {
    chatContainer.style.display = 'none';
});

function addMessage(message, isSent) {
    const messageDiv = document.createElement('div');
    messageDiv.className = message ${isSent ? 'sent' : 'received'};
    messageDiv.textContent = message;
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function processMessage(message) {
    message = message.toLowerCase();
    let response = 'Desculpe, não entendi sua pergunta. Pode reformular?';
    
    // Check for FAQ keywords
    for (const [keyword, answer] of Object.entries(faqResponses)) {
        if (message.includes(keyword)) {
            response = answer;
            break;
        }
    }
    
    // Common greetings
    if (message.match(/olá|oi|bom dia|boa tarde|boa noite/)) {
        response = 'Olá! Como posso ajudar você hoje?';
    }
    
    // Specific questions about school
    if (message.includes('professor') || message.includes('professores')) {
        response = 'Todos os nossos professores são qualificados e possuem formação superior e especialização em suas áreas.';
    }
    
    if (message.includes('turma') || message.includes('vagas')) {
        response = 'Temos turmas do Ensino Fundamental I e II e Ensino Médio. Para verificar disponibilidade de vagas, por favor entre em contato com nossa secretaria.';
    }
    
    if (message.includes('recuperação') || message.includes('reforço')) {
        response = 'Oferecemos aulas de reforço no contraturno para alunos que precisam de apoio adicional. Consulte o coordenador pedagógico.';
    }
    
    setTimeout(() => {
        addMessage(response, false);
    }, 500);
}

sendMessage.addEventListener('click', () => {
    const message = chatInput.value.trim();
    if (message) {
        addMessage(message, true);
        chatInput.value = '';
        processMessage(message);
    }
});

chatInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        sendMessage.click();
    }
});

// Login Modal
const loginButton = document.getElementById('loginButton');
const loginModal = document.getElementById('loginModal');
const closeLoginModal = document.getElementById('closeLoginModal');
const loginForm = document.getElementById('loginForm');
const portalModal = document.getElementById('portalModal');
const closePortalModal = document.getElementById('closePortalModal');
const logoutButton = document.getElementById('logoutButton');

loginButton.addEventListener('click', () => {
    loginModal.style.display = 'flex';
});

closeLoginModal.addEventListener('click', () => {
    loginModal.style.display = 'none';
});

loginForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    
    // Simple validation - in a real app, this would connect to a backend
    if (username && password) {
        loginModal.style.display = 'none';
        portalModal.style.display = 'flex';
        document.getElementById('portalContainer').style.display = 'block';
    }
});

closePortalModal.addEventListener('click', () => {
    portalModal.style.display = 'none';
});

logoutButton.addEventListener('click', (e) => {
    e.preventDefault();
    portalModal.style.display = 'none';
});

// Portal Tabs
const tabButtons = document.querySelectorAll('.tab-button');

tabButtons.forEach(button => {
    button.addEventListener('click', () => {
        // Remove active class from all buttons and contents
        document.querySelectorAll('.tab-button').forEach(btn => {
            btn.classList.remove('active');
        });
        document.querySelectorAll('.tab-content').forEach(content => {
            content.classList.remove('active');
        });
        
        // Add active class to clicked button and corresponding content
        button.classList.add('active');
        const tabId = button.getAttribute('data-tab');
        document.getElementById(tabId).classList.add('active');
    });
});

// Close modals when clicking outside
window.addEventListener('click', (e) => {
    if (e.target === loginModal) {
        loginModal.style.display = 'none';
    }
    if (e.target === portalModal) {
        portalModal.style.display = 'none';
    }
});