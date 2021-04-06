# Factory Method

Padrão criacional que fornece uma interface para criar objetos em uma superclasse, mas permite que as subclasses alterem o tipo de objetos criados. 

Sugere que você substitua chamadas diretas de construção (`new`) por chamadas de um método fábrica especial (que aí sim chama o `new`), esses métodos são chamados de produtos. 

Limitação: as subclasses só podem retornar tipos diferentes de produtos se esses tiverem uma classe/interface em comum. O método fábrica na classe base deve ter seu tipo de retorno declarado como essa interface. 

### Aplicabilidade
 O Factory Method separa o código de construção do produto do código que realmente usa o produto. 
 Economiza recursos do sistema, reutilizando objetos, ao invés de recriá-los sempre. 

### Prós e contras

| Prós                                                 | Contras                                                               |
| ---------------------------------------------------- | --------------------------------------------------------------------- | 
| Evita acoplamento entre criador e produtos concretos | o código pode se tornar muito complicado se colocar muitas subclasses |
| Princípio da responsabilidade única                  |                                                                       |
| Princípio aberto/fechado.                            |                                                                       |
|Menos complicado e mais customizável pelas subclasses||