# ia-ap2

### Mudanças feitas
-  [`src/javaff/search/AstarSearch.java` ](src/javaff/search/AstarSearch.java)
   - Criado classe para o método A*. que herda de Search e é basicamente igual ao BestFirstSearch, mas com um comparador diferente.
-  [`src/javaff/search/HGValueComparator.java`](src/javaff/search/HGValueComparator.java)
   -  Comparador que será utilizado no A*. Ele compara os valores de H+G.
-  [`src/javaff/JavaFF.java`](src/javaff/JavaFF.java)
   - Adicionado a opção de escolher o método de busca (isso é opcional, pode alterar manualmente no código qual algorítmo deseja rodar).

