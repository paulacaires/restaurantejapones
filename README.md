| Request for Proposal  | Outubro de 2025 |
| ----- | :---- |
|  | Nome do projeto: Restaurante Japonês na UFSCar |
|  Restaurante Japonês na UFSCar | Cliente: Alexandre Alvaro Gerente do Projeto: Paula |
|  | **Objetivo estratégico:** Criação de um sistema para auxiliar a gestão do Restaurante Japonês da UFSCar, seguindo como base o termo de Referência para a contratação de serviços de fornecimento de refeições nos Restaurantes Universitários da Universidade Federal de São Carlos (UFSCar). |

# Objetivo do projeto

Com o objetivo de promover o bem-estar, integração cultural e a diversidade alimentar dentro da comunidade universitária, propõe-se o projeto de criação de um sistema (Software) para um Restaurante Japonês no campus da UFSCar.   
A proposta foi elaborada com base no Termo de Referência para a contratação de serviços de fornecimento de refeições nos Restaurantes Universitários da Universidade Federal de São Carlos (UFSCar), com adaptações para o cenário do problema.  
O Termo detalha itens contratados, estimativas de consumo, exigências técnicas, operacionais e sanitárias para o fornecimento de alimentações nos quatro campi, tendo em vista também o compromisso social com a comunidade, incluindo os consumidores finais e os funcionários.

# Gerenciamento do escopo

Seguindo o RFP proposto e o Termo de Referência, o escopo do projeto será:

## Composição do cardápio diário

De acordo com o Termo:  
“O serviço deve contribuir para a promoção de saúde e bem-estar da comunidade  
universitária, ao fornecer refeições nutricionalmente equilibradas e agradáveis do  
ponto de vista sensorial.” (Página 4, artigo 1.3)  
Para atingir esse objetivo, acrescentando também o contexto cultural japonês, propõe-se a elaboração de um gerenciamento de cardápio, o qual armazena as seguintes informações:

### Tabela “Cardápio”

* ID\_Cardápio  
* Dia do cardápio (Ex.: 04/10/2025)  
* Almoço Ou Janta  
* Entrada (Edamame, Sunomono, Gyoza)  
* Main Dishes | Sushi bar (Sushi ou Sashimi do dia, Temaki)  
* Main Dishes | Ramen (Yakisoba, Ramen)  
* Sobremesa (Mochi, Sorvete de Chá verde, Dorayaki)  
* Bebidas (Chá verde, Refrigerante, Suco)

Seguindo o padrão do Restaurante Universitário atual, o preço da refeição será fixo por dia, considerando clientes bolsistas ou não.

## Cliente

### Tabela “Cliente”

* ID\_Cliente  
* Nome  
* Saldo disponível  
* Categoria (0: Gratuidade, 1: Paga metade do valor estudante, 2: Paga o valor inteiro estudante, 3: Visitantes e Professores)  
* Curso

### Tabela “Consumo”

* ID\_Cliente  
* ID\_Cardápio  
* Avaliação

Com base nessas informações, é possível saber o faturamento no dia.

## Reserva de mesas

Com o objetivo de oferecer a melhor experiência para os usuários, o sistema também implementará a reserva de mesas. Isso é um diferencial em relação ao Restaurante Universitário padrão, que não oferece esse serviço.  
Essa feature está elaborada pensando em atingir as seguintes dores:  
Primeiro, o Termo estabelece que:  
“2.2.1. O tempo de espera dos usuários nas filas de acesso aos Restaurantes não  
poderá exceder 20 (vinte) minutos, inclusive nos horários de maior movimento.” (Página 70, artigo 2.2.1)  
Em segundo ponto, para cumprir o objetivo de convivência, a reserva de mesas permite que grupos maiores de acomodem de forma a permanecerem juntos mesmo em momentos de maior movimento no Restaurante.

### Tabela “Reserva de mesas”

* ID\_Reserva  
* ID\_Cliente (Responsável pela reserva)  
* Número da mesa (0-20)  
* Dia da reserva  
* Hora da reserva

### Tabela “Mesas”

* Número da mesa  
* Número de lugares

## Estoque

