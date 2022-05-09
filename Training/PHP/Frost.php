<?php
#传值，变量名为'ctf'
if (!isset($_GET["ctf"])) {
    highlight_file(__FILE__);
    die();
}

if(isset($_GET["ctf"]))
    $ctf = $_GET["ctf"];

#当'ctf'的值为'poc'时，执行解压程序
if($ctf=="poc") {
    #初始化一个ZipArchive对象
    $zip = new \ZipArchive();
    #要压缩的文件在example下，用post方法上传的文件名
    $name_for_zip = "example/" . $_POST["file"];
    #后缀不为zip则退出程序
    if(explode(".",$name_for_zip)[count(explode(".",$name_for_zip))-1]!=="zip") {
        die("要不咱们再看看？");
    }
    if ($zip->open($name_for_zip) !== TRUE) {
        die ("都不能解压呢");
    }

    #要求文件后缀为zip，且可以解压
    echo "可以解压，我想想存哪里";
    #对当前用户的ip地址进行md5加密
    $pos_for_zip = "/tmp/example/" . md5($_SERVER["REMOTE_ADDR"]);
    #解压到该地址
    $zip->extractTo($pos_for_zip);
    $zip->close();
    unlink($name_for_zip);
    #获取解压位置的地址
    $files = glob("$pos_for_zip/*");
    foreach($files as $file){
        if (is_dir($file)) {
            continue;
        }
        #从文件中提取图片信息
        $first = imagecreatefrompng($file);
        #从宽度和高度中选择较小的那一个
        $size = min(imagesx($first), imagesy($first));
        $second = imagecrop($first, ['x' => 0, 'y' => 0, 'width' => $size, 'height' => $size]);
        if ($second !== FALSE) {
            $final_name = pathinfo($file)["basename"];
            imagepng($second, 'example/'.$final_name);
            imagedestroy($second);
        }
        #删除图片和文件
        imagedestroy($first);
        unlink($file);
    }
}