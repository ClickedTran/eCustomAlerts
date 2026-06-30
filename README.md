# eCustomAlerts 📢

[![Endstone Plugin](https://img.shields.io/badge/Platform-Endstone-orange.svg)](https://endstone.readthedocs.io/)
[![Language](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-GPL--3.0-green.svg)](LICENSE)

**eCustomAlerts** is a powerful and highly customizable plugin for **Endstone software**, allowing Minecraft Bedrock Edition server administrators to modify, customize, or completely disable default system alerts (such as player join, player quit, and other server event messages).

---

## ✨ Features

* **Custom Alerts:** Easily change the text format and layout of default in-game announcements.
* **Full Color Support:** Native compatibility with standard Minecraft Bedrock color codes (`§a`, `§b`, `§c`, etc.).
* **Lightweight & Efficient:** Written in Python using the Endstone API, optimized to ensure zero server performance impact.
* **Easy Configuration:** Manage and tweak all alert messages through an intuitive configuration file.

## 🛠️ Requirements

* **Endstone Server Software** (Latest version recommended).
* **Python** (As required by your Endstone server installation).

## 🚀 Installation

1.  Download the latest release from the [Releases](https://github.com/ClickedTran/eCustomAlerts/releases) page.
2.  Move the plugin files into the `plugins/` directory of your Endstone server.
3.  Restart or reload your server.
4.  The configuration file will be automatically generated upon the first startup.

## ⚙️ Configuration

After the first run, navigate to the plugin's `config.toml` folder to customize the messages to your liking.

Example `config.toml` template:
```toml
# Configuration example (Adjust based on your actual config implementation)
[join]
enabled = true
message = "§7[§a+§7] §e{player} §7has joined the server!"

[quit]
enabled = true
message = "§7[§c-§7] §e{player} §7has left the server."
...
```

# 🤝 Contributing
Any contributions, bug reports, or feature requests are welcome! Feel free to open an Issue or submit a Pull Request directly to this GitHub repository.

# 📄 License
This project is licensed under the GPL-3.0 License - see the LICENSE file for more details.
