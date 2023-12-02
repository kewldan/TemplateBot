## Template Bot

My personal starter pack template for creating bots for telegram with aiogram 3.2.0

## Get started

1. Setup default config with your values
```json5
{
  "bot": {
    "token": "", // Telegram bot token
    "database": "", // Mongo database
    "owner": 787751346, // Owner ID
    "debug": true, // Is debug build
    "mongo": "" //Mongo connection URI
  }
}
```
2. Setup `./rebuild.sh` with container name and start options
3. Run `chmod +x ./rebuild.sh` command to mark file as executable
4. Run `./rebuild.sh` command