// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DrexAuth {
    mapping(address => bool) public usuarios;
    mapping(address => bytes32) public chavesPrivadas;

    // Evento que será emitido quando um novo usuário for registrado
    event UsuarioRegistrado(address usuario);

    // Função para registrar um novo usuário
    function registrarUsuario(address usuario, bytes32 chavePrivada) public {
        require(usuario != address(0), "Endereco invalido");
        require(chavesPrivadas[usuario] == 0, "Usuario ja registrado");

        chavesPrivadas[usuario] = chavePrivada;
        usuarios[usuario] = true;

        emit UsuarioRegistrado(usuario);
    }

    // Função para verificar se o usuário está registrado
    function verificarUsuario(address usuario) public view returns (bool) {
        return usuarios[usuario];
    }

    // Função para alterar a chave privada de um usuário
    function alterarChavePrivada(address usuario, bytes32 novaChavePrivada) public {
        require(usuarios[usuario], "Usuario nao registrado");
        chavesPrivadas[usuario] = novaChavePrivada;
    }

    // Função para autenticar o usuário com base na chave privada
    function autenticar(address usuario, bytes32 chavePrivada) public view returns (bool) {
        return chavesPrivadas[usuario] == chavePrivada;
    }
}
