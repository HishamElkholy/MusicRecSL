import streamlit as st

st.title("Introduction")

st.write("Music is a ubiquitous part of our lives. Regardless of where or who you are, you have been a willing or unwilling consumer of music numerous times in your life. For some, music is tied to identity; what genres you listen to define your social group and economic standing in society. For others, music is an enhancing additive to other aspects of life such as exercising, performing chores, or partaking in religious rituals. So pervasive is it within our psyche that sociologists and anthropologists consider music to be a cultural universal alongside other concepts such as language and logical notions.")

st.write("Equally, music production is an activity that is older than recorded history. The oldest evidence of a musical instrument is the Divje Babe flute which is believed to be at least 50,000 years old (Turk, Turk et al. 2020). Similarly, the oldest evidence we have of musical notation is the Hurrian Hymn to Nikkal which is dated to around 1400 BCE (Figure 1).")

st.image("Hurrian.png", caption = "The cuneiform tablet on which the musical notation for the Hurrian Hymn to Nikkal was written")

st.write("Our connection and interaction with music as a species has remained strong throughout the ages. However, with the advent of new technologies such as the radio, television, and personal computers, the way we consume and produce music has drastically changed. Not only do we have more readily available access to music as consumers, but music production has boomed as digital audio workstations (DAWs) have allowed for increased ease in the composition of songs (Figure 2).")

st. image("DAW.png", caption = "A music producer utilizing a DAW, midi keyboard, and table-top electronic drum kit to produce music")

st.write("As such, there arose a need to be able to efficiently connect music consumers with music producers based on preferences. With the increase in genres and subgenres of music, these preferences are increasingly hard to identify but the fields of artificial intelligence and machine learning have presented us with several ways this can be done.")

st.write("Today, music is omnipresent, and music digitization has revolutionized how we consume, produce, and distribute it. Streaming platforms such as Spotify, Apple Music, and Amazon Music have not only increased music production but have also diversified the musical landscape, offering consumers an unprecedented array of genres and artists (Achterberg, Heilbron et al. 2011, Bello and Garcia 2021).")

st.title("Objective")

st.write("The main objective of this study is to predict music appreciation levels based on three different datasets, including twitter analyzes and user feedback. We aim to identify user music preferences by leveraging various data points, ultimately facilitating the connection between music consumers and producers.")
