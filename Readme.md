# Web Scraping e armazenamento em um banco MySQL

Este projeto coleta informações do site "valorinveste.globo.com" através de web scraping e armazena em um banco de dados MySQL. Após o armazenamento dos dados contidos no banco é possível retornar os dados para um DataFrame pandas.

O algoritmo "set_project.py" é responsável por criar a base de dados e tabelas no MySQL. O algoritmo "get_data.py" coleta o nome, o código e valor de fechamento da ação do dia anterior e armazena nas tabelas criadas. Como o alvo é o valor de fechamento, para evitar valores repetidos, o algoritmo somente acrescenta dados uma vez por dia. O algoritmo "return_data.py" retorna os valores armazenados até o momento no banco de dados para um pandas DataFrame.