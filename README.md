# 🌱 AgroAI – Smart Plant Health Assistant

## Professional Offline Plant Disease Detection Web App

AgroAI is a cutting-edge, fully-functional offline web application designed for detecting plant diseases using modern AI-simulation technology. Built with Python Flask and featuring a professional SaaS-style dashboard, it empowers farmers and agricultural professionals to identify plant diseases early and take preventive action.

### ✨ Key Features

- **Offline Operation**: Complete functionality without internet - perfect for rural areas
- **Multi-Language Support**: English, Hindi, and Kannada - Instantly switch languages
- **Professional SaaS Dashboard**: Modern dark theme with glassmorphic UI design
- **Smart Image Analysis**: Upload plant images and get instant disease predictions
- **Real-time Weather Integration**: Local weather conditions for better crop management
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Intuitive Sidebar Navigation**: Easy access to all features with smooth animations
- **Detailed Disease Information**: Comprehensive cause, symptoms, prevention, and treatment
- **Zero Database Required**: All data stored locally in-memory
- **Educational & Professional**: Perfect for college projects and startup demos

### 🎯 Supported Diseases

1. **Tomato Early Blight** - Fungal infection with dark concentric spots
2. **Leaf Spot Disease** - Bacterial/fungal infection with yellow/brown spots
3. **Rust Disease** - Fungal spores causing orange powder spots
4. **Healthy Plant** - No disease detected
5. **Unknown** - Unable to identify from image

### 🛠️ Technology Stack

- **Backend**: Python 3.x + Flask
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Design**: Modern glassmorphism, dark theme, responsive grid layout
- **Styling**: Custom CSS with animations, Google Fonts (Poppins)
- **Language**: Multi-language support (JavaScript-based, no API)
- **Weather**: Open-Meteo free API (no API key required)

### 📋 Project Structure

```
AgroAI/
│
├── app.py                          # Flask backend application
│
├── templates/
│   ├── index.html                  # Home page with sidebar & upload
│   └── result.html                 # Disease analysis result page
│
├── static/
│   ├── style.css                   # Professional dark theme CSS
│   ├── script.js                   # JavaScript functionality
│   └── uploads/                    # Temporary image storage
│
└── README.md                        # This file
```

### 🚀 Quick Start Guide

#### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- Modern web browser (Chrome, Firefox, Safari, Edge)

#### Installation & Running

1. **Clone or download the project**:
   ```bash
   cd AgroAI
   ```

2. **Install Flask**:
   ```bash
   pip install flask
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Open in browser**:
   ```
   http://127.0.0.1:5000
   ```

5. **Start analyzing plants**:
   - Upload a plant leaf image
   - Click "Analyze Plant"
   - View detailed disease information
   - Apply prevention and treatment tips

### 📱 Features Detailed

#### 1. **Sidebar Navigation**
- Home - Main dashboard
- Upload & Predict - Image upload and analysis
- Weather - Current local weather conditions
- Usage Tips - Step-by-step guide
- Language - Switch between English, Hindi, Kannada
- About - Team information and contact

#### 2. **Drag & Drop Upload**
- Simple drag-and-drop interface
- Click to browse files
- Real-time image preview
- File validation

#### 3. **Disease Analysis**
- Rule-based prediction engine
- Confidence scores
- Risk level indicators (Low/Medium/High)
- Color-coded severity badges

#### 4. **Weather Widget**
- Real-time location weather
- Temperature display
- Humidity information
- Weather condition icons

#### 5. **Multi-Language Support**
- English (Default)
- हिंदी (Hindi)
- ಕನ್ನಡ (Kannada)
- **Instant language switching** - All UI text changes immediately when you select language
- Smooth language switching via sidebar
- Persistent language preference (saved in browser)
- Works completely offline - no translation API needed

#### 6. **Professional UI/UX**
- Dark mode with green accent colors
- Smooth animations and transitions
- Mobile-responsive design
- Accessibility-focused
- Modern typography with Google Fonts

### 🎨 UI/UX Highlights

- **Dark Theme**: Eye-friendly dark background with vibrant green accents
- **Glassmorphism**: Modern frosted glass effect on cards
- **Responsive Grid**: Auto-adapting layouts for all screen sizes
- **Smooth Animations**: Fade-in, slide-in, bounce, and hover effects
- **Professional Spacing**: Perfect padding and margins throughout
- **Color Coding**: Green (Healthy), Yellow (Warning), Red (Disease)

### 🔍 How Disease Prediction Works

The prediction system uses **filename-based intelligent matching**:

```
Image filename contains:
- "tomato" → Tomato Early Blight
- "leaf" → Leaf Spot Disease
- "rust" → Rust Disease
- "healthy" → Healthy Plant
- else → Unknown Disease
```

*Note: For demo purposes, name your test images accordingly. In production, this would use actual ML models.*

### 📊 Disease Information Provided

For each detected disease, the app provides:

1. **Cause** - Root cause of the disease
2. **Symptoms** - Visual indicators to look for
3. **Prevention** - Preventive measures to avoid disease
4. **Treatment** - Treatment options and remedies
5. **Confidence Score** - Prediction accuracy percentage
6. **Risk Level** - Green/Yellow/Red severity badge

### 🌐 API Endpoints

```
GET  /                    - Home page
POST /predict             - Upload image and get prediction
GET  /api/weather         - Get current weather data
```

### 🔐 Data Privacy

- ✅ All processing happens locally
- ✅ No data sent to external servers
- ✅ Images stored temporarily in /static/uploads
- ✅ No user tracking or analytics
- ✅ No database - everything in-memory
- ✅ Educational purposes only

### 👥 Team Information

**Team: S3V Developers**

Passionate developers creating intelligent agricultural solutions for sustainable farming.

**Contact:**
- 📧 thantrysharanya@gmail.com

**Works Offline:** ✅ Complete offline functionality - no internet required!

### ⚠️ Disclaimer

⚖️ **This project is for educational purposes only.**

This application is NOT a substitute for professional agricultural advice. Always consult with qualified agricultural experts or plant pathologists for accurate disease diagnosis and treatment recommendations. The predictions are based on simplified rule-based logic for demonstration purposes.

### 💡 Perfect For

- 🎓 College/University projects
- 🏆 Tech competitions
- 💼 Startup demos
- 📚 Educational presentations
- 🌾 Agricultural hackathons
- 👨‍💻 Portfolio projects

### 🚀 Future Enhancement Ideas

- Integration with ML models for better accuracy
- Database integration for user history
- Offline ML models using TensorFlow.js
- Mobile app wrapper (React Native/Flutter)
- Community forum for farmers
- Video upload support
- Real-time crop monitoring
- SMS/WhatsApp notifications
- Integration with agricultural experts
- IoT sensor integration

### 📝 License

Free to use for educational and non-commercial purposes.

### 🤝 Contributing

Students and developers are welcome to contribute and improve this project!

---

**Built with ❤️ by S3V Developers**

*"Helping farmers detect plant diseases early for sustainable agriculture"*

Last Updated: May 2026