document.addEventListener("DOMContentLoaded", function() {
    const loginForm = document.getElementById("login-form");
    const privateKeyInput = document.getElementById("private-key");
    const loginSection = document.getElementById("login-section");
    const registerSection = document.getElementById("register-section");
    const createWalletBtn = document.getElementById("create-wallet-btn");
    const walletAddressDisplay = document.getElementById("wallet-address");
    const privateKeyDisplay = document.getElementById("private-key-display");

    // Função para realizar login
    loginForm.addEventListener("submit", function(event) {
        event.preventDefault();
        const privateKey = privateKeyInput.value;
        
        // Aqui você chamaria a API ou lógica para verificar o login (integrar com Flask ou outra API)
        console.log("Login com chave privada: ", privateKey);
        
        // Exemplo de resposta de sucesso
        alert("Login bem-sucedido!");
    });

    // Função para criar nova carteira
    createWalletBtn.addEventListener("click", function() {
        // Aqui você criaria uma nova carteira e exibiria os detalhes
        console.log("Criando nova carteira...");

        // Exemplo: simulação de um endereço e chave privada
        const newAddress = "0x1234567890abcdef1234567890abcdef12345678";
        const newPrivateKey = "0xabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdef";

        walletAddressDisplay.textContent = newAddress;
        privateKeyDisplay.textContent = newPrivateKey;
        alert("Carteira criada com sucesso!");
    });
});
