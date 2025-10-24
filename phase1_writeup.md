## Phase 1 Report

Github repo: https://github.com/OrionYuSen/cse291a-finance-rag

### Domain Selection & Justification

We select the financial analysis and reporting domain, focusing on corporate disclosure documents such as annual reports, earnings releases, and management discussions. This domain is well-motivated because financial information is dense, high-stakes, and context-dependent. Financial analysts, investors, and regulators frequently need to retrieve precise, fact-grounded evidence from long textual reports (e.g., 10-K filings) when making investment or compliance decisions. Traditional keyword-based search is inadequate, as the same concept (e.g., _liquidity risk_, _revenue guidance_) can be described differently across companies and years.

The financial domain-specific retrieval challenges include:

-   Highly structured documents (Items 1A, 7, 8, etc.) with complex cross-references.
-   Heavy use of financial jargon and abbreviations (e.g., “FX impact,” “EBITDA margin”).
-   The need for grounding and factual accuracy, since errors may lead to financial misinterpretation.
-   Retrieval across text and tables (e.g., linking MD&A commentary with quantitative metrics).

This domain strongly benefits from a RAG approach, as LLMs can provide natural-language synthesis while retrieval ensures factual grounding. A well-designed RAG system can extract relevant context (e.g., risk factors, MD&A explanations, or financial ratios) and generate concise, evidence-backed answers to analyst-style questions.

Stakeholders and Beneficiaries include:

-   Financial analysts — accelerating company and sector research.
-   Institutional investors — improving explainability in AI-assisted investment decisions.
-   Regulatory compliance teams — verifying disclosures and risk factors efficiently.
-   Academic researchers — studying domain-specific RAG alignment and grounding quality.

In summary, the financial-reporting domain provides a realistic, high-impact testbed for developing retrieval-augmented generation systems that emphasize accuracy, interpretability, and domain adaptability.

### Data Sources

Our data sources include both publicly available financial datasets and manually collected filings, ensuring diversity across document types and sources.

Most datasets are drawn from the ACM-ICAIF ’24 FinanceRAG Challenge (Kaggle), which provides seven curated financial retrieval datasets. Each dataset contains a processed corpus of financial document segments, corresponding queries, and ground-truth corpus IDs for evaluation. We specifically use FinDER, FinQA, and Financial-QA-10k for our experiments.

To complement these curated datasets, we additionally collected 10-K filings directly from the SEC EDGAR database (https://www.sec.gov/edgar/browse/), covering real-world corporate financial disclosures.

Together, these sources exceed 100 documents, span multiple data formats (structured APIs and unstructured filings), and provide high-quality, domain-relevant content suitable for retrieval-based financial QA.

### Request Set

**Request 1:** How much revenue does Microsoft generate from contracts with customers?

**Request 2:** When did Coupang`s Farfetch consolidation start?

**Request 3:** What was the change in total expense net of tax for share based compensation from 2014 to 2015 in millions?

**Request 4:** Did abiomed outperform the nasdaq medical equipment index?

**Request 5:** How much revenue does Microsoft generate from contracts with customers?

**Request 6:** When did Coupang’s Farfetch consolidation start?

**Request 7:** What is CPNG's free cash flow?

**Request 8**: What was the difference in percentage cumulative total shareholder return on masco common stock versus the s&p 500 index for the five year period ended 2017?

**Request 9:** what is the growth rate in the balance of standby letters of credit from 2006 to 2007?

**Request 10:** what is the percentage change in revenue generated from non-us currencies from 2015 to 2016?

### Evaluator

To quantitatively assess the performance of our financial RAG system, we adopt the Ragas evaluation framework (Hugging Face, 2024), which enables end-to-end assessment of retrieval-augmented generation systems.

Rather than relying solely on ranking-based information retrieval metrics, Ragas evaluates both the retrieval and generation stages in terms of factual consistency and contextual grounding.

Our evaluator measures the following dimensions:

- **Context Precision** — proportion of retrieved chunks that are relevant to the query, assessing retrieval accuracy.
- **Context Recall** — proportion of relevant chunks successfully retrieved, evaluating coverage of supporting evidence.
- **Context Relevance** — semantic similarity between retrieved contexts and the query, measuring retrieval quality.
- **Faithfulness** — degree to which the generated answer is grounded in the retrieved evidence, detecting hallucinations.
- **Answer Relevance** — semantic alignment between the model’s answer and the reference (golden) answer.
- **Context Utilization** — extent to which the model effectively leverages retrieved content when generating responses.

These metrics jointly reflect factual accuracy, retrieval quality, and contextual grounding, which are essential in financial reasoning tasks.

### References

-   FinQA: A Dataset of Numerical Reasoning over Financial Data (ACL 2022)
-   EDGAR SEC Filings API Documentation
-   HedraRAG: Coordinating LLM Generation and Database Retrieval
-   Seven Failure Points When Engineering a Retrieval-Augmented Generation System