Em relação ao estoque, o sistema se propõe a auxiliar na disponibilidade constante para os consumidores.  
“6.3. Todos os componentes do cardápio deverão estar disponíveis em quantidades  
adequadas para servir do primeiro ao último cliente.” (Página 13, artigo 6.3)  
Porém nem sempre é possível prever o movimento no Restaurante. Por isso, a UFSCar se responsabiliza notificar o Restaurante sobre um aumento na demanda.  
“1.5. Em casos de encontros, congressos e/ou outros tipos de eventos, a demanda do restaurante pode aumentar consideravelmente (estimativamente em até 30%). Nestes casos, a UFSCar será responsável por informar o fornecedor, antecipadamente, em tempo hábil para que este possa se preparar para atender o acréscimo na demanda.” (Página 3, artigo 1.5)  
Por isso, o sistema terá um recurso que avisa quando a demanda do restaurante pode aumentar considerávelmente.  
Dessa forma, é necessário ver o cardápio do dia da notificação e conferir no estoque a disponibilidade dos alimentos propostos no dia.

### Tabela “Estoque”

* Nome do Produto  
* Categoria (Entrada, Main Dishes Sushi, Main Dishes Ramen, Sobremesa, Bebida)  
* Quantidade no estoque  
* Custo Unitário  
* Estoque Mínimo  
* ID\_Funcionário (Funcionário responsável por esse item no estoque. Deve ter a função “Estoquista”)  
* Data de validade

## Equipe de trabalho

O Termo estabelece critérios em relação à equipe de trabalho.

## Cotas sociais para funcionários

“2.1. De forma a atender as exigências de qualidade, principalmente no que tange a  
questão da sustentabilidade em sua dimensão social, e o cumprimento do dever de  
termos um contrato justo e igualitário, e que tenha um impacto positivo na sociedade, fica a empresa CONTRATADA OBRIGADA a contratar pessoas pertencentes a grupos em situação de vulnerabilidade nas quantidades mínimas definidas pela UFSCar.” (Página 48, artigo 2.1)

Seguindo essa política, o Restaurante Japonês da UFSCar se propõe:

* A quantidade mínima de pessoas que a empresa CONTRATADA deve contratar através das cotas sociais é de 10 (dez) pessoas (versus 24 previstos pelo Termo).  
* As 10 (dez) vagas deverão ser preenchidas conforme a divisão descrita a seguir:  
  * 5 vagas exclusivas para Pessoas com Deficiência;  
  * 2 vagas exclusivas para Pessoas Transgênero, Transexuais ou Travestis;  
  * 1 vagas exclusivas para Imigrantes, prioritariamente para pessoas em situação de refúgio;  
  * 1 vagas exclusivas para Pessoas em situação de rua, residentes em abrigos, casas de acolhimento ou afins;  
  * 1 vagas exclusivas para Jovens Aprendizes.

### Tabela “Funcionários”

* Nome  
* Horário (Se atua no Almoço ou na Janta)  
* Função (Cozinheiro, Nutricionista, Operador de Caixa, Auxiliar de Cozinha, Auxiliar de Serviços Gerais, Açogueiro e Estoquista)  
* Data do último exame periódico de saúde  
* Laudos  
* Campus de atuação (Sorocaba, São Carlos, Lagoa do Sino, Araras)  
* À qual grupo de cota social pertence (Null se não pertencer)

## Relatório

É responsabilidade do Restaurante Japonês da UFSCar transparência e auditoria. Para isso,  o sistema se compromete a gerar um relatório referente ao lucro, número de clientes e informações sobre os funcionários. O relatório será gerado dinamicamente.  
Ainda em relação à escopo, nesse projeto, a o banco de dados será estático, sem a implementação de operações básicas de CRUD.

# Estrutura Analítica do Projeto (EAP)

A EAP do projeto foi estruturada de forma hierárquica, permitindo a decomposição progressiva das entregas e atividades em componentes menores e mais gerenciáveis. Essa estrutura facilita a visualização do trabalho a ser executado, a definição clara das responsabilidades e o acompanhamento da evolução do projeto. Abaixo, apresenta-se a EAP organizada em níveis lógicos, contemplando desde a infraestrutura técnica até a integração final dos módulos do sistema.  
 
O EAP apresentado organiza o escopo do projeto, dividindo-o em etapas e componentes menores. Inicialmente, será desenvolvido o fundamento técnico, etapa essencial para a viabilidade do projeto. Nessa fase, ocorrerá a definição da arquitetura, com a escolha das tecnologias: Python para o back-end e HTML/CSS para o front-end. Também serão realizadas a configuração e a população do banco de dados relacional (SQL), além da preparação do ambiente de desenvolvimento, incluindo a criação de elementos visuais como tabelas, fontes e componentes de interface.

