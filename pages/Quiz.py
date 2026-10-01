import streamlit as st
import info

CAREERS = { 
    "AI Engineer": {
        "image": "images/ai.png",
        "emoji": "",
        "blurb": "You love patterns, data, and teaching machines to think. "
                 "Look into machine learning, neural networks, and language models.",
        "next_steps": [
            "Take an intro machine learning course",
            "Train a small image classifier with Python",
            "Join a Kaggle competition",
        ],
    },
    "Robotics Engineer": {
        "image": "images/robotics.png",
        "emoji": "",
        "blurb": "You want your code to move things in the real world. "
                 "Look into controls, sensors, and mechatronics.",
        "next_steps": [
            "Join a robotics team",
            "Build a line-following robot with a microcontroller",
            "Learn about PID controllers",
        ],
    },
    "Space Systems Engineer": {
        "image": "images/space.png",
        "emoji": "",
        "blurb": "You think big and look up. "
                 "Look into orbital mechanics, spacecraft design, and mission software.",
        "next_steps": [
            "Simulate an orbit with Python",
            "Follow a live rocket launch",
            "Explore how rovers navigate other planets",
        ],
    },
}

WIDGET_KEYS = ["q1", "q2", "q3", "q4", "q5", "q6"]


def reset_quiz():
    for key in WIDGET_KEYS + ["scores", "result"]:
        if key in st.session_state:
            del st.session_state[key]


def score_answers(q1, q2, q3, q4, q5, q6):
    scores = {"AI Engineer": 0, "Robotics Engineer": 0, "Space Systems Engineer": 0}

    q1_points = {
        "Train a model that recognizes my handwriting": "AI Engineer",
        "Build a robot that solves a maze": "Robotics Engineer",
        "Design a model rocket and simulate its flight": "Space Systems Engineer",
    }
    scores[q1_points[q1]] += 2

    q2_points = {
        "Python and neural networks": "AI Engineer",
        "Motors, sensors, and microcontrollers": "Robotics Engineer",
        "Telescopes and orbital simulators": "Space Systems Engineer",
        "Chatbots and language models": "AI Engineer",
        "3D printing and CAD": "Robotics Engineer",
        "Rocket launches": "Space Systems Engineer",
    }
    for choice in q2:
        scores[q2_points[choice]] += 1

    
    if q3 <= 3:
        scores["AI Engineer"] += 2
    elif q3 <= 6:
        scores["AI Engineer"] += 1
        scores["Robotics Engineer"] += 1
    else:
        scores["Robotics Engineer"] += 2

    q4_points = {
        "A research lab full of GPUs": "AI Engineer",
        "A workshop with robots everywhere": "Robotics Engineer",
        "Mission control": "Space Systems Engineer",
    }
    scores[q4_points[q4]] += 2

    if q5 <= 10:
        scores["Space Systems Engineer"] += 2
    elif q5 <= 25:
        scores["Space Systems Engineer"] += 1
    else:
        scores["AI Engineer"] += 1

    if q6:
        scores["Robotics Engineer"] += 1
        scores["Space Systems Engineer"] += 1
    else:
        scores["AI Engineer"] += 2

    return scores


def quiz():
    st.title("Which Future Tech Career Fits You?") 
    st.write("Answer the questions below and find out which career path matches your style.")

    col_a, col_b, col_c = st.columns(3)  # NEW
    with col_a:
        st.image("images/ai.png", caption="Artificial Intelligence")  # NEW
    with col_b:
        st.image("images/robotics.png", caption="Robotics")  # NEW
    with col_c:
        st.image("images/space.png", caption="Space Exploration")  # NEW

    with st.form("career_quiz"):  # NEW
        q1 = st.radio(  # NEW
            "1. Pick a weekend project:",
            [
                "Train a model that recognizes my handwriting",
                "Build a robot that solves a maze",
                "Design a model rocket and simulate its flight",
            ],
            key="q1",
        )

        q2 = st.multiselect(  # NEW
            "2. Which of these get you excited? (pick any)",
            [
                "Python and neural networks",
                "Motors, sensors, and microcontrollers",
                "Telescopes and orbital simulators",
                "Chatbots and language models",
                "3D printing and CAD",
                "Rocket launches",
            ],
            key="q2",
        )

        q3 = st.slider(  # NEW
            "3. How much do you prefer building physical things over writing software? "
            "(0 = only software, 10 = only hardware)",
            0, 10, 5,
            key="q3",
        )

        q4 = st.selectbox(  # NEW
            "4. Choose your dream workplace:",
            [
                "A research lab full of GPUs",
                "A workshop with robots everywhere",
                "Mission control",
            ],
            key="q4",
        ) 

        q5 = st.number_input(  # NEW
            "5. In how many years do you think humans will walk on Mars?",
            min_value=1, max_value=100, value=15, step=1,
            key="q5",
        )

        q6 = st.toggle("6. I would rather test my code on a real machine than in a simulation.", key="q6")  # NEW

        submitted = st.form_submit_button("See my result")  # NEW

    if submitted:
        if len(q2) == 0:
            st.warning("Please pick at least one option in question 2.")
        else:
            st.session_state["scores"] = score_answers(q1, q2, q3, q4, q5, q6)
            st.session_state["result"] = max(
                st.session_state["scores"], key=st.session_state["scores"].get
            )
            st.toast("Quiz submitted!")  # NEW
            st.balloons()  # NEW

    if "result" in st.session_state:
        show_result(st.session_state["result"], st.session_state["scores"])


def show_result(result, scores):
    info_box = CAREERS[result]
    total = sum(scores.values())

    st.divider()  # NEW
    st.header(f"{info_box['emoji']} Your match: {result}")
    st.progress(scores[result] / total, text=f"{round(100 * scores[result] / total)}% match")  # NEW

    tab_result, tab_scores = st.tabs(["Your result", "Score breakdown"])  # NEW

    with tab_result:
        st.image(info_box["image"], width=400)  # NEW
        st.write(info_box["blurb"])
        with st.expander("Next steps you could take"):
            for step in info_box["next_steps"]:
                st.write(f"- {step}")

    with tab_scores:
        metric_cols = st.columns(3)
        for col, (career, points) in zip(metric_cols, scores.items()):
            col.metric(label=career, value=f"{points} pts") 

    st.button("Retake the quiz", on_click=reset_quiz)


def links_section():
    st.sidebar.header("Links")

    st.sidebar.text("Check out my GitHub")

    github_link = f'<a href="{info.my_github_url}"><img src="{info.github_image_url}" alt="GitHub" width="75" height="75"></a>'

    st.sidebar.markdown(github_link, unsafe_allow_html=True)

    st.sidebar.text("Connect with me on LinkedIn")

    linkedin_link = f'<a href="{info.my_linkedin_url}"><img src="{info.linkedin_image_url}" alt="LinkedIn" width="75" height="75"></a>'

    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)

    st.sidebar.text("Send me an email")

    email_link = f'<a href="mailto:{info.my_email_address}"><img src="{info.email_image_url}" alt="Email" width="75" height="75"></a>'

    st.sidebar.markdown(email_link, unsafe_allow_html=True)


quiz()
links_section()
