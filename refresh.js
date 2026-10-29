const produkte = [
    { name: "Tastatur", preis: 50 },
    { name: "Maus", preis: 25 },
    { name: "Monitor", preis: 200 }
];

function findeTeureProdukte(produktListe) {
    let teuer = [];
    
    for (let item of produktListe) {
        if (item.preis > 40) {
            teuer.push(item.name);
        }
    }
    
    return teuer;
}

console.log(findeTeureProdukte(produkte));

const warenkorb = [
    { artikel: "Tastatur", menge: 2, preis: 45.0 },
    { artikel: "Maus", menge: 1, preis: 25.0 },
    { artikel: "Monitor", menge: 1, preis: 200.0 }
];

function berechneWarenkorbSumme(positionen) {
    let summe = 0;

    for(let item of positionen) {
        summe += item.menge * item.preis;
    }

    return summe;
}

console.log(berechneWarenkorbSumme(warenkorb));