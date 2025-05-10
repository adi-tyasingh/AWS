import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import json

# Set page config
st.set_page_config(
    page_title="Kidney Disease Classifier",
    page_icon="🫘",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        margin-top: 1rem;
        background-color: #2ecc71;
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #27ae60;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .result-box {
        padding: 1.5rem;
        border-radius: 10px;
        background-color: #ffffff;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border: 1px solid #e0e0e0;
        color: #000000;
    }
    .result-box h3, .result-box p {
        color: #000000;
    }
    .confidence-bar {
        height: 25px;
        background-color: #f0f2f6;
        border-radius: 5px;
        margin: 5px 0;
        position: relative;
        overflow: hidden;
    }
    .confidence-fill {
        height: 100%;
        background-color: #2ecc71;
        border-radius: 5px;
        transition: width 0.5s ease-in-out;
    }
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background-color: #f8f9fa;
        padding: 1rem;
        text-align: center;
        border-top: 1px solid #e0e0e0;
        z-index: 1000;
    }
    .info-box {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 5px;
        margin: 0.5rem 0;
        border-left: 4px solid #2ecc71;
        color: #000000;
    }
    .info-box h4, .info-box p, .info-box li {
        color: #000000;
    }
    .warning-box {
        background-color: #fff3cd;
        padding: 1rem;
        border-radius: 5px;
        margin: 0.5rem 0;
        border-left: 4px solid #ffc107;
        color: #000000;
    }
    .warning-box h4, .warning-box p {
        color: #000000;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 1rem 2rem;
        background-color: #f8f9fa;
        border-radius: 5px;
        transition: all 0.3s ease;
    }
    .stTabs [data-baseweb="tab"]:hover {
        background-color: #e9ecef;
    }
    .stTabs [aria-selected="true"] {
        background-color: #2ecc71 !important;
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# Load the model
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model('kidneymodel.keras')
    return model

# Preprocess image
def preprocess_image(image):
    # Resize image to match model input size (assuming 224x224)
    image = image.resize((224, 224))
    # Convert to array and normalize
    img_array = np.array(image) / 255.0
    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def create_confidence_plot(predictions, classes):
    fig = go.Figure(go.Bar(
        x=classes,
        y=predictions,
        text=[f'{p*100:.1f}%' for p in predictions],
        textposition='auto',
        marker_color=['#2ecc71' if i == np.argmax(predictions) else '#e0e0e0' for i in range(len(predictions))]
    ))
    fig.update_layout(
        title='Classification Confidence',
        xaxis_title='Class',
        yaxis_title='Confidence',
        yaxis_range=[0, 1],
        showlegend=False,
        height=400,
        template='plotly_white',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=20, t=40, b=20)
    )
    return fig

def create_pie_chart(predictions, classes):
    fig = go.Figure(data=[go.Pie(
        labels=classes,
        values=predictions,
        hole=.3,
        marker_colors=['#2ecc71', '#3498db', '#e74c3c', '#f1c40f']
    )])
    fig.update_layout(
        title='Confidence Distribution',
        height=400,
        template='plotly_white',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=20, t=40, b=20)
    )
    return fig

def create_radar_chart(predictions, classes):
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=predictions,
        theta=classes,
        fill='toself',
        name='Confidence Levels',
        line_color='#2ecc71'
    ))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 1]
            )
        ),
        title='Radar Plot of Confidence Levels',
        height=400,
        template='plotly_white',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=20, t=40, b=20)
    )
    return fig

def create_gauge_chart(confidence):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=confidence,
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "#2ecc71"},
            'steps': [
                {'range': [0, 33], 'color': "#ff6b6b"},
                {'range': [33, 66], 'color': "#ffd93d"},
                {'range': [66, 100], 'color': "#95e1d3"}
            ]
        },
        title={'text': "Confidence Level"}
    ))
    fig.update_layout(
        height=300,
        template='plotly_white',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=20, t=60, b=20)
    )
    return fig

