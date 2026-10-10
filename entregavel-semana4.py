produtos = []

quantidade = int(input("Quantos produtos deseja cadastrar? "))

for indice in range(quantidade):
    print(f"\nProduto {indice + 1}")

    nome = input("Nome: ")
    preco = float(input("Preço: ").replace(",", "."))
    categoria = input("Categoria: ")

    produtos.append([nome, preco, categoria])

if quantidade > 0:
    limite_preco = float(
        input("\nInforme o preço para filtragem: ").replace(",", ".")
    )

    print("\n--- Produtos acima do preço informado ---")
    for produto in produtos:
        if produto[1] > limite_preco:
            print(f"{produto[0]} - R$ {produto[1]:.2f}")

    print("\n--- Produtos abaixo do preço informado ---")
    for produto in produtos:
        if produto[1] < limite_preco:
            print(f"{produto[0]} - R$ {produto[1]:.2f}")

    produtos.sort(key=lambda produto: produto[1])

    print("\n--- Preços em ordem crescente ---")
    for produto in produtos:
        print(f"{produto[0]} - R$ {produto[1]:.2f}")

    produtos_decrescentes = sorted(
        produtos,
        key=lambda produto: produto[1],
        reverse=True
    )

    print("\n--- Preços em ordem decrescente ---")
    for produto in produtos_decrescentes:
        print(f"{produto[0]} - R$ {produto[1]:.2f}")

    categorias_unicas = set()

    for produto in produtos:
        categorias_unicas.add(produto[2])

    print("\n--- Categorias únicas ---")
    for categoria in sorted(categorias_unicas):
        print(categoria)

    precos = [produto[1] for produto in produtos]

    estatisticas = (
        min(precos),
        max(precos),
        sum(precos) / len(precos)
    )

    menor_preco, maior_preco, media_precos = estatisticas

    print("\n========== RELATÓRIO FINAL ==========")
    print(f"Total de produtos: {len(produtos)}")
    print(f"Menor preço: R$ {menor_preco:.2f}")
    print(f"Maior preço: R$ {maior_preco:.2f}")
    print(f"Média dos preços: R$ {media_precos:.2f}")
    print(f"Total de categorias únicas: {len(categorias_unicas)}")

else:
    print("Nenhum produto cadastrado.")