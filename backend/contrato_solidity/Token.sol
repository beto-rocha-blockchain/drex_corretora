// contract/Token.sol
pragma solidity ^0.8.0;

contract Token {
    string public name = "MeuToken";
    string public symbol = "MTK";
    uint256 public totalSupply = 1000000;

    mapping(address => uint256) public balanceOf;

    constructor() {
        balanceOf[msg.sender] = totalSupply;
    }

    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(balanceOf[msg.sender] >= amount, "Saldo insuficiente");
        balanceOf[msg.sender] -= amount;
        balanceOf[recipient] += amount;
        return true;
    }
}
