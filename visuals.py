import streamlit as st
import plotly.graph_objects as go


def income_flow_visual(wages, interest, business):

    total = wages + interest + business

    fig = go.Figure(go.Sankey(
        node=dict(
            pad=20,
            thickness=25,
            line=dict(color="black", width=0.5),
            label=["Wages", "Interest", "Business", "Total Income"],
            color=["#1f3c88", "#ffbf00", "#1f3c88", "#154360"]
        ),
        link=dict(
            source=[0,1,2],
            target=[3,3,3],
            value=[wages, interest, business]
        )
    ))

    fig.update_layout(
        title="Income Aggregation Architecture",
        font=dict(size=14)
    )

    st.plotly_chart(fig, use_container_width=True)