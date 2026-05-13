from flask import Flask, request, render_template, redirect, url_for, jsonify
import os
from datetime import datetime

app = Flask(__name__)

# Ensure upload directory exists
UPLOAD_FOLDER = 'static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def get_disease_info(filename):
    """Predict disease based on filename with disease severity"""
    filename_lower = filename.lower()
    
    if 'tomato' in filename_lower:
        return {
            'name': 'Tomato Early Blight',
            'severity': 'high',
            'color': 'red',
            'cause': 'Fungal infection caused by Alternaria solani',
            'symptoms': 'Dark brown spots with concentric rings on lower leaves, yellowing around spots',
            'prevention': 'Avoid overwatering, improve air circulation, remove lower leaves, crop rotation',
            'treatment': 'Remove infected leaves, apply fungicide, improve plant ventilation',
            'confidence': '92%'
        }
    elif 'leaf' in filename_lower:
        return {
            'name': 'Leaf Spot Disease',
            'severity': 'medium',
            'color': 'yellow',
            'cause': 'Bacterial or fungal infection spreading through water droplets',
            'symptoms': 'Yellow/brown spots with halos, spots may have concentric rings',
            'prevention': 'Proper spacing between plants, avoid overhead watering, remove infected leaves',
            'treatment': 'Fungicide spray, remove affected leaves, improve drainage',
            'confidence': '88%'
        }
    elif 'rust' in filename_lower:
        return {
            'name': 'Rust Disease',
            'severity': 'high',
            'color': 'red',
            'cause': 'Fungal spores thriving in warm, wet conditions',
            'symptoms': 'Orange/reddish powder-like spots on leaf undersides, yellow spots on upper side',
            'prevention': 'Crop rotation, resistant varieties, proper spacing for air circulation',
            'treatment': 'Remove infected leaves, apply sulfur-based fungicide, improve ventilation',
            'confidence': '90%'
        }
    elif 'healthy' in filename_lower:
        return {
            'name': 'Healthy Plant',
            'severity': 'none',
            'color': 'green',
            'cause': 'No disease detected',
            'symptoms': 'Plant shows normal growth and development',
            'prevention': 'Continue current care practices, maintain proper watering schedule',
            'treatment': 'No treatment required - maintain good agricultural practices',
            'confidence': '95%'
        }
    else:
        return {
            'name': 'Unknown Plant Status',
            'severity': 'unknown',
            'color': 'gray',
            'cause': 'Unable to identify plant type from image',
            'symptoms': 'Further analysis required',
            'prevention': 'Upload clearer image with plant leaf visible',
            'treatment': 'Consult agricultural expert for detailed diagnosis',
            'confidence': '45%'
        }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify({'error': 'No file uploaded'})
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify({'error': 'No file selected'})
        return redirect(request.url)
    
    if file:
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        result = get_disease_info(filename)
        
        # Format data for JSON response
        response_data = {
            'disease': result['name'],
            'severity': result['severity'].upper(),
            'color': result['color'],
            'description': result['symptoms'],
            'causes': [result['cause']],
            'treatment': result['treatment'].split(', '),
            'prevention': result['prevention'].split(', '),
            'image': url_for('static', filename=f'uploads/{filename}'),
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M')
        }
        
        # Check if it's an AJAX request
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify(response_data)
        else:
            # Traditional form submission - render template
            return render_template('result.html', result=result)

@app.route('/api/weather')
def get_weather():
    """Fetch weather data from Open-Meteo API (free, no API key needed)"""
    try:
        import urllib.request
        import json
        
        # Using Open-Meteo API - free weather API
        url = "https://api.open-meteo.com/v1/forecast?latitude=28.6139&longitude=77.2090&current=temperature_2m,weather_code,relative_humidity_2m&temperature_unit=celsius"
        
        with urllib.request.urlopen(url, timeout=5) as response:
            data = json.loads(response.read())
            current = data.get('current', {})
            
            weather_codes = {
                0: '☀️ Clear',
                1: '🌤️ Mostly Clear',
                2: '⛅ Partly Cloudy',
                3: '☁️ Cloudy',
                45: '🌫️ Foggy',
                48: '🌫️ Foggy',
                51: '🌧️ Light Drizzle',
                53: '🌧️ Moderate Drizzle',
                55: '🌧️ Heavy Drizzle',
                61: '🌧️ Slight Rain',
                63: '🌧️ Moderate Rain',
                65: '⛈️ Heavy Rain',
                80: '🌧️ Light Showers',
                81: '🌧️ Moderate Showers',
                82: '⛈️ Heavy Showers',
                95: '⛈️ Thunderstorm',
                96: '⛈️ Thunderstorm with Hail',
                99: '⛈️ Thunderstorm with Hail'
            }
            
            weather_code = current.get('weather_code', 0)
            weather_desc = weather_codes.get(weather_code, '🌤️ Unknown')
            
            return jsonify({
                'success': True,
                'temperature': current.get('temperature_2m', 'N/A'),
                'weather': weather_desc,
                'humidity': current.get('relative_humidity_2m', 'N/A'),
                'location': 'India'
            })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': 'Weather data unavailable',
            'error': str(e)
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)