<?php

define('CLIENT_ID', 'bdfd4a12d0854a85a0f1d9ab163f81c6'); // wprowadź Client_ID aplikacji
define('CLIENT_SECRET', 'nGVIB3fMXVtsY2yuIzOn6aexFF4fFKeiq0X6IFy7Gn94aYmhq1T26mgvBT1YCIIa'); // wprowadź Client_Secret aplikacji

function getCurl($headers, $url, $content = null) {
	$ch = curl_init();
	curl_setopt_array($ch, array(
		CURLOPT_URL => $url,
		CURLOPT_HTTPHEADER => $headers,
		CURLOPT_SSL_VERIFYPEER => false,
		CURLOPT_RETURNTRANSFER => true
    ));
    if ($content !== null) {
        curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'POST');
        curl_setopt($ch, CURLOPT_POST, true);
        curl_setopt($ch, CURLOPT_POSTFIELDS, $content);
    }
	return $ch;
}

function getAccessToken() {
	$authorization = base64_encode(CLIENT_ID.':'.CLIENT_SECRET);
	$headers = array("Authorization: Basic {$authorization}","Content-Type: application/x-www-form-urlencoded");
	$content = "grant_type=client_credentials";
    $url = "https://allegro.pl/auth/oauth/token";
	$ch = getCurl($headers, $url, $content);
	$tokenResult = curl_exec($ch);
    $resultCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
	curl_close($ch);
    if ($tokenResult === false || $resultCode !== 200) {
        exit ("Something went wrong");
    }
	return json_decode($tokenResult)->access_token;
}

 function main()
{
    echo getAccessToken();
}

main();