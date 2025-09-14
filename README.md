# Inlämningsuppgift – Reverse Proxy, Frontend/Backend och Redis

I denna uppgift ska du bygga en container-baserad lösning där flera tjänster samverkar.

Du ska använda ett verktyg som gör det möjligt att starta upp och samordna flera containrar som tillsammans utgör en fungerande helhet.

Nuvarande version av applikationen (Flask baserad) startas manuellt på en server med `python app.py` för vardera frontend och backend.

Ni finner de två applikationerna i **frontend** respektive **backend** mapparna i detta repot.

## Krav på lösningen

- Det ska finnas en **reverse proxy**, som lyssnar på port 80 och routar inkommande trafik till rätt tjänst.

- Det ska finnas tre frontend-tjänster, som nås på `frontend.localhost` och ska lastbalanseras.

- Det ska finnas en backend-tjänst som tar emot data från frontenderna.
Backend tjänsten ska kunna nås på `backend.localhost` och `http://backend.localhost/messages` ska visa en JSON key/value lista.

- Det ska finnas en **Redis-tjänst** där den data som skickas från frontenderna via backend sparas.

- Det ska finnas en **dashboard** för reverse proxyn.

- Det ska gå att läsa **accesslog** från reverse proxyn.

- Endast ett kommando `docker compose up -d` ska starta alla containrar och hela projektet ska då vara fungerande.

## Tips

Eftersom applikationen har kört lokalt på en server utan containers så kan det finnas ställen i koden där hostnames kan behöva bytas ut för att passa ny setup.

## Önskemål

- Om möjligt starta containers i lämplig ordning.

- Om möjligt så isolera de olika komponenterna på bästa möjliga sätt.

- Om möjligt så persistera Redis datan så den finns kvar om Redis containern startar om.

- Om möjligt gör så att det går att nå reverse proxy dashboard på `dashboard.localhost`.
