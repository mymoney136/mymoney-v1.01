from flask import Flask, send_from_directory, jsonify
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__, static_folder='.')

@app.route('/')
def index():
	return send_from_directory('.', 'index.html')

@app.route('/config', methods=['GET'])
def config():
	try:
		# Load environment variables but do NOT expose secrets by default.
		supabase_url = os.getenv('SUPABASE_URL')
		supabase_anon = os.getenv('SUPABASE_ANON_KEY')
		allow_expose = os.getenv('ALLOW_EXPOSE_KEYS', '0')

		has_keys = bool(supabase_url and supabase_anon)

		if allow_expose == '1':
			# Only expose full values if the developer explicitly set ALLOW_EXPOSE_KEYS=1
			return jsonify({'hasKeys': has_keys, 'SUPABASE_URL': supabase_url, 'SUPABASE_ANON_KEY': supabase_anon})
		else:
			# Return presence flag and masked values for safety
			masked_url = None
			masked_anon = None
			if supabase_url:
				masked_url = supabase_url if len(supabase_url) < 8 else supabase_url[:8] + '...'
			if supabase_anon:
				masked_anon = '*****'  # do not reveal anon key unless explicitly allowed
			return jsonify({'hasKeys': has_keys, 'SUPABASE_URL': masked_url, 'SUPABASE_ANON_KEY': masked_anon})
	except Exception as e:
		return jsonify({'hasKeys': False, 'error': str(e)}), 500

@app.errorhandler(404)
def not_found(e):
	# Try to serve static files, otherwise return JSON error
	return jsonify({'error': 'Endpoint not found. Use /config or /'}), 404

if __name__ == '__main__':
	print("Starting Glass Budget server on http://127.0.0.1:8000")
	print("Open in browser: http://localhost:8000")
	app.run(host='127.0.0.1', port=8000, debug=True)

