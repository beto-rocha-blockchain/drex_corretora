// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";

contract NFTMarketplace {
    IERC721 public nft;

    struct Oferta {
        address vendedor;
        uint256 preco;
    }

    mapping(uint256 => Oferta) public ofertas;

    // Evento para quando uma NFT é colocada à venda
    event NFTColocadaAVenda(address vendedor, uint256 nftId, uint256 preco);

    constructor(address nftAddress) {
        nft = IERC721(nftAddress);
    }

    // Função para colocar uma NFT à venda
    function colocarAVenda(uint256 nftId, uint256 preco) public {
        require(nft.ownerOf(nftId) == msg.sender, "Voce nao e o proprietario da NFT");
        require(preco > 0, "Preco deve ser maior que 0");

        ofertas[nftId] = Oferta(msg.sender, preco);

        emit NFTColocadaAVenda(msg.sender, nftId, preco);
    }

    // Função para comprar uma NFT
    function comprarNFT(uint256 nftId) public payable {
        Oferta memory oferta = ofertas[nftId];

        require(oferta.vendedor != address(0), "NFT nao esta a venda");
        require(msg.value >= oferta.preco, "Preco insuficiente");

        // Transferir a NFT para o comprador
        nft.safeTransferFrom(oferta.vendedor, msg.sender, nftId);

        // Transferir o valor para o vendedor
        payable(oferta.vendedor).transfer(msg.value);

        // Limpar a oferta
        delete ofertas[nftId];
    }
}
