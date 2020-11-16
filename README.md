<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/Carol111/feedback">
    <img src="https://imgur.com/jOnRoZg.png" alt="Logo" height="100">
  </a>


  <p align="center">
    Projeto desenvolvido para o TCC em Eng. de COmputação na UNIVASF
    <br />
    <a href="https://feedback-web.herokuapp.com/">Visualizar aplicação</a>
  </p>
</p>


<!-- ABOUT THE PROJECT -->
## Sobre o projeto

![Screen Shot](https://imgur.com/I67VcGe.png)

**feedback** é uma ferramenta de código aberto desenvolvida durante o TCC do curso de Engenharia de Computação da Univasf.

**feedback** utiliza o análise de sentimentos para classificar comentários de discentes em positivos e negativos, permitindo que os docentes tenham conhecimento das opiniões acerca da sua disciplina.


**Caroline Carvalho Machado**

- **Orientador:** Prof. Dr. Ricardo Argenton Ramos
- **Co-orientador:** Me. Lucas Florêncio de Brito



### Installation

1. Clone o repositório
```sh
git clone git@github.com:Carol111/feedback.git
```
2. Instale os requisitos
```sh
pip3 install -r requirements.txt
```
3. Crie um arquivo .env copiando o .env.example
4. Colete os arquivos estáticos para STATIC_ROOT
```sh
python manage.py collectstatic
```
5. Rode as migrations
```sh
python manage.py migrate   
```
6. Rode a aplicação
```sh
python manage.py runserver 
```

