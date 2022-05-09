from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl
import os
import sys
import argparse

if __name__ == '__main__':

  top_parser = argparse.ArgumentParser(description='Simple HTTPS server')
  top_parser.add_argument('--port', action="store", dest="port", type=int, help="The port to listen on", default="443")
  top_parser.add_argument('--model', action="store", dest="model", required=True, help="The model to emulate.", default="443")
  args = top_parser.parse_args()
  
  options = [ "atp100", "atp200", "atp500", "atp700", "usgflex100", "usgflex100w", "usgflex200", "usgflex500", "usgflex700", "usg20-vpn", "usg20w-vpn"]
  if args.model not in options:
    print("[!] Provided model is not an option. Please select one of the following:")
    for option in options:
      print("\t- " + option)
    sys.exit(0)
  
  os.system("openssl req -nodes -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -subj '/CN=mylocalhost'")
    
  httpd = HTTPServer(('0.0.0.0', args.port), SimpleHTTPRequestHandler)
  sslctx = ssl.SSLContext()
  sslctx.check_hostname = False 
  sslctx.load_cert_chain(certfile='cert.pem', keyfile="key.pem")
  os.chdir(args.model)
  httpd.socket = sslctx.wrap_socket(httpd.socket, server_side=True)
  print(f"Server running on https://0.0.0.0:{args.port}")
  httpd.serve_forever()

