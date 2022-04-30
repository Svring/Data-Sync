<?php 
highlight_file(__FILE__);
//显示文件内容
function check_inner_ip($url) 
{ 
    $match_result=preg_match('/^(http|https)?:\/\/.*(\/)?.*$/',$url); 
    #进行正则表达式格式检查
    #要求以http或https开头，？表示匹配零次或一次
    #':\/\/'匹配接在http后的://
    #'.'匹配任意一个字符，'*'表示重复次数不限
    #'(\/)?'匹配零次或一次/
    #'$'表示结束
    if (!$match_result) 
    { 
        die('url fomat error'); 
        #格式不正确则退出
    } 
    try 
    { 
        $url_parse=parse_url($url); 
        #把url分段存入数组
    } 
    catch(Exception $e) 
    { 
        die('url fomat error'); 
        #出现任意异常类型，程序结束
        return false; 
        #无法传递的False波
    } 
    $hostname=$url_parse['host']; 
    $ip=gethostbyname($hostname); 
    #用域名获取地址
    $int_ip=ip2long($ip); 
    #ip地址转换为数字形式（'2'是谐音梗？）
    return ip2long('127.0.0.0')>>24 == $int_ip>>24 || ip2long('10.0.0.0')>>24 == $int_ip>>24 || ip2long('172.16.0.0')>>20 == $int_ip>>20 || ip2long('192.168.0.0')>>16 == $int_ip>>16; 
    #判断是否为私有地址，详见（2），'>>'表示比特位右移
} 

function safe_request_url($url) 
{ 
     
    if (check_inner_ip($url)) 
    { 
        echo $url.' is inner ip'; 
        #如果是私有地址，则显示此行
    } 
    else 
    {
        $ch = curl_init(); 
        #初始化一个curl会话，详见（3）
        curl_setopt($ch, CURLOPT_URL, $url); 
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1); 
        curl_setopt($ch, CURLOPT_HEADER, 0); 
        #设置请求选项
        $output = curl_exec($ch); 
        #执行curl请求，返回到变量output
        $result_info = curl_getinfo($ch); 
        #curl_getinfo详见（1）
        if ($result_info['redirect_url']) 
        { 
            safe_request_url($result_info['redirect_url']); 
            #传入重定向的地址
        } 
        curl_close($ch); 
        #关闭会话
        var_dump($output); 
        #显示flag
    } 
     
} 

$url = $_GET['url']; 
//接收变量url
if(!empty($url)){ 
    safe_request_url($url); 
    #url非空的情况下，传入safe函数
} 
?>
