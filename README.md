# Engineering_of_information_systems
## UML classes:
Информационная система содержит в себе массив пользователей. Пользователи, в свою очередь, содержат объявления, которые они размещают.
Для удаления/размещения объявлений пользователи вызывают соответствующие функции, которые делегируют свое выполнение соответствующим функциям в системе через
интерфейс, т.к. именно система отвечает за логику. Такое же дело обстоит и с покупкой подписки.
   
Пользователь может разместить ограниченное кол-во объявлений без подписки.

## UML activities:
Пользователь может выполнить следующий набор действий:
- Размещение объявления (если он уже разместил предельное кол-во объявлений без подписки, то ему будет предложена её покупка)
- Размещение/удаление объявления
- Пополнение балланса с целью покупки подписки

## Lab2:
В данной работе реализовано два итератора для обхода дерева:
1. Итератор, которые обходит дерево в глубину слева-направо
2. Итератор, которые обходит дерево в глубину справа-налево