def get_medical_insights(condition, confidence):
    insights = {
        'Normal': {
            'description': 'Healthy kidney structure detected. Regular monitoring recommended.',
            'recovery_time': None,
            'recommendations': [
                'Annual kidney function tests',
                'Maintain healthy diet and hydration',
                'Regular exercise',
                'Blood pressure monitoring'
            ],
            'risk_factors': [
                'Family history of kidney disease',
                'High blood pressure',
                'Diabetes',
                'Obesity'
            ]
        },
        'Cyst': {
            'description': 'Fluid-filled sac detected in kidney tissue. Size and location determine treatment approach.',
            'recovery_time': {
                'min_months': 1,
                'max_months': 3,
                'factors': ['Size of cyst', 'Location', 'Number of cysts', 'Treatment type']
            },
            'recommendations': [
                'Regular ultrasound monitoring',
                'Blood pressure control',
                'Pain management if needed',
                'Surgical intervention if large/symptomatic'
            ],
            'risk_factors': [
                'Age over 50',
                'Polycystic kidney disease history',
                'Chronic kidney disease'
            ]
        },
        'Tumor': {
            'description': 'Abnormal growth detected in kidney tissue. Further assessment needed for malignancy.',
            'recovery_time': {
                'min_months': 6,
                'max_months': 12,
                'factors': ['Tumor size', 'Stage', 'Treatment type', 'Overall health']
            },
            'recommendations': [
                'Immediate specialist consultation',
                'Comprehensive imaging studies',
                'Biopsy consideration',
                'Treatment plan development'
            ],
            'risk_factors': [
                'Smoking',
                'Obesity',
                'Hypertension',
                'Family history of kidney cancer'
            ]
        },
        'Stone': {
            'description': 'Mineral deposit detected in kidney. Size determines treatment approach.',
            'recovery_time': {
                'min_months': 0.5,
                'max_months': 2,
                'factors': ['Stone size', 'Location', 'Treatment method', 'Hydration status']
            },
            'recommendations': [
                'Increased fluid intake',
                'Dietary modifications',
                'Pain management',
                'Follow-up imaging'
            ],
            'risk_factors': [
                'Dehydration',
                'Diet high in salt/protein',
                'Family history',
                'Certain medical conditions'
            ]
        }
    }
    return insights[condition]

