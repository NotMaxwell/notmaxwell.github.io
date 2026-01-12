#!/usr/bin/env python3
"""
Local web server for testing the site before deployment.

Usage:
    python3 serve.py              # Start server at localhost:8000
    python3 serve.py --port 3000  # Start at custom port
"""

import sys
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

DEFAULT_PORT = 8000
HOST = "localhost"

class SiteHandler(SimpleHTTPRequestHandler):
    """Custom handler that serves index.html for directories."""
    
    def end_headers(self):
        """Add cache control headers."""
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
        self.send_header("Expires", "0")
        super().end_headers()
    
    def do_GET(self):
        """Serve index.html for directory requests."""
        if self.path.endswith('/'):
            self.path += 'index.html'
        return super().do_GET()

def start_server(port=DEFAULT_PORT):
    """Start the local development server."""
    server_address = (HOST, port)
    httpd = HTTPServer(server_address, SiteHandler)
    
    print(f"🚀 Starting local server...")
    print(f"   → http://{HOST}:{port}")
    print(f"   → Press Ctrl+C to stop")
    print()
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n✓ Server stopped")
        sys.exit(0)

if __name__ == "__main__":
    port = DEFAULT_PORT
    
    # Parse arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == "--port" and len(sys.argv) > 2:
            try:
                port = int(sys.argv[2])
            except ValueError:
                print(f"ERROR: Invalid port {sys.argv[2]}")
                sys.exit(1)
        else:
            print(f"Usage: python3 serve.py [--port PORT]")
            sys.exit(1)
    
    start_server(port)
