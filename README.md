# Inlämningsuppgift – Reverse Proxy, Frontend/Backend och Redis

I denna uppgift ska du bygga en container-baserad lösning där flera tjänster samverkar.

Du ska använda ett verktyg som gör det möjligt att starta upp och samordna flera containrar som tillsammans utgör en fungerande helhet.

Nuvarande version av applikationen (Flask baserad) startas manuellt på en server med `python app.py` för vardera frontend och backend.

Ni finner de två applikationerna i **frontend** respektive **backend** mapparna i detta repot.

Det går att testa nuvarande version genom att starta vardera applikation i separata terminaler och samtidigt starta en Redis container med `docker run -d --name redis -p 6379:6379 redis:latest`.

## Krav på lösningen

- Den ska vara container-baserad.

- Det ska finnas en **reverse proxy**, som lyssnar på port 80 och routar inkommande trafik till rätt tjänst.

- Det ska finnas tre frontend-tjänster, som nås på `frontend.localhost` och ska lastbalanseras.

- Det ska finnas en backend-tjänst som tar emot data från frontenderna.

- Det ska finnas en **Redis-tjänst** där den data som skickas från frontenderna via backend sparas.

- Det ska finnas en **dashboard** för reverse proxyn.

- Det ska gå att läsa **accesslog** från reverse proxyn.

- Endast ett kommando `docker compose up -d` ska starta alla containrar och hela projektet ska då vara fungerande.

## Tips

Eftersom applikationen har kört lokalt på en server utan containers så kan det finnas ställen i koden där hostnames kan behöva bytas ut för att passa ny setup.

## Önskemål som kan ge högre betyg

- Om möjligt starta containers i lämplig ordning.

- Om möjligt så isolera de olika komponenterna på bästa möjliga sätt.

- Om möjligt så persistera Redis datan så den finns kvar om Redis containern startar om.

- Om möjligt gör så att det går att nå reverse proxy dashboard på `dashboard.localhost`.

- Om möjligt ska backend tjänsten kunna nås på `backend.localhost` så att `http://backend.localhost/messages` visar en JSON key/value lista.

## Inlämning av uppgift

Inlämning av färdig uppgift sker via Learnpoint där ni zippat ihop ert projekt och laddat upp det.
