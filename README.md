# Algebra-Linear-Computacional

Projeto realizado em python3 por Amanda Lucio e Nayara Gomes.

## Table of Contents:

- [Estrutura do projeto](#Estrutura)
- [Como usar](#Como-usar)
- [Como rodar](#Como-Rodar)

## Estrutura do projeto

O projeto foi estrutura visando a construção de uma pasta com programa reutilizados por todas as tasks, evitando a repetição de código.

```
C:.
├───data
│   ├───inputs
│   └───outputs
│
├───files
│
└───src
    ├───task_1
    │   ├───decomposition
    │   └───iterative_procedure
    └───task_2

```

## Como usar

O projeto possui uma pasta para [inputs](https://github.com/AmandaACLucio/Algebra-Linear-Computacional/tree/master/files/inputs), na mesma você precisará alterar o conteúdo dos arquivos .dat, de acordo com a task desejada. Além disso, é necessário alterar o arquivo de [configurações](https://github.com/AmandaACLucio/Algebra-Linear-Computacional/blob/master/files/inputs/config.json) para selecionar o programa da task que deseja rodar e os outros flags.

## Como rodar

Para rodar basta usar o comando abaixo:

```sh
$ python main.py
> Escolha a task desejada
```

Desta forma, basta digitar o número da task correspondente:

- [Task1](https://github.com/AmandaACLucio/Algebra-Linear-Computacional/tree/master/src/task_1)
- [Task2](https://github.com/AmandaACLucio/Algebra-Linear-Computacional/tree/master/src/task_2)
