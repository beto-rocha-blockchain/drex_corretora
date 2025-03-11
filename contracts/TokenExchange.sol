// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract TokenExchange {
    IERC20 public token;

    // Evento para quando uma troca de tokens é realizada
    event TokensTrocados(address from, address to, uint256 amount);

    constructor(address tokenAddress) {
        token = IERC20(tokenAddress);
    }

    // Função para trocar tokens
    function trocarTokens(address to, uint256 amount) public {
        require(token.balanceOf(msg.sender) >= amount, "Saldo insuficiente");
        require(token.transfer(to, amount), "Falha na transferencia");

        emit TokensTrocados(msg.sender, to, amount);
    }
}
