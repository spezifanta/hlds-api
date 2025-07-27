# HLDS API

A simple Flask API for querying Half-Life Dedicated Server (HLDS) information using Python 3.13 and uv. Built with [SourceWatch](https://github.com/spezifanta/SourceWatch) and Flask to create a REST API for Half-Life Dedicated Servers.

## Features

- Query HLDS server info, rules, and players via HTTP API
- Built-in caching (10-second TTL)
- Docker support with Gunicorn

## API Endpoints

### `GET /`
Get server information, rules, and players.

**Query Parameters:**
- `server` - Server IP/hostname (default: env HLDS_DEFAULT_QUERY_SERVER or steamcalculator.com)
- `port` - Server port (default: env HLDS_DEFAULT_QUERY_PORT or 27015)

**Example:**
```bash
curl "http://localhost:27000/?server=steamcalculator.com&port=27015"
```

**Response:**
```json
{
  "info": {
    "game_app_id": 70,
    "game_description": "Half-Life",
    "game_directory": "valve",
    "game_map": "crossfire",
    "game_version": "1.1.2.2/Stdio",
    "players_bot": 0,
    "players_current": 2,
    "players_human": 2,
    "players_max": 12,
    "server_name": "spezi|Saufbude #1 HLDM",
    "server_os": "l",
    "server_password_protected": 0,
    "server_port": 27015,
    "server_protocol_version": 48,
    "server_steam_id": 90119497483802634,
    "server_type": "d",
    "server_vac_secured": 1
  },
  "players": [
    {
      "id": 0,
      "kills": 4,
      "name": "spezi|Fanta",
      "play_time": 814.7973022460938
    },
    {
      "id": 1,
      "kills": 14,
      "name": "spezi|Cola",
      "play_time": 462.9696044921875
    }
  ],
  "rules": {
    "allow_spectators": "0.0",
    "coop": "0",
    "deathmatch": "1",
    "mp_fraglimit": "0",
    "mp_fragsleft": "0",
    "mp_friendlyfire": "0",
    "mp_logfile": "0",
    "mp_teamlist": "hgrunt;scientist",
    "mp_teamplay": "0",
    "mp_timeleft": "4602",
    "mp_timelimit": "120",
    "mp_weaponstay": "0",
    "pausable": "0",
    "sv_accelerate": "10",
    "sv_aim": "0",
    "sv_airaccelerate": "10",
    "sv_allowupload": "0",
    "sv_alltalk": "1",
    "sv_bounce": "1",
    "sv_cheats": "0",
    "sv_clienttrace": "1",
    "sv_contact": "steamcalculator.com",
    "sv_friction": "4",
    "sv_gravity": "800",
    "sv_maxspeed": "320"
  },
  "server": {
    "ip": "94.130.15.22",
    "ping": 10.73,
    "port": 27015
  }
}
```

### `GET /ping`
Health check endpoint.

**Response:** `pong`

## Development

### Requirements
- Python 3.13+
- uv package manager

### Setup
```bash
# Clone repository
git clone https://github.com/spezifanta/hlds-api
cd hlds-api

# Install dependencies
uv sync

# Run development server
uv run python app.py
```

The server will start on `http://localhost:27000`

## Docker

### Build and run locally
```bash
docker build -t hlds-api .
docker run -p 27000:27000 hlds-api
```

### Using docker-compose
```bash
docker-compose up
```

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `HLDS_DEFAULT_QUERY_SERVER` | Default server IP or hostname to query  | `steamcalculator.com` |
| `HLDS_DEFAULT_QUERY_PORT` | Default server port to query | `27015` |
| `HLDS_ADDRESS` | Bind address for web server | `127.0.0.1` |
| `HLDS_PORT` | Bind port for web server | `27000` |

## Deployment

The project includes GitHub Actions workflow that:
- Tests the application
- Builds multi-platform Docker images (amd64/arm64)
- Pushes to GitHub Container Registry (ghcr.io)
- Runs on pushes to master/main branch

### Using published image
```bash
docker run -p 27000:27000 ghcr.io/spezifanta/hlds-api:latest
```

## Error Handling

The API returns JSON error responses with 400 status code for:
- Invalid port parameters
- Network timeouts
- SourceWatch query failures

Example error response:
```json
{"error": "timed out"}
```
