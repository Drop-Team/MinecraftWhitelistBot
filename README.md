# Minecraft Whitelist Bot

Telegram bot for managing the whitelist on the Minecraft server.

## Table of Contents

- [About](#about)
- [Used](#used)
- [Deploy](#deploy)


## About

Bot provides an interface:
- To manage unlimited number of nicknames on the Minecraft server as admin
- To add limited number of nicknames to whitelist as user

It is hosted at Innopolis University, so it uses [InnoID](https://github.com/Drop-Team/InnoID) to verify the user.

## Used

- [AIOGram](https://github.com/aiogram/aiogram) as framework for Telegram Bot API
- [Whitelist HTTP API](https://github.com/MUNComputerScienceSociety/Whitelist-HTTP-API) as plugin for Minecraft server for whitelist management via HTTP API

## Deploy

### Plugin

1. [Download](https://github.com/MUNComputerScienceSociety/Whitelist-HTTP-API/releases) plugin
2. Install it and [Configure](https://github.com/MUNComputerScienceSociety/Whitelist-HTTP-API/blob/master/README.md) Bearer Token

### Environment

1. Rename [.env-example](https://github.com/Drop-Team/InnoPrintBot/blob/main/.env-example) to `.env`.
2. Edit it:
```
PROMETHEUS_PORT - Port where metrics for Prometheus are hosted

TELEGRAM_BOT_TOKEN - Token for Telegram Bot from @BotFather bot

INNOID_API_URL - URL for API of InnoID
INNOID_API_AUTH_TOKEN - Token for InnoID app from @InnoIDBot bot

WHITELIST_API_URL - URL for plugin's HTTP API
WHITELIST_API_TOKEN - Token for authorization in plugin's API which has been configured in plugin's configuration file
```

### Limits

[limits.json](https://github.com/Drop-Team/MinecraftWhitelistBot/blob/master/limits.json) is a file that stores limits of users on the number of nicknames available for creating or changing.

```
123456789: 20  # User with Telegram ID 123456789 has a limit of 20 nicknames
__all__: 1  # All other users have a limit of 1 nickname
```

### Docker

To run use Docker:
```bash
docker-compose build
docker-compose -d up  # -d to run in background 
docker-compose ps
```