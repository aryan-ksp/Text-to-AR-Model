Text-to-AR Model

This project converts text descriptions into depth maps and then into 3D models using Python and various AI-based libraries. The output is a .obj file that can be viewed in 3D modeling tools.

🚀 Features

Generates a depth map from text input.

Converts the depth map into a 3D model (.obj file).

Simple Flask web app to interact with the model.

Supports Trimesh for 3D mesh processing.

🛠️ Installation

1️⃣ Install Dependencies

Make sure you have Python 3.12 installed, then run:

pip install torch torchvision torchaudio openai trimesh flask numpy opencv-python matplotlib

📂 Project Directory Structure

Text-to-AR-Model/
│-- static/              # Stores generated images & models
│   ├── depth_map.png    # Generated depth map
│   ├── model.obj        # 3D object file
│-- templates/           # HTML templates for Flask
│   ├── index.html
│-- app.py               # Flask application
│-- depth_to_3d.py       # Converts depth map to 3D model
│-- requirements.txt     # Project dependencies
│-- README.md            # Project documentation

🔧 Usage

2️⃣ Run the Flask App

python app.py

3️⃣ Open the Web App

Once the server starts, open your browser and go to:

http://127.0.0.1:5000/

Upload a depth map or enter a text prompt, and the app will generate a 3D model (.obj) file.

🖥️ Viewing the .obj Model

Option 1: Using Blender

Open Blender.

Go to File → Import → Wavefront (.obj).

Select static/model.obj and import.

Option 2: Using Windows 3D Viewer

Locate static/model.obj.

Right-click → Open With → 3D Viewer.

Option 3: Using an Online Viewer

Upload to:

Sketchfab

3DViewer.net

❌ Troubleshooting

Error: "IndexError: index ... out of bounds"

Ensure the depth map is correctly generated.

Try resizing the depth map to 256x256 before processing.

Generated model looks flat (just a wall)?

Depth map might not have enough variation.

Adjust brightness/contrast before processing.

📌 Future Improvements

Integrate Shap-E or MeshGPT for better 3D structure generation.

Add text-to-3D generation directly without requiring a depth map.

🤝 Contributing

Pull requests are welcome! Feel free to submit any bug fixes or improvements.

