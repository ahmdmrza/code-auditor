import time
import streamlit as st
import ollama
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

page_bg_img = """
<style>

/* Background styling for the app container */
[data-testid="stAppViewContainer"] {
background: radial-gradient(circle at 24.1% 68.8%, rgb(50, 50, 50) 0%, rgb(0, 0, 0) 80.4%);
}


/* Hover effect for all Streamlit buttons */
button:hover {
    color: #0097b2 !important;
    border: #0097b2 !important;
}

button:active {
    background-color: #c4cccf !important;  /* Keep the same background color as hover */
    color: white !important;               /* White text color on click */
    border-color: #0097b2 !important;     /* Light blue border on click */
}

/* Focus effect to highlight button when clicked/focused */
button:focus {
    color: #0097b2 !important;
    border: #0097b2 !important;
    outline: none;                         /* Remove default focus outline */
    box-shadow: 0 0 5px 2px rgba(0, 151, 178, 0.7);  /* Add a glowing effect */
}

/* Hover effect specifically for file uploader */
[data-testid="stFileUploader"] > label div:hover {
    color: #0097b2 !important;
}



</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

particle_css = """
<style>
body {
    width: 100%;
    height: 100%;
    background-image: radial-gradient(#021027, #000000);
}

.container {
    width: 100%;
    height: 100%;
    position: relative;
}

.circle-container {
    position: absolute;
    transform: translateY(-10vh);
    animation-iteration-count: infinite;
    animation-timing-function: linear;
}

.circle-container .circle {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    mix-blend-mode: screen;
    background-image: radial-gradient(
        hsl(180, 100%, 80%),
        hsl(180, 100%, 80%) 10%,
        hsla(180, 100%, 80%, 0) 56%
    );
    animation: fade-frames 200ms infinite, scale-frames 2s infinite;
}

/* Keyframes for fade and scale animations */
@keyframes fade-frames {
    0% { opacity: 1; }
    50% { opacity: 0.7; }
    100% { opacity: 1; }
}

@keyframes scale-frames {
    0% { transform: scale3d(0.4, 0.4, 1); }
    50% { transform: scale3d(2.2, 2.2, 1); }
    100% { transform: scale3d(0.4, 0.4, 1); }
}

/* Example styling for individual particles */
.circle-container:nth-child(1) .circle {
    width: 8px;
    height: 8px;
    animation-name: move-frames-1;
    animation-duration: 7500ms;
    animation-delay: 5000ms;
}

.circle-container:nth-child(2) .circle {
    width: 7px;
    height: 7px;
    animation-name: move-frames-2;
    animation-duration: 9000ms;
    animation-delay: 3000ms;
}

.circle-container:nth-child(3) .circle {
    width: 6px;
    height: 6px;
    animation-name: move-frames-3;
    animation-duration: 8500ms;
    animation-delay: 4000ms;
}

.circle-container:nth-child(4) .circle {
    width: 9px;
    height: 9px;
    animation-name: move-frames-4;
    animation-duration: 7800ms;
    animation-delay: 2000ms;
}

.circle-container:nth-child(5) .circle {
    width: 5px;
    height: 5px;
    animation-name: move-frames-5;
    animation-duration: 7200ms;
    animation-delay: 2500ms;
}

.circle-container:nth-child(6) .circle {
    width: 10px;
    height: 10px;
    animation-name: move-frames-6;
    animation-duration: 9500ms;
    animation-delay: 1000ms;
}

.circle-container:nth-child(7) .circle {
    width: 4px;
    height: 4px;
    animation-name: move-frames-7;
    animation-duration: 6800ms;
    animation-delay: 3500ms;
}

.circle-container:nth-child(8) .circle {
    width: 11px;
    height: 11px;
    animation-name: move-frames-8;
    animation-duration: 10000ms;
    animation-delay: 6000ms;
}

.circle-container:nth-child(9) .circle {
    width: 7px;
    height: 7px;
    animation-name: move-frames-9;
    animation-duration: 8700ms;
    animation-delay: 4500ms;
}

.circle-container:nth-child(10) .circle {
    width: 6px;
    height: 6px;
    animation-name: move-frames-10;
    animation-duration: 9200ms;
    animation-delay: 3000ms;
}

.circle-container:nth-child(11) .circle {
    width: 8px;
    height: 8px;
    animation-name: move-frames-11;
    animation-duration: 9600ms;
    animation-delay: 5000ms;
}

.circle-container:nth-child(12) .circle {
    width: 9px;
    height: 9px;
    animation-name: move-frames-12;
    animation-duration: 8800ms;
    animation-delay: 2000ms;
}

.circle-container:nth-child(13) .circle {
    width: 6px;
    height: 6px;
    animation-name: move-frames-3;
    animation-duration: 8500ms;
    animation-delay: 4000ms;
}

.circle-container:nth-child(14) .circle {
    width: 9px;
    height: 9px;
    animation-name: move-frames-4;
    animation-duration: 7800ms;
    animation-delay: 2000ms;
}

.circle-container:nth-child(15) .circle {
    width: 5px;
    height: 5px;
    animation-name: move-frames-5;
    animation-duration: 7200ms;
    animation-delay: 2500ms;
}

.circle-container:nth-child(16) .circle {
    width: 10px;
    height: 10px;
    animation-name: move-frames-6;
    animation-duration: 9500ms;
    animation-delay: 1000ms;
}

.circle-container:nth-child(17) .circle {
    width: 4px;
    height: 4px;
    animation-name: move-frames-7;
    animation-duration: 6800ms;
    animation-delay: 3500ms;
}

.circle-container:nth-child(18) .circle {
    width: 11px;
    height: 11px;
    animation-name: move-frames-8;
    animation-duration: 10000ms;
    animation-delay: 6000ms;
}

.circle-container:nth-child(19) .circle {
    width: 7px;
    height: 7px;
    animation-name: move-frames-9;
    animation-duration: 8700ms;
    animation-delay: 4500ms;
}

.circle-container:nth-child(20) .circle {
    width: 6px;
    height: 6px;
    animation-name: move-frames-10;
    animation-duration: 9200ms;
    animation-delay: 3000ms;
}

.circle-container:nth-child(21) .circle {
    width: 8px;
    height: 8px;
    animation-name: move-frames-11;
    animation-duration: 9600ms;
    animation-delay: 5000ms;
}

.circle-container:nth-child(22) .circle {
    width: 9px;
    height: 9px;
    animation-name: move-frames-12;
    animation-duration: 8800ms;
    animation-delay: 2000ms;
}

/* Add more nth-child styles here for each particle if desired */

@keyframes move-frames-1 {
    from { transform: translate3d(10vw, 100vh, 0); }
    to { transform: translate3d(20vw, -10vh, 0); }
}

@keyframes move-frames-2 {
    from { transform: translate3d(30vw, 110vh, 0); }
    to { transform: translate3d(50vw, -15vh, 0); }
}

@keyframes move-frames-3 {
    from { transform: translate3d(15vw, 100vh, 0); }
    to { transform: translate3d(35vw, -20vh, 0); }
}

@keyframes move-frames-4 {
    from { transform: translate3d(25vw, 110vh, 0); }
    to { transform: translate3d(45vw, -25vh, 0); }
}

@keyframes move-frames-5 {
    from { transform: translate3d(5vw, 105vh, 0); }
    to { transform: translate3d(15vw, -15vh, 0); }
}

@keyframes move-frames-6 {
    from { transform: translate3d(35vw, 100vh, 0); }
    to { transform: translate3d(55vw, -20vh, 0); }
}

@keyframes move-frames-7 {
    from { transform: translate3d(10vw, 120vh, 0); }
    to { transform: translate3d(30vw, -15vh, 0); }
}

@keyframes move-frames-8 {
    from { transform: translate3d(40vw, 115vh, 0); }
    to { transform: translate3d(60vw, -10vh, 0); }
}

@keyframes move-frames-9 {
    from { transform: translate3d(20vw, 130vh, 0); }
    to { transform: translate3d(40vw, -15vh, 0); }
}

@keyframes move-frames-10 {
    from { transform: translate3d(0vw, 125vh, 0); }
    to { transform: translate3d(20vw, -5vh, 0); }
}

@keyframes move-frames-11 {
    from { transform: translate3d(30vw, 105vh, 0); }
    to { transform: translate3d(50vw, -30vh, 0); }
}

@keyframes move-frames-12 {
    from { transform: translate3d(5vw, 115vh, 0); }
    to { transform: translate3d(25vw, -20vh, 0); }
}

@keyframes move-frames-13 {
    from { transform: translate3d(15vw, 100vh, 0); }
    to { transform: translate3d(35vw, -20vh, 0); }
}

@keyframes move-frames-14 {
    from { transform: translate3d(25vw, 110vh, 0); }
    to { transform: translate3d(45vw, -25vh, 0); }
}

@keyframes move-frames-15 {
    from { transform: translate3d(5vw, 105vh, 0); }
    to { transform: translate3d(15vw, -15vh, 0); }
}

@keyframes move-frames-16 {
    from { transform: translate3d(35vw, 100vh, 0); }
    to { transform: translate3d(55vw, -20vh, 0); }
}

@keyframes move-frames-17 {
    from { transform: translate3d(10vw, 120vh, 0); }
    to { transform: translate3d(30vw, -15vh, 0); }
}

@keyframes move-frames-18 {
    from { transform: translate3d(40vw, 115vh, 0); }
    to { transform: translate3d(60vw, -10vh, 0); }
}

@keyframes move-frames-19 {
    from { transform: translate3d(20vw, 130vh, 0); }
    to { transform: translate3d(40vw, -15vh, 0); }
}

@keyframes move-frames-20 {
    from { transform: translate3d(0vw, 125vh, 0); }
    to { transform: translate3d(20vw, -5vh, 0); }
}

@keyframes move-frames-21 {
    from { transform: translate3d(30vw, 105vh, 0); }
    to { transform: translate3d(50vw, -30vh, 0); }
}

@keyframes move-frames-22 {
    from { transform: translate3d(5vw, 115vh, 0); }
    to { transform: translate3d(25vw, -20vh, 0); }
}
/* Add more @keyframes for additional particles */
</style>
"""

# Inject CSS
st.markdown(particle_css, unsafe_allow_html=True)

# HTML for particles
particles_html = """
<div class="container">
    """ + "\n".join([
        '<div class="circle-container"><div class="circle"></div></div>'
        for _ in range(100)
    ]) + """
</div>
"""



# Inject HTML
st.markdown(particles_html, unsafe_allow_html=True)
client = ollama.Client()

def review_code(content, progress_callback=None):
    prompts = (
        f'Review this code. classify the script as either "bad", "mediocre", "decent", or "good"; alert any security vulnerabilities first such as SQL injection and risks of attacks. '
        f'Provide suggestions for improvement, coding best practices, and improving readability and maintainability. Provide code examples for your suggestion.\n\n{content}'
    )

    # Simulate different stages with progress
    if progress_callback:
        progress_callback(20)  # 20% - Preparing prompt

    # Generate response (simulate time for response generation)
    response = client.generate(model='cauditor', prompt=prompts)
    
    if progress_callback:
        progress_callback(70)  # 70% - Generating response

    time.sleep(1)  # Simulate processing time
    
    if 'response' in response:
        if progress_callback:
            progress_callback(100)  # 100% - Completed
        return response['response']
    else:
        st.error("Unexpected response format from Cauditor")
        st.write(response) 
        return "Review generation failed. Please try again."

# Set up the app interface
st.markdown(
    """
    <style>
        @import url('https://fonts.cdnfonts.com/css/expletus-sans-2');
        
        h1 {
            font-family: 'Expletus Sans', sans-serif;
            text-align: center;
        }
    </style>
    <h1>
    Code Review with 
    <span style="color: #c4cccf;">Caud</span><span style="color: #0097b2;">It</span><span style="color: #c4cccf;">Or</span>
    </h1>
    """,
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader("Upload your script file", type=["py", "js", "java", "cpp", "ts", "rb", "php", "html"])
code_input = st.text_area("Or write your code here")

# Check for uploaded file or text input
if uploaded_file is not None:
    code = uploaded_file.read().decode("utf-8")
else:
    code = code_input

if st.button("Review Code"):
    if code:
        # Initialize a progress bar
        progress_bar = st.progress(0)
        
        # Define a progress callback function
        def update_progress(value):
            progress_bar.progress(value)

        with st.spinner("Cauditor is reviewing your code..."):
            # Run code review with progress updates
            review = review_code(code, progress_callback=update_progress)
        
        # Display the result
        st.subheader("Code Review")
        st.write(review)
        


        def generate_pdf(content):
            buffer = BytesIO()
            c = canvas.Canvas(buffer, pagesize=letter)
            width, height = letter  # Get the size of the page (612 x 792 points for letter size)

            # Set up text object with a smaller font size and starting position
            text_object = c.beginText(40, height - 40)
            text_object.setFont("Helvetica", 10)
            text_object.setTextOrigin(40, height - 40)  # Start position
            
            # Maximum line width for text (leaving some padding)
            max_line_width = width - 80  # 40 points padding on both sides

            # Wrap text based on max_line_width
            lines = content.split("\n")
            for line in lines:
                # Split the line into words to ensure proper word wrapping
                words = line.split(" ")
                current_line = ""

                for word in words:
                    # Check if adding the word exceeds the max line width
                    test_line = current_line + " " + word if current_line else word
                    text_width = c.stringWidth(test_line, "Helvetica", 10)
                    
                    if text_width < max_line_width:
                        # If the line fits, add the word
                        current_line = test_line
                    else:
                        # If the line overflows, write the current line and start a new one
                        text_object.textLine(current_line)
                        current_line = word  # Start the new line with the current word
                
                # After the loop, add the last line
                text_object.textLine(current_line)

            c.drawText(text_object)
            c.showPage()
            c.save()
            buffer.seek(0)
            return buffer

        # Convert the review to a PDF
        pdf_buffer = generate_pdf(review)

        # Provide the PDF as a downloadable file
        st.download_button(
            label="Download Review as PDF",
            data=pdf_buffer,
            file_name="code_review.pdf",
            mime="application/pdf"
        )
    else:
        st.warning("Please enter code or upload a file.")