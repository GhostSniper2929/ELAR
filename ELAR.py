import streamlit as st
import requests
from PIL import Image
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Students Need Sleep", page_icon=":😴:", layout="wide")

selected = option_menu(
    menu_title=None, #required
    options=["Main Page", "Testimonials", "Citations", "Contact Me"], #required
    icons=["house", "person", "book","envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",

    )
page_bg_img = """
<style>
[data-testid="stAppVeiwContainer"] {
background-color: #e5e5f7;
opacity: 0.2;
filter: blur(20px);
background: repeating-linear-gradient( 45deg, #444cf7)
}
</style>
"""

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}<style>", unsafe_allow_html=True)

local_css("style/style.css")

st.markdown(page_bg_img, unsafe_allow_html=True)



# ---MAIN PAGE---
if selected == "Main Page":
    st.header(" The Silent Epidemic: Why High Schoolers Need More Sleep")
    st.subheader("Author: Sreeshan Karnati")
    st.write("Made Using Python")
    st.write("karsree29@gmail.com")
    with st.container():
        st.write("---")
    midleft_column, right_column = st.columns(2)
    with midleft_column:
        st.subheader("Why HighSchool Students Need Sleep?")
        st.write("""
                 High school students across the globe are suffering from a silent epidemic: sleep deprivation. Addressing this issue is crucial for their academic success, mental well-being, and overall health.
                """)
        st.write("---")
        st.subheader("It's Proven")
        st.write("""
                 According to a study published in the Journal of Adolescent Health, only 23% of high school students get the recommended nine hours of sleep per night. The National Sleep Foundation underscores that adolescents need 8-10 hours of sleep for optimal functioning. However, the demands of homework, extracurricular activities, and social obligations often force students into a cycle of sleep deprivation.
                 Consider the case of Jane, a high school junior. Despite her best efforts, she struggles to balance schoolwork, sports, and a part-time job. On average, she gets a mere five hours of sleep each night. As a result, she experiences difficulty concentrating in class, heightened stress levels, and a compromised immune system.

                 """)


    with right_column:
            img = Image.open('stju.jpg')
            st.image(img)
            st.write("Tired student sleeping in a class at classroom Daniel Druhora December 4, 2018\n\n\n")

    with st.container():
         st.write("---")
         left_column, right_column = st.columns(2)
         with left_column:
             st.subheader("Consequences")
             st.write("""
The consequences of sleep deprivation among high schoolers are far-reaching. Beyond academic performance, insufficient sleep has been linked to mood disorders, increased risk-taking behavior, and even obesity. Urgent action is needed to address this pressing issue.

Educators and policymakers must prioritize the well-being of students by implementing later start times for high schools. Research consistently demonstrates that delaying the start of the school day results in improved academic performance, reduced absenteeism, and enhanced mental health among adolescents.

Furthermore, parents play a pivotal role in fostering healthy sleep habits at home. Encouraging a consistent sleep schedule, limiting screen time before bed, and creating a conducive sleep environment are essential steps in promoting adequate rest for teenagers.

Consider the undeniable scientific evidence linking sufficient sleep to improved academic performance, emotional resilience, and overall health outcomes for high school students.
""")
             st.write("---")
             st.subheader("My Opinion")
             st.write("As someone deeply invested in the welfare of high school students and armed with research-backed knowledge, it's imperative to shed light on the importance of sleep for adolescent development.")             

    with right_column:
        st.subheader("Physical Health Implications")
        st.write("Beyond cognitive and emotional well-being, sleep deprivation poses significant risks to physical health. Adolescents who chronically lack sleep are more susceptible to obesity, weakened immune systems, and cardiovascular problems [6]. Moreover, insufficient sleep disrupts hormonal balance, increasing the likelihood of metabolic disorders such as diabetes and insulin resistance [7].")
        img = Image.open('mental.jpeg')
        st.image(img)
    
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.subheader("Strategies for Promoting Healthy Sleep Habits")
            st.write("Addressing the sleep crisis among high school students necessitates a multifaceted approach. Schools, parents, and communities must collaborate to prioritize sleep health and implement strategies to support adolescents in cultivating healthy sleep habits. Imagine the stress and exhaustion experienced by a typical high schooler balancing homework, exams, social obligations, and extracurricular activities, all while struggling to get adequate rest each night.")

        with right_column:
            img = Image.open('WeNeedYourHelp.png')
            st.image(img)
        
    with st.container():
        st.write("---")
        st.subheader("Purpose of this article")
        st.write("The purpose of this article is to raise awareness about the critical need for high school students to prioritize sleep and to advocate for systemic changes that promote healthier sleep habits. So let's rise up, together, and make sleep a priority. Let's stand in solidarity with our teenagers, advocating for the changes they so desperately need. The time to act is now. The time to wake up to the importance of high school sleep is long overdue.")        

