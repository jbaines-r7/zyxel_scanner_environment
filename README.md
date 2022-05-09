# Zyxel Version Scanning Test Setup

The targets of interest (USG FLEX, USG20-VPN, and ATP) all have versioning information in the management web interface's index.html. This allows an unauthenticated and remote individual to get semi-accurate information on versioning. In particular, the individual can extract two things:

1. The specific model of appliance. e.g. ATP200 or USG FLEX 100.
2. The date the firmware was assembled. This value is appended to `ico`, `.css` and `.js` fetches (although older versions only seem to appened it to the `.ico`). E.g. `favicon.ico?v=220315035335` is March 15, 2022. This date is typically a few days before the actual firmware release though. 🤷‍♂️

The embeded `index.html` are from live samples taken off of Shodan. Some of them probably still contain their IP address but no biggie. These are publicly facing pages with no authentication that we've borrowed for testing purposes.

## Usage Example:

```
albinolobster@ubuntu:~/zyxel_scanner_environment$ python3 server.py --model lol
[!] Provided model is not an option. Please select one of the following:
	- atp100
	- atp200
	- atp500
	- atp700
	- usgflex100
	- usgflex100w
	- usgflex200
	- usgflex500
	- usgflex700
	- usg20-vpn
	- usg20w-vpn
albinolobster@ubuntu:~/zyxel_scanner_environment$ sudo python3 server.py --model atp700
[sudo] password for albinolobster: 
Generating a RSA private key
......++++
..................++++
writing new private key to 'key.pem'
-----
Server running on https://0.0.0.0:443
127.0.0.1 - - [09/May/2022 06:34:07] "GET / HTTP/1.1" 200 -
```

```
albinolobster@ubuntu:~$ curl --insecure https://localhost
<!DOCTYPE html>
<html class="x-strict"><head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0,minimum-scale=1.0, maximum-scale=1.0, user-scalable=no">
<meta name="HandheldFriendly" content="true">
<title>ATP700</title>
<link rel="shortcut icon" href="https://76.79.109.196/images/favicon.ico?v=220420024657" type="image/x-icon">
<link href="index_files/bootstrap.css" rel="stylesheet" type="text/css">
<link href="index_files/login.css" rel="stylesheet" type="text/css">
<link href="index_files/responsive.css" rel="stylesheet" type="text/css">
<script type="text/javascript" src="index_files/ext-all.js"></script>
<script type="text/javascript" src="index_files/zld_product_spec.js"></script>
<script type="text/javascript" src="index_files/zyFunction.js"></script>
<link rel="stylesheet" type="text/css" href="index_files/custmiz_page.css">
<script type="text/javascript" src="index_files/language_panel.js"></script>
<script language="javascript" src="index_files/jquery-3.js"></script>
<script language="javascript" src="index_files/custom.js"></script>
<script language="JavaScript">
```
