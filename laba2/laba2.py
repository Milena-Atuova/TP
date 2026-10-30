
class GameObject:
    """Общие свойства любого объекта на игровой карте."""

    def __init__(self, objectId: int, name: str, x: int, y: int) -> None:
        self._id = objectId
        self._name = name
        self._x = x
        self._y = y

    def getId(self) -> int:
        return self._id

    def getName(self) -> str:
        return self._name

    def getX(self) -> int:
        return self._x

    def getY(self) -> int:
        return self._y


class Unit(GameObject):
    """Игровой юнит: имеет здоровье и получает урон."""

    def __init__(self, objectId: int, name: str, x: int, y: int,
                 hp: float = 100.0) -> None:
        super().__init__(objectId, name, x, y)
        if hp < 0:
            raise ValueError("Здоровье не может быть отрицательным")
        self._hp = float(hp)

    def isAlive(self) -> bool:
        return self._hp > 0

    def getHp(self) -> float:
        return self._hp

    def receiveDamage(self, damage: float) -> None:
        if damage < 0:
            raise ValueError("Урон не может быть отрицательным")
        self._hp = max(0.0, self._hp - damage)


class Building(GameObject):
    """Постройка: может быть недостроенной или готовой."""

    def __init__(self, objectId: int, name: str, x: int, y: int,
                 built: bool = False) -> None:
        super().__init__(objectId, name, x, y)
        self._built = built

    def isBuilt(self) -> bool:
        return self._built

    def build(self) -> None:
        self._built = True


class Attacker:
    def attack(self, unit):
        raise NotImplementedError


class Moveable:
    def moveTo(self, x, y):
        raise NotImplementedError

class Archer(Unit, Attacker, Moveable):
    """Лучник: юнит, который умеет атаковать и двигаться."""

    def __init__(self, objectId: int, name: str, x: int, y: int,
                 hp: float = 100.0, damage: float = 25.0) -> None:
        super().__init__(objectId, name, x, y, hp)
        self._damage = damage

    def attack(self, unit: Unit) -> None:
        if not self.isAlive():
            raise RuntimeError("Мёртвый лучник не может атаковать")
        unit.receiveDamage(self._damage)

    def moveTo(self, x: int, y: int) -> None:
        self._x = x
        self._y = y


class Fort(Building, Attacker):
    """Крепость: построенное здание, которое может атаковать."""

    def __init__(self, objectId: int, name: str, x: int, y: int,
                 built: bool = False, damage: float = 40.0) -> None:
        super().__init__(objectId, name, x, y, built)
        self._damage = damage

    def attack(self, unit: Unit) -> None:
        if not self.isBuilt():
            raise RuntimeError("Недостроенная крепость не может атаковать")
        unit.receiveDamage(self._damage)


class MobileHouse(Building, Moveable):
    """Дом на колёсах: постройка, которая может перемещаться."""

    def moveTo(self, x: int, y: int) -> None:
        self._x = x
        self._y = y


def main() -> None:
    game_object = GameObject(1, "Камень", 0, 0)
    enemy = Unit(2, "Противник", 7, 4, hp=60)
    building = Building(3, "Склад", 1, 1)
    archer = Archer(4, "Лучник", 2, 3)
    fort = Fort(5, "Крепость", 10, 10)
    house = MobileHouse(6, "Дом на колёсах", 4, 4, built=True)

    print("Лабораторная работа №2. Основы ООП")

    print("\n1. Общие данные GameObject:")
    print(f"   ID={game_object.getId()}, имя={game_object.getName()}, "
          f"координаты=({game_object.getX()}, {game_object.getY()})")
    print(f"   Противник: HP={enemy.getHp():g}, жив={enemy.isAlive()}")

    print("\n2. Строительство Building:")
    print(f"   Склад построен: {building.isBuilt()}")
    building.build()
    print(f"   После build(): {building.isBuilt()}")

    print("\n3. Перемещение через интерфейс Moveable:")
    movers: list[Moveable] = [archer, house]
    for mover in movers:
        mover.moveTo(8, 6)
        print(f"   {mover.getName()}: ({mover.getX()}, {mover.getY()})")

    print("\n4. Проверка недостроенной крепости:")
    try:
        fort.attack(enemy)
    except RuntimeError as error:
        print(f"   {error}")

    print(f"   HP противника: {enemy.getHp():g}")
    fort.build()

    print("\n5. Атаки через интерфейс Attacker:")
    attackers: list[Attacker] = [archer, fort]
    for attacker in attackers:
        attacker.attack(enemy)
        print(f"   Атаковал {attacker.getName()}: "
              f"HP противника = {enemy.getHp():g}")

    print(f"   Противник жив: {enemy.isAlive()}")

    print("\n6. Проверка смерти и неправильного урона:")
    archer.receiveDamage(500)
    print(f"   Лучник жив: {archer.isAlive()}, HP={archer.getHp():g}")

    try:
        archer.attack(enemy)
    except RuntimeError as error:
        print(f"   {error}")

    try:
        enemy.receiveDamage(-10)
    except ValueError as error:
        print(f"   {error}")

    print("\nВсе проверки выполнены.")


if __name__ == "__main__":
    main()