Na segunda etapa, o foco será a implementação das funcionalidades voltadas ao Restaurante, abrangendo os módulos de Cardápio Diário, Estoque e Funcionários, com o desenvolvimento completo do back-end, front-end e respectivos testes.

Em seguida, será desenvolvida a parte voltada ao cliente, que contempla os módulos de Cliente, Consumo e Reserva de Mesas.

Por fim, na última etapa, será realizada a integração entre todas as funcionalidades, bem como a implementação dos relatórios e sistemas de alerta, responsáveis por indicar estoque crítico e aumento de demanda, conforme definido no escopo do projeto.

Plano de projeto

O plano de projeto define a organização geral do trabalho, abrangendo o escopo, o cronograma, os recursos e a metodologia de execução. O desenvolvimento será conduzido de forma incremental, em ciclos semanais de entrega e validação, com reuniões semanais de acompanhamento entre a equipe e o cliente. 

O prazo total estimado para a execução é de oito semanas, contemplando uma semana final de contingência para mitigação de riscos de atraso. O projeto será executado por uma equipe composta por Jean e Paula, em comunicação direta com o cliente Alexandre Alvaro.

# Gerenciamento do Tempo

O gerenciamento de tempo do projeto será consolidado em um cronograma de oito semanas. A primeira semana será dedicada à fase de preparação do ambiente de trabalho, que envolve atividades fundamentais como a definição da arquitetura do projeto, a população inicial do banco de dados com dados de teste, a preparação do ambiente de desenvolvimento e a criação dos padrões de front-end.

As duas semanas seguintes, serão focadas no desenvolvimento dos módulos do restaurante, que incluem a implementação das funcionalidades de Cardápio Diário, Estoque e Funcionários. Dando continuidade, durante as semanas quatro e cinco serão utilizadas para o desenvolvimento das funcionalidades voltadas aos clientes, contemplando os módulos de Clientes, Consumo e Reserva de Mesas. 

Já nas semanas seis e sete, o projeto entrará na fase final de integração do sistema, na qual serão implementados os sistemas de alerta de demanda e de estoque, o módulo de relatório e os testes de integração completos.

Por fim, para tornar o planejamento mais seguro e evitar riscos de atraso, a oitava semana funcionará como uma reserva de contingência. Essa semana de segurança é uma resposta de mitigação ao risco de atrasos no cronograma, que podem ocorrer devido a imprevistos técnicos ou estimativas que se provem otimistas demais. Portanto, essa semana final não será usada para novas tarefas, mas sim para absorver eventuais atrasos das fases anteriores, garantindo que o prazo de entrega do projeto seja cumprido.  
![][image3]

# Gerenciamento da Qualidade

Para incorporar a qualidade em nossos processos e entregáveis desde o início, visando diminuir o retrabalho e lidar com erros no final do projeto, o planejamento inicial do projeto incluirá:

* Fundação e Preparação (Prevenção): A primeira semana será dedicada ao treinamento técnico, ao estabelecimento do ambiente de desenvolvimento e à criação de padrões de codificação para todas as funcionalidades.  
* Garantia da Qualidade (Quality Assurance \- QA): Durante cada ciclo de desenvolvimento (iteração/sprint), a nós aplicaremos práticas de prevenção para identificar e corrigir defeitos o mais cedo possível, como o uso do recurso de Pull Requests (revisão por pares no código) e testes manuais e automatizados unitários e de integração para validar as funcionalidades automaticamente e de forma contínua.

# Gerenciamento de Riscos

O gerenciamento de riscos será realizado ao longo de todo o ciclo de vida do projeto. As etapas adotadas serão:

1. Identificação dos riscos: a primeira identificação foi feita em uma sessão de brainstorming com a equipe do projeto. Novas ameaças podem ser identificadas e adicionadas ao registro durante as reuniões de acompanhamento.

2. Análise qualitativa: para cada risco identificado, a equipe avaliará a probabilidade de ocorrência e o impacto no projeto, usando uma escala qualitativa de alta, média e baixa. A combinação desses fatores gerará a exposição do risco, que definirá a prioridade de tratamento, como mostrado na tabela abaixo.

3. Planejamento de respostas: para cada risco serão definidos planos de mitigação e de contingência.  
4. Monitoramento: os riscos serão revistos durante as reuniões de acompanhamento da equipe, com novos riscos podendo ser incluídos no registro.

