
project_code: shipments-s01

## Obzor sistemy
Sistema sostoit iz treh mikroservisov:

1. `shipments-svc-s01` - osnovnoy servis upravleniya otpravleniyami.
2. `tracking-svc` - servis chteniya i obnovleniya treking statusov.
3. `notifications-svc` - servis otpravki uvedomleniy.

## Potok vzaimodeystviya
- Klientskiy UI i vneshnie integracii vyzyvayut API Gateway po REST (`/api/shipments`).
- Gateway peresylaet zaprosy v `shipments-svc-s01`.
- `shipments-svc-s01` vyzyvaet `tracking-svc` po gRPC dlya bystrogo vnutrennego RPC.
- Pri klyuchevyh sobytiyah (`created`, `in_transit`, `delivered`) osnovnoy servis otpravlyaet sobytie v `notifications-svc`.

## Hranenie dannyh
- `shipments-svc-s01`: PostgreSQL (dannye ob otpravlenii, adres, tekushchiy status).
- `tracking-svc`: Redis (bystryy dostup k poslednemu trekingu po shipment_id).
- `notifications-svc`: PostgreSQL (istoriya uvedomleniy).

## Infrastruktura
- Lokalnyy zapusk: Docker Compose (gateway + servisy + bazy dannyh).
- CI pipeline: lint, testy, sborka docker obrazov, upload artefaktov.
- Opcionalnyy Kubernetes: Helm chart s dev/stage/prod values.

## Obosnovanie
- REST vybran dlya public API, potomu chto eto prosto dlya frontend/vneshnih klientov.
- gRPC vybran dlya service-to-service vyzovov iz-za strogogo kontrakta i skorosti.
- Razdelenie servisov uluchshaet nezavisimoe masshtabirovanie i podderzhku.
