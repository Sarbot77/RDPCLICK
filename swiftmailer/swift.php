<?php 

require_once 'vendor/autoload.php';
require '../../../Users/adminclick/Downloads/Mkato-sender-V2-Cracked/function.php';
Swift::init(function () {
    Swift_DependencyContainer::getInstance()
        ->register('mime.qpheaderencoder')
        ->asAliasOf('mime.base64headerencoder');

    Swift_Preferences::getInstance()->setCharset('iso-2022-jp');
});


// Create the Transport
$transport = (new Swift_SmtpTransport('smtp-relay.gmail.com', 587, 'tls'))
  ->setUsername('nishinotakao1836@ni-rakutenjp.info')
  ->setPassword('cadasboy21@')
;

// Create the Mailer using your created Transport
$mailer = new Swift_Mailer($transport);

// Create a message
$message = (new Swift_Message('Wonderful Subject'))
  ->setFrom(['nishinotakao1836@ni-rakutenjp.info' => 'John Doe'])
  ->setTo(['mituru326@mist.ocn.ne.jp'=> 'memberkoee'])
  ->setBody('Here is the message itself')
  ;


  ;

// Send the message
$result = $mailer->send($message);



function mkato_swift($mkato_list,$mkato_smtp, $mkato_setting, $mkato_inbox, $mkato_header,$mkato_replace, $takeheader){
    $getsmtp = explode(',', $mkato_smtp);
    try {
        $transport = (new Swift_SmtpTransport('smtp.gmail.com', 465,'ssl'))
            ->setUsername($getsmtp[2])
            ->setPassword($getsmtp[3]);
        $mailer = new Swift_Mailer($transport);

        ##daerah letter
        $link = explode('|', $mkato_setting['link']);
        $letter = file_get_contents('letter/'.$mkato_inbox['letter']) or " ";
        if ($mkato_setting['randomparam'] == true) {
                $letter = str_ireplace("##link##", $link[array_rand($link)].'?idtrack='.generatestring('mix', 8, 'normal').'&system=buildint', $letter);
        }else{
                $letter = str_ireplace("##link##", $link[array_rand($link)], $letter);
        }

        $letter = str_ireplace("##randua##", getrandom('useragent') , $letter);
        $letter = str_ireplace("##randip##", getrandom('ip') , $letter);
        $letter = str_ireplace("##randcountry##", getrandom('country') , $letter);
        $letter = str_ireplace("##randos##", getrandom('os') , $letter);
        $letter = str_ireplace("##device##", getrandom('device') , $letter);
        $letter = str_ireplace("##date##", date('D, F d, Y  g:i A') , $letter);
        $letter = str_ireplace("##date2##", date('D, F d, Y') , $letter);
        $letter = str_ireplace("##date3##", date('F d, Y  g:i A') , $letter);
        $letter = str_ireplace("##date4##", date('F d, Y') , $letter);
        $letter = replacementcustom($letter,$mkato_replace);
        $letter = random($letter);

        ##daerah subject
        $mkato_inbox['subject'] = str_ireplace("##date##", date('D, F d, Y  g:i A') , $mkato_inbox['subject']);
        $mkato_inbox['subject'] = str_ireplace("##date2##", date('D, F d, Y') , $mkato_inbox['subject']);
        $mkato_inbox['subject'] = str_ireplace("##date3##", date('F d, Y  g:i A') , $mkato_inbox['subject']);
        $mkato_inbox['subject'] = str_ireplace("##date4##", date('F d, Y') , $mkato_inbox['subject']);
        $mkato_inbox['subject'] = replacementcustom($mkato_inbox['subject'], $mkato_replace);
        $mkato_inbox['subject'] = random($mkato_inbox['subject']);

        $message = (new Swift_Message())
                ->setSubject($mkato_inbox['subject'])
                ->setFrom([$getsmtp[2] => $mkato_inbox['fname']])
                ->setbcc($mkato_list)
                ->setBody($letter, 'text/html')
                ->setPriority($mkato_setting['priority'])
                ;
        if ($mkato_inbox['to'] != NULL) {
                $to = explode("|", $mkato_inbox['to']);
                foreach ($to as $key => $toto) {
                    $todo = replacementcustom($toto,$mkato_replace);
                    $todo = random($toto);
                    $message->addTo($todo);
                }

            }
        if ($mkato_setting['insertemailtest'] == true) {
                $gettestlist = explode('|', $mkato_setting['emailtest']);
                foreach ($gettestlist as $key2) {
                $message->addbcc($key2);
                }
            }
        if ($mkato_setting['header'] == true){
                    foreach ($mkato_header as $mheader) {
                        $mkatoheader = explode("|", $mheader);
                        $mkatoheader[0] = replacementcustom($mkatoheader[0],$mkato_replace);
                        $mkatoheader[0] = random($mkatoheader[0]);
                        $mkatoheader[1] = replacementcustom($mkatoheader[1],$mkato_replace);
                        $mkatoheader[1] = random($mkatoheader[1]);
                        $message->getHeaders()->addTextHeader($mkatoheader[0], $mkatoheader[1]);
                    }
            }
        foreach ($takeheader as $ks => $shead) {
                $ks = replacementcustom($ks,$mkato_replace);
                $ks = random($ks);
                $shead = replacementcustom($shead,$mkato_replace);
                $shead = random($shead);
                $message->getHeaders()->addTextHeader($ks, $shead);
            }
        $message->getHeaders()->get('Content-Type')->setParameter('charset', $mkato_setting['charset']);
        $message->getHeaders()->get('Content-Transfer-Encoding')->setValue($mkato_setting['encoding']);
        if ($mkato_inbox['attachfile'] != NULL) {
                $daste = explode("|", $mkato_inbox['attachfile']);
                $dastu = explode("|", $mkato_inbox['attachname']);
                for ($i=0; $i < count($daste); $i++) {
                    $attachment = Swift_Attachment::fromPath('attachment/'.$daste[$i]);
                    $attachment->setFilename(replacementcustom(random($dastu[$i]),$mkato_replace));
                    $message->attach($attachment);
                }

            }


        // Send the message
        $mailer->send($message);
        return array('status' => 'ok', 'info' => '');
    } catch (Exception $e) {
      file_put_contents('log/'.date('F d Y D').".txt", implode("\r\n", $mkato_list), FILE_APPEND);
      return array('status' => 'bad', 'info' => $e->getmessage());
    }
}



echo 'sukses';
?>