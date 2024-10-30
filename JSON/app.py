import json

# Suponha que você tenha uma lista de dicionários para todas as escolas
todas_as_escolas = [
    {
        "instituicao": "Centro Educacional Especializado Alegria de Viver",
        "equipe_gestora": {
            "diretora": "Joelma Queiroz Santana",
            "coordenadora": "Larissa Alves Costa",
            "secretario_escolar": "Waneylla Leal Santos"
        },
        "servidores_efetivos": {
            "docentes": [
                {
                    "ordem": 1,
                    "nome": "Águina Matos dos Anjos",
                    "ch": "20",
                    "observacoes": ""
                },
                {
                    "ordem": 2,
                    "nome": "Ana Claudia Santos Lucas",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "ordem": 3,
                    "nome": "Carla Cristina Rodrigues Silva dos Anjos",
                    "ch": "20",
                    "observacoes": ""
                },
                {
                    "ordem": 4,
                    "nome": "Claudinea Pereira Dias Queiroz",
                    "ch": "20/20",
                    "observacoes": ""
                },
                {
                    "ordem": 5,
                    "nome": "Isolda Santos Sena",
                    "ch": "20",
                    "observacoes": ""
                },
                {
                    "ordem": 6,
                    "nome": "Ivonilde Moraes Santos Vieira",
                    "ch": "20",
                    "observacoes": ""
                },
                {
                    "ordem": 7,
                    "nome": "Mª da Conceição dos Santos Ribeiro",
                    "ch": "20/20",
                    "observacoes": "Readaptada"
                },
                {
                    "ordem": 8,
                    "nome": "Maria Célia Coelho Sampaio",
                    "ch": "20",
                    "observacoes": ""
                },
                {
                    "ordem": 9,
                    "nome": "Maristela Amaral Ribeiro",
                    "ch": "20/20",
                    "observacoes": "Doutorado"
                },
                {
                    "ordem": 10,
                    "nome": "Renildo da Cruz Santos",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "ordem": 11,
                    "nome": "Rosemery Sousa Martinelli",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "ordem": 12,
                    "nome": "Soraia Pereira dos Santos",
                    "ch": "20",
                    "observacoes": ""
                },
                {
                    "ordem": 13,
                    "nome": "Vera Lúcia Bastos dos Santos",
                    "ch": "40",
                    "observacoes": ""
                }
            ],
            "coordenadora_pedagogica": {
                "nome": "Joelma Queiroz Santana",
                "ch": "20",
                "observacoes": "Diretora"
            },
            "professores_desdobrados": [
                {
                    "nome": "Carlos Roberto Oliveira",
                    "ch": "20",
                    "observacoes": "SMED"
                },
                {
                    "nome": "Jurema Gomes Sousa",
                    "ch": "20",
                    "observacoes": ""
                }
            ],
            "secretario_escolar": {
                "nome": "Waneylla Leal Santos",
                "ch": "20",
                "observacoes": "Delminda"
            },
            "atendente_de_classe": {
                "nome": "Erinalva Brito dos Santos",
                "ch": "40",
                "observacoes": ""
            },
            "interpretes_libras": [
                {
                    "nome": "Carlos Roberto Oliveira",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "nome": "Jurema Gomes Sousa",
                    "ch": "40",
                    "observacoes": ""
                }
            ],
            "aux_servico_escolar": [
                {
                    "nome": "Antônio Jorge F. Bento",
                    "ch": "40",
                    "observacoes": "Vigilante noturno"
                },
                {
                    "nome": "Eronice Pereira da Silva",
                    "ch": "30",
                    "observacoes": "Readaptada"
                },
                {
                    "nome": "Jussiara Oliveira",
                    "ch": "30",
                    "observacoes": ""
                }
            ],
            "servidores_infraestrutura": [
                {
                    "nome": "Maria Irene Costa Felix",
                    "ch": "40",
                    "observacoes": "INSS"
                },
                {
                    "nome": "Zenilda Batista Pereira",
                    "ch": "40",
                    "observacoes": "INSS"
                }
            ]
        },
        "servidores_contratados": {
            "atendentes_de_classe": [
                {
                    "nome": "Aiala Mikaele Santos Cerqueira",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "nome": "Antonia Cristina Cassemiro Dos Santos",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "nome": "Cleise Cardoso Dos Santos",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "nome": "Iohanna Kayena Evangelista Santos Souza",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "nome": "Marialva Ferreira Da Silva",
                    "ch": "40",
                    "observacoes": ""
                }
            ],
            "auxiliares_infraestrutura": [
                {
                    "nome": "Alcione Dutra Santos",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "nome": "Amanda Xavier Dos Santos",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "nome": "Ana Paula Santos Da Silva",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "nome": "Antonia Oliveira Bomfim Dos Santos Filha",
                    "ch": "20",
                    "observacoes": ""
                },
                {
                    "nome": "Jamili Silva Araújo",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "nome": "Simone De Jesus Santos",
                    "ch": "40",
                    "observacoes": ""
                }
            ],
            "coordenador_pedagogico": {
                "nome": "Larissa Alves Costa",
                "ch": "20",
                "observacoes": ""
            },
            "fisioterapeuta": {
                "nome": "Drielle Pires Bomfim",
                "ch": "20",
                "observacoes": ""
            },
            "professores": [
                {
                    "nome": "Erenice de Jesus Santos Rodrigues",
                    "ch": "20",
                    "observacoes": ""
                },
                {
                    "nome": "Leandro Reis Santos",
                    "ch": "20",
                    "observacoes": ""
                },
                {
                    "nome": "Tailane Silva de Araujo",
                    "ch": "20",
                    "observacoes": ""
                }
            ],
            "vigilantes_escolares": [
                {
                    "nome": "Alan Emerson Barbosa da Silva",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "nome": "Cesar Francisco de Sousa",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "nome": "Wilberto Souto Bispo",
                    "ch": "40",
                    "observacoes": ""
                }
            ]
        }
    },
    {
        "instituicao": "Escola Arlinda Emília de Assis",
        "equipe_gestora": {
            "diretor": "Ildete Santos Costa",
            "vice_diretores": [
                "Girleide Ramos dos Santos",
                "Cristiane Nascimento da Silva"
            ],
            "coordenador": "Maria da Conceição Sacramento",
            "secretario_escolar": "Manoel da Hora Santos Junior",
            "assistente_administrativo": "Maria da Conceição Sousa Santana"
        },
        "servidores_efetivos": {
            "docentes": [
                {
                    "ordem": 1,
                    "nome": "Adelice de Jesus da Silva",
                    "ch": "20",
                    "observacoes": ""
                },
                {
                    "ordem": 2,
                    "nome": "Adriana Silva Pelegrini",
                    "ch": "20",
                    "observacoes": ""
                },
                {
                    "ordem": 3,
                    "nome": "Cristiane Monteiro Coelho",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "ordem": 4,
                    "nome": "Cristiane Nascimento da Silva",
                    "ch": "40",
                    "observacoes": "Vice-Diretora"
                },
                {
                    "ordem": 5,
                    "nome": "Gilcilea Marinho Peixoto",
                    "ch": "20",
                    "observacoes": "SMED"
                },
                {
                    "ordem": 6,
                    "nome": "Girleide Ramos dos Santos",
                    "ch": "20/20",
                    "observacoes": "Vice-Diretora"
                },
                {
                    "ordem": 7,
                    "nome": "Ivanete Santos Costa",
                    "ch": "20/20",
                    "observacoes": "SMED"
                },
                {
                    "ordem": 8,
                    "nome": "Ildete Santos Costa",
                    "ch": "20",
                    "observacoes": "Diretora"
                },
                {
                    "ordem": 9,
                    "nome": "Joçara Alencar de Oliveira",
                    "ch": "20/20",
                    "observacoes": ""
                },
                {
                    "ordem": 10,
                    "nome": "Josivânia Ferreira Barbosa da Hora",
                    "ch": "20",
                    "observacoes": ""
                },
                {
                    "ordem": 11,
                    "nome": "Leda Suely Souza Santos",
                    "ch": "20",
                    "observacoes": ""
                },
                {
                    "ordem": 12,
                    "nome": "Lede Ana Santos Bispo",
                    "ch": "20",
                    "observacoes": ""
                },
                {
                    "ordem": 13,
                    "nome": "Letícia Coelho dos Santos",
                    "ch": "20",
                    "observacoes": ""
                },
                {
                    "ordem": 14,
                    "nome": "Rejane da Silva Pinheiro",
                    "ch": "20",
                    "observacoes": ""
                },
                {
                    "ordem": 15,
                    "nome": "Sileia Alves dos Santos",
                    "ch": "20/20",
                    "observacoes": ""
                },
                {
                    "ordem": 16,
                    "nome": "Valdenice Alves de Souza",
                    "ch": "40",
                    "observacoes": ""
                }
            ],
            "professores_desdobrados": [
                {
                    "nome": "Adelice de Jesus da Silva",
                    "ch": "20",
                    "observacoes": ""
                },
                {
                    "nome": "Leda Suely Souza Santos",
                    "ch": "20",
                    "observacoes": ""
                }
            ],
            "coordenadora_pedagogica": {
                "nome": "Maria da Conceição Sacramento",
                "ch": "20",
                "observacoes": ""
            },
            "secretario_escolar": {
                "nome": "Manoel da Hora Santos Junior",
                "ch": "",
                "observacoes": ""
            },
            "vigilantes": [
                {
                    "nome": "Moacir Santiago da Hora",
                    "ch": "40",
                    "observacoes": "Noturno"
                },
                {
                    "nome": "Ritonio de Oliveira Moreira",
                    "ch": "40",
                    "observacoes": "Noturno"
                }
            ],
            "atendentes_de_classe": [
                {
                    "nome": "Silvana Fonseca Santiago Santos",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "nome": "Cristiane da Paixão Lima Passos",
                    "ch": "40",
                    "observacoes": "Está cedida"
                },
                {
                    "nome": "Elival de Jesus dos Santos",
                    "ch": "40",
                    "observacoes": "SMED"
                },
                {
                    "nome": "Iracema de Souza",
                    "ch": "40",
                    "observacoes": ""
                }
            ],
            "auxiliares_infraestrutura_escolar": [
                {
                    "nome": "Gilson Oliveira da Costa",
                    "ch": "30",
                    "observacoes": ""
                },
                {
                    "nome": "Leidiane Santos Souza",
                    "ch": "30",
                    "observacoes": "SMED"
                },
                {
                    "nome": "Maria das Graças de Jesus Vilarino",
                    "ch": "30",
                    "observacoes": ""
                },
                {
                    "nome": "Miriam dos Santos Brito",
                    "ch": "30",
                    "observacoes": "Está cedida"
                },
                {
                    "nome": "Nilda da Silva Piropo de Oliveira",
                    "ch": "30",
                    "observacoes": ""
                },
                {
                    "nome": "Simone Margarida dos Santos",
                    "ch": "30",
                    "observacoes": ""
                },
                {
                    "nome": "Sule Kunta Kinte dos Santos Sampaio",
                    "ch": "30",
                    "observacoes": ""
                },
                {
                    "nome": "Thaylana Costa S. de Andrade",
                    "ch": "30",
                    "observacoes": "Readaptada"
                },
                {
                    "nome": "Zenildo Dutra da Silva",
                    "ch": "30",
                    "observacoes": "Luzia Silva"
                }
            ],
            "servidor_cedido_pela_sec_infraestrutura": {
                "nome": "Valdivan Silva Dias",
                "ch": "40",
                "observacoes": ""
            }
        },
        "servidores_contratados": {
            "assistente_administrativo": {
                "nome": "Maria da Conceição Sousa Santana",
                "ch": "40",
                "observacoes": ""
            },
            "atendentes_de_classe": [
                {
                    "nome": "Claudia Eunice Souza Teles",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "nome": "Josiane da Ressurreicao Santos",
                    "ch": "20",
                    "observacoes": ""
                },
                {
                    "nome": "Paula Leticia Peixoto Lima",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "nome": "Valeria Santos Silva",
                    "ch": "40",
                    "observacoes": ""
                }
            ],
            "merendeira": {
                "nome": "Iselinda de Jesus Trindade",
                "ch": "40",
                "observacoes": ""
            },
            "auxiliar_alimentacao_escolar": {
                "nome": "Karine Bandeira Santos",
                "ch": "40",
                "observacoes": ""
            },
            "auxiliares_infraestrutura_escolar": [
                {
                    "nome": "Larissa de Santana Fontes",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "nome": "Nívia Ferreira Santos",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "nome": "Thamires Santos Souza",
                    "ch": "40",
                    "observacoes": ""
                }
            ],
            "professores_regentes": [
                {
                    "nome": "Djamary Fonseca Santos Barreto",
                    "ch": "20",
                    "observacoes": ""
                },
                {
                    "nome": "Irailda Ferreira dos Santos",
                    "ch": "20",
                    "observacoes": ""
                },
                {
                    "nome": "Leislangela dos Santos Rodrigues",
                    "ch": "20",
                    "observacoes": ""
                }
            ],
            "profissionais_apoio_alunos_com_deficiencia": [
                {
                    "nome": "Eliete Rodrigues Cardoso",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "nome": "Gleice Kelly Rodrigues da Silva",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "nome": "Leidinea Umbelino dos Santos",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "nome": "Lizandra Nascimento Santana",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "nome": "Luciane Sena de Franca",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "nome": "Maria Gabriela Oliveira de Jesus",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "nome": "Michele Fonseca Lima Ferreira",
                    "ch": "40",
                    "observacoes": ""
                }
            ],
            "vigilante_diurno": {
                "nome": "Rodrigo Silva de Jesus",
                "ch": "40",
                "observacoes": ""
            }
        }
    },
    {
        "instituicao": "Cantina Central",
        "servidores_efetivos": [
            {
                "ordem": 1,
                "cargo": "Auxiliar Serv. Escolar",
                "ch": "30",
                "funcionario": "Lucineide Paixão dos Santos",
                "observacoes": ""
            },
            {
                "ordem": 2,
                "cargo": "Auxiliar Serv. Escolar",
                "ch": "30",
                "funcionario": "Roberto da Costa Lima",
                "observacoes": ""
            }
        ],
        "servidores_contratados": {
            "nutricionistas": [
                {
                    "ordem": 1,
                    "funcionario": "Hyan Emanuel da Silva Souza",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "ordem": 2,
                    "funcionario": "Allana Pereira Viana",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "ordem": 3,
                    "funcionario": "Tainã",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "ordem": 4,
                    "funcionario": "Rosana Piropo de Jesus",
                    "ch": "40",
                    "observacoes": ""
                }
            ],
            "carregadores": [
                {
                    "ordem": 5,
                    "funcionario": "Alisson de Jesus Costa",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "ordem": 6,
                    "funcionario": "Erisvaldo Bispo dos Santos",
                    "ch": "40",
                    "observacoes": ""
                }
            ],
            "motoristas": [
                {
                    "ordem": 1,
                    "funcionario": "Almiro Santos dos Anjos",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "ordem": 2,
                    "funcionario": "Juscelio Santos São Pedro",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "ordem": 3,
                    "funcionario": "Wagner Souza Moraes",
                    "ch": "40",
                    "observacoes": ""
                }
            ]
        }
    },
    {
        "instituicao": "Escola Carneiro Ribeiro",
        "equipe_gestora": {
            "diretora": "Jurema Bomfim de Quadros",
            "vice_diretora": "Ivana Carla Xavier Silva",
            "coordenadora": "Marisa dos Santos Sampaio",
            "secretario_escolar": "Marcelo Vinicius Almeida Santos"
        },
        "servidores_efetivos": {
            "docentes": [
                {
                    "ordem": 1,
                    "nome": "Ivana Carla Xavier Silva",
                    "ch": "20",
                    "observacoes": ""
                },
                {
                    "ordem": 2,
                    "nome": "Jurema Bomfim de Quadros",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "ordem": 3,
                    "nome": "Mª Telma Santos Costa",
                    "ch": "40",
                    "observacoes": "SMED"
                },
                {
                    "ordem": 4,
                    "nome": "Maria Gorete Andrade de Almeida",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "ordem": 5,
                    "nome": "Maria Rita Bastos da Costa",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "ordem": 6,
                    "nome": "Valdeir dos Santos Vieira",
                    "ch": "40",
                    "observacoes": "Readaptada"
                }
            ],
            "coordenadora_pedagogica": [
                {
                    "nome": "Acenate Santos de Souza",
                    "ch": "20",
                    "observacoes": "Mestrado"
                }
            ],
            "vigilantes": [
                {
                    "nome": "Paulo Sergio Souza de Sena",
                    "ch": "44",
                    "observacoes": ""
                },
                {
                    "nome": "Gilmar Ribeiro da Silva",
                    "ch": "44",
                    "observacoes": ""
                }
            ],
            "auxiliares_infraestrutura_escolar": [
                {
                    "nome": "Aldemira Gomes dos Santos",
                    "ch": "30",
                    "observacoes": ""
                },
                {
                    "nome": "Alexsandro Barbosa dos Santos",
                    "ch": "30",
                    "observacoes": "SMED"
                },
                {
                    "nome": "Amanda Bomfim Sales",
                    "ch": "30",
                    "observacoes": "Remoção provisória"
                },
                {
                    "nome": "Anderson Couto da Silva",
                    "ch": "30",
                    "observacoes": ""
                },
                {
                    "nome": "Ednéia Almeida Silva",
                    "ch": "30",
                    "observacoes": ""
                },
                {
                    "nome": "Josenilda Silva Fonseca",
                    "ch": "30",
                    "observacoes": "Merendeira"
                },
                {
                    "nome": "Rozalina Margarida Jesus dos Santos",
                    "ch": "30",
                    "observacoes": ""
                },
                {
                    "nome": "Valdiléia de Almeida Lopes",
                    "ch": "30",
                    "observacoes": ""
                }
            ]
        },
        "servidores_contratados": {
            "auxiliares_alimentacao_escolar": [
                {
                    "ordem": 1,
                    "nome": "Luana Bomfim Sales",
                    "ch": "40",
                    "observacoes": ""
                }
            ],
            "coordenador_pedagogico": [
                {
                    "ordem": 1,
                    "nome": "Marisa dos Santos Sampaio",
                    "ch": "20",
                    "observacoes": ""
                }
            ],
            "professores_regentes": [
                {
                    "ordem": 1,
                    "nome": "Alaine Silva Coelho",
                    "ch": "20",
                    "observacoes": ""
                },
                {
                    "ordem": 2,
                    "nome": "Franciane Suares da Silva",
                    "ch": "20",
                    "observacoes": ""
                },
                {
                    "ordem": 3,
                    "nome": "Jussara Almeida Santos",
                    "ch": "20",
                    "observacoes": ""
                },
                {
                    "ordem": 4,
                    "nome": "Valdinelia Rodrigues dos Santos",
                    "ch": "20",
                    "observacoes": ""
                }
            ],
            "profissionais_apoio_deficiencia": [
                {
                    "ordem": 1,
                    "nome": "Francielle Lima Dos Santos",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "ordem": 2,
                    "nome": "Jossilene da Rocha Oliveira",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "ordem": 3,
                    "nome": "Mª do Carmo Barbosa Cerqueira",
                    "ch": "40",
                    "observacoes": ""
                }
            ],
            "secretario_escolar": [
                {
                    "ordem": 1,
                    "nome": "Marcelo Vinicius Almeida Santos",
                    "ch": "40",
                    "observacoes": ""
                }
            ],
            "auxiliares_infraestrutura_escolar": [
                {
                    "ordem": 1,
                    "nome": "Viviane Almeida Dos Santos",
                    "ch": "40",
                    "observacoes": ""
                }
            ],
            "vigilantes": [
                {
                    "ordem": 1,
                    "nome": "Valdir Alves de Sousa",
                    "ch": "40",
                    "observacoes": "Diurno"
                },
                {
                    "ordem": 2,
                    "nome": "Cleiton Agustinho Alves",
                    "ch": "40",
                    "observacoes": "Noturno"
                },
                {
                    "ordem": 3,
                    "nome": "Fabiano Silva Moura",
                    "ch": "40",
                    "observacoes": "Noturno"
                }
            ]
        }
    },
    {
        "instituicao": "Escola Presidente Castelo Branco",
        "equipe_gestora": {
            "diretor": "Rosilene Almeida",
            "vice_diretor": [
                "Neide Santiago da Hora",
                "Josefa Raimunda Santos da Silva"
            ],
            "coordenador": "Eline Santana Ramos",
            "secretario_escolar": "Eduardo Gonçalves de Arruda",
            "assistente_administrativo": "Dilma Teixeira Santos"
        },
        "servidores_efetivos": {
            "docentes": [
                {
                    "ordem": 1,
                    "nome": "Analu Galvão dos Santos",
                    "ch": "20",
                    "observacoes": ""
                },
                {
                    "ordem": 2,
                    "nome": "Claudina Santos Lima",
                    "ch": "20",
                    "observacoes": "Remoção Provisória"
                },
                {
                    "ordem": 3,
                    "nome": "Ednalva Santos Costa",
                    "ch": "20",
                    "observacoes": "Remoção Provisória"
                },
                {
                    "ordem": 4,
                    "nome": "Evely Larissa Moreira Cavalcante",
                    "ch": "20",
                    "observacoes": "Remoção Provisória - INSS"
                },
                {
                    "ordem": 5,
                    "nome": "Erenice Dias Bispo",
                    "ch": "20",
                    "observacoes": ""
                },
                {
                    "ordem": 6,
                    "nome": "Ildete Santos Costa",
                    "ch": "20",
                    "observacoes": "Diretora Arlinda"
                },
                {
                    "ordem": 7,
                    "nome": "Ivonete Ferreira da Silva",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "ordem": 8,
                    "nome": "Joana Angélica dos Santos Silva",
                    "ch": "40",
                    "observacoes": "APLB Sindicato"
                },
                {
                    "ordem": 9,
                    "nome": "Josefa Raimunda Santos da Silva",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "ordem": 10,
                    "nome": "Luzinete de J. O. Miranda",
                    "ch": "20",
                    "observacoes": "Remoção Provisória"
                },
                {
                    "ordem": 11,
                    "nome": "Maria Arlinda Pereira Bonfim",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "ordem": 12,
                    "nome": "Maria Conceição dos Santos Ribeiro Reis",
                    "ch": "20",
                    "observacoes": "CEMAEE"
                },
                {
                    "ordem": 13,
                    "nome": "Marcia Silene Silva Menezes Almeida",
                    "ch": "20",
                    "observacoes": "Diretora Menandro"
                },
                {
                    "ordem": 14,
                    "nome": "Neide Santiago da Hora",
                    "ch": "20",
                    "observacoes": ""
                },
                {
                    "ordem": 15,
                    "nome": "Regina Celi Santos de Souza",
                    "ch": "20",
                    "observacoes": "Monteiro"
                },
                {
                    "ordem": 16,
                    "nome": "Regina Célia Almeida Santos",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "ordem": 17,
                    "nome": "Rosilene Almeida",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "ordem": 18,
                    "nome": "Romilda dos Santos Costa",
                    "ch": "20",
                    "observacoes": "Remoção Provisória"
                },
                {
                    "ordem": 19,
                    "nome": "Veronica Marques dos Santos Rebouças",
                    "ch": "20",
                    "observacoes": "Remoção Provisória"
                }
            ],
            "professor_desdobrado": [
                {
                    "ordem": 1,
                    "nome": "Neide Santiago da Hora",
                    "ch": "20",
                    "observacoes": ""
                },
                {
                    "ordem": 2,
                    "nome": "Veronica Marques dos Santos Rebouças",
                    "ch": "20",
                    "observacoes": ""
                }
            ],
            "vigilantes": [
                {
                    "ordem": 1,
                    "nome": "Alan Galvão dos Santos",
                    "ch": "44",
                    "observacoes": "Noturno"
                },
                {
                    "ordem": 2,
                    "nome": "Edvaldo Trindade Santana",
                    "ch": "44",
                    "observacoes": "Noturno"
                }
            ],
            "portaria": [
                {
                    "ordem": 1,
                    "nome": "Goreth Santos dos Anjos",
                    "ch": "30",
                    "observacoes": "Readaptada/Diurno"
                },
                {
                    "ordem": 2,
                    "nome": "Pascoal Sousa",
                    "ch": "30",
                    "observacoes": "Portaria/Diurno"
                }
            ],
            "atendentes_de_classe": [
                {
                    "ordem": 1,
                    "nome": "Flávia da Cruz Ribeiro",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "ordem": 2,
                    "nome": "Normali Sousa Silva Cerqueira",
                    "ch": "40",
                    "observacoes": ""
                }
            ],
            "secretario_escolar": [
                {
                    "ordem": 1,
                    "nome": "Eduardo Gonçalves de Arruda",
                    "ch": "40",
                    "observacoes": ""
                }
            ],
            "auxiliares_servicos_escolares": [
                {
                    "ordem": 1,
                    "nome": "Alessio Silva Santos",
                    "ch": "30",
                    "observacoes": ""
                },
                {
                    "ordem": 2,
                    "nome": "Arilza Pereira dos Santos de Jesus",
                    "ch": "30",
                    "observacoes": "INSS"
                },
                {
                    "ordem": 3,
                    "nome": "Dionísio Silva Piropo",
                    "ch": "30",
                    "observacoes": "Cedido a Saúde"
                },
                {
                    "ordem": 4,
                    "nome": "Marineide Santos C. Marques",
                    "ch": "30",
                    "observacoes": ""
                },
                {
                    "ordem": 5,
                    "nome": "Silvia Silva Santana",
                    "ch": "30",
                    "observacoes": "INSS"
                }
            ],
            "funcionaria_cedida": [
                {
                    "nome": "Dilma Teixeira Santos",
                    "observacoes": "Itaquara"
                }
            ],
            "cozinheira_efetiva": [
                {
                    "nome": "Luzimere Souza Galvão",
                    "observacoes": "Saúde"
                }
            ]
        },
        "servidores_contratados": {
            "atendentes_de_classe": [
                {
                    "ordem": 1,
                    "nome": "Laridsa Santos De Quadros",
                    "ch": "40",
                    "observacoes": ""
                }
            ],
            "auxiliares_alimentacao_escolar": [
                {
                    "ordem": 1,
                    "nome": "Luciana Dos Santos Conceição",
                    "ch": "40",
                    "observacoes": ""
                }
            ],
            "coordenador_pedagogico": [
                {
                    "ordem": 1,
                    "nome": "Eline Santana Ramos",
                    "ch": "40",
                    "observacoes": ""
                }
            ],
            "merendeira": [
                {
                    "ordem": 1,
                    "nome": "Maria Francisca Dos Santos Teixeira",
                    "ch": "40",
                    "observacoes": ""
                }
            ],
            "professores_regentes": [
                {
                    "ordem": 1,
                    "nome": "Adilene Costa Almeida Santos",
                    "ch": "20",
                    "observacoes": ""
                },
                {
                    "ordem": 2,
                    "nome": "Luciana Dos Santos Silva Bispo",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "ordem": 3,
                    "nome": "Maria dos Santos Menezes",
                    "ch": "20",
                    "observacoes": ""
                },
                {
                    "ordem": 4,
                    "nome": "Miralda Bastos Santos",
                    "ch": "20",
                    "observacoes": ""
                }
            ],
            "profissionais_apoio_deficiencia": [
                {
                    "ordem": 1,
                    "nome": "Aiala Dos Santos Souza",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "ordem": 2,
                    "nome": "Euselia Mira Lopes",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "ordem": 3,
                    "nome": "Keliane Victoria dos Santos Oliveira",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "ordem": 4,
                    "nome": "Mateus de Souza Santos",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "ordem": 5,
                    "nome": "Saulo Oliveira",
                    "ch": "41",
                    "observacoes": ""
                }
            ],
            "auxiliares_infraestrutura_escolar": [
                {
                    "ordem": 1,
                    "nome": "Antonieta Almeida da Silva",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "ordem": 2,
                    "nome": "Francirleide Moreira de Santana",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "ordem": 3,
                    "nome": "Isabel Cristina Pereira Pellegrini",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "ordem": 4,
                    "nome": "Joselina Pereira",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "ordem": 5,
                    "nome": "Kaio Silva Santos",
                    "ch": "40",
                    "observacoes": ""
                }
            ]
        }
    },
    {
        "instituicao": "Escola Centro Educacional do Trabalhador",
        "equipe_gestora": {
            "diretora": "Mírian Santiago da Hora",
            "vice_diretoras": [
                "Joalce Jesus dos Santos Albino",
                "Joseli Cerqueira Freitas"
            ],
            "coordenador": "Wagner Rocha Galvão",
            "secretario_escolar": "Gilberto Oliveira Santos",
            "auxiliar_administrativo_ii": "Benilde Dias Silva"
        },
        "servidores_efetivos": {
            "docentes": [
                {
                    "ordem": 1,
                    "nome": "Ana Luiza Vieira dos Santos",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "ordem": 2,
                    "nome": "Andréia Dias da Silva",
                    "ch": "40",
                    "observacoes": "CME"
                },
                {
                    "ordem": 3,
                    "nome": "Cecília Oliveira Menezes Andrade",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "ordem": 4,
                    "nome": "Claudia Moreira Costa",
                    "ch": "20",
                    "observacoes": ""
                },
                {
                    "ordem": 5,
                    "nome": "Cleidineia Carvalho Santos",
                    "ch": "40",
                    "observacoes": "Doutorado"
                },
                {
                    "ordem": 6,
                    "nome": "Eva Katia da Silva Santos",
                    "ch": "20/20",
                    "observacoes": "Remoção Provisória"
                },
                {
                    "ordem": 7,
                    "nome": "Gerlan Oliveira Santos",
                    "ch": "20",
                    "observacoes": "Remoção Provisória"
                },
                {
                    "ordem": 8,
                    "nome": "Iramaia Araújo Santos",
                    "ch": "40",
                    "observacoes": "SMED"
                },
                {
                    "ordem": 9,
                    "nome": "Jaciara Tâmara Araújo",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "ordem": 10,
                    "nome": "Joalce Jesus dos Santos Albino",
                    "ch": "20",
                    "observacoes": "Vice-Diretora"
                },
                {
                    "ordem": 11,
                    "nome": "Joseli Cerqueira Freitas",
                    "ch": "20",
                    "observacoes": "Vice-Diretora"
                },
                {
                    "ordem": 12,
                    "nome": "Josenilda Moreira de Araújo",
                    "ch": "20",
                    "observacoes": ""
                },
                {
                    "ordem": 13,
                    "nome": "Katiane Castro dos Santos",
                    "ch": "20/20",
                    "observacoes": "Remoção Provisória"
                },
                {
                    "ordem": 14,
                    "nome": "Luiz Carlos Oliveira Santos",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "ordem": 15,
                    "nome": "Magnovalda Rocha Santos Sena",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "ordem": 16,
                    "nome": "Maria da Solidade Martins Sousa",
                    "ch": "20",
                    "observacoes": ""
                },
                {
                    "ordem": 17,
                    "nome": "Mariney Ramos de Sousa Sena",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "ordem": 18,
                    "nome": "Mirian Santiago da Hora",
                    "ch": "20",
                    "observacoes": "Diretora"
                },
                {
                    "ordem": 19,
                    "nome": "Patrícia Lara de Oliveira",
                    "ch": "20",
                    "observacoes": ""
                },
                {
                    "ordem": 20,
                    "nome": "Paulo Gentil dos Santos",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "ordem": 21,
                    "nome": "Rosenilda Silva Santos",
                    "ch": "40",
                    "observacoes": "Menandro"
                },
                {
                    "ordem": 22,
                    "nome": "Rosivany dos Santos",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "ordem": 23,
                    "nome": "Sueli Maria Bomfim de Andrade",
                    "ch": "40",
                    "observacoes": "Readaptada"
                },
                {
                    "ordem": 24,
                    "nome": "Tereza Cristina Sousa Silva",
                    "ch": "40",
                    "observacoes": ""
                }
            ],
            "professores_desdobrados": [
                {
                    "ordem": 1,
                    "nome": "Joalce Jesus dos Santos Albino",
                    "ch": "20",
                    "observacoes": ""
                }
            ],
            "professor_permutado": [
                {
                    "ordem": 1,
                    "nome": "Mª Dolores Novaes de Jesus",
                    "ch": "20",
                    "observacoes": ""
                }
            ],
            "secretario_escolar": [
                {
                    "ordem": 1,
                    "nome": "Gilberto Oliveira Santos",
                    "ch": "40",
                    "observacoes": ""
                }
            ],
            "auxiliar_administrativo_ii": [
                {
                    "ordem": 1,
                    "nome": "Benilde Dias Silva",
                    "ch": "40",
                    "observacoes": ""
                }
            ],
            "vigilantes": [
                {
                    "ordem": 1,
                    "nome": "Gilmar Vieira Fonseca",
                    "ch": "40",
                    "observacoes": ""
                },
                {
                    "ordem": 2,
                    "nome": "Roberto Ribeiro da Cruz",
                    "ch": "40",
                    "observacoes": ""
                }
            ],
            "atendente_de_classe": [
                {
                    "ordem": 1,
                    "nome": "Joselita Jesus dos S. Lisboa",
                    "ch": "40",
                    "observacoes": ""
                }
            ],
            "auxiliares_servicos_escolares": [
                {
                    "ordem": 1,
                    "nome": "Carmen Célia A. dos Stos",
                    "ch": "30",
                    "observacoes": ""
                },
                {
                    "ordem": 4,
                    "nome": "Nilzete Oliveira",
                    "ch": "30",
                    "observacoes": "INSS"
                },
                {
                    "ordem": 5,
                    "nome": "Noely Oliveira Souza",
                    "ch": "30",
                    "observacoes": ""
                }
            ]
        },
        "servidores_contratados": {
            "profissionais_apoio_deficiencia": [
                {
                    "ordem": 1,
                    "nome": "Ianara Eleuterio dos Santos",
                    "ch": "40h",
                    "observacoes": ""
                },
                {
                    "ordem": 2,
                    "nome": "Maibson de Jesus Santos",
                    "ch": "40h",
                    "observacoes": ""
                },
                {
                    "ordem": 3,
                    "nome": "Raquel Santos da Silva",
                    "ch": "40h",
                    "observacoes": ""
                },
                {
                    "ordem": 4,
                    "nome": "Sonia Silva Ribeiro",
                    "ch": "40h",
                    "observacoes": ""
                }
            ],
            "auxiliares_infraestrutura_escolar": [
                {
                    "ordem": 1,
                    "nome": "Angeli Maria Dias da Silva",
                    "ch": "40h",
                    "observacoes": ""
                },
                {
                    "ordem": 2,
                    "nome": "Daiane Lopes Mendes",
                    "ch": "40h",
                    "observacoes": ""
                },
                {
                    "ordem": 3,
                    "nome": "Edileide de Jesus Nascimento",
                    "ch": "40h",
                    "observacoes": ""
                },
                {
                    "ordem": 4,
                    "nome": "Everson Ferreira Couto",
                    "ch": "40h",
                    "observacoes": ""
                },
                {
                    "ordem": 5,
                    "nome": "Irani dos Santos Barbosa",
                    "ch": "40h",
                    "observacoes": ""
                },
                {
                    "ordem": 6,
                    "nome": "Ivaneide dos Santos Maciel",
                    "ch": "40h",
                    "observacoes": ""
                },
                {
                    "ordem": 7,
                    "nome": "Silmara Cruz de Almeida",
                    "ch": "40h",
                    "observacoes": ""
                }
            ],
            "coordenador_pedagogico": [
                {
                    "ordem": 1,
                    "nome": "Wagner Rocha Galvão",
                    "ch": "40h",
                    "observacoes": ""
                }
            ],
            "professores": [
                {
                    "ordem": 1,
                    "nome": "Bianca Reis Ramos",
                    "ch": "20h",
                    "observacoes": ""
                },
                {
                    "ordem": 2,
                    "nome": "Darley da Silva Andrade",
                    "ch": "20h",
                    "observacoes": ""
                },
                {
                    "ordem": 3,
                    "nome": "Joelma Sandra da Silveira Rios",
                    "ch": "20h",
                    "observacoes": ""
                },
                {
                    "ordem": 4,
                    "nome": "Michele Silva Santos",
                    "ch": "20h",
                    "observacoes": ""
                },
                {
                    "ordem": 5,
                    "nome": "Neidiane Machado de Almeida",
                    "ch": "20h",
                    "observacoes": ""
                },
                {
                    "ordem": 6,
                    "nome": "Railan Brito de Almeida",
                    "ch": "20h",
                    "observacoes": ""
                },
                {
                    "ordem": 7,
                    "nome": "Vladimir de Mendonça Brazil",
                    "ch": "20h",
                    "observacoes": ""
                }
            ],
            "vigilantes_escolares": [
                {
                    "ordem": 1,
                    "nome": "Agenor Luiz da Silva Neto",
                    "ch": "40h",
                    "observacoes": ""
                },
                {
                    "ordem": 2,
                    "nome": "Joilson dos Santos Lopes Ribeiro",
                    "ch": "20h",
                    "observacoes": ""
                },
                {
                    "ordem": 3,
                    "nome": "Josimaldo Santos de Souza",
                    "ch": "20h",
                    "observacoes": ""
                }
            ]
        }
    },
    {
        "escola": "Escola Mundo Infantil - C.S.U/Creche",
        "equipe_gestora": {
            "diretor": "Elyane de Souza Colchesque",
            "vice_diretor": "Flávia Andrade Aragão",
            "secretaria_escolar": "Laysa Gabriele Mendes Martins",
            "coordenadora": "Claudia Moreira Costa"
        },
        "servidores_efetivos": {
            "docentes": [
                {
                    "nome": "Daiane Marques de Oliveira Ferreira",
                    "CH": 20
                },
                {
                    "nome": "Eliana dos Santos Nascimento Brandão",
                    "CH": 40
                },
                {
                    "nome": "Elisabete Cortes Piropo",
                    "CH": 20
                },
                {
                    "nome": "Elisângela Almeida dos Santos",
                    "CH": 20
                },
                {
                    "nome": "Elizabeth Santos Silva",
                    "CH": 20
                },
                {
                    "nome": "Elyane de Souza Colchesque",
                    "CH": 20,
                    "observacao": "Diretora"
                },
                {
                    "nome": "Flávia Andrade Aragão",
                    "CH": 20,
                    "observacao": "Vice-diretora"
                },
                {
                    "nome": "Iara Carneiro Lula",
                    "CH": 20,
                    "observacao": "Readaptada"
                },
                {
                    "nome": "Juciane Moraes dos Santos",
                    "CH": 20,
                    "observacao": "Remoção provisória"
                },
                {
                    "nome": "Raimunda Macedo Bomfim Costa",
                    "CH": 40
                },
                {
                    "nome": "Viviane Silva Sousa",
                    "CH": 40,
                    "observacao": "Remoção provisória"
                }
            ],
            "professor_desdobrado": {
                "nome": "Juciane Moraes dos Santos",
                "CH": 20
            },
            "coordenadora_pedagogica": {
                "nome": "Claudia Moreira Costa",
                "CH": 20
            },
            "vigilantes": [
                {
                    "nome": "Vandivaldo de Jesus Trindade",
                    "CH": 40,
                    "turno": "Diurno"
                }
            ],
            "atendente_classe": [
                {
                    "nome": "Jamily Mota Teixeira",
                    "CH": 40,
                    "observacao": "Está no Luzia"
                },
                {
                    "nome": "Ezenilda Santos dos Anjos",
                    "CH": 40
                },
                {
                    "nome": "Leila Cristina Silva de Abreu",
                    "CH": 40,
                    "observacao": "Cedida à cultura"
                },
                {
                    "nome": "Liliane Barbosa Cardozo",
                    "CH": 40,
                    "observacao": "Está na Stela"
                }
            ],
            "aux_servico_escolar": [
                {
                    "nome": "Edna Maria Oliveira de Souza",
                    "CH": 30
                },
                {
                    "nome": "Eli Silva Carvalho",
                    "CH": 40,
                    "observacao": "Vigilante Noturno"
                }
            ]
        }
    },
    {
        "escola": "Delminda Farias de Almeida",
        "equipe_gestora": {
            "diretor": "Rosana da Silva Ramos",
            "vice_diretor": "Vanderli Ribeiro S de Oliveira",
            "coordenador": "Sandra Martins de Souza",
            "secretario_escolar": "Aline Sousa Santos"
        },
        "servidores_efetivos": [
            {
                "ordem": 1,
                "docente": "Elissandra Sousa Gomes",
                "ch": "20h",
                "observacoes": ""
            },
            {
                "ordem": 2,
                "docente": "Heraine Almeida Mendonça",
                "ch": "20h",
                "observacoes": "Está na Emanoel"
            },
            {
                "ordem": 3,
                "docente": "Ithana Dayse Alves Santos",
                "ch": "20h",
                "observacoes": "Está na Menenadro"
            },
            {
                "ordem": 4,
                "docente": "Jacilene Silva Cunha",
                "ch": "20h",
                "observacoes": ""
            },
            {
                "ordem": 5,
                "docente": "Katiane Castro dos Santos",
                "ch": "20h",
                "observacoes": "Está no CET"
            },
            {
                "ordem": 6,
                "docente": "Leidiane Rocha Andrade",
                "ch": "20h",
                "observacoes": ""
            },
            {
                "ordem": 7,
                "docente": "Rosana da Silva Ramos",
                "ch": "20h",
                "observacoes": "Diretora"
            },
            {
                "ordem": 8,
                "docente": "Sandra Martins de Souza",
                "ch": "20h",
                "observacoes": "Coordenação"
            },
            {
                "ordem": 9,
                "docente": "Tamirys Maciel Vital de Pinho",
                "ch": "20h",
                "observacoes": ""
            },
            {
                "ordem": 10,
                "docente": "Vanderli Ribeiro de Oliveira",
                "ch": "20h",
                "observacoes": "Vice-Diretora"
            },
            {
                "ordem": 11,
                "docente": "Vaneia Costa Silva",
                "ch": "20/20h",
                "observacoes": ""
            }
        ],
        "professores_desdobrados": [
            {
                "docente": "Leidiane Rocha Andrade",
                "ch": "20h"
            },
            {
                "docente": "Tamirys Maciel Vital de Pinho",
                "ch": "20h"
            }
        ],
        "porteiro": [
            {
                "nome": "Valdemir Oliveira Cerqueira",
                "ch": "30h",
                "observacoes": "Lic. sem vencimento"
            }
        ],
        "atendente_de_classe": [
            {
                "nome": "Dinorah Marques Ribeiro",
                "ch": "40h",
                "observacoes": "Readaptada"
            }
        ],
        "aux_servico_escolar": [
            {
                "nome": "Consuelo Amorim de França Mendes",
                "ch": "30h",
                "observacoes": ""
            },
            {
                "nome": "Rosangela dos Santos",
                "ch": "30h",
                "observacoes": "APLB"
            }
        ],
        "servidores_cedidos_pela_infraestrutura": [
            {
                "nome": "José Santana dos Anjos",
                "ch": "40h",
                "observacoes": "Vigilante"
            }
        ],
        "servidores_contratados": [
            {
                "n": 1,
                "servidor": "Carina Silva dos Santos",
                "ch": 40,
                "funcao": "Atendente de Classe",
                "observacao": ""
            },
            {
                "n": 2,
                "servidor": "Josiane De Jesus Brandao",
                "ch": 40,
                "funcao": "Atendente de Classe",
                "observacao": ""
            },
            {
                "n": 3,
                "servidor": "Nubia Nascimento Guirre",
                "ch": 40,
                "funcao": "Atendente de Classe",
                "observacao": ""
            },
            {
                "n": 4,
                "servidor": "Ruan Amorim Teixeira",
                "ch": 40,
                "funcao": "Atendente de Classe",
                "observacao": ""
            },
            {
                "n": 5,
                "servidor": "Amora Patricia de Jesus Silva",
                "ch": 40,
                "funcao": "Auxiliar de Infraestrutura Escolar",
                "observacao": ""
            },
            {
                "n": 6,
                "servidor": "Ana Paula Bispo Almeida",
                "ch": 40,
                "funcao": "Auxiliar de Infraestrutura Escolar",
                "observacao": ""
            },
            {
                "n": 7,
                "servidor": "Eliana Santos de Oliveira",
                "ch": 40,
                "funcao": "Auxiliar de Infraestrutura Escolar",
                "observacao": ""
            },
            {
                "n": 8,
                "servidor": "Eliane Barbosa Santos",
                "ch": 40,
                "funcao": "Auxiliar de Infraestrutura Escolar",
                "observacao": ""
            },
            {
                "n": 9,
                "servidor": "Elinalva dos Santos Ramos",
                "ch": 40,
                "funcao": "Auxiliar de Infraestrutura Escolar",
                "observacao": ""
            },
            {
                "n": 10,
                "servidor": "Lucivania Felix dos Santos",
                "ch": 40,
                "funcao": "Auxiliar de Infraestrutura Escolar",
                "observacao": ""
            },
            {
                "n": 11,
                "servidor": "Marilia Santos Pitanga",
                "ch": 40,
                "funcao": "Auxiliar de Infraestrutura Escolar",
                "observacao": ""
            },
            {
                "n": 12,
                "servidor": "Nilzelia Sousa Silva",
                "ch": 40,
                "funcao": "Auxiliar de Infraestrutura Escolar",
                "observacao": ""
            },
            {
                "n": 13,
                "servidor": "Roseli da Silva Ramos",
                "ch": 40,
                "funcao": "Auxiliar de Infraestrutura Escolar",
                "observacao": ""
            },
            {
                "n": 14,
                "servidor": "Annaly dos Santos Almeida",
                "ch": 20,
                "funcao": "Professor",
                "observacao": ""
            },
            {
                "n": 15,
                "servidor": "Dailane de Jesus dos Santos",
                "ch": 20,
                "funcao": "Professor",
                "observacao": ""
            },
            {
                "n": 16,
                "servidor": "Daniel Oliveira dos Santos",
                "ch": 20,
                "funcao": "Professor",
                "observacao": ""
            },
            {
                "n": 17,
                "servidor": "Daniela Novaes Oliveira Gomes",
                "ch": 20,
                "funcao": "Professor",
                "observacao": ""
            },
            {
                "n": 18,
                "servidor": "Elisabete Pereira da Silva",
                "ch": 20,
                "funcao": "Professor",
                "observacao": ""
            },
            {
                "n": 19,
                "servidor": "Erlania Vieira dos Santos",
                "ch": 20,
                "funcao": "Professor",
                "observacao": ""
            },
            {
                "n": 20,
                "servidor": "Jamile Santana do Carmo",
                "ch": 20,
                "funcao": "Professor",
                "observacao": ""
            },
            {
                "n": 21,
                "servidor": "Joselia de Matos Marques",
                "ch": 20,
                "funcao": "Professor",
                "observacao": ""
            },
            {
                "n": 22,
                "servidor": "Jucenelia Oliveira Franca",
                "ch": 20,
                "funcao": "Professor",
                "observacao": ""
            },
            {
                "n": 23,
                "servidor": "Priscilla Vieira Santedicola",
                "ch": 20,
                "funcao": "Professor",
                "observacao": ""
            },
            {
                "n": 24,
                "servidor": "Thaise de Jesus Ferreira",
                "ch": 20,
                "funcao": "Professor",
                "observacao": ""
            },
            {
                "n": 25,
                "servidor": "Aline Sousa Sena",
                "ch": 40,
                "funcao": "Secretário Escolar",
                "observacao": ""
            },
            {
                "n": 26,
                "servidor": "Alex Sandro dos Santos Cerqueira",
                "ch": 40,
                "funcao": "Vigilante Escolar",
                "observacao": ""
            },
            {
                "n": 27,
                "servidor": "Elvis Carneiro de Araujo",
                "ch": 40,
                "funcao": "Vigilante Escolar",
                "observacao": ""
            },
            {
                "n": 28,
                "servidor": "Esdras Santos Silva",
                "ch": 40,
                "funcao": "Vigilante Escolar",
                "observacao": ""
            }
        ]
    },
    {
        "escola": "Diana Jussiênne",
        "equipe_gestora": {
            "diretor": "Ronaldo Silva Trindade",
            "vice_diretor": [
                "Elania Barreto da Silva",
                "Joelma dos Santos Silva"
            ],
            "coordenador_pedagogico": [
                "Cosmildo S. Rocha",
                "Rhaone da Hora Santos"
            ],
            "secretario": "Kaike Pereira de Araujo",
            "assistente_administrativo": "Jozimara Barbosa da Silva"
        },
        "servidores_efetivos": [
            {
                "ordem": 1,
                "docente": "Agnoita Sousa Caldas Nunes",
                "ch": "40h",
                "observacoes": ""
            },
            {
                "ordem": 2,
                "docente": "Celina Moreira de Souza",
                "ch": "20h",
                "observacoes": ""
            },
            {
                "ordem": 3,
                "docente": "Claudinéia Gomes de Andrade Lima",
                "ch": "20h/20h",
                "observacoes": ""
            },
            {
                "ordem": 4,
                "docente": "Ednaldo da Cruz Santana",
                "ch": "20h",
                "observacoes": "Licença sem vencimentos"
            },
            {
                "ordem": 5,
                "docente": "Elania Barreto da Silva",
                "ch": "",
                "observacoes": "Vice-Diretor"
            },
            {
                "ordem": 6,
                "docente": "Eliana Suares da Silva",
                "ch": "20h",
                "observacoes": ""
            },
            {
                "ordem": 7,
                "docente": "Eva Kátia da Silva Santos",
                "ch": "40h",
                "observacoes": "Está no CET"
            },
            {
                "ordem": 8,
                "docente": "Fernando de Almeida Silva",
                "ch": "40h",
                "observacoes": ""
            },
            {
                "ordem": 9,
                "docente": "Inês Almeida Silva Oliveira",
                "ch": "20h",
                "observacoes": ""
            },
            {
                "ordem": 10,
                "docente": "Jeane Sousa Santos",
                "ch": "20h",
                "observacoes": ""
            },
            {
                "ordem": 11,
                "docente": "Joelma dos Santos Silva",
                "ch": "",
                "observacoes": "Vice-Diretor"
            },
            {
                "ordem": 12,
                "docente": "Maria Darismar Duarte Henes Cortes",
                "ch": "40h",
                "observacoes": ""
            },
            {
                "ordem": 13,
                "docente": "Maria Gorete Oliveira dos Santos",
                "ch": "40h",
                "observacoes": ""
            },
            {
                "ordem": 14,
                "docente": "Maria Rute Ribeiro Almeida da Hora",
                "ch": "40h",
                "observacoes": ""
            },
            {
                "ordem": 15,
                "docente": "Marlene Martinelli Marinho",
                "ch": "20h",
                "observacoes": ""
            },
            {
                "ordem": 16,
                "docente": "Marly Gonçalves da Silva",
                "ch": "20h",
                "observacoes": "Doutorado"
            },
            {
                "ordem": 17,
                "docente": "Rita de Cássia Silva Moreira",
                "ch": "40h",
                "observacoes": "Readaptação Funcional"
            },
            {
                "ordem": 18,
                "docente": "Ronaldo Silva Trindade",
                "ch": "",
                "observacoes": "Diretor"
            },
            {
                "ordem": 19,
                "docente": "Rose Claudia Oliveira de Andrade",
                "ch": "40h",
                "observacoes": ""
            },
            {
                "ordem": 20,
                "docente": "Valdivan de Araújo Santos",
                "ch": "40h",
                "observacoes": ""
            },
            {
                "ordem": 21,
                "docente": "Vânia Alves de Oliveira",
                "ch": "20h",
                "observacoes": ""
            },
            {
                "ordem": 22,
                "docente": "Vécio Luiz Leite Lima",
                "ch": "20h",
                "observacoes": "Remoção provisória"
            },
            {
                "ordem": 23,
                "docente": "Wagston Felix Pereira",
                "ch": "40h",
                "observacoes": ""
            }
        ],
        "professores_desdobrados": [
            {
                "docente": "Elania Barreto da Silva",
                "ch": "20h"
            },
            {
                "docente": "Joelma dos Santos Silva",
                "ch": "20h"
            }
        ],
        "coordenador_pedagogico": [
            {
                "docente": "Cosmildo S. Rocha",
                "ch": "20h"
            }
        ],
        "assistente_administrativo": [
            {
                "nome": "Jozimara Barbosa da Silva",
                "ch": "40h"
            }
        ],
        "aux_servico_escolar": [
            {
                "nome": "Débora Teixeira Amorim",
                "ch": "30h",
                "observacoes": "Cedida à saúde"
            },
            {
                "nome": "Marileide Santos Cerqueira",
                "ch": "30h",
                "observacoes": ""
            },
            {
                "nome": "Valdinelia Lemos da Anunciação",
                "ch": "30h",
                "observacoes": ""
            },
            {
                "nome": "José Eric Souza Santos",
                "ch": "30h",
                "observacoes": ""
            },
            {
                "nome": "Keila Ricardo dos Santos Silva",
                "ch": "30h",
                "observacoes": ""
            }
        ],
        "servidores_contratados": [
            {
                "n": 1,
                "servidor": "Eliene Andrade de Souza",
                "ch": 40,
                "funcao": "Profissional de Apoio à alunos com deficiência",
                "observacao": ""
            },
            {
                "n": 2,
                "servidor": "Marines Correia dos Santos",
                "ch": 40,
                "funcao": "Profissional de Apoio à alunos com deficiência",
                "observacao": ""
            },
            {
                "n": 3,
                "servidor": "Railda Rosa Cardoso",
                "ch": 40,
                "funcao": "Profissional de Apoio à alunos com deficiência",
                "observacao": ""
            },
            {
                "n": 4,
                "servidor": "Tamiles Souza da Silva",
                "ch": 40,
                "funcao": "Profissional de Apoio à alunos com deficiência",
                "observacao": ""
            },
            {
                "n": 5,
                "servidor": "Edna Lemos Ribeiro",
                "ch": 40,
                "funcao": "Auxiliar de Infraestrutura Escolar",
                "observacao": ""
            },
            {
                "n": 6,
                "servidor": "Gleidiane de Oliveira Santos",
                "ch": 40,
                "funcao": "Auxiliar de Infraestrutura Escolar",
                "observacao": ""
            },
            {
                "n": 7,
                "servidor": "Lucas Barreto Silva",
                "ch": 40,
                "funcao": "Auxiliar de Infraestrutura Escolar",
                "observacao": ""
            },
            {
                "n": 8,
                "servidor": "Marcia Maria Braz de Freitas",
                "ch": 40,
                "funcao": "Auxiliar de Infraestrutura Escolar",
                "observacao": ""
            },
            {
                "n": 9,
                "servidor": "Natiele Nunes Pereira dos Santos",
                "ch": 40,
                "funcao": "Auxiliar de Infraestrutura Escolar",
                "observacao": ""
            },
            {
                "n": 10,
                "servidor": "Noelma Sampaio de Jesus",
                "ch": 40,
                "funcao": "Auxiliar de Infraestrutura Escolar",
                "observacao": ""
            },
            {
                "n": 11,
                "servidor": "Simone Araújo dos Santos",
                "ch": 40,
                "funcao": "Auxiliar de Infraestrutura Escolar",
                "observacao": ""
            },
            {
                "n": 12,
                "servidor": "Sinara Silva Santos",
                "ch": 40,
                "funcao": "Auxiliar de Infraestrutura Escolar",
                "observacao": ""
            },
            {
                "n": 13,
                "servidor": "Taciane Brito Santana",
                "ch": 40,
                "funcao": "Auxiliar de Infraestrutura Escolar",
                "observacao": ""
            },
            {
                "n": 14,
                "servidor": "Rhaone da Hora Santos",
                "ch": "",
                "funcao": "Coordenador Pedagógico",
                "observacao": ""
            },
            {
                "n": 15,
                "servidor": "Camila Souza Mascarenhas",
                "ch": 20,
                "funcao": "Professor",
                "observacao": ""
            },
            {
                "n": 16,
                "servidor": "Denilson Silva da Hora",
                "ch": 20,
                "funcao": "Professor",
                "observacao": ""
            },
            {
                "n": 17,
                "servidor": "Jadiara Araujo de Oliveira Gomes",
                "ch": 20,
                "funcao": "Professor",
                "observacao": ""
            },
            {
                "n": 18,
                "servidor": "Lucas Souza Santos",
                "ch": 40,
                "funcao": "Professor",
                "observacao": ""
            },
            {
                "n": 19,
                "servidor": "Thais Melo Santos",
                "ch": 20,
                "funcao": "Professor",
                "observacao": ""
            },
            {
                "n": 20,
                "servidor": "William Moreira dos Santos Vilas Boas",
                "ch": 20,
                "funcao": "Professor",
                "observacao": ""
            },
            {
                "n": 21,
                "servidor": "Kaike Pereira de Araujo",
                "ch": 40,
                "funcao": "Secretário Escolar",
                "observacao": ""
            },
            {
                "n": 22,
                "servidor": "Fernando Campos Meneses",
                "ch": 40,
                "funcao": "Vigilante Escolar",
                "observacao": ""
            },
            {
                "n": 23,
                "servidor": "Marcio Antonio dos Santos Souza",
                "ch": 40,
                "funcao": "Vigilante Escolar",
                "observacao": ""
            },
            {
                "n": 24,
                "servidor": "Marlon Lisboa Fontes",
                "ch": 40,
                "funcao": "Vigilante Escolar",
                "observacao": ""
            },
            {
                "n": 25,
                "servidor": "Rafael Moraes da Silva",
                "ch": 40,
                "funcao": "Vigilante Escolar",
                "observacao": ""
            },
            {
                "n": 26,
                "servidor": "Sergio Santana Couto",
                "ch": 40,
                "funcao": "Vigilante Escolar",
                "observacao": ""
            }
        ]
    },
    {
        "escola": "Emanoel de Oliveira Brito",
        "equipe_gestora": {
            "diretor": "Sara Barreto Lima",
            "vice_diretor": [
                "Mª de Lurdes Soares Souza",
                "Marucia Cristina da Silva"
            ],
            "coordenadora_pedagogica": "Nadja Santana da Hora Santos",
            "secretaria": "Amora Monteiro de Lemos",
            "assistente_administrativo": "Pedro Henrique Lopes Gondim"
        },
        "servidores_efetivos": [
            {
                "ordem": 1,
                "docente": "Ângela Gomes dos Santos",
                "ch": "20h",
                "observacoes": ""
            },
            {
                "ordem": 2,
                "docente": "Deizon Coelho da Silva",
                "ch": "20h",
                "observacoes": ""
            },
            {
                "ordem": 3,
                "docente": "Elisangela de Sousa Costa",
                "ch": "40h",
                "observacoes": "Readaptada - CET"
            },
            {
                "ordem": 4,
                "docente": "Euflosina Izidio dos Santos",
                "ch": "20h",
                "observacoes": "INSS"
            },
            {
                "ordem": 5,
                "docente": "Fernanda dos Santos Mussi",
                "ch": "20h",
                "observacoes": "SMED"
            },
            {
                "ordem": 6,
                "docente": "Heraine Almeida Mendonça",
                "ch": "20h",
                "observacoes": "Remoção Provisória"
            },
            {
                "ordem": 7,
                "docente": "Jaciara Silva Santos Lima",
                "ch": "20h",
                "observacoes": "Remoção Provisória"
            },
            {
                "ordem": 8,
                "docente": "Joanadarc Menezes Trindade",
                "ch": "20/20h",
                "observacoes": "Remoção Provisória /SMED"
            },
            {
                "ordem": 9,
                "docente": "Jurema Bomfim de Quadros",
                "ch": "40h",
                "observacoes": "Escola Carneiro Ribeiro"
            },
            {
                "ordem": 10,
                "docente": "Luciana Teixeira Matos",
                "ch": "20h",
                "observacoes": "CEMAEE Alegria de Viver"
            },
            {
                "ordem": 11,
                "docente": "Malena Gonçalves dos Santos",
                "ch": "20h",
                "observacoes": "Remoção Provisória"
            },
            {
                "ordem": 12,
                "docente": "Maria da Paz Santos Brito Nogueira",
                "ch": "40h",
                "observacoes": ""
            },
            {
                "ordem": 13,
                "docente": "Marucia Cristina da Silva",
                "ch": "20/20h",
                "observacoes": ""
            },
            {
                "ordem": 14,
                "docente": "Ronalva de Fátima M. Amaral",
                "ch": "40h",
                "observacoes": ""
            },
            {
                "ordem": 15,
                "docente": "Sara de Oliveira Neves",
                "ch": "40h",
                "observacoes": ""
            },
            {
                "ordem": 16,
                "docente": "Simone Barreto Lima",
                "ch": "20/20h",
                "observacoes": "SMED"
            },
            {
                "ordem": 17,
                "docente": "Thayse Santos Dattoli",
                "ch": "40h",
                "observacoes": "Readaptada"
            },
            {
                "ordem": 18,
                "docente": "Viviane Silva Souza",
                "ch": "40h",
                "observacoes": "CSU"
            },
            {
                "ordem": 19,
                "docente": "Wilma Martins Araújo",
                "ch": "20/20h",
                "observacoes": "APLB Sindicato"
            },
            {
                "ordem": 20,
                "docente": "Mª de Lurdes Soares Souza",
                "ch": "20h",
                "observacoes": "Vice-Diretora"
            },
            {
                "ordem": 21,
                "docente": "Sara Barreto Lima",
                "ch": "20h",
                "observacoes": "Diretora"
            }
        ],
        "professores_desdobrados": [
            {
                "docente": "Mª de Lurdes Soares Souza",
                "ch": "20h"
            },
            {
                "docente": "Jaciara Silva Santos Lima",
                "ch": "20h"
            }
        ],
        "secretaria_escolar": [
            {
                "nome": "Amora Monteiro de Lemos",
                "ch": "40h"
            }
        ],
        "vigilantes": [
            {
                "nome": "Claudiolino de Jesus Silva",
                "ch": "44h"
            },
            {
                "nome": "Gesse Judson Sousa dos Santos",
                "ch": "44h"
            }
        ],
        "aux_servico_escolar": [
            {
                "nome": "Amanda Bomfim Sales",
                "ch": "30h",
                "observacoes": "Carneiro Ribeiro"
            },
            {
                "nome": "Antonio Marcos Ramos dos Santos",
                "ch": "30h",
                "observacoes": "Afastado"
            },
            {
                "nome": "Daiany dos Santos Barreto Barbosa",
                "ch": "30h",
                "observacoes": "Readaptada"
            },
            {
                "nome": "Eleni Pereira",
                "ch": "30h",
                "observacoes": ""
            },
            {
                "nome": "Eline da Silva Santos",
                "ch": "30h",
                "observacoes": "Readaptada"
            },
            {
                "nome": "Eloina Silva Lima",
                "ch": "30h",
                "observacoes": ""
            }
        ],
        "servidores_contratados": [
            {
                "n": 1,
                "funcionario": "Pedro Henrique Lopes Gondim",
                "ch": 40,
                "funcao": "Assistente Administrativo",
                "observacao": ""
            },
            {
                "n": 1,
                "funcionario": "Maiane Sousa Silva",
                "ch": 40,
                "funcao": "Atendente de Classe",
                "observacao": ""
            },
            {
                "n": 1,
                "funcionario": "Aldecir de Jesus Macedo",
                "ch": 40,
                "funcao": "Auxiliar de Infraestrutura Escolar",
                "observacao": ""
            },
            {
                "n": 2,
                "funcionario": "Deisiane Brito Dos Santos",
                "ch": 40,
                "funcao": "Auxiliar de Infraestrutura Escolar",
                "observacao": ""
            },
            {
                "n": 3,
                "funcionario": "Eliana Geralda Santos",
                "ch": 40,
                "funcao": "Auxiliar de Infraestrutura Escolar",
                "observacao": ""
            },
            {
                "n": 4,
                "funcionario": "Ivonaide Guedes Pereira Santos",
                "ch": 40,
                "funcao": "Auxiliar de Infraestrutura Escolar",
                "observacao": ""
            },
            {
                "n": 5,
                "funcionario": "Jaine dos Santos Costa",
                "ch": 40,
                "funcao": "Auxiliar de Infraestrutura Escolar",
                "observacao": ""
            },
            {
                "n": 1,
                "funcionario": "Nadja Santana da Hora Santos",
                "ch": 20,
                "funcao": "Coordenador Pedagógico",
                "observacao": ""
            },
            {
                "n": 1,
                "funcionario": "Ana Lucia Flois Lima",
                "ch": 20,
                "funcao": "Professor",
                "observacao": ""
            },
            {
                "n": 2,
                "funcionario": "Eliane Costa Araujo Vaes",
                "ch": 20,
                "funcao": "Professor",
                "observacao": ""
            },
            {
                "n": 3,
                "funcionario": "Jamile de Jesus Santos",
                "ch": 20,
                "funcao": "Professor",
                "observacao": ""
            },
            {
                "n": 4,
                "funcionario": "Leisy Mony de Souza Freitas",
                "ch": 20,
                "funcao": "Professor",
                "observacao": ""
            },
            {
                "n": 5,
                "funcionario": "Luciane Araujo Sampaio",
                "ch": 20,
                "funcao": "Professor",
                "observacao": ""
            },
            {
                "n": 6,
                "funcionario": "Magdiel Costa Sousa",
                "ch": 20,
                "funcao": "Professor",
                "observacao": ""
            },
            {
                "n": 7,
                "funcionario": "Mateus Santos Costa",
                "ch": 20,
                "funcao": "Professor",
                "observacao": ""
            },
            {
                "n": 8,
                "funcionario": "Mirele dos Santos Costa",
                "ch": 20,
                "funcao": "Professor",
                "observacao": ""
            },
            {
                "n": 9,
                "funcionario": "Naiara dos Santos Brandão",
                "ch": 20,
                "funcao": "Professor",
                "observacao": ""
            },
            {
                "n": 10,
                "funcionario": "Tamara Mascarenhas de Oliveira",
                "ch": 20,
                "funcao": "Professor",
                "observacao": ""
            },
            {
                "n": 1,
                "funcionario": "Vinicius de Sousa Dias",
                "ch": 40,
                "funcao": "Secretário Escolar",
                "observacao": ""
            },
            {
                "n": 1,
                "funcionario": "Marcelo Ribeiro dos Santos",
                "ch": 40,
                "funcao": "Vigilante Escolar",
                "observacao": ""
            },
            {
                "n": 2,
                "funcionario": "Moises Passos de Brito",
                "ch": 40,
                "funcao": "Vigilante Escolar",
                "observacao": ""
            },
            {
                "n": 3,
                "funcionario": "Valdemir Dias Bispo",
                "ch": 40,
                "funcao": "Vigilante Escolar",
                "observacao": ""
            }
        ]
    },
    {
        "escolas": {
            "Ensino_Fundamental": [
                "CARNEIRO RIBEIRO",
                "CENTRO EDUCACIONAL DO TRABALHADOR",
                "COLEGIO LUZIA SILVA",
                "DELMINDA FARIAS DE ALMEIDA",
                "EMANOEL DE OLIVEIRA BRITO",
                "EVERALDO SOUZA SANTOS",
                "JOAQUIM NERY DE SOUZA",
                "LOURIVAL ROSA DE SENA",
                "MENANDRO MINAHIM",
                "MONTEIRO LOBATO",
                "MUNICIPAL DIANA JUSSIENE",
                "NÚCLEO",
                "PRESIDENTE CASTELO BRANCO",
                "RURAL DE IPIUNA",
                "STELA CAMARA DUBOIS",
                "TERRABRAS",
                "VICENZO GASBARRE"
            ],
            "Educação_Infantil": [
                "ARLINDA EMILIA DE ASSIS",
                "ALEGRIA DE VIVER",
                "CENTRO SOCIAL URBANO - CRECHE",
                "CRECHE M. MARLEIDE PINTO DE N. NUNES",
                "ERALDO TINOCO DE MELO",
                "GRUPO ESCOLAR LOMANTO JUNIOR",
                "MONTEIRO LOBATO",
                "MUNICIPAL IRMA DULCE",
                "NÚCLEO",
                "PRESIDENTE CASTELO BRANCO",
                "RURAL DE IPIUNA",
                "STELA CAMARA DUBOIS",
                "TERRABRAS"
            ]
        }
    },
    {
        "escola": "Eraldo Tinoco de Melo",
        "equipe_gestora": {
            "diretor": "Jucilene da Cruz Leal Rodrigues",
            "vice_diretor": "Jussara Gomes Sousa Leite",
            "coordenadora": "Rosivany dos Santos",
            "secretario": "Rodrigo"
        },
        "servidores_efetivos": [
            {
                "n": 1,
                "docente": "Alessandra Bispo dos Santos",
                "ch": "20h",
                "observacoes": ""
            },
            {
                "n": 2,
                "docente": "Alessandra de Novais Loiola",
                "ch": "20h",
                "observacoes": ""
            },
            {
                "n": 3,
                "docente": "Almiraene Regis de O. Duarte",
                "ch": "20h",
                "observacoes": ""
            },
            {
                "n": 4,
                "docente": "Geonice Maria da Silva Xavier",
                "ch": "20h",
                "observacoes": ""
            },
            {
                "n": 5,
                "docente": "Janara Aragão Duarte",
                "ch": "20h",
                "observacoes": "INSS"
            },
            {
                "n": 6,
                "docente": "Jovana Barros S. Almeida",
                "ch": "20h",
                "observacoes": ""
            },
            {
                "n": 7,
                "docente": "Jucilene da Cruz Leal Rodrigues",
                "ch": "",
                "observacoes": "Diretora"
            },
            {
                "n": 8,
                "docente": "Jussara Gomes Sousa Leite",
                "ch": "40h",
                "observacoes": "20h Vice-Diretora"
            },
            {
                "n": 9,
                "docente": "Lenilza Barbosa dos Santos",
                "ch": "20h",
                "observacoes": ""
            },
            {
                "n": 10,
                "docente": "Mariza de Andrade Santos",
                "ch": "20h",
                "observacoes": "INSS"
            },
            {
                "n": 11,
                "docente": "Marly Ribeiro Santos",
                "ch": "40h",
                "observacoes": ""
            },
            {
                "n": 12,
                "docente": "Rosivany dos Santos",
                "ch": "20h",
                "observacoes": "Coordenadora Pedagógica"
            },
            {
                "n": 13,
                "docente": "Leniani Mello",
                "ch": "40h",
                "observacoes": "Secretária Escolar (Cedida)"
            }
        ],
        "vigilantes": [
            {
                "n": 1,
                "nome": "Jildaci Arruda Neri",
                "ch": "40h"
            }
        ],
        "atendentes_classe": [
            {
                "n": 1,
                "nome": "Cleide Almeida Oliveira",
                "ch": "40h"
            },
            {
                "n": 2,
                "nome": "Elaine Cristina Oliveira da Silva",
                "ch": "40h"
            },
            {
                "n": 3,
                "nome": "Elizevera Anselmo de Santana",
                "ch": "40h",
                "observacoes": "Cultura"
            },
            {
                "n": 4,
                "nome": "Monsangela Aprigio dos Santos",
                "ch": "40h"
            },
            {
                "n": 5,
                "nome": "Renata da Silva Bispo",
                "ch": "40h"
            },
            {
                "n": 6,
                "nome": "Tailana Lins Miranda Santana",
                "ch": "40h"
            },
            {
                "n": 7,
                "nome": "Vanessa Anselmo de S. Araújo Santos",
                "ch": "40h"
            }
        ],
        "aux_servico_escolar": [
            {
                "n": 1,
                "nome": "Cristovaldo de S. Nascimento",
                "ch": "30h",
                "observacoes": "Vigilante Noturno"
            },
            {
                "n": 2,
                "nome": "Dilvânia Bomfim dos Santos",
                "ch": "30h"
            },
            {
                "n": 3,
                "nome": "Elian Ferreira Bastos",
                "ch": "30h"
            },
            {
                "n": 4,
                "nome": "Eliana Silva da Cruz",
                "ch": "30h",
                "observacoes": "Readaptada"
            },
            {
                "n": 5,
                "nome": "Eliane de Queiroz Borges",
                "ch": "30h"
            },
            {
                "n": 6,
                "nome": "Jackson Duca Cerqueira",
                "ch": "30h"
            },
            {
                "n": 7,
                "nome": "Josiel O. Nascimento",
                "ch": "30h",
                "observacoes": "Vigilante Noturno"
            },
            {
                "n": 8,
                "nome": "Leide Batista Oliveira Rosa",
                "ch": "30h",
                "observacoes": "Cultura"
            }
        ],
        "servidores_contratados": [
            {
                "n": 1,
                "funcionario": "Tania Sousa De Jesus",
                "ch": "40h",
                "funcao": "Atendente de Classe",
                "observacao": ""
            },
            {
                "n": 2,
                "funcionario": "Webia Fontes Do Carmo Sousa",
                "ch": "40h",
                "funcao": "Atendente de Classe",
                "observacao": ""
            },
            {
                "n": 3,
                "funcionario": "Gilson Sousa Dos Santos",
                "ch": "40h",
                "funcao": "Aux. de Infraestrutura escolar",
                "observacao": ""
            },
            {
                "n": 4,
                "funcionario": "Indiara Fonseca Soares",
                "ch": "40h",
                "funcao": "Merendeira",
                "observacao": ""
            },
            {
                "n": 5,
                "funcionario": "Noilma Oliveira Sousa",
                "ch": "40h",
                "funcao": "Auxiliar de Alimentação Escolar",
                "observacao": ""
            },
            {
                "n": 6,
                "funcionario": "Francyne Dos Santos Lima",
                "ch": "40h",
                "funcao": "Profis de Apoio à alunos com deficiência",
                "observacao": ""
            },
            {
                "n": 7,
                "funcionario": "Juliana Fonseca Costa Almeida",
                "ch": "40h",
                "funcao": "Profis de Apoio à alunos com deficiência",
                "observacao": ""
            },
            {
                "n": 8,
                "funcionario": "Juliana Xavier Dos Santos",
                "ch": "40h",
                "funcao": "Profis de Apoio à alunos com deficiência",
                "observacao": ""
            },
            {
                "n": 9,
                "funcionario": "Rayssa Brito Da Silva",
                "ch": "40h",
                "funcao": "Profis de Apoio à alunos com deficiência",
                "observacao": ""
            },
            {
                "n": 10,
                "funcionario": "Eliane Santos Gentil",
                "ch": "40h",
                "funcao": "Profis. de Apoio à alunos com deficiência",
                "observacao": ""
            },
            {
                "n": 11,
                "funcionario": "Sidneia Do Carmo Costa",
                "ch": "40h",
                "funcao": "Profis. de Apoio à alunos com deficiência",
                "observacao": ""
            },
            {
                "n": 12,
                "funcionario": "Tais Cruz Dos Santos",
                "ch": "40h",
                "funcao": "Profis. de Apoio à alunos com deficiência",
                "observacao": ""
            },
            {
                "n": 13,
                "funcionario": "Rodrigo Santos da Silva",
                "ch": "40h",
                "funcao": "Secretário(a) Escolar",
                "observacao": ""
            },
            {
                "n": 14,
                "funcionario": "Marcello Heduardo N. Borges",
                "ch": "40h",
                "funcao": "Vigilante Diurno",
                "observacao": ""
            }
        ]
    },
    {
        "escola": "Everaldo Souza Santos",
        "equipe_gestora": {
            "diretor": "Fabiana Soares de Araujo da Hora",
            "vice_diretor": "Neusa de Souza Felix dos Santos",
            "coordenador": "Leonara Machado Melo",
            "secretario_escolar": "Nicollas Cardoso da Silva",
            "assistente_administrativo": "Josiel Cabral Carrilho"
        },
        "servidores_efetivos": [
            {
                "nome": "Adilson Novaes",
                "ch": "20h",
                "observacoes": ""
            },
            {
                "nome": "Adriana Barreto Scotti Porto",
                "ch": "20h",
                "observacoes": "Vice-Diretora"
            },
            {
                "nome": "Ana Paula M. da Silva",
                "ch": "20h",
                "observacoes": "Remoção Provisória"
            },
            {
                "nome": "Anatildes Lima de Carvalho Caroso",
                "ch": "20h",
                "observacoes": "Está permutada em Jequié"
            },
            {
                "nome": "Daniela Souza Santos",
                "ch": "20h",
                "observacoes": ""
            },
            {
                "nome": "Eliene Santana Meira Sousa",
                "ch": "20h",
                "observacoes": "Sede Vicenzo"
            },
            {
                "nome": "Fabiana Soares de Araujo da Hora",
                "ch": "20h",
                "observacoes": "Diretora"
            },
            {
                "nome": "Gardênia Oliveira Muniz",
                "ch": "20h",
                "observacoes": ""
            },
            {
                "nome": "Gerlan Oliveira Santos",
                "ch": "20h",
                "observacoes": "Está no CET"
            },
            {
                "nome": "Gilma Leda Pedro Coelho",
                "ch": "20h",
                "observacoes": "Readaptada"
            },
            {
                "nome": "Ianara Moraes Pereira",
                "ch": "20h",
                "observacoes": "Está permutada em Jequié"
            },
            {
                "nome": "Ines Almeida Silva Oliveira",
                "ch": "20h",
                "observacoes": "Está 20h na Diana"
            },
            {
                "nome": "Jeane Souza da Silva",
                "ch": "40h",
                "observacoes": ""
            },
            {
                "nome": "José Carlos Almeida Silva Filho",
                "ch": "20h",
                "observacoes": ""
            },
            {
                "nome": "Leandra Pereira de Oliveira",
                "ch": "20h",
                "observacoes": "Está cedida a Feira de Santana"
            },
            {
                "nome": "Lívia Santos de Santana",
                "ch": "20h",
                "observacoes": "Lic sem vencimento"
            },
            {
                "nome": "Luciene Alves dos Santos",
                "ch": "40h",
                "observacoes": ""
            },
            {
                "nome": "Maria Aparecida Santos Santiago",
                "ch": "20h",
                "observacoes": "Readaptada"
            },
            {
                "nome": "Mariete da Silva Lima",
                "ch": "40h",
                "observacoes": "INSS"
            },
            {
                "nome": "Marilene Andrade Correia Almeida",
                "ch": "40h",
                "observacoes": "Diretora Terrabras"
            },
            {
                "nome": "Neusa de Souza Felix dos Santos",
                "ch": "20h",
                "observacoes": ""
            },
            {
                "nome": "Raiana Araújo de Oliveira",
                "ch": "20h",
                "observacoes": ""
            },
            {
                "nome": "Roemeire das Neves S. Aragão",
                "ch": "20h",
                "observacoes": ""
            },
            {
                "nome": "Rosemary Mendes dos Santos",
                "ch": "40h",
                "observacoes": ""
            },
            {
                "nome": "Vera Lúcia Machado da Silva",
                "ch": "40h",
                "observacoes": "Diretora Irmã Dulce"
            },
            {
                "nome": "Vilma Oliveira D’emídio",
                "ch": "20h",
                "observacoes": ""
            },
            {
                "nome": "Vilmara Araújo da Silva",
                "ch": "40h",
                "observacoes": "Diretora Creche"
            }
        ],
        "desdobramentos": [
            {
                "nome": "Adilson Novaes",
                "ch": "20h"
            },
            {
                "nome": "Neusa de Souza Felix dos Santos",
                "ch": "20h"
            }
        ],
        "professores_permutados": [
            {
                "nome": "Cosmildo Santana Rocha",
                "ch": "40h"
            }
        ],
        "atendente_de_classe": [
            {
                "nome": "Inês Nardes dos Santos",
                "ch": "40h"
            }
        ],
        "auxiliares_servico_escolar": [
            {
                "nome": "Adriana Mendes da Cruz Santos",
                "ch": "30h",
                "observacoes": ""
            },
            {
                "nome": "Irailde Santos Braga Lima",
                "ch": "30h",
                "observacoes": ""
            },
            {
                "nome": "Maria do Carmo Nascimento dos Santos",
                "ch": "30h",
                "observacoes": "Readaptada"
            },
            {
                "nome": "Meirilande Ribeiro de Souza",
                "ch": "30h",
                "observacoes": "Lic sem vencimento"
            },
            {
                "nome": "Rosangela Assunção Souza Oliveira",
                "ch": "30h",
                "observacoes": ""
            },
            {
                "nome": "Noemia Nunes Camilo",
                "ch": ""
            }
        ],
        "servidor_cedido": [
            {
                "nome": "Vivaldo Pereira dos S. Souza",
                "ch": "40h",
                "observacoes": "Vigilante"
            }
        ],
        "servidores_contratados": [
            {
                "nome": "Josiel Cabral Carrilho",
                "ch": "40h",
                "funcao": "Assistente Administrativo"
            },
            {
                "nome": "Alessandra Santos Freitas",
                "ch": "40h",
                "funcao": "Profissional de Apoio à alunos com deficiência"
            },
            {
                "nome": "Messias da Anunciação Nascimento",
                "ch": "40h",
                "funcao": "Profissional de Apoio à alunos com deficiência"
            },
            {
                "nome": "Rita Lilian de Jesus Dos Santos",
                "ch": "40h",
                "funcao": "Profissional de Apoio à alunos com deficiência"
            },
            {
                "nome": "Robson Thiago Sampaio Rabelo",
                "ch": "40h",
                "funcao": "Profissional de Apoio à alunos com deficiência"
            },
            {
                "nome": "Rosivane Teles dos Santos",
                "ch": "40h",
                "funcao": "Profissional de Apoio à alunos com deficiência"
            },
            {
                "nome": "Viviane Nogueira Novaes",
                "ch": "40h",
                "funcao": "Profissional de Apoio à alunos com deficiência"
            },
            {
                "nome": "Andreia Santos Alves de Almeida",
                "ch": "40h",
                "funcao": "Auxiliar de Infraestrutura Escolar"
            },
            {
                "nome": "Elma Barreto Silva",
                "ch": "40h",
                "funcao": "Auxiliar de Infraestrutura Escolar"
            },
            {
                "nome": "Givanilda Cerqueira Santos",
                "ch": "40h",
                "funcao": "Auxiliar de Infraestrutura Escolar"
            },
            {
                "nome": "Iracy Oliveira Santos",
                "ch": "40h",
                "funcao": "Auxiliar de Infraestrutura Escolar"
            },
            {
                "nome": "Ivanisia Pereira Dos Santos Sousa",
                "ch": "40h",
                "funcao": "Auxiliar de Infraestrutura Escolar"
            },
            {
                "nome": "Luciana Almeida Silva",
                "ch": "40h",
                "funcao": "Auxiliar de Infraestrutura Escolar"
            },
            {
                "nome": "Marly Silva Souza",
                "ch": "40h",
                "funcao": "Auxiliar de Infraestrutura Escolar"
            },
            {
                "nome": "Valdirene Lemos da Anunciação",
                "ch": "40h",
                "funcao": "Auxiliar de Infraestrutura Escolar"
            },
            {
                "nome": "Leonara Machado de Melo",
                "ch": "40h",
                "funcao": "Coordenador Pedagógico"
            },
            {
                "nome": "Adriano Alves da Silva",
                "ch": "20h",
                "funcao": "Professor"
            },
            {
                "nome": "Ana Carolina Ramos dos Santos",
                "ch": "20h",
                "funcao": "Professor"
            },
            {
                "nome": "Irenice Oliveira de Deus",
                "ch": "20h",
                "funcao": "Professor"
            },
            {
                "nome": "Ivoneide de Jesus Santos Parreiras",
                "ch": "20h",
                "funcao": "Professor"
            },
            {
                "nome": "Murilo Silva dos Santos",
                "ch": "20h",
                "funcao": "Professor"
            },
            {
                "nome": "Renata da Paixão Santos",
                "ch": "20h",
                "funcao": "Professor"
            },
            {
                "nome": "Rosany Santana Santos",
                "ch": "20h",
                "funcao": "Professor"
            },
            {
                "nome": "Tamiles Caje e Santos",
                "ch": "20h",
                "funcao": "Professor"
            },
            {
                "nome": "Tiago Silva Moraes",
                "ch": "20h",
                "funcao": "Professor"
            },
            {
                "nome": "Viviane Mendes Brito",
                "ch": "20h",
                "funcao": "Professor"
            },
            {
                "nome": "Nicollas Cardoso da Silva",
                "ch": "40h",
                "funcao": "Secretário Escolar"
            },
            {
                "nome": "Carlos Batista dos Santos",
                "ch": "40h",
                "funcao": "Vigilante Escolar"
            },
            {
                "nome": "Daniel Pereira Barbosa",
                "ch": "40h",
                "funcao": "Vigilante Escolar"
            },
            {
                "nome": "Fernando Santos Oliveira",
                "ch": "40h",
                "funcao": "Vigilante Escolar"
            },
            {
                "nome": "Helder Camilo Nogueira",
                "ch": "40h",
                "funcao": "Vigilante Escolar"
            }
        ]
    },
    {
        "escola": "Escola Irmã Dulce",
        "equipe_gestora": {
            "diretora": "Vera Lúcia Machado da Silva",
            "coordenadora": "Alessandra de Novaes Santana",
            "secretario_escolar": "Marco Antônio Alves Meira"
        },
        "servidores_efetivos": {
            "docentes": [
                {
                    "nome": "Edna Sandra Martins Pires",
                    "ch": 40
                },
                {
                    "nome": "Jaqueline Trindade Araujo",
                    "ch": 20
                },
                {
                    "nome": "Jovenita Santos Andrade",
                    "ch": 40
                },
                {
                    "nome": "Marlucia Melo Gaia",
                    "ch": 40
                },
                {
                    "nome": "Noélia de Sousa",
                    "ch": 20
                },
                {
                    "nome": "Vera Lucia Machado da Silva",
                    "ch": "20/20"
                }
            ],
            "coordenadora_pedagogica": [
                {
                    "nome": "Alessandra de Novaes Santana",
                    "ch": 20
                }
            ],
            "atendentes_de_classe": [
                {
                    "nome": "Antonela Andrade Santos",
                    "ch": 40,
                    "observacoes": "Readaptada"
                },
                {
                    "nome": "Joselita de Jesus dos S. Lisboa",
                    "ch": 40,
                    "observacoes": "Está No Joaquim Nery"
                },
                {
                    "nome": "Nilma de Cassia Pereira da Silva",
                    "ch": 40,
                    "observacoes": "Está em Lajedo Permuta"
                },
                {
                    "nome": "Valquiria dos Santos Silva",
                    "ch": 40
                }
            ],
            "secretario_escolar": [
                {
                    "nome": "Marco Antônio Alves Meira",
                    "ch": 40
                }
            ],
            "auxiliares_de_servico_escolar": [
                {
                    "nome": "Dalva Vieira de Jesus",
                    "ch": 30
                },
                {
                    "nome": "Dionatas Oliveira de Souza",
                    "ch": 30
                },
                {
                    "nome": "Gilvanda de Andrade Brazil",
                    "ch": 30
                },
                {
                    "nome": "Ivanildes de Jesus Damascena",
                    "ch": 30
                },
                {
                    "nome": "Núbia dos Santos Lula",
                    "ch": 30
                }
            ]
        },
        "servidores_contratados": {
            "atendentes_de_classe": [
                {
                    "nome": "Aiara dos Santos Cerqueira",
                    "ch": 40
                },
                {
                    "nome": "Alanna Souza Ribas",
                    "ch": 40
                },
                {
                    "nome": "Crislane Braz Santos",
                    "ch": 40
                },
                {
                    "nome": "Clodoaldo Carvalho dos Santos",
                    "ch": 40
                },
                {
                    "nome": "Daniela Silva Mascarenhas",
                    "ch": 40
                },
                {
                    "nome": "Diely Pereira Santos",
                    "ch": 40
                },
                {
                    "nome": "Erika Dutra dos Santos",
                    "ch": 40
                },
                {
                    "nome": "Geovana dos Santos Cintra",
                    "ch": 40
                },
                {
                    "nome": "Jamile dos Santos Vieira",
                    "ch": 40
                },
                {
                    "nome": "Janiele Santos Matos",
                    "ch": 40
                },
                {
                    "nome": "Nubia Bezerra dos Santos",
                    "ch": 40
                },
                {
                    "nome": "Tamiris Dutra Santos",
                    "ch": 40
                }
            ],
            "auxiliares_de_infraestrutura_escolar": [
                {
                    "nome": "Ivonildes Cardoso dos Santos",
                    "ch": 40
                },
                {
                    "nome": "Lavinia Oliveira Silva",
                    "ch": 40
                },
                {
                    "nome": "Mª de Lourdes Amaral dos Santos",
                    "ch": 40
                },
                {
                    "nome": "Maria Karolina Braga dos Santos",
                    "ch": 40
                },
                {
                    "nome": "Michely Santos da Silva",
                    "ch": 40
                },
                {
                    "nome": "Raimunda Cerqueira Santos",
                    "ch": 40
                }
            ],
            "professores": [
                {
                    "nome": "Edione Silva dos Santos",
                    "ch": 20
                },
                {
                    "nome": "Gabriela Oliveira e Silva",
                    "ch": 20
                },
                {
                    "nome": "Tatiane Couto Correia",
                    "ch": 20
                }
            ],
            "vigilantes_escolares": [
                {
                    "nome": "Isaurito Batista do Rosario",
                    "ch": 40
                },
                {
                    "nome": "Joao Garcia",
                    "ch": 40
                },
                {
                    "nome": "Marinaldo da Hora Gonçalves",
                    "ch": 40
                }
            ]
        }
    },
    {
        "escola": "Escola Joaquim Nery de Souza",
        "equipe_gestora": {
            "diretora": "Marcia Araújo da Silva",
            "vice_diretora": "Maria de Fátima F. de Carvalho Reis",
            "coordenadora": "Ilmara Souza Santos",
            "secretaria_escolar": "Geisa Feitosa de Sena Santos"
        },
        "servidores_efetivos": {
            "docentes": [
                {
                    "nome": "Edina Teodoro dos Santos",
                    "ch": 20
                },
                {
                    "nome": "Ivanildes B. Mascarenhas",
                    "ch": 20
                },
                {
                    "nome": "Joelma dos Santos Silva",
                    "ch": 20,
                    "observacoes": "Vice Diana"
                },
                {
                    "nome": "Josilene Oliveira S. Portela",
                    "ch": "20/20"
                },
                {
                    "nome": "Karine Nascimento Silva",
                    "ch": "20/20",
                    "observacoes": "Doutorado"
                },
                {
                    "nome": "Lauraci Araujo Oliveira",
                    "ch": 20,
                    "observacoes": "+ 20 permuta de Itiruçu"
                },
                {
                    "nome": "Luzinete de Jesus Miranda",
                    "ch": 20,
                    "observacoes": "Sede"
                },
                {
                    "nome": "Marcia Araujo da Silva",
                    "ch": 20
                },
                {
                    "nome": "Maria de Fátima Freitas de Carvalho",
                    "ch": 20
                },
                {
                    "nome": "Rosa Nery Costa",
                    "ch": 40,
                    "observacoes": "Readaptada"
                },
                {
                    "nome": "Tatiane Santos D’ Emídio",
                    "ch": "20/20"
                }
            ],
            "professores_desdobrados": [
                {
                    "nome": "Maria de Fátima Freitas de Carvalho",
                    "ch": 20
                },
                {
                    "nome": "Ivanildes B. Mascarenhas",
                    "ch": 20
                }
            ],
            "atendentes_de_classe": [
                {
                    "nome": "Marlene dos Santos Figueredo",
                    "ch": 40
                }
            ],
            "auxiliares_de_servico_escolar": [
                {
                    "nome": "Indiara Lima dos Santos",
                    "ch": 30
                },
                {
                    "nome": "Maria Auxiliadora Barreto de Souza",
                    "ch": 30
                },
                {
                    "nome": "Maria das Graças Araujo Correia",
                    "ch": 30,
                    "observacoes": "INSS"
                },
                {
                    "nome": "Roseli Correia de Oliveira",
                    "ch": 30
                }
            ],
            "servidores_cedidos_pela_infraestrutura": [
                {
                    "nome": "Abelúcia Correira dos Santos",
                    "ch": 30,
                    "observacoes": "Gari"
                }
            ]
        },
        "servidores_contratados": {
            "atendentes_de_classe": [
                {
                    "nome": "Evelin Carla de Deus Dos Santos",
                    "ch": 40
                },
                {
                    "nome": "Geany Antonia Santos dos Santos",
                    "ch": 40
                },
                {
                    "nome": "Lusiene Santos Almeida",
                    "ch": 40
                }
            ],
            "auxiliares_de_infraestrutura_escolar": [
                {
                    "nome": "Adriano Bastos Lima",
                    "ch": 40
                },
                {
                    "nome": "Aparecida da Cassia Almeida Rodrigues Souza",
                    "ch": 40
                },
                {
                    "nome": "Maria Larissa Sousa Cruz",
                    "ch": 40
                },
                {
                    "nome": "Nubia Coelho Santana",
                    "ch": 40
                },
                {
                    "nome": "Rosineide Santos Da Silva",
                    "ch": 40
                }
            ],
            "coordenador_pedagogico": [
                {
                    "nome": "Ilmara Souza Santos",
                    "ch": 20
                }
            ],
            "professores": [
                {
                    "nome": "Bruna de Jesus Silva",
                    "ch": 20
                },
                {
                    "nome": "Denilce Silva da Hora",
                    "ch": 20
                },
                {
                    "nome": "Fabia Coelho Santana",
                    "ch": 20
                },
                {
                    "nome": "Geisa Teles dos Santos Henes",
                    "ch": 20
                },
                {
                    "nome": "Judiquele Silva Lima",
                    "ch": 20
                },
                {
                    "nome": "Leiliane Nascimento Santos",
                    "ch": 20
                },
                {
                    "nome": "Monica Barbosa Queiroz Machado",
                    "ch": 20
                },
                {
                    "nome": "Simone Brito da Cruz",
                    "ch": 20
                },
                {
                    "nome": "Valdecy de Jesus Bonfim",
                    "ch": 20
                }
            ],
            "secretaria_escolar": [
                {
                    "nome": "Geisa Feitosa de Sena Santos",
                    "ch": 40
                }
            ],
            "vigilantes_escolares": [
                {
                    "nome": "Carlos Henrique Silva Felix",
                    "ch": 40
                },
                {
                    "nome": "Dorimar dos Santos",
                    "ch": 40
                },
                {
                    "nome": "Joilton dos Santos Souza",
                    "ch": 40
                },
                {
                    "nome": "Nildo Sousa Gouveia",
                    "ch": 40
                }
            ]
        }
    },
    {
        "escola": "Grupo Escolar Lomanto Júnior",
        "equipe_gestora": {
            "diretora": "Roziane Souza de Almeida Andrade",
            "vice_diretora": "Iolene Bastos Nascimento",
            "coordenadora": "Lilian Pereira Guedes",
            "secretaria_escolar": "Karine Menezes do Amaral"
        },
        "servidores_efetivos": {
            "docentes": [
                {
                    "nome": "Arizete Mendes Souza",
                    "ch": 20,
                    "observacoes": "Readaptada"
                },
                {
                    "nome": "Elismara Bispo dos Santos",
                    "ch": 20,
                    "observacoes": "SMED"
                },
                {
                    "nome": "Gilneide Santos de Almeida",
                    "ch": 20
                },
                {
                    "nome": "Ilma Cristina Bastos Nascimento Pereira",
                    "ch": 20
                },
                {
                    "nome": "Iolene Bastos Nascimento",
                    "ch": 20,
                    "observacoes": "Vice-Diretora"
                },
                {
                    "nome": "Isnaia dos Santos Chaves",
                    "ch": 20,
                    "observacoes": "INSS"
                },
                {
                    "nome": "Lidiane Almeida Silva",
                    "ch": 40
                },
                {
                    "nome": "Roziane Souza de Almeida Andrade",
                    "ch": 20,
                    "observacoes": "Diretora"
                },
                {
                    "nome": "Sheila Souza Gonçalves",
                    "ch": 40,
                    "observacoes": "Remoção temporária"
                },
                {
                    "nome": "Vilmaci dos Santos Dias",
                    "ch": 20
                }
            ],
            "professores_desdobrados": [
                {
                    "nome": "Ilma Cristina Bastos Nascimento Pereira",
                    "ch": 20
                },
                {
                    "nome": "Iolene Bastos Nascimento",
                    "ch": 20
                }
            ],
            "coordenadora_pedagogica": [
                {
                    "nome": "Lilian Pereira Guedes",
                    "ch": 20
                }
            ],
            "secretario_escolar": [
                {
                    "nome": "Karine Menezes do Amaral",
                    "ch": 40
                }
            ],
            "vigilantes": [
                {
                    "nome": "Alysson Hébert Almeida da Silva",
                    "ch": 40
                },
                {
                    "nome": "Paulo Gonçalves da Silva",
                    "ch": 40
                },
                {
                    "nome": "Antonio Cesar Santos Jesus",
                    "ch": 40
                }
            ],
            "auxiliares_de_servico_escolar": [
                {
                    "nome": "Ana Carla Ferreira Oliveira",
                    "ch": 30
                },
                {
                    "nome": "Magiane Cardoso Ferreira Oliveira",
                    "ch": 30
                },
                {
                    "nome": "Norma de Fátima Louzada dos Santos",
                    "ch": 30
                },
                {
                    "nome": "Sandra Helena Felix Santos Araújo",
                    "ch": 30,
                    "observacoes": "INSS"
                },
                {
                    "nome": "Solange Santos Cardoso da Silva",
                    "ch": 30
                }
            ],
            "servidores_cedidos_pela_infraestrutura": [
                {
                    "nome": "Edna Anunciação de Jesus",
                    "ch": 40
                }
            ]
        },
        "servidores_contratados": {
            "atendentes_de_classe": [
                {
                    "nome": "Adriana dos Santos Borges",
                    "ch": 40
                },
                {
                    "nome": "Anilda Bomfim da Silva",
                    "ch": 40
                },
                {
                    "nome": "Elisangela Andrade Brasil",
                    "ch": 40
                },
                {
                    "nome": "Elizabeth Rocha Pereira",
                    "ch": 40
                },
                {
                    "nome": "Leiliane Sousa Felis",
                    "ch": 40
                },
                {
                    "nome": "Silvone Dos S. Caje e Santos",
                    "ch": 40
                }
            ],
            "auxiliares_de_alimentacao_escolar": [
                {
                    "nome": "Daiana Teles dos Santos",
                    "ch": 40
                }
            ],
            "merendeira": [
                {
                    "nome": "Edinelia Carvalho Sousa",
                    "ch": 40
                }
            ],
            "professores_regentes": [
                {
                    "nome": "Erica O. Lima dos Santos"
                },
                {
                    "nome": "Rosevania Souza Correia"
                },
                {
                    "nome": "Veronica Santos Batista"
                }
            ],
            "profissionais_de_apoio_a_alunos_com_deficiencia": [
                {
                    "nome": "Bruna Dos Santos Costa",
                    "ch": 40
                },
                {
                    "nome": "Larissa Figueiredo de Souza",
                    "ch": 40
                },
                {
                    "nome": "Milena Batista Souza Santos",
                    "ch": 40
                },
                {
                    "nome": "Nayana Galvao Oliveira",
                    "ch": 40
                },
                {
                    "nome": "Patricia Silva de Almeida",
                    "ch": 40
                },
                {
                    "nome": "Regia Oliveira de Souza",
                    "ch": 40
                },
                {
                    "nome": "Sossiane Oliveira Santos",
                    "ch": 40
                }
            ],
            "servicos_gerais": [
                {
                    "nome": "Agnelita Bispo dos Santos",
                    "ch": 40
                },
                {
                    "nome": "Bruna Teles de Q. Cardoso",
                    "ch": 40
                },
                {
                    "nome": "Carolina Alves dos Santos",
                    "ch": 40
                }
            ],
            "vigilante_diurno": [
                {
                    "nome": "Adenilton Nunes dos Santos",
                    "ch": 40
                }
            ]
        }
    },
    {
        "escola": "Grupo Escolar Lomanto Júnior",
        "equipe_gestora": {
            "diretora": "Roziane Souza de Almeida Andrade",
            "vice_diretora": "Iolene Bastos Nascimento",
            "coordenadora": "Lilian Pereira Guedes",
            "secretaria_escolar": "Karine Menezes do Amaral"
        },
        "servidores_efetivos": {
            "docentes": [
                {
                    "nome": "Arizete Mendes Souza",
                    "ch": 20,
                    "observacoes": "Readaptada"
                },
                {
                    "nome": "Elismara Bispo dos Santos",
                    "ch": 20,
                    "observacoes": "SMED"
                },
                {
                    "nome": "Gilneide Santos de Almeida",
                    "ch": 20
                },
                {
                    "nome": "Ilma Cristina Bastos Nascimento Pereira",
                    "ch": 20
                },
                {
                    "nome": "Iolene Bastos Nascimento",
                    "ch": 20,
                    "observacoes": "Vice-Diretora"
                },
                {
                    "nome": "Isnaia dos Santos Chaves",
                    "ch": 20,
                    "observacoes": "INSS"
                },
                {
                    "nome": "Lidiane Almeida Silva",
                    "ch": 40
                },
                {
                    "nome": "Roziane Souza de Almeida Andrade",
                    "ch": 20,
                    "observacoes": "Diretora"
                },
                {
                    "nome": "Sheila Souza Gonçalves",
                    "ch": 40,
                    "observacoes": "Remoção temporária"
                },
                {
                    "nome": "Vilmaci dos Santos Dias",
                    "ch": 20
                }
            ],
            "professores_desdobrados": [
                {
                    "nome": "Ilma Cristina Bastos Nascimento Pereira",
                    "ch": 20
                },
                {
                    "nome": "Iolene Bastos Nascimento",
                    "ch": 20
                }
            ],
            "coordenadora_pedagogica": [
                {
                    "nome": "Lilian Pereira Guedes",
                    "ch": 20
                }
            ],
            "secretario_escolar": [
                {
                    "nome": "Karine Menezes do Amaral",
                    "ch": 40
                }
            ],
            "vigilantes": [
                {
                    "nome": "Alysson Hébert Almeida da Silva",
                    "ch": 40
                },
                {
                    "nome": "Paulo Gonçalves da Silva",
                    "ch": 40
                },
                {
                    "nome": "Antonio Cesar Santos Jesus",
                    "ch": 40
                }
            ],
            "auxiliares_de_servico_escolar": [
                {
                    "nome": "Ana Carla Ferreira Oliveira",
                    "ch": 30
                },
                {
                    "nome": "Magiane Cardoso Ferreira Oliveira",
                    "ch": 30
                },
                {
                    "nome": "Norma de Fátima Louzada dos Santos",
                    "ch": 30
                },
                {
                    "nome": "Sandra Helena Felix Santos Araújo",
                    "ch": 30,
                    "observacoes": "INSS"
                },
                {
                    "nome": "Solange Santos Cardoso da Silva",
                    "ch": 30
                }
            ],
            "servidores_cedidos_pela_infraestrutura": [
                {
                    "nome": "Edna Anunciação de Jesus",
                    "ch": 40
                }
            ]
        },
        "servidores_contratados": {
            "atendentes_de_classe": [
                {
                    "nome": "Adriana dos Santos Borges",
                    "ch": 40
                },
                {
                    "nome": "Anilda Bomfim da Silva",
                    "ch": 40
                },
                {
                    "nome": "Elisangela Andrade Brasil",
                    "ch": 40
                },
                {
                    "nome": "Elizabeth Rocha Pereira",
                    "ch": 40
                },
                {
                    "nome": "Leiliane Sousa Felis",
                    "ch": 40
                },
                {
                    "nome": "Silvone Dos S. Caje e Santos",
                    "ch": 40
                }
            ],
            "auxiliares_de_alimentacao_escolar": [
                {
                    "nome": "Daiana Teles dos Santos",
                    "ch": 40
                }
            ],
            "merendeira": [
                {
                    "nome": "Edinelia Carvalho Sousa",
                    "ch": 40
                }
            ],
            "professores_regentes": [
                {
                    "nome": "Erica O. Lima dos Santos"
                },
                {
                    "nome": "Rosevania Souza Correia"
                },
                {
                    "nome": "Veronica Santos Batista"
                }
            ],
            "profissionais_de_apoio_a_alunos_com_deficiencia": [
                {
                    "nome": "Bruna Dos Santos Costa",
                    "ch": 40
                },
                {
                    "nome": "Larissa Figueiredo de Souza",
                    "ch": 40
                },
                {
                    "nome": "Milena Batista Souza Santos",
                    "ch": 40
                },
                {
                    "nome": "Nayana Galvao Oliveira",
                    "ch": 40
                },
                {
                    "nome": "Patricia Silva de Almeida",
                    "ch": 40
                },
                {
                    "nome": "Regia Oliveira de Souza",
                    "ch": 40
                },
                {
                    "nome": "Sossiane Oliveira Santos",
                    "ch": 40
                }
            ],
            "servicos_gerais": [
                {
                    "nome": "Agnelita Bispo dos Santos",
                    "ch": 40
                },
                {
                    "nome": "Bruna Teles de Q. Cardoso",
                    "ch": 40
                },
                {
                    "nome": "Carolina Alves dos Santos",
                    "ch": 40
                }
            ],
            "vigilante_diurno": [
                {
                    "nome": "Adenilton Nunes dos Santos",
                    "ch": 40
                }
            ]
        }
    },
    {
        "escola": "Colégio Luzia Silva",
        "equipe_gestora": {
            "diretor": "Jocélia Santos Andrade",
            "vice_diretores": [
                "Iracema da S. S. Oliveira",
                "Indiara da Silva Pereira"
            ],
            "coordenador": "Adrielly Di Tommaso Colangeli Carvalho",
            "secretario_escolar": "Ângela Bispo Soares"
        },
        "servidores_efetivos": {
            "docentes": [
                {
                    "nome": "Carmelita Nasc. Santos",
                    "ch": 40
                },
                {
                    "nome": "Cristina Tereza A. de Almeida",
                    "ch": 40
                },
                {
                    "nome": "Elisângela Cerqueira Pereira",
                    "ch": 20
                },
                {
                    "nome": "Elisangela Silva das Neves",
                    "ch": 40
                },
                {
                    "nome": "Indiara da Silva Pereira",
                    "ch": 40,
                    "observacoes": "20 provisória"
                },
                {
                    "nome": "Iracema da S. S. Oliveira",
                    "ch": 20,
                    "observacoes": "Vice-diretora"
                },
                {
                    "nome": "Itana Sousa da Silva",
                    "ch": 20,
                    "observacoes": "Stela"
                },
                {
                    "nome": "Jocélia Santos Andrade",
                    "ch": 20,
                    "observacoes": "Diretora"
                },
                {
                    "nome": "Núbia Cristina R. Silva",
                    "ch": 20
                },
                {
                    "nome": "Rosa Maria Araújo Porto",
                    "ch": 20
                },
                {
                    "nome": "Tamandaré Gandhi Piropo",
                    "ch": 20
                },
                {
                    "nome": "Zilma Cabral de Aragão",
                    "ch": 40,
                    "observacoes": "20 provisória"
                }
            ],
            "professores_desdobrados": [
                {
                    "nome": "Elisângela Cerqueira Pereira",
                    "ch": 20
                },
                {
                    "nome": "Iracema da S. S. Oliveira",
                    "ch": 20
                }
            ],
            "secretario_escolar": [
                {
                    "nome": "Ângela Bispo Soares",
                    "ch": 40
                }
            ],
            "professora_permutada": [
                {
                    "nome": "Maíra Lemos Reis",
                    "ch": 20
                }
            ],
            "atendente_de_classe": [
                {
                    "nome": "Jamilly Mota Teixeira",
                    "ch": 40
                }
            ],
            "auxiliares_infraestrutura_escolar": [
                {
                    "nome": "Claudionice de Jesus Silva",
                    "ch": 30,
                    "observacoes": "Readaptada"
                },
                {
                    "nome": "Eliane Cerqueira Pereira",
                    "ch": 30
                },
                {
                    "nome": "Genilda de Jesus Santos",
                    "ch": 30
                },
                {
                    "nome": "Juciara Andrade Almeida",
                    "ch": 30,
                    "observacoes": "Readaptada"
                },
                {
                    "nome": "Luziana Almeida de Jesus",
                    "ch": 30
                },
                {
                    "nome": "Uilma Sampaio dos Santos",
                    "ch": 30
                },
                {
                    "nome": "Verlandio dos Santos",
                    "ch": 30,
                    "observacoes": "Vigilante noturno"
                }
            ]
        },
        "servidores_contratados": {
            "assistente_administrativo": [
                {
                    "nome": "Breno Reis Andrade",
                    "ch": 40
                }
            ],
            "atendentes_de_classe": [
                {
                    "nome": "Ingrid da Silva Santos",
                    "ch": 40
                },
                {
                    "nome": "Ludimila Bonfim Nascimento",
                    "ch": 40
                },
                {
                    "nome": "Naiane dos Santos Souza Moreira",
                    "ch": 40
                },
                {
                    "nome": "Shirley Santos de Almeida",
                    "ch": 40
                },
                {
                    "nome": "Suely Santos Pereira",
                    "ch": 40
                },
                {
                    "nome": "Vilma Souza Santos Mira Lopes",
                    "ch": 40
                }
            ],
            "auxiliares_infraestrutura_escolar": [
                {
                    "nome": "Angelia Souza Dos Santos",
                    "ch": 40
                },
                {
                    "nome": "Betania Pereira Amorim Peixinho",
                    "ch": 40
                },
                {
                    "nome": "Cassia Ferreira de Santana",
                    "ch": 40
                },
                {
                    "nome": "Ieda Dos Santos Silva",
                    "ch": 40
                },
                {
                    "nome": "Jose Carlos Cerqueira Mascarenhas Jr",
                    "ch": 40
                },
                {
                    "nome": "Karolyne Santos de Jesus",
                    "ch": 40
                }
            ],
            "coordenador_pedagogico": [
                {
                    "nome": "Adrielly Di Tommaso Colangeli Carvalho",
                    "ch": 20
                }
            ],
            "professores": [
                {
                    "nome": "Edineia Carvalho Dos Santos de Assis",
                    "ch": 20
                },
                {
                    "nome": "Eliane Santos Moreira",
                    "ch": 20
                },
                {
                    "nome": "Erica Costa Da Silva",
                    "ch": 20
                },
                {
                    "nome": "Luana Clissia Santos Franco",
                    "ch": 20
                },
                {
                    "nome": "Marcio Santos Costa",
                    "ch": 20
                },
                {
                    "nome": "Maria do Carmo Oliveira Dos Santos",
                    "ch": 20
                },
                {
                    "nome": "Tarcília Saraiva dos Santos Souza",
                    "ch": 20
                },
                {
                    "nome": "Veridiana Severina da Silva",
                    "ch": 20
                }
            ],
            "vigilante_escolar": [
                {
                    "nome": "Magno Marcel Piropo Santos",
                    "ch": 40
                }
            ]
        }
    },
    {
        "escola": "Creche Municipal Marleide Pinto de Novaes Nunes",
        "equipe_gestora": {
            "diretor": "Vilmara Araujo da Silva Correia",
            "coordenadora": "Alani dos Santos Cardoso",
            "secretario_escolar": "Micheli Lima dos Santos"
        },
        "servidores_efetivos": {
            "docentes": [
                {
                    "nome": "Vilmara Araujo da Silva Correia",
                    "ch": 40,
                    "observacoes": "Diretora"
                }
            ]
        },
        "servidores_contratados": {
            "atendentes_de_classe": [
                {
                    "nome": "Adriana Teles Bomfim",
                    "ch": 40
                },
                {
                    "nome": "Angela Ferreira dos Santos",
                    "ch": 40
                },
                {
                    "nome": "Camila Mira Santos",
                    "ch": 40
                },
                {
                    "nome": "Cleomar Alves Pedroza Costa",
                    "ch": 40
                },
                {
                    "nome": "Dairlane dos Santos Pereira",
                    "ch": 40
                },
                {
                    "nome": "Eliana Mendes Santos",
                    "ch": 40
                },
                {
                    "nome": "Eliene Vieira Serra Sena",
                    "ch": 40
                },
                {
                    "nome": "Erika Vitoria Oliveira de Jesus",
                    "ch": 40
                },
                {
                    "nome": "Fabiola Barbosa de Jesus Souza",
                    "ch": 40
                },
                {
                    "nome": "Jamile Rodrigues Ribeiro",
                    "ch": 40
                },
                {
                    "nome": "Jucimere Correia dos Santos",
                    "ch": 40
                },
                {
                    "nome": "Kamilly Oliveira Santos",
                    "ch": 40
                },
                {
                    "nome": "Karoline Ribeiro dos Santos",
                    "ch": 40
                },
                {
                    "nome": "Magdalia Oliveira de Jesus",
                    "ch": 40
                },
                {
                    "nome": "Manuela Barbosa de Santana",
                    "ch": 40
                },
                {
                    "nome": "Pedrina de Jesus do Amparo",
                    "ch": 40
                },
                {
                    "nome": "Rozeli Sousa Santos",
                    "ch": 40
                },
                {
                    "nome": "Simone Sena Santos",
                    "ch": 40
                },
                {
                    "nome": "Tainara Souza dos Santos",
                    "ch": 40
                },
                {
                    "nome": "Victoria de Moreira Farias",
                    "ch": 40
                }
            ],
            "auxiliares_infraestrutura_escolar": [
                {
                    "nome": "Adriana dos Santos Souza Menezes",
                    "ch": 40
                },
                {
                    "nome": "Ana Paula Severino da Silva",
                    "ch": 40
                },
                {
                    "nome": "Diana Almeida Nascimento",
                    "ch": 40
                },
                {
                    "nome": "Eliete Nardes dos Santos e Santos",
                    "ch": 40
                },
                {
                    "nome": "Karen Kettilen Santos da Silva",
                    "ch": 40
                },
                {
                    "nome": "Lais Santana Souza",
                    "ch": 40
                },
                {
                    "nome": "Rosinelia das Neves Gomes",
                    "ch": 40
                },
                {
                    "nome": "Sara Aquino dos Santos",
                    "ch": 40
                },
                {
                    "nome": "Simone Santos Silva",
                    "ch": 40
                },
                {
                    "nome": "Talita Luana Souza",
                    "ch": 40
                }
            ],
            "coordenador_pedagogico": [
                {
                    "nome": "Alani dos Santos Cardoso",
                    "ch": 40
                }
            ],
            "professores": [
                {
                    "nome": "Anivania Andrade Silva",
                    "ch": 20
                },
                {
                    "nome": "Arlete de Jesus Oliveira",
                    "ch": 20
                },
                {
                    "nome": "Camila de Jesus Andrade",
                    "ch": 20
                },
                {
                    "nome": "Daniela Nascimento dos Santos",
                    "ch": 20
                },
                {
                    "nome": "Geani Teles Bomfim",
                    "ch": 20
                },
                {
                    "nome": "Heronilda Duarte Henes Pedroza",
                    "ch": 20
                },
                {
                    "nome": "Irani dos Santos Correia",
                    "ch": 20
                },
                {
                    "nome": "Ivana Andrade Rocha",
                    "ch": 20
                },
                {
                    "nome": "Joseane Gomes dos Santos",
                    "ch": 20
                },
                {
                    "nome": "Jucilene Santos de Oliveira",
                    "ch": 20
                },
                {
                    "nome": "Mailza Oliveira de Jesus",
                    "ch": 20
                },
                {
                    "nome": "Maria de Fatima de Jesus Matos",
                    "ch": 20
                },
                {
                    "nome": "Marta Souza Silva",
                    "ch": 20
                },
                {
                    "nome": "Nevia Oliveira Ramos",
                    "ch": 20
                },
                {
                    "nome": "Rabeche da Silva Souza",
                    "ch": 20
                },
                {
                    "nome": "Rosimare dos Santos Correia",
                    "ch": 20
                }
            ],
            "secretario_escolar": [
                {
                    "nome": "Micheli Lima dos Santos",
                    "ch": 40
                }
            ],
            "vigilante_escolar": [
                {
                    "nome": "Antonio Carlos Barbosa de Souza",
                    "ch": 40
                },
                {
                    "nome": "Braz Nardes dos Santos",
                    "ch": 40
                },
                {
                    "nome": "Gilvan Santos Araujo",
                    "ch": 40
                },
                {
                    "nome": "Jailson dos Santos Souza",
                    "ch": 40
                }
            ]
        }
    },
    {
        "escola": "Escola Menandro Minahim",
        "equipe_gestora": {
            "diretor": "Marcia Silene Silva Menezes Almeida",
            "vice_diretor": "Cleide Lopes de Almeida Di Gregório",
            "coordenador": "Vanessa Bonkoski dos Santos",
            "secretario_escolar": "Lady Jane Pereira Araujo"
        },
        "servidores_efetivos": {
            "docentes": [
                {
                    "nome": "Cleide Lopes de Almeida Di Gregório",
                    "ch": None,
                    "observacoes": "Vice Diretora"
                },
                {
                    "nome": "Daniela Almeida da Silva Andrade",
                    "ch": 20,
                    "observacoes": None
                },
                {
                    "nome": "Girlandia Neves de Souza",
                    "ch": 20,
                    "observacoes": "Remoção provisória"
                },
                {
                    "nome": "Ithana Dayse Alves Santos",
                    "ch": 20,
                    "observacoes": "Remoção provisória"
                },
                {
                    "nome": "Joalce Jesus dos Santos Albino",
                    "ch": 20,
                    "observacoes": "Vice CET"
                },
                {
                    "nome": "Leda Barreto Santos Reis",
                    "ch": 20,
                    "observacoes": "Mestrado"
                },
                {
                    "nome": "Marcia Silene Silva Menezes Almeida",
                    "ch": 20,
                    "observacoes": "Diretora"
                },
                {
                    "nome": "Miriam Santiago da Hora",
                    "ch": 20,
                    "observacoes": "Diretora CET"
                },
                {
                    "nome": "Rosenilda Silva Santos",
                    "ch": 40,
                    "observacoes": "Remoção provisória"
                },
                {
                    "nome": "Sueli Maria Bomfim de Andrade",
                    "ch": 40,
                    "observacoes": "Readaptada CET"
                },
                {
                    "nome": "Tania Braga Santos",
                    "ch": 20,
                    "observacoes": "Remoção Temporária"
                }
            ],
            "professor_desdobrado": [
                {
                    "nome": "Daniela Almeida da Silva Andrade",
                    "ch": 20
                },
                {
                    "nome": "Girlandia Neves de Souza",
                    "ch": 20
                }
            ],
            "coordenadora_pedagogica": [
                {
                    "nome": "Leda Barreto Santos Reis",
                    "ch": 20,
                    "observacoes": "Mestrado"
                }
            ],
            "secretario_escolar": [
                {
                    "nome": "Lady Jane Pereira Araujo",
                    "ch": 40,
                    "observacoes": "Lic. sem vencimento"
                }
            ],
            "vigilantes": [
                {
                    "nome": "Givanildo Lopes de Jesus",
                    "ch": 44,
                    "observacoes": "Noturno"
                },
                {
                    "nome": "Jose Roberto Mira Lopes",
                    "ch": 44,
                    "observacoes": "Noturno"
                }
            ],
            "atendente_de_classe": [
                {
                    "nome": "Joelma Almeida Santos Alves",
                    "ch": None
                }
            ],
            "aux_servico_escolar": [
                {
                    "nome": "Albert de Sousa Silva",
                    "ch": 30,
                    "observacoes": "Portaria"
                },
                {
                    "nome": "Edileusa Silva dos Santos",
                    "ch": 30
                },
                {
                    "nome": "Edla Novais dos Santos",
                    "ch": 30
                },
                {
                    "nome": "Ivan Santos Araújo",
                    "ch": 30,
                    "observacoes": "Portaria"
                },
                {
                    "nome": "Jurandi Jafé Sousa Barbosa",
                    "ch": 30
                },
                {
                    "nome": "Olival Gonçalves da Silva",
                    "ch": 30
                },
                {
                    "nome": "Vera Lucia Souza Santos",
                    "ch": 30
                },
                {
                    "nome": "Viviane Andrade Santos",
                    "ch": 30
                }
            ],
            "funcionaria_cedida_pela_infra": [
                {
                    "nome": "Agnalva Oliveira Silva",
                    "ch": 40
                }
            ]
        },
        "servidores_contratados": {
            "profissional_de_apoio": [
                {
                    "nome": "Aliane Silva Coelho",
                    "ch": 40,
                    "funcao": "Profissional de Apoio à alunos com deficiência"
                },
                {
                    "nome": "Anderson dos Santos Vasconcelos",
                    "ch": 40,
                    "funcao": "Profissional de Apoio à alunos com deficiência"
                },
                {
                    "nome": "Roseli Silva Santos",
                    "ch": 40,
                    "funcao": "Profissional de Apoio à alunos com deficiência"
                },
                {
                    "nome": "Vanderleia Santos Sena",
                    "ch": 40,
                    "funcao": "Profissional de Apoio à alunos com deficiência"
                }
            ],
            "auxiliar_infraestrutura_escolar": [
                {
                    "nome": "Angela Oliveira da Cruz",
                    "ch": 40
                },
                {
                    "nome": "Eliane Brandao Santos",
                    "ch": 40
                },
                {
                    "nome": "Mariana Santos Almeida",
                    "ch": 40
                },
                {
                    "nome": "Rosimary dos Santos",
                    "ch": 40
                }
            ],
            "coordenador_pedagogico": [
                {
                    "nome": "Vanessa Bonkoski dos Santos",
                    "ch": 20
                }
            ],
            "professores": [
                {
                    "nome": "Anadalva Bispo Oliveira",
                    "ch": 20
                },
                {
                    "nome": "Marineide Bastos Santos",
                    "ch": 20
                },
                {
                    "nome": "Marli dos Santos Almeida Lima",
                    "ch": 20
                },
                {
                    "nome": "Tatiana Rodrigues N. de Almeida",
                    "ch": 20
                }
            ]
        }
    },
    {
        "escola": "Escola Monteiro Lobato",
        "equipe_gestora": {
            "diretor": "Ana Neta Sampaio de Jesus",
            "vice_diretor": [
                "Marivaldo Silva",
                "Ramon Silva Trindade"
            ],
            "coordenador": "Ivana Patrícia S. de Almeida",
            "secretario_escolar": "Daniel Santos Fonseca",
            "assistente_administrativo": "Maria Edineia Lima da Silva"
        },
        "servidores_efetivos": {
            "docentes": [
                {
                    "nome": "Afrânio Jesus Passos",
                    "ch": 20
                },
                {
                    "nome": "Ana Neta Sampaio de Jesus",
                    "ch": 20,
                    "observacoes": "Diretora"
                },
                {
                    "nome": "Ana Valéria Pereira",
                    "ch": 20,
                    "observacoes": "Núcleo"
                },
                {
                    "nome": "Barbara Ferreira S. Silva",
                    "ch": 20,
                    "observacoes": "Remoção Provisória"
                },
                {
                    "nome": "Edilton Andrade Santos",
                    "ch": 20
                },
                {
                    "nome": "Evely Larissa Moreira Cavalcante",
                    "ch": 20,
                    "observacoes": "Sede do município"
                },
                {
                    "nome": "Isolda Santos Sena",
                    "ch": 20,
                    "observacoes": "Sede do município"
                },
                {
                    "nome": "Ivanil Geralda Maia Pereira",
                    "ch": 20
                },
                {
                    "nome": "Jackeline Ferreira de Jesus",
                    "ch": 20
                },
                {
                    "nome": "Janete Ferreira Santos",
                    "ch": 20,
                    "observacoes": "Remoção Provisória"
                },
                {
                    "nome": "Joana D’Arc Menezes Trindade",
                    "ch": 20,
                    "observacoes": "Sede do município"
                },
                {
                    "nome": "Joanita Santos Porto",
                    "ch": 20
                },
                {
                    "nome": "Lanusse Moreira Cavalcante",
                    "ch": 20,
                    "observacoes": "Sede do município"
                },
                {
                    "nome": "Malena Gonçalves dos Santos",
                    "ch": 20,
                    "observacoes": "Sede do município"
                },
                {
                    "nome": "Maria Anízia Ferreira Santos",
                    "ch": 20,
                    "observacoes": "INSS"
                },
                {
                    "nome": "Marivaldo Silva Santos",
                    "ch": 20,
                    "observacoes": "Vice Diretor"
                },
                {
                    "nome": "Maria das Graças Ramos de Novaes",
                    "ch": 20,
                    "observacoes": "Núcleo"
                },
                {
                    "nome": "Murilo Silva Santos",
                    "ch": 20
                },
                {
                    "nome": "Ramon Silva Trindade",
                    "ch": 20
                },
                {
                    "nome": "Regina Celi S. de Souza",
                    "ch": 20,
                    "observacoes": "Remoção Provisória"
                },
                {
                    "nome": "Roberto Santos Amorim",
                    "ch": 20
                },
                {
                    "nome": "Silenildo Lima Souza",
                    "ch": 20
                },
                {
                    "nome": "Silvia Leticia Santos da Silva",
                    "ch": 20
                }
            ],
            "solicitacao_desdobramento": [
                {
                    "nome": "Ivanil Geralda Maia Pereira",
                    "ch": 20
                },
                {
                    "nome": "Marivaldo Silva Santos",
                    "ch": 20
                },
                {
                    "nome": "Ramon Silva Trindade",
                    "ch": 20
                },
                {
                    "nome": "Silvia Leticia Santos da Silva",
                    "ch": 20
                },
                {
                    "nome": "Joanita Santos Porto",
                    "ch": 20
                }
            ],
            "vigilante": [
                {
                    "nome": "Josafá Ribeiro Pereira",
                    "ch": 44
                }
            ],
            "aux_servico_escolar": [
                {
                    "nome": "Beatriz Pereira Andrade",
                    "ch": 30
                },
                {
                    "nome": "Carine Santos Barreto",
                    "ch": 30
                },
                {
                    "nome": "Edileuza Alves dos Santos",
                    "ch": 30
                },
                {
                    "nome": "Enizaldete Uhl dos Santos",
                    "ch": 30
                },
                {
                    "nome": "Luzinete Rocha Santos",
                    "ch": 30
                },
                {
                    "nome": "Marcos Santos Pereirta",
                    "ch": 30
                },
                {
                    "nome": "Neila Ribeiro de Sena Uhl",
                    "ch": 30
                },
                {
                    "nome": "Railda da Silva Matos",
                    "ch": 30
                },
                {
                    "nome": "Samuel dos Santos Nascimento",
                    "ch": 30
                },
                {
                    "nome": "Sandra Carmo da Silva",
                    "ch": 30
                }
            ]
        },
        "servidores_contratados": {
            "assistente_administrativo": [
                {
                    "nome": "Maria Edineia Lima da Silva",
                    "ch": 40
                }
            ],
            "profissional_apoio_deficiencia": [
                {
                    "nome": "Elaine Santos Silva do Carmo",
                    "ch": 40
                },
                {
                    "nome": "Katiele dos Santos Brito",
                    "ch": 40
                },
                {
                    "nome": "Lorrany Vitoria Santos de Jesus",
                    "ch": 40
                },
                {
                    "nome": "Thaina Santos Bispo",
                    "ch": 40
                }
            ],
            "auxiliar_infraestrutura_escolar": [
                {
                    "nome": "Alcione Cardoso dos Santos",
                    "ch": 40
                },
                {
                    "nome": "Edenilda Ribeiro dos Reis",
                    "ch": 40
                },
                {
                    "nome": "Edneuza de Jesus Pereira dos Santos",
                    "ch": 40
                },
                {
                    "nome": "Ricardo Amorim Rocha",
                    "ch": 40
                }
            ],
            "coordenador_pedagogico": [
                {
                    "nome": "Ivana Patricia Santana de Almeida",
                    "ch": 20
                }
            ],
            "professores": [
                {
                    "nome": "Derivania de Sousa Trindade",
                    "ch": 20
                },
                {
                    "nome": "Elayne Uhl Andrade",
                    "ch": 20
                },
                {
                    "nome": "Eliane Teixeira Batista",
                    "ch": 20
                },
                {
                    "nome": "Elisangela Pereira Soares",
                    "ch": 20
                },
                {
                    "nome": "Geisa Sousa Silva Oliveira",
                    "ch": 20
                },
                {
                    "nome": "Juliana Ramos dos Santos Barreto",
                    "ch": 20
                },
                {
                    "nome": "Leda Santos de Jesus",
                    "ch": 20
                },
                {
                    "nome": "Luana Souza Santos",
                    "ch": 20
                },
                {
                    "nome": "Lucicleide Rodrigues Arruda",
                    "ch": 20
                },
                {
                    "nome": "Neilma Santos Silva de Almeida",
                    "ch": 20
                },
                {
                    "nome": "Silvana Rocha Santos",
                    "ch": 20
                }
            ],
            "secretario_escolar": [
                {
                    "nome": "Daniel Santos Fonseca",
                    "ch": 40
                }
            ],
            "vigilante_escolar": [
                {
                    "nome": "Alison Silva dos Santos",
                    "ch": 40
                },
                {
                    "nome": "Ivanildo de Souza Santos",
                    "ch": 40
                },
                {
                    "nome": "Jurandy Mota Pereira",
                    "ch": 40
                }
            ]
        }
    },
    {
        "document": {
            "company": "JGS NEMAS",
            "municipality": "Prefeitura Municipal de Jaguaquara/BA",
            "auction": {
                "type": "Pregão Eletrônico",
                "number": "007/2024"
            },
            "bank_info": {
                "name": "Banco do Brasil",
                "id": "1041412"
            },
            "items": [
                {
                    "item": 1,
                    "description": "Recarga de Tonner Brother 200 gr",
                    "unit": "UND",
                    "quantity": 349,
                    "unit_price": "R$ 49,44",
                    "total_price": "R$ 17.254,56",
                    "brand": "PRÓPRIA"
                },
                {
                    "item": 2,
                    "description": "Recarga de Tonner Brother 125 gr",
                    "unit": "UND",
                    "quantity": 369,
                    "unit_price": "R$ 45,50",
                    "total_price": "R$ 16.789,50",
                    "brand": "PRÓPRIA"
                },
                {
                    "item": 3,
                    "description": "Recarga de Tonner HP 70 gr",
                    "unit": "UND",
                    "quantity": 245,
                    "unit_price": "R$ 42,20",
                    "total_price": "R$ 10.339,00",
                    "brand": "PRÓPRIA"
                },
                {
                    "item": 4,
                    "description": "Recarga de Tonner HP 100 gr",
                    "unit": "UND",
                    "quantity": 338,
                    "unit_price": "R$ 45,10",
                    "total_price": "R$ 15.243,80",
                    "brand": "PRÓPRIA"
                },
                {
                    "item": 5,
                    "description": "Recarga de Tonner HP 600 gr",
                    "unit": "UND",
                    "quantity": 359,
                    "unit_price": "R$ 84,00",
                    "total_price": "R$ 30.156,00",
                    "brand": "PRÓPRIA"
                },
                {
                    "item": 6,
                    "description": "Recarga de Tonner HP 150 gr",
                    "unit": "UND",
                    "quantity": 208,
                    "unit_price": "R$ 58,00",
                    "total_price": "R$ 12.064,00",
                    "brand": "PRÓPRIA"
                },
                {
                    "item": 7,
                    "description": "Recarga Tinta Collor (3x2 ml)",
                    "unit": "UND",
                    "quantity": 25,
                    "unit_price": "R$ 12,99",
                    "total_price": "R$ 324,75",
                    "brand": "PRÓPRIA"
                },
                {
                    "item": 8,
                    "description": "Recarga Kioera 400gr",
                    "unit": "UND",
                    "quantity": 239,
                    "unit_price": "R$ 84,00",
                    "total_price": "R$ 20.076,00",
                    "brand": "PRÓPRIA"
                },
                {
                    "item": 9,
                    "description": "Recarga Tinta Collor (3 ml)",
                    "unit": "UND",
                    "quantity": 27,
                    "unit_price": "R$ 14,97",
                    "total_price": "R$ 404,19",
                    "brand": "PRÓPRIA"
                },
                {
                    "item": 10,
                    "description": "Recarga OKI com chip 200gr",
                    "unit": "UND",
                    "quantity": 76,
                    "unit_price": "R$ 123,00",
                    "total_price": "R$ 9.348,00",
                    "brand": "PRÓPRIA"
                }
            ],
            "total_amount": "R$ 131.999,80",
            "validity": {
                "proposal_days": 60,
                "delivery_time": "De acordo com o edital"
            },
            "bank_details": {
                "bank": "Banco Caixa Econômica Federal",
                "agency": "0070",
                "account": {
                    "number": "6987-2",
                    "operation": "003"
                }
            },
            "signature": {
                "date": "Itabuna/BA 05 de abril 2024",
                "signed_by": "Hercinês Dias dos Anjos"
            }
        }
    },
    {
        "escolas_nucleadas": {
            "equipe_gestora": {
                "diretor": "Ana Paula de Freitas",
                "vice_diretor": [
                    "Fernanda Xavier dos S. Almeida",
                    "Rosemery Costa S. da Purificação"
                ],
                "coordenador": [
                    "Gilcilea Marinho Peixoto",
                    "Aline Santos Aragão"
                ],
                "secretario_escolar": "Elaine Costa Lopes"
            },
            "servidores_efetivos": [
                {
                    "escola": "Alirio Santos Souza",
                    "docente": "Virginia Silva Santos",
                    "ch": 20,
                    "observacoes": "Sede"
                },
                {
                    "escola": "Dom Sebastião Leme",
                    "docente": "Barbara Ferreira Santos Silva",
                    "ch": 20,
                    "observacoes": "Monteiro"
                },
                {
                    "escola": "Dom Sebastião Leme",
                    "docente": "Mª Conceição dos S. Ribeiro Reis",
                    "ch": 20,
                    "observacoes": "Sede"
                },
                {
                    "escola": "Dom Sebastião Leme",
                    "docente": "Alex Moreira dos Santos",
                    "ch": 20,
                    "observacoes": "ok"
                },
                {
                    "escola": "Estrelinha",
                    "docente": "Janete Ferreira dos Santos",
                    "ch": 20,
                    "observacoes": "Monteiro"
                },
                {
                    "escola": "Frei Mariano de Inhambupe",
                    "docente": "Regina Celi Santos de Souza",
                    "ch": 20,
                    "observacoes": "Monteiro"
                },
                {
                    "escola": "Frei Mariano de Inhambupe",
                    "docente": "Mª das Graças R. Novais",
                    "ch": None,
                    "observacoes": "Remoção provisória"
                },
                {
                    "escola": "Gloria Barreto",
                    "docente": "Ana Célia Pereira de Oliveira",
                    "ch": 20,
                    "observacoes": "Sede"
                },
                {
                    "escola": "Idalina Andrade",
                    "docente": "Elania Barreto da Silva",
                    "ch": 20,
                    "observacoes": "Entroncamento"
                },
                {
                    "escola": "Ipiranga",
                    "docente": "Jusciane Moraes dos Santos",
                    "ch": 20,
                    "observacoes": "Sede"
                },
                {
                    "escola": "Italo Rabelo do Amaral",
                    "docente": "Maria Aparecida de Jesus Santos",
                    "ch": 20,
                    "observacoes": "Sede"
                },
                {
                    "escola": "José Inácio Pinto",
                    "docente": "Soraia Pereira dos Santos",
                    "ch": 20,
                    "observacoes": "Sede"
                },
                {
                    "escola": "José Raimundo Damasceno",
                    "docente": "Maria de Lourdes Soares Souza",
                    "ch": 20,
                    "observacoes": ""
                },
                {
                    "escola": "São Bento",
                    "docente": "Cleide Lopes de Almeida",
                    "ch": 20,
                    "observacoes": "Sede"
                }
            ],
            "desdobramentos": [
                {
                    "docente": "Alirio Santos Souza",
                    "observacoes": "Rosimery Costa S. da Purificação, 20h, Vice Diretora"
                },
                {
                    "docente": "Osvaldo Cruz",
                    "observacoes": "Fernanda Xavier dos S. Almeida, 20h, Vice Diretora"
                },
                {
                    "docente": "Dom Sebastião Leme",
                    "observacoes": "Alex Moreira dos Santos, 20h"
                },
                {
                    "docente": "Gilcilea Marinho Peixoto",
                    "observacoes": "20h, Coordenadora"
                }
            ],
            "servidores_contratados": [
                {
                    "funcionario": "Leilane Silva Lima",
                    "ch": 40,
                    "funcao": "Atendente de Classe",
                    "escola": "José Raimundo/Alírio",
                    "observacoes": ""
                },
                {
                    "funcionario": "Adrielle dos Santos Menezes",
                    "ch": 20,
                    "funcao": "Professor",
                    "escola": "Pedro Avelino",
                    "observacoes": ""
                },
                {
                    "funcionario": "Daiana Santos da Silva",
                    "ch": 20,
                    "funcao": "Professor",
                    "escola": "São Bento",
                    "observacoes": ""
                },
                {
                    "funcionario": "Eliana Ramos dos Santos",
                    "ch": 20,
                    "funcao": "Professor",
                    "escola": "Idalina Andrade",
                    "observacoes": ""
                },
                {
                    "funcionario": "Jossélia dos Santos Silva",
                    "ch": 20,
                    "funcao": "Professor",
                    "escola": "Santa Luzia",
                    "observacoes": ""
                },
                {
                    "funcionario": "Renata Isabel dos Santos",
                    "ch": 20,
                    "funcao": "Professor",
                    "escola": "Valdemar José de Queiroz",
                    "observacoes": ""
                }
            ]
        }
    },
    {
        "escola_rural_de_ipiuna": {
            "equipe_gestora": {
                "diretor": "Gorete Miranda dos Santos",
                "vice_diretor": [
                    "Maria Sonia Costa Lima",
                    "Miralva da Silva Santos"
                ],
                "coordenador": [
                    "Leila Cristina de Souza Costa Barreto",
                    "Marli S. Andrade"
                ],
                "secretario_escolar": "Carlos Alberto Marques Nascimento",
                "assistente_administrativo": "Elane Santana Santos"
            },
            "servidores_efetivos": [
                {
                    "docente": "Amarildo de Sousa Teixeira",
                    "ch": 20,
                    "observacoes": "SMED/UPT"
                },
                {
                    "docente": "Ana Lucia da Costa Lima",
                    "ch": 20,
                    "observacoes": ""
                },
                {
                    "docente": "Daiani da Costa Amaral",
                    "ch": 20,
                    "observacoes": ""
                },
                {
                    "docente": "Debora da Silva Porto",
                    "ch": 20,
                    "observacoes": "Itiruçu/Permuta"
                },
                {
                    "docente": "Gorete Miranda dos Santos",
                    "ch": 20,
                    "observacoes": "Diretora"
                },
                {
                    "docente": "Hemilena Bastos de Santana",
                    "ch": "20/20",
                    "observacoes": "Readaptada"
                },
                {
                    "docente": "Iany Caroline Melo de Souza",
                    "ch": 20,
                    "observacoes": "Mestrado"
                },
                {
                    "docente": "Indiara da Silva Pereira",
                    "ch": 20,
                    "observacoes": "Luzia Silva"
                },
                {
                    "docente": "Jocilene Santos Portugal",
                    "ch": "20/20",
                    "observacoes": ""
                },
                {
                    "docente": "Keila S. Borges",
                    "ch": 20,
                    "observacoes": ""
                },
                {
                    "docente": "Luciano Olímpio Rabelo",
                    "ch": 20,
                    "observacoes": ""
                },
                {
                    "docente": "Marcia de Almeida Correia",
                    "ch": 20,
                    "observacoes": "Readaptada Luzia Silva"
                },
                {
                    "docente": "Maria Gorete Ferreira Santos",
                    "ch": "20/20",
                    "observacoes": ""
                },
                {
                    "docente": "Maria Sônia Costa Lima",
                    "ch": 40,
                    "observacoes": "20 vice"
                },
                {
                    "docente": "Miralva da Silva Santos",
                    "ch": 20,
                    "observacoes": "Vice-Diretora"
                },
                {
                    "docente": "Rosenildo dos Santos Piropo",
                    "ch": 40,
                    "observacoes": "Afastado"
                },
                {
                    "docente": "Rossilva Nascimento dos Santos",
                    "ch": 40,
                    "observacoes": ""
                },
                {
                    "docente": "Roziane Sousa de Almeida",
                    "ch": 20,
                    "observacoes": "Lomanto Jr"
                },
                {
                    "docente": "Tamandaré Gandhi Piropo",
                    "ch": 20,
                    "observacoes": "Luzia Silva"
                },
                {
                    "docente": "Thayse Santos Dattoli",
                    "ch": 20,
                    "observacoes": "Sede"
                },
                {
                    "docente": "Vécio Luiz L. Lima",
                    "ch": 20,
                    "observacoes": "Diana"
                },
                {
                    "docente": "Viviane Pereira Santos",
                    "ch": "20/20",
                    "observacoes": "CME"
                }
            ],
            "professor_desdobrado": [
                {
                    "docente": "Luciano Olímpio Rabelo",
                    "ch": 20
                },
                {
                    "docente": "Miralva da Silva Santos",
                    "ch": 20
                }
            ],
            "coordenadora_pedagogica": {
                "nome": "Leila Cristina de Souza Costa Barreto",
                "ch": 40
            },
            "secretario_escolar": {
                "nome": "Carlos Alberto Marques Nascimento",
                "ch": 40
            },
            "vigilantes": [
                {
                    "nome": "Givanildo Braga dos Santos",
                    "ch": 40
                }
            ],
            "aux_infraestrutura_escolar": [
                {
                    "nome": "Edvânia Fernandes Brandão",
                    "ch": 30,
                    "observacoes": "Readaptada"
                },
                {
                    "nome": "Franciara Fonseca Alves",
                    "ch": 30
                },
                {
                    "nome": "Helena de Souza Santos",
                    "ch": 30,
                    "observacoes": "Merendeira"
                },
                {
                    "nome": "Solange Coelho Oliveira",
                    "ch": 30
                }
            ],
            "servidores_contratados": {
                "atendentes_de_classe": [
                    {
                        "nome": "Natane Brandão Santana",
                        "ch": 40
                    }
                ],
                "aux_alimentacao_escolar": [
                    {
                        "nome": "Alielza de Jesus Palma Brito",
                        "ch": 40
                    },
                    {
                        "nome": "Juliana Franca dos Santos",
                        "ch": 40
                    }
                ],
                "professores_regentes": [
                    {
                        "nome": "Conceição de O. Deodato Leal",
                        "ch": 20
                    },
                    {
                        "nome": "Daiana Brito de Jesus",
                        "ch": 20
                    },
                    {
                        "nome": "Eriene Pereira Ribeiro",
                        "ch": 20
                    },
                    {
                        "nome": "Irandir Santos Aragão",
                        "ch": 20
                    },
                    {
                        "nome": "Ivonice Coelho R. de Jesus",
                        "ch": 20
                    },
                    {
                        "nome": "Juliana Santos de Matos",
                        "ch": 20
                    },
                    {
                        "nome": "Jurema Ribeiro de Sena",
                        "ch": 20
                    },
                    {
                        "nome": "Katia Bastos Oliveira",
                        "ch": 20
                    },
                    {
                        "nome": "Lana Coelho dos S. Marinho",
                        "ch": 20
                    },
                    {
                        "nome": "Leiliane Rocha Andrade",
                        "ch": 20
                    },
                    {
                        "nome": "Luzinete Santos de Jesus",
                        "ch": 20
                    },
                    {
                        "nome": "Magnolia Lima Barreto",
                        "ch": 20
                    },
                    {
                        "nome": "Samia Lima Alves",
                        "ch": 20
                    },
                    {
                        "nome": "Sara Palma Brito",
                        "ch": 20
                    },
                    {
                        "nome": "Vivia Carla M. das Mercês",
                        "ch": 20
                    }
                ],
                "profissionais_de_apoio": [
                    {
                        "nome": "Cleidineia Santos Pereira",
                        "ch": 40,
                        "funcao": "Profissional de Apoio à alunos com deficiência"
                    },
                    {
                        "nome": "Silvana Silva Brandao",
                        "ch": 40,
                        "funcao": "Profissional de Apoio à aluno com deficiência"
                    },
                    {
                        "nome": "Taislane de Jesus Coelho",
                        "ch": 40,
                        "funcao": "Profissional de Apoio à aluno com deficiência"
                    }
                ],
                "servicos_gerais": [
                    {
                        "nome": "Daiane Mendes da Silva",
                        "ch": 40
                    },
                    {
                        "nome": "Geisa Palma Moraes",
                        "ch": 40
                    },
                    {
                        "nome": "Gilvania Sousa dos Santos",
                        "ch": 40
                    },
                    {
                        "nome": "Henrique Brito Bispo",
                        "ch": 40
                    },
                    {
                        "nome": "Jacilvania de O. Santos Evaristo",
                        "ch": 40
                    }
                ],
                "vigilantes": [
                    {
                        "nome": "Adenilton Gomes dos Santos",
                        "ch": 40,
                        "turno": "Diurno"
                    },
                    {
                        "nome": "Jose Paulo de Sousa",
                        "ch": 40,
                        "turno": "Noturno"
                    }
                ]
            }
        }
    },
    {
        "escola_stela_camara_dubois": {
            "equipe_gestora": {
                "diretor": "Vanusa Ferreira Pirôpo",
                "vice_diretor": [
                    "Marcia Santos Miranda",
                    "Rosilene Alves Matos"
                ],
                "coordenador": [
                    "Robeleide Cintra Souza Silva",
                    "Lucas Colangeli de Souza"
                ],
                "secretario": "Nilton Bastos de Santana",
                "assistente_administrativo": "Tyana Gonçalves dos Santos"
            },
            "servidores_efetivos": [
                {
                    "docente": "Andreya Costa Soares e Sousa",
                    "ch": 20,
                    "observacoes": ""
                },
                {
                    "docente": "Cristina Lima Sousa",
                    "ch": 40,
                    "observacoes": ""
                },
                {
                    "docente": "Cristina Sousa Nascimento",
                    "ch": 40,
                    "observacoes": ""
                },
                {
                    "docente": "Edinalva Sandra de Jesus dos Santos",
                    "ch": 20,
                    "observacoes": ""
                },
                {
                    "docente": "Eliene Andrade Texeira da Hora",
                    "ch": 40,
                    "observacoes": ""
                },
                {
                    "docente": "Geovanice da Silva D’Onófrio",
                    "ch": 20,
                    "observacoes": ""
                },
                {
                    "docente": "Guadnajara Teles Barreto",
                    "ch": 20,
                    "observacoes": "Diretora Lourival"
                },
                {
                    "docente": "Katiane Castro",
                    "ch": 20,
                    "observacoes": "CET"
                },
                {
                    "docente": "Marcia Santos Miranda",
                    "ch": 20,
                    "observacoes": "Vice-Diretora"
                },
                {
                    "docente": "Milena Lima Tamboriello",
                    "ch": 20,
                    "observacoes": ""
                },
                {
                    "docente": "Nelma Oliveira Souza",
                    "ch": 20,
                    "observacoes": "Remoção Provisória"
                },
                {
                    "docente": "Núbia Andrade Ribeiro",
                    "ch": 20,
                    "observacoes": "Readaptada"
                },
                {
                    "docente": "Patrícia Santiago Ferreira",
                    "ch": 20,
                    "observacoes": "Dotourado"
                },
                {
                    "docente": "Robeleide Cintra Souza Silva",
                    "ch": 40,
                    "observacoes": "Readaptada"
                },
                {
                    "docente": "Rosilene Alves Matos",
                    "ch": 20,
                    "observacoes": "Remoção Provisória"
                },
                {
                    "docente": "Tânia Silva Reis Sampaio",
                    "ch": 20,
                    "observacoes": ""
                },
                {
                    "docente": "Valdilene Costa Silva",
                    "ch": 40,
                    "observacoes": ""
                },
                {
                    "docente": "Valdir dos Santos",
                    "ch": 20,
                    "observacoes": "SMED"
                },
                {
                    "docente": "Vanusa Ferreira Piropô",
                    "ch": 40,
                    "observacoes": "Diretora"
                },
                {
                    "docente": "Virginia Silva Santos",
                    "ch": 20,
                    "observacoes": "Remoção Provisória"
                }
            ],
            "professor_desdobrado": [
                {
                    "docente": "Rosilene Alves Matos",
                    "ch": 20
                },
                {
                    "docente": "Nelma Oliveira Souza",
                    "ch": 20
                }
            ],
            "coordenadora_pedagogica": [
                {
                    "nome": "Rita de Cássia da Silva Trindade Santos",
                    "ch": 20,
                    "observacoes": "SMED"
                },
                {
                    "nome": "Robeleide Cintra Souza Silva",
                    "ch": 20
                }
            ],
            "secretario_escolar": {
                "nome": "Nilton Bastos de Santana"
            },
            "vigilantes": [
                {
                    "nome": "Ivan Jesus dos Santos",
                    "ch": 40
                },
                {
                    "nome": "Josevaldo Procopio de Santana",
                    "ch": 40
                }
            ],
            "atendentes_de_classe": [
                {
                    "nome": "Carina de Jesus Conceição",
                    "ch": 40
                },
                {
                    "nome": "Edinelia dos Santos Oliveira",
                    "ch": 40
                },
                {
                    "nome": "Liliane Santana Couto",
                    "ch": 40
                },
                {
                    "nome": "Liliane Barbosa Cardoso",
                    "ch": 40,
                    "observacoes": "Remoção Provisória"
                }
            ],
            "aux_servico_escolar": [
                {
                    "nome": "Ana Marcia Vieira dos Santos",
                    "ch": 30
                },
                {
                    "nome": "Antonia Silva Santos",
                    "ch": 30
                },
                {
                    "nome": "Irani Santos Araújo",
                    "ch": 30
                },
                {
                    "nome": "Jamille Nascimento de Souza",
                    "ch": 30,
                    "observacoes": "Readaptada"
                },
                {
                    "nome": "Janete da Silva Souza",
                    "ch": 30
                },
                {
                    "nome": "Jeane Teixeira dos Santos",
                    "ch": 30
                },
                {
                    "nome": "Juciara Macedo Nascimento",
                    "ch": 30,
                    "observacoes": "Readaptada"
                },
                {
                    "nome": "Valdicélia dos Santos",
                    "ch": 30,
                    "observacoes": "INSS"
                },
                {
                    "nome": "Viviane das Mercês Aprigio",
                    "ch": 30,
                    "observacoes": "SMED"
                },
                {
                    "nome": "Cristovaldo Sousa Nascimento",
                    "ch": 40,
                    "observacoes": "Eraldo Tinoco (Vigilante)"
                }
            ],
            "servidores_contratados": {
                "assistente_administrativo": [
                    {
                        "nome": "Tyana Goncalves Dos Santos",
                        "ch": 40
                    }
                ],
                "atendentes_de_classe": [
                    {
                        "nome": "Liliane Das Merces Santos",
                        "ch": 40
                    },
                    {
                        "nome": "Nivea Sousa Rezende",
                        "ch": 40
                    },
                    {
                        "nome": "Tainara Cardoso Santos",
                        "ch": 40
                    }
                ],
                "auxiliares_de_infraestrutura": [
                    {
                        "nome": "Antonia de Jesus Santos",
                        "ch": 40
                    },
                    {
                        "nome": "Etan Ferreira Bastos",
                        "ch": 40
                    },
                    {
                        "nome": "Keli Viana Souza",
                        "ch": 40
                    },
                    {
                        "nome": "Noelia Martins Santos de Sena",
                        "ch": 40
                    },
                    {
                        "nome": "Terezinha da Silva Santos",
                        "ch": 40
                    },
                    {
                        "nome": "Vera Lucia Moraes",
                        "ch": 40
                    },
                    {
                        "nome": "Veronice Martins dos Santos",
                        "ch": 40
                    },
                    {
                        "nome": "Ziran dos Santos",
                        "ch": 40
                    }
                ],
                "coordenador_pedagogico": {
                    "nome": "Lucas Colangeli de Souza",
                    "ch": 20
                },
                "professores_regentes": [
                    {
                        "nome": "Ana Paula N. da Silva",
                        "ch": 20
                    },
                    {
                        "nome": "Jairo da Silva Bonfim",
                        "ch": 20
                    },
                    {
                        "nome": "Jusandra da Silva Lima",
                        "ch": 20
                    },
                    {
                        "nome": "Larissa Guirre Souza",
                        "ch": 20
                    },
                    {
                        "nome": "Marilan de Souza Santos",
                        "ch": 20
                    },
                    {
                        "nome": "Maryvane Araujo Barbosa",
                        "ch": 20
                    },
                    {
                        "nome": "Naiara B. da Ressurreição",
                        "ch": 20
                    },
                    {
                        "nome": "Neilan Conceição da S. Barbosa",
                        "ch": 20
                    }
                ],
                "vigilantes": [
                    {
                        "nome": "Antonio Santos Rosa",
                        "ch": 40,
                        "funcao": "Vigilante Escolar"
                    },
                    {
                        "nome": "Railton Sousa Passos",
                        "ch": 40,
                        "funcao": "Vigilante Escolar"
                    }
                ]
            }
        }
    },
    {
        "escola_terrabras": {
            "equipe_gestora": {
                "diretor": "Marilene Andrade Correia Almeida",
                "vice_diretor": "Zenilde de Souza",
                "coordenador": "Veridiana Santos de Jesus",
                "secretario_escolar": "Luciana de Jesus Santos"
            },
            "servidores_efetivos": [
                {
                    "docente": "Ana Paula M. da Silva",
                    "ch": 20,
                    "observacoes": "Everaldo"
                },
                {
                    "docente": "Nelma Oliveira Souza",
                    "ch": 20,
                    "observacoes": "Sede"
                },
                {
                    "docente": "Renilda Gomes Sampaio",
                    "ch": 20,
                    "observacoes": "Remoção Provisória"
                },
                {
                    "docente": "Sheila Souza Gonçalves",
                    "ch": 20,
                    "observacoes": "Lomanto"
                },
                {
                    "docente": "Verônica dos Santos Rebouças",
                    "ch": 20,
                    "observacoes": "Sede"
                },
                {
                    "docente": "Zenilde de Souza",
                    "ch": 20,
                    "observacoes": "Vice-Diretora"
                }
            ],
            "desdobramentos": [
                {
                    "docente": "Zenilde de Souza",
                    "ch": 20
                },
                {
                    "docente": "Renilda Gomes Sampaio",
                    "ch": 20
                }
            ],
            "vigilantes": [
                {
                    "nome": "Izac Vaniski da Silva",
                    "ch": 40
                }
            ],
            "secretario_escolar": {
                "nome": "Luciana de Jesus Santos",
                "ch": 40
            },
            "servidores_contratados": {
                "atendentes_de_classe": [
                    {
                        "nome": "Luciana Pereira Dos Santos",
                        "ch": 40
                    },
                    {
                        "nome": "Tatiane Santana Silva",
                        "ch": 40
                    }
                ],
                "auxiliares_de_infraestrutura": [
                    {
                        "nome": "Ana Lucia Bispo dos Santos",
                        "ch": 40
                    },
                    {
                        "nome": "Breno Oliveira Silva",
                        "ch": 40
                    },
                    {
                        "nome": "Cristiana Campos Ferraz",
                        "ch": 40
                    },
                    {
                        "nome": "Gutemberg Menezes dos Santos",
                        "ch": 40
                    },
                    {
                        "nome": "Sandra Santos de Jesus",
                        "ch": 40
                    },
                    {
                        "nome": "Sarah Queiroz de Oliveira",
                        "ch": 40
                    },
                    {
                        "nome": "Silvana dos Santos Cerqueira",
                        "ch": 40
                    }
                ],
                "merendeira": [
                    {
                        "nome": "Edna dos Santos Barbosa",
                        "ch": 40
                    }
                ],
                "professores_regentes": [
                    {
                        "nome": "Ana Cleude Carmo de Santana"
                    },
                    {
                        "nome": "Beatriz Alcântara de Souza"
                    },
                    {
                        "nome": "Clessia Nery Costa"
                    },
                    {
                        "nome": "Elane Santana Moreira"
                    },
                    {
                        "nome": "Karoline de Jesus Coelho"
                    },
                    {
                        "nome": "Morgana Lula Galvão Brito"
                    },
                    {
                        "nome": "Neila Silva de Oliveira"
                    },
                    {
                        "nome": "Renilda Costa de Almeida"
                    },
                    {
                        "nome": "Veridiana Santos de Jesus"
                    }
                ],
                "profissionais_apoio_deficiencia": [
                    {
                        "nome": "Barbara Ferreira dos Santos",
                        "ch": 40
                    },
                    {
                        "nome": "Daniela da A. Nascimento",
                        "ch": 40
                    },
                    {
                        "nome": "Gicelia Vieira Ferreira",
                        "ch": 40
                    },
                    {
                        "nome": "Julia dos Santos Figueredo",
                        "ch": 40
                    },
                    {
                        "nome": "Kailane dos Santos Braga",
                        "ch": 40
                    },
                    {
                        "nome": "Kailane Santos Souza Silva",
                        "ch": 40
                    },
                    {
                        "nome": "Laiane Santos Moraes",
                        "ch": 40
                    }
                ],
                "vigilantes": [
                    {
                        "nome": "Daniel Santos Silva",
                        "ch": 40,
                        "funcao": "Vigilante Diurno"
                    },
                    {
                        "nome": "Maciel Damaceno Andrade",
                        "ch": 40,
                        "funcao": "Vigilante Noturno"
                    },
                    {
                        "nome": "Moabe Araujo Silva",
                        "ch": 40,
                        "funcao": "Vigilante Diurno"
                    },
                    {
                        "nome": "Quelson Carlos O. dos Santos",
                        "ch": 40,
                        "funcao": "Vigilante Diurno"
                    },
                    {
                        "nome": "Ronildo Correia Neris",
                        "ch": 40,
                        "funcao": "Vigilante Noturno"
                    }
                ]
            }
        }
    },
    {
        "escola_vicenzo_gasbarre": {
            "equipe_gestora": {
                "diretor": "Elizete de Azevedo Pereira",
                "vice_diretor": [
                    "Eliana Costa Santos",
                    "Vilma Ferreira da Silva"
                ],
                "coordenador": [
                    "Jorge R. de Sousa",
                    "Líbia Vieira Pitalli Garcia"
                ],
                "secretario_escolar": "Jeane Sousa dos Santos",
                "assistente_administrativo": "Nilda Santos Gomes"
            },
            "servidores_efetivos": [
                {
                    "docente": "Alexandra Dias Teixeira Santos",
                    "ch": 20
                },
                {
                    "docente": "Ana Célia Pereira de Almeida",
                    "ch": 20,
                    "observacoes": "Remoção Temporária"
                },
                {
                    "docente": "Ana Selma Matos Sales",
                    "ch": 20
                },
                {
                    "docente": "Antonio de Souza Gomes",
                    "ch": 40
                },
                {
                    "docente": "Claudio dos Santos",
                    "ch": 20
                },
                {
                    "docente": "Creusa Ribeiro dos Santos",
                    "ch": "20/20"
                },
                {
                    "docente": "Eliana Costa Santos",
                    "ch": "20/20",
                    "observacoes": "20h vice"
                },
                {
                    "docente": "Eliene Santana Meira Souza",
                    "ch": 20,
                    "observacoes": "Mestrado"
                },
                {
                    "docente": "Elizete de Azevedo Pereira",
                    "ch": 40,
                    "observacoes": "Diretora"
                },
                {
                    "docente": "Geosenita Mª da Silva Bispo Nascimento",
                    "ch": 20
                },
                {
                    "docente": "Gilene Pires Ribeiro",
                    "ch": 20
                },
                {
                    "docente": "Giuliano Pablo Almeida Mendonça",
                    "ch": 20
                },
                {
                    "docente": "Ionara Souza Santos",
                    "ch": 20,
                    "observacoes": "Remoção Temporária"
                },
                {
                    "docente": "Isvanilda Almeida Santos Costa",
                    "ch": 40
                },
                {
                    "docente": "Leila Diane Teixeira Santos",
                    "ch": 20
                },
                {
                    "docente": "Luciene Pires da Silva",
                    "ch": 20
                },
                {
                    "docente": "Maisa Lima Barbosa Portugal",
                    "ch": "20/20"
                },
                {
                    "docente": "Maria da Conceição Silva Sacramento",
                    "ch": 20
                },
                {
                    "docente": "Maria das Graças Assis dos Santos",
                    "ch": 40
                },
                {
                    "docente": "Naiara de Melo Nogueira",
                    "ch": 20
                },
                {
                    "docente": "Patrícia Regina Pires de Souza Dias",
                    "ch": 20
                },
                {
                    "docente": "Solange Bispo Silva",
                    "ch": 20,
                    "observacoes": "Readaptada"
                },
                {
                    "docente": "Vana Lucia Argolo Sousa Andrade",
                    "ch": 20
                },
                {
                    "docente": "Vania Pereira",
                    "ch": 20
                },
                {
                    "docente": "Vilma Ferreira da Silva",
                    "ch": 20,
                    "observacoes": "Vice Diretora"
                }
            ],
            "desdobramentos": [
                {
                    "docente": "Alexandra Dias Teixeira Santos",
                    "ch": 20
                },
                {
                    "docente": "Claudio dos Santos",
                    "ch": 20
                },
                {
                    "docente": "Vania Pereira",
                    "ch": 20
                },
                {
                    "docente": "Vilma Ferreira da Silva",
                    "ch": 20
                }
            ],
            "coordenadores_pedagogicos": [
                {
                    "nome": "Jorge Ramos de Sousa",
                    "ch": 20
                },
                {
                    "nome": "Pedro Marques",
                    "ch": 20
                }
            ],
            "secretaria_escolar": {
                "nome": "Jeane Sousa dos Santos",
                "ch": 40
            },
            "assistente_administrativo": {
                "nome": "Nilda Santos Gomes",
                "ch": 40
            },
            "auxiliares_servico_escolar": [
                {
                    "nome": "Eurides Silva do Nascimento",
                    "ch": 30
                },
                {
                    "nome": "Fabiana Silva Santos",
                    "ch": 30
                },
                {
                    "nome": "Geisa da Silva Mota",
                    "ch": 30,
                    "observacoes": "INSS"
                },
                {
                    "nome": "Geny Souza Reis dos Santos",
                    "ch": 30
                },
                {
                    "nome": "Iracema Santana Almeida Sousa",
                    "ch": 30
                },
                {
                    "nome": "Lucinéia da Silva Cordeiro",
                    "ch": 30
                },
                {
                    "nome": "Marilene Francisca dos Santos",
                    "ch": 30
                },
                {
                    "nome": "Selma Santos Siqueira",
                    "ch": 30,
                    "observacoes": "Readaptada"
                },
                {
                    "nome": "Silvan Nunes Gonçalves",
                    "ch": 30,
                    "observacoes": "Portaria"
                },
                {
                    "nome": "Zenilda Santos Souza",
                    "ch": 30,
                    "observacoes": "INSS"
                }
            ],
            "servidores_cedidos": [
                {
                    "nome": "Ailton de Jesus Santos",
                    "ch": 40,
                    "funcao": "Vigilante Diurno"
                },
                {
                    "nome": "Edinaldo Fonseca de Jesus",
                    "ch": 40,
                    "funcao": "Vigilante Noturno"
                },
                {
                    "nome": "João Paulo S. Nascimento",
                    "ch": 40,
                    "funcao": "Gari"
                },
                {
                    "nome": "Paulino de Jesus Pereira",
                    "ch": 40,
                    "funcao": "Gari"
                },
                {
                    "nome": "Wagner Silva Nascimento",
                    "ch": 40,
                    "funcao": "Gari/Vigilante Noturno"
                }
            ],
            "servidores_contratados": {
                "profissionais_apoio_deficiencia": [
                    {
                        "nome": "Eliana Santana Barreto",
                        "ch": 40
                    },
                    {
                        "nome": "Erick Silva Borges",
                        "ch": 40
                    },
                    {
                        "nome": "Jemima Ventura Leal Dgusmao",
                        "ch": 40
                    },
                    {
                        "nome": "Maria da Paz Bispo dos Santos",
                        "ch": 40
                    }
                ],
                "auxiliares_infraestrutura": [
                    {
                        "nome": "Bruna Alexandre Santana",
                        "ch": 40
                    },
                    {
                        "nome": "Deiane da Silva Nunes",
                        "ch": 40
                    },
                    {
                        "nome": "Geovania Sousa Ramos",
                        "ch": 40
                    },
                    {
                        "nome": "Gessica Santana De Jesus",
                        "ch": 40
                    },
                    {
                        "nome": "Maria das Graças Santos Rocha",
                        "ch": 40
                    },
                    {
                        "nome": "Mickelle Santos Barbosa",
                        "ch": 40
                    },
                    {
                        "nome": "Regiane de Jesus Pereira",
                        "ch": 40
                    },
                    {
                        "nome": "Simone Almeida de Santana",
                        "ch": 40
                    }
                ],
                "coordenador_pedagogico": [
                    {
                        "nome": "Libia Vieira Pitalli Garcia",
                        "ch": 20
                    }
                ],
                "professores": [
                    {
                        "nome": "Aline Nunes Almeida",
                        "ch": 20
                    },
                    {
                        "nome": "Carla Cristina dos Santos Reis",
                        "ch": 20
                    },
                    {
                        "nome": "Edinaldo da Silva Santos",
                        "ch": 20
                    },
                    {
                        "nome": "Sarah Costa de Almeida",
                        "ch": 20
                    },
                    {
                        "nome": "Selma Oliveira da Costa",
                        "ch": 20
                    },
                    {
                        "nome": "Urania Andrade Fonseca",
                        "ch": 20
                    }
                ],
                "vigilantes": [
                    {
                        "nome": "Marcos Henrique Santos São Pedro",
                        "ch": 40,
                        "funcao": "Vigilante Escolar"
                    }
                ]
            }
        }
    }
]
   
import json

# Carregar o JSON
with open(r'C:\Users\Aux Administrativo\Documents\leob\relatorio\JSON\dados\vicenzo.json', 'r', encoding='utf-8') as file:
    dados = json.load(file)

# Função para extrair e exibir os dados
def extrair_dados(dados):
    # Nome da instituição
    escola_nome = dados.get("instituicao", "Escola não especificada")
    
    # Imprime o nome da escola uma vez
    print(f"Escola: {escola_nome}")
    
    # Lista de servidores que contêm docentes
    servidores = [
        ("servidores_efetivos", "docentes"),
        ("servidores_contratados", "professores")
    ]
    
    # Itera pelos diferentes conjuntos de servidores
    for tipo_servidor, categoria_professor in servidores:
        if tipo_servidor in dados and categoria_professor in dados[tipo_servidor]:
            for professor in dados[tipo_servidor][categoria_professor]:
                nome_professor = professor.get("nome", "Nome não especificado")
                observacoes = professor.get("observacoes", "")
                
                # Exibe apenas o nome do professor e as observações
                print(f"  Professor: {nome_professor}, Observações: {observacoes}")

# Executa a função
extrair_dados(dados)