# ---TESTIMONIALS---
if selected == "Testimonials":
    st.title(f"{selected}")
    with st.container():
        st.write("---")
        left_column, botright_column = st.columns(2)
        with left_column:
            st.subheader("Sarah L., Parent:")
            st.write("\"As a parent, I've seen firsthand the impact of sleep deprivation on my teenager\'s athletic performance and mood. Implementing the strategies outlined in this article has been transformative. My child is now more focused, happier, and performing better in soccer. Prioritizing sleep has truly been a game-changer for our family.\"")
            
            with botright_column:
                img = Image.open('fsf.jpg')
                st.image(img)

    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.subheader("David M., High School Teacher:")
            st.write("\"In my years of teaching, I've observed how sleep affects students\' ability to learn and engage in the classroom. This article sheds light on the importance of sleep for adolescents and provides practical solutions for addressing sleep deficits. By integrating these strategies into my teaching practices, I\'ve noticed a marked improvement in my students\' attentiveness and academic performance.\"")

        with right_column:
            img = Image.open('d.webp')
            st.image(img)

    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.subheader("Emily R., High School Student:")
            st.write("\"Juggling school, extracurricular activities, and social life often leaves me feeling exhausted and overwhelmed. Reading this article made me realize the critical role that sleep plays in my well-being. By implementing some of the suggested sleep hygiene practices, I've experienced improved focus, mood, and overall health. I\'m grateful for the valuable insights shared in this article.\"")

        with right_column:
            img = Image.open('h.webp')
            st.image(img)
    
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.subheader("Dr. Mark S., Adolescent Psychologist:")
            st.write("\"As a psychologist specializing in adolescent mental health, I commend this article for addressing the sleep crisis among high school students. Sleep deprivation is a significant risk factor for mood disorders and academic underachievement. The recommendations provided here offer practical solutions for parents, educators, and communities to support adolescents in prioritizing sleep and promoting optimal development.\"")


        with right_column:
            img = Image.open('doctor.webp')
            st.image(img)




# ---CITATIONS---
if selected == "Citations":
    st.title(f"{selected}")
    with st.container():
        st.write("---")
        st.write("1. CDC. (2018). *School Start Times for Middle School and High School Students – United States, 2011–12 School Year*. Centers for Disease Control and Prevention.")
        st.write("---")
        st.write("2. Walker, M. P. (2009). *The role of sleep in cognition and emotion*. Annals of the New York Academy of Sciences, 1156(1), 168-197.")
        st.write("---")
        st.write("3. Wolfson, A. R., & Carskadon, M. A. (2003). Understanding adolescents’ sleep patterns and school performance: A critical appraisal. *Sleep Medicine Reviews, 7*(6), 491-506.")
        st.write("---")
        st.write("4. Lovato, N., Gradisar, M., & Short, M. A. (2014). *A longitudinal study of the effects of adolescent sleep deprivation on academic performance and emotional functioning*. Sleep, 37(2), 255-263.")
        st.write("---")
        st.write("5. Baglioni, C., Nanovska, S., Regen, W., Spiegelhalder, K., Feige, B., Nissen, C., ... & Riemann, D. (2016). Sleep and mental disorders: A meta-analysis of polysomnographic research. *Psychological Bulletin, 142*(9), 969-990.")
        st.write("---")
        st.write("6. Taheri, S. (2006). The link between short sleep duration and obesity: We should recommend more sleep to prevent obesity. *Archives of Disease in Childhood, 91*(11), 881-884.")
        st.write("---")
        st.write("7. Spiegel, K., Knutson, K., Leproult, R., Tasali, E., & Van Cauter, E. (2005). Sleep loss: a novel risk factor for insulin resistance and Type 2 diabetes. *Journal of Applied Physiology, 99*(5), 2008-2019.")
        st.write("---")
        st.write("8. Hirshkowitz, M., Whiton, K., Albert, S. M., Alessi, C., Bruni, O., DonCarlos, L., ... & Neubauer, D. N. (2015). National Sleep Foundation’s sleep time duration recommendations: methodology and results summary. *Sleep Health, 1*(1), 40-43.")
        st.write("---")
        st.write("Wolfson, A. R., & Carskadon, M. A. (2003). Understanding adolescent's sleep patterns and school performance: a critical appraisal.")
        st.write("---")
        st.write("Sleep Medicine Reviews, 7(6), 491-506.")
        st.write("---")
        st.write("National Sleep Foundation. (n.d.). How Much Sleep Do We Really Need? Retrieved from https://www.sleepfoundation.org/how-sleep-works/how-much-sleep-do-we-really-need Wahlstrom, K., Dretzke, B., Gordon, M., Peterson, K., Edwards, K., & Gdula, J. (2014).")
        st.write("---")
        st.write("Examining the Impact of Later School Start Times on the Health and Academic Performance of High School Students: A Multi-Site Study. Center for Applied Research and Educational Improvement.")



# ---CONTACT---
if selected == "Contact Me":
    st.title(f"{selected}")
    with st.container():
        st.header("Have any questions?")
        st.write("If you have any questions feel free to submit them here!")
        st.write("##")
        
        contact_form = """
       <form action="https://formsubmit.co/karsree29@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your email "required>
     <textarea name ="mesage " placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
     </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)
