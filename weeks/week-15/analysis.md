# Analiz proizvoditelnosti

project_code: logs-s01

## Usloviya testa
- Instrumenty: wrk (REST), ghz (gRPC)
- Dlitelnost: 30s
- Parallelizm: 1, 10, 100

## Rezultaty

| Protokol | Parallelizm | Propusknaya sposobnost (RPS) | P50 latency (ms) | P99 latency (ms) |
|----------|-------------|------------------|------------------|------------------|
| REST     | 1           | 120              | 8                | 20               |
| REST     | 10          | 780              | 22               | 65               |
| REST     | 100         | 910              | 120              | 410              |
| gRPC     | 1           | 180              | 5                | 14               |
| gRPC     | 10          | 1100             | 14               | 40               |
| gRPC     | 100         | 1450             | 70               | 230              |

## Vyvody
- Zaderzhka uvelichivaetsya s rostom parallelizma v oboih protokolah.
- REST dostigaet nasyshcheniya ran'she: RPS perestaet rasti okolo 900.
- gRPC demonstriruet luchshuyu propusknuyu sposobnost i menshuyu latency pri vysokoy nagruzke.