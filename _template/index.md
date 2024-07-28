---
title: "Translation of Dwarf Fortress to 'your language'"
description: "Translation of Dwarf Fortress to 'your language'"
lang: "en" # replace it with your language code
permalink: /en/
additional_links: false
---

### Localization for 50.* and newer versions of Dwarf Fortress

> There is a support of DF 51.01 betas (with Adventure Mode)

Download the localization installer (supports version of DF 50.10 and newer):

[![dfint/installer](https://img.shields.io/badge/dfint%2Finstaller-forestgreen?style=for-the-badge)](https://github.com/dfint/installer/releases/latest)

Brief instructions:

- Download the package (press the button above, download `win` package for windows, or `lin` for linux), unpack it, execute the `dfint-installer` file.
- Select ("Open") the game's executable file (`Dwarf Fortress.exe` or `dwarfort`). Alternatively, you can put the `dfint-installer` file into the game's directory, then it will find the game's executable by itself.
- Choose the translation language, then press "Update".
- Run the game.
- To update translation or configuration for a newer version of the game, run the installer again (while the game is shut down) then press "Update".

If you have some troubles with the installer (e.g. you are useing Windows 7 or 8), you can use the [package-buidler](https://dfint-package-build.streamlit.app) instead.

### Links

- [Translation project on transifex](https://app.transifex.com/dwarf-fortress-translation/dwarf-fortress-steam)
- [The project on github](https://github.com/dfint) - this is a place where we develop tools for the localization
- [The official Dwarf Fortress site](https://bay12games.com/dwarves/), [steam](https://store.steampowered.com/app/975370/Dwarf_Fortress/), [itch.io](https://kitfoxgames.itch.io/dwarf-fortress)
{% if page.additional_links %}{% include_relative additional_links.md %}{% endif %}