Os riscos identificados de forma imediata foram a limitação da equipe e a estrutura do projeto. Um dos principais riscos está associado a possíveis atrasos, já que todas as etapas dependem do trabalho dos membros do grupo. Caso algum deles enfrente imprevistos ou sobrecarga de tarefas, o cronograma poderá ser impactado.  
Outros riscos identificados são os riscos técnicos, como dificuldades de integração entre módulos ou problemas de desempenho próximos à entrega final. Para mitigar esses riscos, foi incluída uma semana de contingência no cronograma, que pode ser utilizada caso haja algum atraso durante o projeto.   
Além disso, os desenvolvedores do projeto realizarão alinhamentos frequentes para detectar possíveis problemas e adaptar a distribuição de tarefas conforme a necessidade do projeto. O contato direto com o cliente facilitará a comunicação de eventuais impactos, permitindo tomar decisões rapidamente para minimizar prejuízos ao prazo e à qualidade. 

# Gerenciamento das Comunicações

O gerenciamento das comunicações tem como objetivo garantir que as informações sobre o andamento do projeto sejam transmitidas de forma clara e estruturada entre todos os envolvidos. A comunicação eficiente será fundamental para alinhar expectativas, identificar problemas e assegurar que as decisões sejam tomadas com base em informações atualizadas.  
A equipe contará com reuniões semanais de acompanhamento nas quais serão revisadas as atividades concluídas, os impedimentos e os planos para a semana seguinte. Relatórios de progresso resumidos poderão ser compartilhados por e-mail ou plataforma de mensagens para manter um histórico de decisões e evolução.  
A comunicação interna entre os membros da equipe será realizada diariamente, permitindo alinhamentos rápidos e coordenação das atividades em andamento. Já a comunicação com o cliente ocorrerá por e-mail, para registros, envio de documentos e notificações relevantes. Com o intuito de apresentar o progresso, alinhar expectativas e validar entregas parciais diretamente com o cliente.

# Gerenciamento das Partes Interessadas

O gerenciamento das partes interessadas visa identificar todos os indivíduos e grupos impactados pelo projeto, analisar suas expectativas e planejar estratégias de engajamento. Para classificar as partes interessadas e definir a abordagem de comunicação, foi utilizada a Matriz de Poder X Interesse.  
 
Essa matriz avalia os stakeholders com base na influência que essa parte pode ter de impactar o projeto e o interesse do quanto essa parte é afetada pelo projeto e dando um plano de engajamento para as partes.  
Para gerenciar de perto, separamos duas partes interessadas, que têm alto interesse e alta influência sobre o projeto, que seria o Cliente Álvaro, por ser patrocinador principal, deve ser mantido em comunicações constantes, e a equipe de desenvolvimento, responsáveis pela execução do projeto.  
Na parte de manter satisfeito, por possuir alta influência e baixo interesse foi adicionada a parte da administração da UFSCAR. É importante garantir que suas expectativas sejam atendidas, mas não existe a necessidade de detalhes técnicos do andamento do projeto.  
Para manter informado, que seria um grupo que será muito afetado pelo projeto, porém possui pouca influência, temos os funcionários do restaurantes, que como usuários finais, devem ser informados sobre o desenvolvimento e receber um treinamento adequado para operar o sistema.  
Na parte interessada de baixa influência e interesse, existe a comunidade universitária da faculdade, podem ser comunicados sobre o lançamento do sistema e suas funcionalidades, sem atualizações sobre o desenvolvimento.

# Referências

UNIVERSIDADE FEDERAL DE SÃO CARLOS. Anexo Termo de Referência – Processo SEI nº 23112.037652/2022-51. São Carlos: UFSCar, 2022\. Disponível em: https://www.proad.ufscar.br/anexos-tr-licitacao-ru-ufscar\_compressed.pdf. Acesso em: 04 de Outubro de 2025\.

Espinha, Roberto Gil. EAP (Estrutura Analítica do Projeto): o que é, aprenda a fazer em 4 passos e benefícios na gestão de projetos. Artia, 01 abr. 2024 (atualizado em 12 jun. 2025). Disponível em: [https://artia.com/blog/como-fazer-eap-na-gestao-de-projetos/](https://artia.com/blog/como-fazer-eap-na-gestao-de-projetos/)

PROJECT MANAGEMENT INSTITUTE. A guide to the project management body of knowledge (PMBOK® guide) – seventh edition and the standard for project management . 7\. ed. \[s.l.\] Project Management Institute, 2021\.