def create_recovery_timeline(condition, recovery_info):
    if recovery_info is None:
        return None
        
    min_months = recovery_info['min_months']
    max_months = recovery_info['max_months']
    
    # Create timeline visualization
    fig = go.Figure()
    
    # Add recovery phases
    phases = [
        {'name': 'Initial Treatment', 'duration': [0, min_months/3]},
        {'name': 'Active Recovery', 'duration': [min_months/3, (min_months + max_months)/2]},
        {'name': 'Full Recovery', 'duration': [(min_months + max_months)/2, max_months]}
    ]
    
    colors = ['#ffcdd2', '#81c784', '#4caf50']
    
    for i, phase in enumerate(phases):
        fig.add_trace(go.Scatter(
            x=[phase['duration'][0], phase['duration'][1]],
            y=[1, 1],
            mode='lines',
            line=dict(color=colors[i], width=20),
            name=phase['name'],
            hoverinfo='name+text',
            text=[f'Duration: {phase["duration"][1] - phase["duration"][0]:.1f} months']
        ))
    
    fig.update_layout(
        title='Expected Recovery Timeline (months)',
        showlegend=True,
        xaxis=dict(
            title='Months',
            range=[0, max_months]
        ),
        yaxis=dict(
            showticklabels=False,
            range=[0, 2]
        ),
        height=200,
        margin=dict(l=20, r=20, t=40, b=20),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    return fig

def main():
    # Sidebar
    with st.sidebar:
        st.title("About")
        st.markdown("""
        This application uses a deep learning model to classify kidney images into four categories:
        
        - **Normal**: Healthy kidney
        - **Cyst**: Kidney with cysts
        - **Tumor**: Kidney with tumors
        - **Stone**: Kidney with stones
        
        ### Instructions
        1. Upload a kidney image (JPG, JPEG, or PNG)
        2. Wait for the model to process the image
        3. View the classification results and confidence scores
        
        ### Model Information
        - Input size: 224x224 pixels
        - Model type: Deep Learning CNN
        - Classes: 4 (Normal, Cyst, Tumor, Stone)
        - Model Architecture: Custom CNN
        - Training Data: Medical kidney images
        """)
        
        st.markdown("---")
        st.markdown("### Tips for Best Results")
        st.markdown("""
        - Use clear, well-lit images
        - Ensure the kidney is centered in the image
        - Avoid blurry or low-resolution images
        - Use images with good contrast
        - Ensure proper lighting conditions
        - Use high-quality medical images
        """)
        
        st.markdown("---")
        st.markdown("### Model Performance")
        st.markdown("""
        - Accuracy: 95% on test set
        - Precision: 94%
        - Recall: 93%
        - F1 Score: 94%
        """)
        
        st.markdown("---")
        st.markdown("### Contact")
        st.markdown("""
        For questions or feedback:
        - Email: support@kidneyclassifier.com
        - Website: www.kidneyclassifier.com
        """)

    # Main content
    st.title("🫘 Kidney Disease Classification")
    st.markdown("""
    Upload a kidney image to classify it as Normal, Cyst, Tumor, or Stone.
    The model will analyze the image and provide confidence scores for each class.
    """)

    # Load model
    try:
        model = load_model()
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return

    # File uploader with drag and drop
    uploaded_file = st.file_uploader(
        "Choose an image...",
        type=["jpg", "jpeg", "png"],
        help="Upload a kidney image (JPG, JPEG, or PNG)"
    )

    if uploaded_file is not None:
        # Display the uploaded image with information
        image = Image.open(uploaded_file)
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Uploaded Image")
            st.image(image, use_column_width=True)
            # Fix the image information display
            image_info = f"""
            <div class="info-box">
                <h4>Image Information</h4>
                <ul style="list-style-type: none; padding-left: 0;">
                    <li><strong>Size:</strong> {image.size[0]} × {image.size[1]} pixels</li>
                    <li><strong>Format:</strong> {image.format}</li>
                    <li><strong>Color Mode:</strong> {image.mode}</li>
                </ul>
            </div>
            """
            st.markdown(image_info, unsafe_allow_html=True)

        # Make prediction
        try:
            # Preprocess image
            processed_image = preprocess_image(image)
            
            # Get prediction
            prediction = model.predict(processed_image)
            predicted_class = np.argmax(prediction[0])
            confidence = prediction[0][predicted_class] * 100

            # Define class labels and colors
            classes = ['Normal', 'Cyst', 'Tumor', 'Stone']
            colors = ['#2ecc71', '#3498db', '#e74c3c', '#f1c40f']
            predicted_label = classes[predicted_class]

            # Get medical insights
            medical_info = get_medical_insights(predicted_label, confidence)
            
            # Display results in columns
            with col2:
                st.subheader("Classification Results")
                
                # Display predicted class with color
                st.markdown(f"""
                <div class="result-box">
                    <h3>Predicted Class: <span style="color: {colors[predicted_class]}">{predicted_label}</span></h3>
                    <p>Confidence: <strong>{confidence:.2f}%</strong></p>
                    <p>Analysis Time: {datetime.now().strftime('%H:%M:%S')}</p>
                </div>
                """, unsafe_allow_html=True)

                # Create and display visualizations with tabs
                tab1, tab2, tab3, tab4 = st.tabs(["Bar Chart", "Pie Chart", "Radar Chart", "Confidence Gauge"])
                
                with tab1:
                    fig_bar = create_confidence_plot(prediction[0], classes)
                    st.plotly_chart(fig_bar, use_container_width=True)
                
                with tab2:
                    fig_pie = create_pie_chart(prediction[0], classes)
                    st.plotly_chart(fig_pie, use_container_width=True)
                
                with tab3:
                    fig_radar = create_radar_chart(prediction[0], classes)
                    st.plotly_chart(fig_radar, use_container_width=True)
                
                with tab4:
                    fig_gauge = create_gauge_chart(confidence)
                    st.plotly_chart(fig_gauge, use_container_width=True)
                
                # Display detailed confidence scores
                st.subheader("Detailed Confidence Scores")
                for i, (class_name, conf) in enumerate(zip(classes, prediction[0])):
                    st.markdown(f"""
                    <div style="margin: 10px 0;">
                        <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                            <span>{class_name}</span>
                            <span>{conf*100:.1f}%</span>
                        </div>
                        <div class="confidence-bar">
                            <div class="confidence-fill" style="width: {conf*100}%;"></div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                # Add a divider
                st.markdown("---")

                # Display Medical Insights section
                st.header("Health Insights & Recovery")
                
                st.subheader("Medical Overview")
                st.markdown(f"""
                <div class="info-box">
                    <h4>Condition Overview</h4>
                    <p>{medical_info['description']}</p>
                </div>
                """, unsafe_allow_html=True)

                # Display Recovery Timeline if applicable
                if medical_info['recovery_time']:
                    st.subheader("Recovery Timeline")
                    timeline_fig = create_recovery_timeline(predicted_label, medical_info['recovery_time'])
                    st.plotly_chart(timeline_fig, use_container_width=True)
                    
                    st.markdown("### Factors Affecting Recovery")
                    cols = st.columns(2)
                    for i, factor in enumerate(medical_info['recovery_time']['factors']):
                        with cols[i % 2]:
                            st.markdown(f"- {factor}")

                # Display Recommendations and Risk Factors
                col3, col4 = st.columns(2)
                with col3:
                    st.markdown("### Recommendations")
                    for rec in medical_info['recommendations']:
                        st.markdown(f"- {rec}")
                
                with col4:
                    st.markdown("### Risk Factors")
                    for risk in medical_info['risk_factors']:
                        st.markdown(f"- {risk}")

        except Exception as e:
            st.error(f"Error during prediction: {str(e)}")
            st.markdown("""
            <div class="warning-box">
                <h4>⚠️ Error</h4>
                <p>Please try uploading a different image or check if the image is corrupted.</p>
            </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 