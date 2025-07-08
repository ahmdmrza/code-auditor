import streamlit as st

# Set up the page layout in Streamlit
st.set_page_config(layout="wide")

# HTML and CSS styling
st.markdown(
    """
    <style>
        /* Importing Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Nabla&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Poppins&display=swap');

        /* Animated background with sliding effect */
        [data-testid="stAppViewContainer"] {
            background-image: url('https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiWFEIdP4w_ejkYffMuqS0L2Sdxgg8c7IkC6PeAoWVLnBHTzP-UqfbDdW-N4DNJ-yn3y3VwCrIeUa7XVdnD3xsnbPuuOqQMF5E_RyjuU1ZDt47CsjNrtlhj3XvHu4POIVdAr29LFJqnTdHV/s1600-rw/ufo-desktop-wallpaper-HD.png');
            background-size: cover;
            background-position: center -70%; /* Shifts the background down */
            position: relative;
            height: 100vh;
        }

        /* Typewriter effect styling */
        .typewriter h1 {
            overflow: hidden;
            border-right: .15em solid orange;
            white-space: nowrap;
            margin: 0 auto;
            letter-spacing: .15em;
            animation: 
                typing 3.5s steps(40, end),
                blink-caret .75s step-end infinite;
        }

        /* Keyframes for the typing effect */
        @keyframes typing {
            from { width: 0 }
            to { width: 100% }
        }

        /* Keyframes for the blinking caret */
        @keyframes blink-caret {
            from, to { border-color: transparent }
            50% { border-color: orange; }
        }

        /* Styling for the h1 title */
        h1 {
            font-size: 5vw;
            font-family: 'Nabla', sans-serif;
            color: #ffffff;
            text-align: center;
            white-space: nowrap;
            overflow: hidden;
            margin: 0;
            text-shadow: 0 0 15px rgba(255, 0, 102, 0.8), 0 0 30px rgba(0, 204, 255, 0.8);
        }

        /* Button and hover effects */
        button {
            padding: 40px 80px;
            padding-top: 30px !important;
            padding-bottom: 30px !important;
        }

        button:hover {
            color: #0097b2 !important;
            border: #0097b2 !important;
        }
        button:active {
            background-color: #c4cccf !important;
            color: white !important;
            border-color: #0097b2 !important;
        }
        button:focus {
            color: #0097b2 !important;
            border: #0097b2 !important;
            outline: none;
            box-shadow: 0 0 5px 2px rgba(0, 151, 178, 0.7);
        }

        /* Glow button style */
        .glow-button {
            font-size: 60px;  /* Increase the font size */
            padding: 40px 80px;  /* Increase padding for larger button */
            border: 20px solid #39FF14;
            color: #39FF14;
            border-radius: 50px;
            background-color: transparent;
            box-shadow: 0 0 50px rgba(57, 255, 20, 0.8), 0 0 20px rgba(57, 255, 20, 0.5);
            transition: box-shadow 0.3s ease;
        }

        .glow-button:hover {
            box-shadow: 0 0 20px rgba(57, 255, 20, 1), 0 0 40px rgba(57, 255, 20, 0.8);
        }

        /* Centered paragraph text style */
        p {
            font-size: 25px;
            text-align: center;
            color: #ffffff;
            font-family: 'Poppins', sans-serif;
        }

    </style>
    <br><br>
    <!-- Typewriter effect for the heading -->
    <div class="typewriter">
        <h1>Review your code with Gen AI</h1>
    </div>

    <br>
    """,
    unsafe_allow_html=True
)

# Add whitespace before the button
st.markdown('<br><br><br><br>', unsafe_allow_html=True) 

# Create columns for centering the button
columns = st.columns((2.25, 1, 2))  # Three columns with the center one being 1/3 of the width
with columns[1]:
    if st.button("Check my code", key="glow-button"):
        st.switch_page("pages/Review.py")
