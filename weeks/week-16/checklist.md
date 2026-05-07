# Chek-list

## Proverki na osnove OWASP

- [ ] Autentifikaciya: est zashchita ot brute-force i rate limiting.
- [ ] Hranenie paroley: ispolzuetsya heshirovanie bcrypt/argon2 i unikalnaya sol.
- [ ] Avtorizaciya: proveryaetsya dostup k obektam na kajdom zashchishchennom endpoint.
- [ ] Validaciya vhoda: strogie shemy dlya REST/gRPC/GraphQL payload.
- [ ] Zashchita ot SQL/NoSQL inekciy: tolko parametrizovannye zaprosy.
- [ ] Utechka chuvstvitelnyh dannyh: net sekretov, tokenov i PII v logah.
- [ ] Bezopasnost transporta: HTTPS/TLS obyazatelen vne lokalnoy sredy.
- [ ] Bezopasnost JWT/sessiy: proverka podpisi, sroka deystviya i issuer.
- [ ] Politika CORS: razresheny tolko doverennye origin.
- [ ] Security headers: HSTS, X-Content-Type-Options, CSP gde primenimo.
- [ ] Bezopasnost zavisimostey: zavisimosti regulyarno proveryayutsya i obnovlyayutsya.
- [ ] Usilenie konteinera: zapusk ne ot root, minimalnyy bazovyy obraz.
