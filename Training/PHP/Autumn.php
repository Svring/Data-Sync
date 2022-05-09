<?php
#传值，变量名为'ctf'
if (!isset($_GET["ctf"])) {
    highlight_file(__FILE__);
    die();
}

#传入的值赋值给变量'ctf'
if(isset($_GET["ctf"]))
    $ctf = $_GET["ctf"];

#当'ctf'的值为'upload'时，进入if语句内部
if($ctf=="upload") {
    #上传文件的大小不能超过1024*512字节
    #为什么get方法上传的文件在postedFile里，NTR吗。
    if ($_FILES['postedFile']['size'] > 1024*512) {
        die("这么大个的东西你是想d我吗？");
    }
    #获取图片信息
    $imageinfo = getimagesize($_FILES['postedFile']['tmp_name']);
    #如果上传文件不是图片，则上传失败
    if ($imageinfo === FALSE) {
        die("如果不能好好传图片的话就还是不要来打扰我了");
    }
    #要求图片宽和高都为一个像素
    if ($imageinfo[0] !== 1 && $imageinfo[1] !== 1) {
        die("东西不能方方正正的话就很讨厌");
    }
    #解码上传的文件的原名称，十六进制字符串转中文字符
    $fileName=urldecode($_FILES['postedFile']['name']);
    #大小写不敏感的检测
    if(stristr($fileName,"c") || stristr($fileName,"i") || stristr($fileName,"h") || stristr($fileName,"ph")) {
        die("有些东西让你传上去的话那可不得了");
    }
    #mb_strtolower字符串转小写，拼在image/后面
    $imagePath = "image/" . mb_strtolower($fileName);
    #移动上传的文件到imagePath
    if(move_uploaded_file($_FILES["postedFile"]["tmp_name"], $imagePath)) {
        echo "upload success, image at $imagePath";
    } else {
        die("传都没有传上去");
    }
}