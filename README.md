# HLDS API

This Project uses [SourceWatch](https://github.com/spezifanta/SourceWatch) and
Flask to create a query REST API for Half-Life Dedicated Servers.

## Usage

Set `HLDS_IP` and `HLDS_PORT` to the gameserver you would like not montior.

```bash
export HLDS_IP="steamcalculator.com"
export HLDS_PORT="27015"
python app.py
```

This will create webserver on port `27014`.

## Endpoints

### `/`

Request basic server information, current players and game rules.

#### Request

```
curl localhost:27014
```

#### Response

```
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
      "name": "On error resume next",
      "play_time": 814.7973022460938
    },
    {
      "id": 1,
      "kills": 14,
      "name": "muhittin",
      "play_time": 462.9696044921875
    }
  ],
  "rules": {
    "allow_spectators": "0.0",
    "coop": "0",
    "deathmatch": "1",
    "decalfrequency": "30",
    "edgefriction": "2",
    "max_queries_sec": "1",
    "max_queries_sec_global": "1",
    "max_queries_window": "1",
    "metamod_version": "1.21p38",
    "mp_allowmonsters": "0",
    "mp_autocrosshair": "0",
    "mp_chattime": "10",
    "mp_consistency": "1",
    "mp_falldamage": "0",
    "mp_flashlight": "0",
    "mp_footsteps": "1",
    "mp_forcerespawn": "1",
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
    "sv_logblocks": "0",
    "sv_maxrate": "100000",
    "sv_maxspeed": "320",
    "sv_minrate": "5000",
    "sv_password": "0",
    "sv_proxies": "0",
    "sv_stepsize": "18",
    "sv_stopspeed": "100",
    "sv_uploadmax": "0.5",
    "sv_voiceenable": "1",
    "sv_wateraccelerate": "10",
    "sv_waterfriction": "1"
  },
  "server": {
    "ip": "94.130.15.22",
    "ping": 10.73,
    "port": 27015
  }
}
```

### `/ping`

Used as healthcheck for Docker.

#### Request

```
curl localhost:27014/ping
```

#### Response

```
pong
```
