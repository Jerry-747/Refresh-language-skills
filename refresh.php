<?php

$warenkorb = [
    ["artikel" => "Tastatur", "menge" => 2, "preis" => 45.0],
    ["artikel" => "Maus", "menge" => 1, "preis" => 25.0],
    ["artikel" => "Monitor", "menge" => 1, "preis" => 200.0]
];

function berechneWarenkorbSumme($positionen) {
    $summe = 0;
    
    foreach ($positionen as $item) {
        $summe += $item["menge"] * $item["preis"];
    }
    
    return $summe;
}

echo berechneWarenkorbSumme($warenkorb);

?>