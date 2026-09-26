import streamlit as st

from crew import generate_article, get_research

st.set_page_config(
    page_title="AI News Reporter",
    page_icon="📰",
    layout="wide",
)


# ---------------------------------
# Page Header
# ---------------------------------

st.title("📰 AI News Reporter")

st.caption(
    "Research current AI and technology developments and turn them "
    "into a source-backed article."
)


# ---------------------------------
# User Inputs
# ---------------------------------

topic = st.text_input(
    "What would you like to research?",
    placeholder="e.g. AI agents in healthcare",
)

col1, col2 = st.columns(2)

with col1:
    article_style = st.selectbox(
        "Article style",
        [
            "News Report",
            "Research Brief",
            "Explainer",
        ],
    )

with col2:
    article_length = st.selectbox(
        "Article length",
        [
            "Short",
            "Medium",
            "Detailed",
        ],
    )


# ---------------------------------
# Generate
# ---------------------------------

if st.button("🚀 Generate Article", type="primary"):
    if not topic.strip():
        st.warning("Please enter a topic first.")

    else:
        topic = topic.strip()

        # =================================
        # PHASE 1 — RESEARCH
        # =================================

        st.divider()

        st.subheader("🔎 Research Findings")

        with st.spinner("Finding relevant articles..."):
            research = get_research(topic)

        if not research.strip():
            st.warning(
                "No relevant research was found for this topic. Try a broader topic."
            )

        else:
            st.success("Research collected successfully.")

            st.markdown("Here are the sources retrieved for your topic:")

            # Display the retrieved research
            # exactly as returned by the search tool.
            st.markdown(research)

        # =================================
        # PHASE 2 — ARTICLE GENERATION
        # =================================

        if research.strip():
            st.divider()

            st.subheader("✍️ Writing Article")

            st.caption(
                f"Creating a {article_length.lower()} "
                f"{article_style.lower()} from the retrieved research."
            )

            with st.spinner("Turning the research into an article..."):
                article = generate_article(
                    topic=topic,
                    research=research,
                    article_style=article_style,
                    article_length=article_length,
                )

            # =================================
            # FINAL ARTICLE
            # =================================

            st.divider()

            st.subheader("📰 Final Article")

            st.markdown(article)

            # =================================
            # DOWNLOAD
            # =================================

            st.download_button(
                label="⬇️ Download Markdown",
                data=article,
                file_name="ai_news_article.md",
                mime="text/markdown",
            )
