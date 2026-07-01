"""Simple public-facing SEACAPT dashboard.

Run with:
    streamlit run dashboard_simple.py
"""

from __future__ import annotations

from pathlib import Path

import streamlit as st


ROOT = Path(__file__).resolve().parent
LOGO_PATH = ROOT / "assets" / "seacapt_logo.jpg"
SIMPLE_PROCESS_FLOW_PATH = ROOT / "assets" / "seacapt_simple_process_flow.png"


def apply_styles() -> None:
    """Apply light styling for a calm public-facing page."""
    st.markdown(
        """
        <style>
        :root {
            --seacapt-green: #0d6657;
            --seacapt-blue: #14324a;
            --seacapt-soft: #f3f8f7;
            --seacapt-page: #f7fbfa;
            --seacapt-line: #d9e5e2;
            --seacapt-muted: #4f6670;
            --seacapt-text: #203036;
            --seacapt-card: #ffffff;
            --seacapt-card-soft: #eef7f4;
        }
        .stApp {
            background: var(--seacapt-page);
            color: var(--seacapt-text);
        }
        .block-container {
            max-width: 1060px;
            padding-top: 2rem;
            padding-bottom: 3rem;
            color: var(--seacapt-text);
        }
        .stMarkdown,
        .stMarkdown p,
        .stMarkdown li,
        .stMarkdown span,
        .stText,
        p,
        li {
            color: var(--seacapt-text);
        }
        .stMarkdown h1,
        .stMarkdown h2,
        .stMarkdown h3,
        .stMarkdown h4 {
            color: var(--seacapt-blue);
        }
        [data-testid="stCaptionContainer"],
        [data-testid="stCaptionContainer"] p,
        [data-testid="stCaptionContainer"] div {
            color: var(--seacapt-muted);
            opacity: 1;
        }
        [data-testid="stAlert"] {
            background: #edf7f4;
            color: var(--seacapt-text);
            border-color: var(--seacapt-line);
        }
        [data-testid="stAlert"] p,
        [data-testid="stAlert"] div {
            color: var(--seacapt-text);
        }
        .simple-hero {
            padding: 1.3rem 1.5rem;
            border: 1px solid var(--seacapt-line);
            border-radius: 18px;
            background: linear-gradient(135deg, #f7fbfa 0%, #eef7f4 100%);
            margin-bottom: 1.4rem;
        }
        .simple-hero h1 {
            color: var(--seacapt-blue);
            margin-bottom: 0.35rem;
            line-height: 1.12;
            font-size: 3rem;
            letter-spacing: 0.02em;
        }
        .simple-hero .slogan {
            color: var(--seacapt-green);
            font-size: 1.75rem;
            font-weight: 750;
            line-height: 1.2;
            margin: 0 0 0.35rem 0;
        }
        .simple-hero .tagline {
            color: var(--seacapt-blue);
            font-size: 1.18rem;
            font-weight: 600;
            margin: 0 0 0.85rem 0;
        }
        .simple-hero p {
            color: var(--seacapt-muted);
            font-size: 1.05rem;
            max-width: 850px;
        }
        .note-card {
            border: 1px solid var(--seacapt-line);
            border-radius: 14px;
            padding: 1rem 1.1rem;
            background: var(--seacapt-card);
            color: var(--seacapt-text);
            height: 100%;
            box-shadow: 0 1px 4px rgba(20, 50, 74, 0.06);
        }
        .note-card h3 {
            color: var(--seacapt-blue);
            margin-top: 0;
            font-size: 1.05rem;
        }
        .note-card p {
            color: var(--seacapt-text);
            margin-bottom: 0;
        }
        .flow-step {
            text-align: center;
            border: 1px solid var(--seacapt-line);
            border-radius: 14px;
            padding: 0.8rem 0.55rem;
            background: var(--seacapt-card-soft);
            font-weight: 650;
            color: var(--seacapt-blue);
            min-height: 4.6rem;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .flow-arrow {
            text-align: center;
            color: var(--seacapt-green);
            font-size: 1.4rem;
            font-weight: 700;
            padding-top: 1.35rem;
        }
        .small-muted {
            color: var(--seacapt-muted);
            font-size: 0.92rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_header() -> None:
    """Render the public-facing page header."""
    logo_col, text_col = st.columns([1, 5], vertical_alignment="center")
    with logo_col:
        if LOGO_PATH.exists():
            st.image(str(LOGO_PATH), width=95)
    with text_col:
        st.markdown(
            """
            <div class="simple-hero">
                <h1>SEACAPT</h1>
                <p class="slogan">We do nature, only quicker</p>
                <p class="tagline">Working with the ocean to explore a new route for carbon removal.</p>
                <p class="hero-intro">
                    SEACAPT is an early-stage R&D project. The goal is to test whether a carefully
                    controlled land-based process could help remove CO₂ from seawater and store part
                    of that carbon in solid carbonate minerals.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_simple_flow() -> None:
    """Render a compact non-technical process flow."""
    st.markdown("### The SEACAPT idea in one simple flow")
    labels = [
        "Air CO₂",
        "Ocean",
        "Seawater intake",
        "Controlled reactor",
        "Carbonate minerals",
        "Safe water return",
    ]
    columns = st.columns([1, 0.22, 1, 0.22, 1, 0.22, 1, 0.22, 1, 0.22, 1])
    for index, label in enumerate(labels):
        with columns[index * 2]:
            st.markdown(f'<div class="flow-step">{label}</div>', unsafe_allow_html=True)
        if index < len(labels) - 1:
            with columns[index * 2 + 1]:
                st.markdown('<div class="flow-arrow">→</div>', unsafe_allow_html=True)
    st.caption(
        "This is a simplified explanation. The real validation work must measure the carbon balance, "
        "water chemistry and environmental effects carefully."
    )


def render_process_illustration() -> None:
    """Render the public-safe simple process illustration when available."""
    st.markdown("### A simple visual overview")
    caption = (
        "Simple overview of the SEACAPT idea: seawater is treated in a controlled process to "
        "explore whether CO₂ can be removed and stored in mineral form, after which safe water "
        "can return to the ocean."
    )
    if SIMPLE_PROCESS_FLOW_PATH.exists():
        st.image(
            str(SIMPLE_PROCESS_FLOW_PATH),
            caption=caption,
            width="stretch",
        )
    else:
        st.info(
            "A simple public process illustration can be shown here once "
            "`assets/seacapt_simple_process_flow.png` is available in the repository."
        )
        st.caption(caption)


def render_five_steps() -> None:
    """Explain the process in five plain-language steps."""
    st.markdown("### How the process works in 5 steps")
    steps = [
        (
            "1. Take in seawater",
            "A controlled stream of seawater is brought into a land-based test setup.",
        ),
        (
            "2. Adjust the water chemistry",
            "The water chemistry is carefully adjusted in a controlled setting. In plain terms: the "
            "test asks whether dissolved carbon can be encouraged to become solid mineral material.",
        ),
        (
            "3. Form mineral particles",
            "Inside the reactor, SEACAPT aims to test whether carbonate minerals can form in a "
            "measurable and controlled way. These are solid particles that can contain carbon.",
        ),
        (
            "4. Measure what happened",
            "The water, solids and process inputs must be measured. SEACAPT cannot count any climate "
            "benefit unless the carbon balance is proven.",
        ),
        (
            "5. Return safe water",
            "Before water could go back to the sea, its quality would need to be checked carefully.",
        ),
    ]
    for row_start in range(0, len(steps), 2):
        columns = st.columns(2)
        for column, (title, body) in zip(columns, steps[row_start : row_start + 2]):
            with column:
                st.markdown(
                    f"""
                    <div class="note-card">
                        <h3>{title}</h3>
                        <p>{body}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )


def render_proof_points() -> None:
    """Show what still needs to be proven."""
    st.markdown("### What we still need to prove")
    st.write(
        "SEACAPT is not yet a proven commercial carbon removal process. The next work is about "
        "evidence: what works, what does not, what it costs, and what can be measured reliably."
    )
    columns = st.columns(3)
    proof_points = [
        (
            "Carbon balance",
            "Could the process remove more CO₂ than it causes through energy, materials and operation?",
        ),
        (
            "Water safety",
            "Could treated water be returned without harmful changes to seawater quality or marine conditions?",
        ),
        (
            "Solid minerals",
            "Can carbonate particles be formed, collected and analysed in a controlled way?",
        ),
        (
            "Energy and cost",
            "Can the process be improved enough to become practical beyond lab scale?",
        ),
        (
            "Measurement",
            "Could independent reviewers check the main inputs, outputs and carbon accounting?",
        ),
        (
            "Scale-up",
            "Could a small test grow into a pilot while still staying controlled and measurable?",
        ),
    ]
    for index, (title, body) in enumerate(proof_points):
        with columns[index % 3]:
            st.markdown(
                f"""
                <div class="note-card">
                    <h3>{title}</h3>
                    <p>{body}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_status_and_support() -> None:
    """Explain current status, next step and partner need."""
    status_col, support_col = st.columns(2)
    with status_col:
        st.markdown("### Current status and next step")
        st.write(
            "SEACAPT is currently in the concept and validation-planning stage. The priority is a "
            "controlled lab setup that can answer basic scientific and engineering questions before "
            "larger tests are considered."
        )
        st.write(
            "The next practical milestone is a small lab validation system. If that produces useful "
            "data, the following step could be a modest pilot with stronger measurement."
        )
    with support_col:
        st.markdown("### Why partners and R&D support are needed")
        st.write(
            "This work needs more than a good idea. It needs laboratory testing, marine chemistry "
            "expertise, equipment support, environmental review, measurement design and funding."
        )
        st.write(
            "SEACAPT is looking for potential R&D partners who can help turn an early concept into "
            "testable evidence, without pretending that the hard questions are already solved."
        )


def render_technical_expander() -> None:
    """Add a short translation layer for technical readers."""
    with st.expander("For technical readers"):
        st.markdown(
            """
            - **Direct ocean removal:** an approach that explores CO₂ removal linked to the ocean-atmosphere system, rather than capturing CO₂ directly from a smokestack.
            - **Ocean alkalinity enhancement:** a broad field that studies how seawater chemistry could be adjusted to help manage dissolved carbon. SEACAPT still needs lab validation before making performance claims.
            - **Controlled mineralization:** testing whether solid carbonate minerals can form inside a managed land-based setup.
            - **MRV / measurement and verification:** the evidence system needed to check whether the process really works. This dashboard does not define a final MRV method.
            - **Lab validation:** the next step is a small test setup that can generate real data before larger claims are made.
            - **Pilot stage:** a possible later step after lab validation, still focused on learning and measurement rather than commercial deployment.
            """
        )


def render_contact() -> None:
    """Render the contact section."""
    st.markdown("### Contact")
    st.write(
        "SEACAPT is founder-led and looking for R&D partners, technical reviewers and "
        "organisations interested in careful early-stage marine carbon removal validation."
    )
    st.write(
        "For questions, technical review or potential collaboration, please contact:"
    )
    st.markdown(
        """
        **Peter Krabbendam**  
        Co-founder, SEACAPT B.V. i.o.  
        Industrial gases and decarbonisation applications  
        Email: [pkrabbendam@gmail.com](mailto:pkrabbendam@gmail.com)

        **Fred Bergwerff**  
        Co-founder, SEACAPT B.V. i.o.  
        Experimental validation and process development  
        Email: [FB@dutchgcc.com](mailto:FB@dutchgcc.com)
        """
    )
    st.write(
        "SEACAPT welcomes conversations with marine chemistry experts, laboratory partners, "
        "equipment suppliers, environmental reviewers, industrial host sites and organisations "
        "interested in responsible carbon removal innovation."
    )


def main() -> None:
    """Run the simple SEACAPT public dashboard."""
    st.set_page_config(
        page_title="SEACAPT simple dashboard",
        page_icon="🌊",
        layout="wide",
    )
    apply_styles()
    render_header()

    st.markdown("### The problem")
    st.write(
        "The ocean and the air constantly exchange CO₂. As humans add more CO₂ to the atmosphere, "
        "the ocean absorbs part of it. This helps slow warming, but it also changes seawater chemistry."
    )
    st.write(
        "SEACAPT explores whether some of the carbon already present in seawater could be converted into "
        "solid mineral form in a controlled land-based process."
    )

    render_process_illustration()
    render_simple_flow()

    render_five_steps()
    render_proof_points()
    render_status_and_support()
    render_technical_expander()
    render_contact()

    st.caption(
        "Important note: SEACAPT outputs are preliminary R&D assumptions. They should not be read as "
        "verified carbon removal, carbon credit eligibility or a claim of commercial readiness."
    )


if __name__ == "__main__":
    main()
