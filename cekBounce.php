<?php 
function cekBounce(){
    $curl = curl_init();
    curl_setopt_array($curl, [
        CURLOPT_URL => "https://www.namecheap.com/Cart/ajax/Validation.ashx",
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_FOLLOWLOCATION => true,
        CURLOPT_ENCODING => "",
        CURLOPT_MAXREDIRS => 10,
        CURLOPT_TIMEOUT => 30,
        CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
        CURLOPT_CUSTOMREQUEST => "POST",
        CURLOPT_HTTPHEADER, [
            'User-agent:Linux Mozilla 5/0',
            'Accept-Encoding : none',
        ],
    ]);
    $response = curl_exec($curl);
    curl_close($curl);
    return $response;

}

var_dump(cekBounce());
