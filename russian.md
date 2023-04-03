---
title: Проект русификации игры Dwarf Fortress
lang: "ru-RU"
---

### Локализация для 50.* версий Dwarf Fortress

Инструменты для применения перевода к игре в разработке, есть ранние версии патча:

- **<https://boosty.to/dfrus>**

Там же можно поддержать разработчиков донатами.

### Сборка DF 0.42.06 под Windows (обновлено 21.03.2016)

- [**Сборка на основе PeridexisErrant's Starter Pack 0.42.06-r02**](https://bitbucket.org/dfint/downloads/downloads/PeridexisErrants_Starter_Pack_0.42.06-r02-ru21.03.2016.7z)
  - Ввод кириллицы пока не работает
  - Требуется тестирование
  - Вырезаны утилиты из папки LNP/utilities
  - dfhack в сборку входит, но не тестировался
  - Добавлены два графических пакета: [Taffer's Tileset](http://www.bay12forums.com/smf/index.php?topic=107924.0) и [burnedfx Graphic Set](http://www.bay12forums.com/smf/index.php?topic=143588.0)

### Сборка DF 0.42.01 под Linux

- **[Тестовая сборка DF 0.42.01](https://bitbucket.org/dfint/downloads/downloads/df_linux_sborka_42_01.tar.gz)**

### Cборка DF 0.40.24 под Windows

- Тестовая сборка на основе урезанного DF 0.40.24 Starter Pack r3
  - Практически полный перевод DF 0.40.24
  - Частичное исправление грамматики при помощи скрипта [changetext.py](https://github.com/dfint/changetextpy_script)
  - Решены две основные проблемы: вывод кириллицы на экране "Thoughts and prefences" (и других) и возможность поиска в менеджере.
  - Как и в оригинальном Starter Pack, в сборку входят 6 графических пакетов, однако из сборки вырезаны утилиты, в том числе dfhack
  - Грамматика исправляется пока не везде и не идеально
  - В общем и целом перевод не идеален
  - Сборка довольно сырая и требует тестирования
- **В связи с выходом DF 0.42.\* обновление сборки DF 0.40.24 не предполагается**

### Тестовая сборка DF 0.40.24 под Linux

- [DF_0.40.24_rus.tgz](https://bitbucket.org/dfint/downloads/downloads/DF_0.40.24_rus.tgz)
  - Должен быть установлен Python 3.4. Под 64-битной системой - libpython3.4:i386.
  - Не везде сделан перевод
  - Пока не работает поиск в менеджере

### Ссылки

- [Проект перевода на transifex](https://app.transifex.com/dwarf-fortress-translation/dwarf-fortress-steam) - собственно, здесь ведется перевод
- [Проект на github](https://github.com/dfint) - здесь ведется разработка инструментов для локализации
- [Официальный сайт Dwarf Fortress](https://bay12games.com/dwarves/), [steam](https://store.steampowered.com/app/975370/Dwarf_Fortress/)
- [Группа ВК, посвященная русификации DF и утилит](https://vk.com/dfrus)
- [Обсуждение перевода на forum.dfwk.ru](http://forum.dfwk.ru/index.php/topic,204.0.html)
