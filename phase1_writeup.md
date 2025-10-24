# FinRAG

Financial Domain-Specific RAG System

## Phase 1

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

### Request Set & Manual Baseline

**Request 1:** How much revenue does Microsoft generate from contracts with customers?

**Golden Answer 1:** Revenue allocated to remaining performance obligations, which includes unearned revenue and amounts that will be invoiced and recognized as revenue in future periods, was 229 billion as of June 30, 2023, of which 224 billion is related to the commercial portion of revenue. We expect to recognize approximately 45% of this revenue over the next 12 months and the remainder thereafter.

**Request 2:** When did Coupang`s Farfetch consolidation start?

**Golden Answer 2:** As announced on January 31, 2024, the acquisition was completed. At closing, the limited partnership provided additional cash funding to Farfetch of 150 million. Additionally, 150 million previously provided under the bridge loan was contributed towards the Farfetch Acquisition. The limited partnership is further obligated to fund Farfetch up to $200 million within twelve months of the acquisition date.

**Request 3:** What was the change in total expense net of tax for share based compensation from 2014 to 2015 in millions?

**Golden Answer 3:** zimmer biomet holdings , inc .
2015 form 10-k annual report notes to consolidated financial statements ( continued ) these unaudited pro forma results have been prepared for comparative purposes only and include adjustments such as inventory step-up , amortization of acquired intangible assets and interest expense on debt incurred to finance the merger .
material , nonrecurring pro forma adjustments directly attributable to the biomet merger include : 2022 the \$ 90.4 million of merger compensation expense for unvested lvb stock options and lvb stock-based awards was removed from net earnings for the year ended december 31 , 2015 and recognized as an expense in the year ended december 31 , 2014 .
2022 the \$ 73.0 million of retention plan expense was removed from net earnings for the year ended december 31 , 2015 and recognized as an expense in the year ended december 31 , 2014 .
2022 transaction costs of \$ 17.7 million was removed from net earnings for the year ended december 31 , 2015 and recognized as an expense in the year ended december 31 , other acquisitions we made a number of business acquisitions during the years 2014 and 2013 .
in october 2014 , we acquired etex holdings , inc .
( 201cetex 201d ) .
the etex acquisition enhanced our biologics portfolio through the addition of etex 2019s bone void filler products .
in may 2013 , we acquired the business assets of knee creations , llc ( 201cknee creations 201d ) .
the knee creations acquisition enhanced our product portfolio of joint preservation solutions .
in june 2013 , we acquired normed medizin-technik gmbh ( 201cnormed 201d ) .
the normed acquisition strengthened our extremities and trauma product portfolios and brought new product development capabilities in the foot and ankle and hand and wrist markets .
the results of operations of these acquired companies have been included in our consolidated results of operations subsequent to the transaction dates , and the respective assets and liabilities of the acquired companies have been recorded at their estimated fair values in our consolidated statement of financial position as of the transaction dates , with any excess purchase price being recorded as goodwill .
pro forma financial information and other information required by gaap have not been included for these acquisitions as they , individually and in the aggregate , did not have a material impact upon our financial position or results of operations .
5 .
share-based compensation our share-based payments primarily consist of stock options and restricted stock units ( 201crsus 201d ) .
share-based compensation expense was as follows ( in millions ) : .

| for the years ended december 31, | 2015           | 2014           | 2013           |
| -------------------------------- | -------------- | -------------- | -------------- |
| total expense pre-tax            | $ 46.4         | $ 49.4         | $ 48.5         |
| tax benefit related to awards    | -14.5 ( 14.5 ) | -15.5 ( 15.5 ) | -15.6 ( 15.6 ) |
| total expense net of tax         | $ 31.9         | $ 33.9         | $ 32.9         |

stock options we had two equity compensation plans in effect at december 31 , 2015 : the 2009 stock incentive plan ( 201c2009 plan 201d ) and the stock plan for non-employee directors .
the 2009 plan succeeded the 2006 stock incentive plan ( 201c2006 plan 201d ) and the teamshare stock option plan ( 201cteamshare plan 201d ) .
no further awards have been granted under the 2006 plan or under the teamshare plan since may 2009 , and shares remaining available for grant under those plans have been merged into the 2009 plan .
vested stock options previously granted under the 2006 plan , the teamshare plan and another prior plan , the 2001 stock incentive plan , remained outstanding as of december 31 , 2015 .
we have reserved the maximum number of shares of common stock available for award under the terms of each of these plans .
we have registered 57.9 million shares of common stock under these plans .
the 2009 plan provides for the grant of nonqualified stock options and incentive stock options , long-term performance awards in the form of performance shares or units , restricted stock , rsus and stock appreciation rights .
the compensation and management development committee of the board of directors determines the grant date for annual grants under our equity compensation plans .
the date for annual grants under the 2009 plan to our executive officers is expected to occur in the first quarter of each year following the earnings announcements for the previous quarter and full year .
in 2015 , the compensation and management development committee set the closing date as the grant date for awards to our executive officers .
the stock plan for non-employee directors provides for awards of stock options , restricted stock and rsus to non-employee directors .
it has been our practice to issue shares of common stock upon exercise of stock options from previously unissued shares , except in limited circumstances where they are issued from treasury stock .
the total number of awards which may be granted in a given year and/or over the life of the plan under each of our equity compensation plans is limited .
at december 31 , 2015 , an aggregate of 5.6 million shares were available for future grants and awards under these plans .
stock options granted to date under our plans vest over four years and have a maximum contractual life of 10 years .
as established under our equity compensation plans , vesting may accelerate upon retirement after the first anniversary date of the award if certain criteria are met .
we recognize expense related to stock options on a straight-line basis over the requisite service period , less awards expected to be forfeited using estimated forfeiture rates .
due to the accelerated retirement provisions , the requisite service period of our stock options range from one to four years .
stock options are granted with an exercise price equal to the market price of our common stock on the date of grant , except in limited circumstances where local law may dictate otherwise.

**Request 4:** Did abiomed outperform the nasdaq medical equipment index?

**Golden Answer 4:**  
performance graph the following graph compares the yearly change in the cumulative total stockholder return for our last five full fiscal years, based upon the market price of our common stock, with the cumulative total return on a nasdaq composite index (u.s. companies) and a peer group, the nasdaq medical equipment-sic code 3840-3849 index, which is comprised of medical equipment companies, for that period. the performance graph assumes the investment of \$ 100 on march 31, 2007 in our common stock, the nasdaq composite index (u.s. companies) and the peer group index, and the reinvestment of any and all dividends.

|                                             | 3/31/2007 | 3/31/2008 | 3/31/2009 | 3/31/2010 | 3/31/2011 | 3/31/2012 |
| ------------------------------------------- | --------: | --------: | --------: | --------: | --------: | --------: |
| abiomed inc                                 |       100 |     96.19 |     35.87 |     75.55 |    106.37 |    162.45 |
| nasdaq composite index                      |       100 |     94.11 |     63.12 |     99.02 |    114.84 |    127.66 |
| nasdaq medical equipment sic code 3840-3849 |       100 |     82.91 |     41.56 |     77.93 |     94.54 |     74.40 |

this graph is not "soliciting material" under regulation 14a or 14c of the rules promulgated under the securities exchange act of 1934, is not deemed filed with the securities and exchange commission and is not to be incorporated by reference in any of our filings under the securities act of 1933, as amended, or the exchange act whether made before or after the date hereof and irrespective of any general incorporation language in any such filing.
transfer agent american stock transfer & trust company, 59 maiden lane, new york, ny 10038, is our stock transfer agent.

**Request 5:** How much revenue does Microsoft generate from contracts with customers?

**Golden Answer 5:**
Revenue allocated to remaining performance obligations, which includes unearned revenue and amounts that will be invoiced and recognized as revenue in future periods, was $229 billion as of June 30, 2023, of which $224 billion is related to the commercial portion of revenue. We expect to recognize approximately 45% of this revenue over the next 12 months and the remainder thereafter.

**Request 6:** When did Coupang’s Farfetch consolidation start?

**Golden Answer 6:**
As announced on January 31, 2024, the acquisition was completed. At closing, the limited partnership provided additional cash funding to Farfetch of $150 million. Additionally, $150 million previously provided under the bridge loan was contributed towards the Farfetch Acquisition. The limited partnership is further obligated to fund Farfetch up to $200 million within twelve months of the acquisition date.

**Request 7:** What is CPNG's free cash flow?

**Golden Answer 7:** 

Key Financial and Operating Highlights: (in millions)####2023######2022####% Change## Total net revenues##$##24,383####$##20,583####18##% Total net revenues, constant currency(1)##$##24,637####$##23,236####20##% Gross profit(2)##$##6,190####$##4,710####31##% Net income (loss)##$##1,360####$##(92)####NM(3)## Net income (loss) margin####5.6##%####(0.4)##%#### Adjusted EBITDA(1)##$##1,074####$##381####182##% Adjusted EBITDA margin(1)####4.4##%####1.9##%#### Net cash provided by operating activities##$##2,652####$##565####NM(3)## Free cash flow(1)##$##1,775####$##(246)####NM(3)## Segment adjusted EBITDA:################ Product Commerce##$##1,540####$##606####154##% Developing Offerings##$##(466)####$##(225)####107##%

**Request 8**: What was the difference in percentage cumulative total shareholder return on masco common stock versus the s&p 500 index for the five year period ended 2017?

**Golden Answer 8:** 

performance graph the table below compares the cumulative total shareholder return on our common stock with the cumulative total return of ( i ) the standard & poor's 500 composite stock index ( \"s&p 500 index\" ) , ( ii ) the standard & poor's industrials index ( \"s&p industrials index\" ) and ( iii ) the standard & poor's consumer durables & apparel index ( \"s&p consumer durables & apparel index\" ) , from december 31 , 2012 through december 31 , 2017 , when the closing price of our common stock was $ 43.94 .\nthe graph assumes investments of $ 100 on december 31 , 2012 in our common stock and in each of the three indices and the reinvestment of dividends .\nthe table below sets forth the value , as of december 31 for each of the years indicated , of a $ 100 investment made on december 31 , 2012 in each of our common stock , the s&p 500 index , the s&p industrials index and the s&p consumer durables & apparel index and includes the reinvestment of dividends. .\n\n                   | 2013   | 2014   | 2015   | 2016   | 2017  \n------------------------------------- | -------- | -------- | -------- | -------- | --------\nmasco                 | $ 138.48 | $ 155.26 | $ 200.79 | $ 227.08 | $ 318.46\ns&p 500 index             | $ 132.04 | $ 149.89 | $ 151.94 | $ 169.82 | $ 206.49\ns&p industrials index         | $ 140.18 | $ 153.73 | $ 149.83 | $ 177.65 | $ 214.55\ns&p consumer durables & apparel index | $ 135.84 | $ 148.31 | $ 147.23 | $ 138.82 | $ 164.39\n\n$ 50.00 $ 100.00 $ 150.00 $ 200.00 $ 250.00 $ 300.00 $ 350.00 masco s&p 500 index s&p industrials index s&p consumer durables & apparel index

**Request 9:** what is the growth rate in the balance of standby letters of credit from 2006 to 2007?

**Golden Answer 9:** 

the goldman sachs group , inc .\nand subsidiaries notes to consolidated financial statements the firm is unable to develop an estimate of the maximum payout under these guarantees and indemnifications .\nhowever , management believes that it is unlikely the firm will have to make any material payments under these arrangements , and no material liabilities related to these guarantees and indemnifications have been recognized in the consolidated statements of financial condition as of both december 2017 and december 2016 .\nother representations , warranties and indemnifications .\nthe firm provides representations and warranties to counterparties in connection with a variety of commercial transactions and occasionally indemnifies them against potential losses caused by the breach of those representations and warranties .\nthe firm may also provide indemnifications protecting against changes in or adverse application of certain u.s .\ntax laws in connection with ordinary-course transactions such as securities issuances , borrowings or derivatives .\nin addition , the firm may provide indemnifications to some counterparties to protect them in the event additional taxes are owed or payments are withheld , due either to a change in or an adverse application of certain non-u.s .\ntax laws .\nthese indemnifications generally are standard contractual terms and are entered into in the ordinary course of business .\ngenerally , there are no stated or notional amounts included in these indemnifications , and the contingencies triggering the obligation to indemnify are not expected to occur .\nthe firm is unable to develop an estimate of the maximum payout under these guarantees and indemnifications .\nhowever , management believes that it is unlikely the firm will have to make any material payments under these arrangements , and no material liabilities related to these arrangements have been recognized in the consolidated statements of financial condition as of both december 2017 and december 2016 .\nguarantees of subsidiaries .\ngroup inc .\nfully and unconditionally guarantees the securities issued by gs finance corp. , a wholly-owned finance subsidiary of the firm .\ngroup inc .\nhas guaranteed the payment obligations of goldman sachs & co .\nllc ( gs&co. ) and gs bank usa , subject to certain exceptions .\nin addition , group inc .\nguarantees many of the obligations of its other consolidated subsidiaries on a transaction-by-transaction basis , as negotiated with counterparties .\ngroup inc .\nis unable to develop an estimate of the maximum payout under its subsidiary guarantees ; however , because these guaranteed obligations are also obligations of consolidated subsidiaries , group inc . 2019s liabilities as guarantor are not separately disclosed .\nnote 19 .\nshareholders 2019 equity common equity as of both december 2017 and december 2016 , the firm had 4.00 billion authorized shares of common stock and 200 million authorized shares of nonvoting common stock , each with a par value of $ 0.01 per share .\ndividends declared per common share were $ 2.90 in 2017 , $ 2.60 in 2016 and $ 2.55 in 2015 .\non january 16 , 2018 , the board of directors of group inc .\n( board ) declared a dividend of $ 0.75 per common share to be paid on march 29 , 2018 to common shareholders of record on march 1 , 2018 .\nthe firm 2019s share repurchase program is intended to help maintain the appropriate level of common equity .\nthe share repurchase program is effected primarily through regular open-market purchases ( which may include repurchase plans designed to comply with rule 10b5-1 ) , the amounts and timing of which are determined primarily by the firm 2019s current and projected capital position , but which may also be influenced by general market conditions and the prevailing price and trading volumes of the firm 2019s common stock .\nprior to repurchasing common stock , the firm must receive confirmation that the frb does not object to such capital action .\nthe table below presents the amount of common stock repurchased by the firm under the share repurchase program. .\n\nin millions except per share amounts  | year ended december 2017 | year ended december 2016 | year ended december 2015\n-------------------------------------- | ------------------------ | ------------------------ | ------------------------\ncommon share repurchases        | 29.0           | 36.6           | 22.1          \naverage cost per share         | $ 231.87         | $ 165.88         | $ 189.41        \ntotal cost of common share repurchases | $ 6721          | $ 6069          | $ 4195         \n\npursuant to the terms of certain share-based compensation plans , employees may remit shares to the firm or the firm may cancel rsus or stock options to satisfy minimum statutory employee tax withholding requirements and the exercise price of stock options .\nunder these plans , during 2017 , 2016 and 2015 , 12165 shares , 49374 shares and 35217 shares were remitted with a total value of $ 3 million , $ 7 million and $ 6 million , and the firm cancelled 8.1 million , 6.1 million and 5.7 million of rsus with a total value of $ 1.94 billion , $ 921 million and $ 1.03 billion , respectively .\nunder these plans , the firm also cancelled 4.6 million , 5.5 million and 2.0 million of stock options with a total value of $ 1.09 billion , $ 1.11 billion and $ 406 million during 2017 , 2016 and 2015 , respectively .\n166 goldman sachs 2017 form 10-k

**Request 10:** what is the percentage change in revenue generated from non-us currencies from 2015 to 2016?

**Golden Answer 10:** 

in september 2015 , the company entered into treasury lock hedges with a total notional amount of $ 1.0 billion , reducing the risk of changes in the benchmark index component of the 10-year treasury yield .\nthe company designated these derivatives as cash flow hedges .\non october 13 , 2015 , in conjunction with the pricing of the $ 4.5 billion senior notes , the company terminated these treasury lock contracts for a cash settlement payment of $ 16 million , which was recorded as a component of other comprehensive earnings and will be reclassified as an adjustment to interest expense over the ten years during which the related interest payments that were hedged will be recognized in income .\nforeign currency risk we are exposed to foreign currency risks that arise from normal business operations .\nthese risks include the translation of local currency balances of foreign subsidiaries , transaction gains and losses associated with intercompany loans with foreign subsidiaries and transactions denominated in currencies other than a location's functional currency .\nwe manage the exposure to these risks through a combination of normal operating activities and the use of foreign currency forward contracts and non- derivative investment hedges .\ncontracts are denominated in currencies of major industrial countries .\nour exposure to foreign currency exchange risks generally arises from our non-u.s .\noperations , to the extent they are conducted in local currency .\nchanges in foreign currency exchange rates affect translations of revenues denominated in currencies other than the u.s .\ndollar .\nduring the years ended december 31 , 2017 , 2016 and 2015 , we generated approximately $ 1830 million , $ 1909 million and $ 1336 million , respectively , in revenues denominated in currencies other than the u.s .\ndollar .\nthe major currencies to which our revenues are exposed are the brazilian real , the euro , the british pound sterling and the indian rupee .\na 10% ( 10 % ) move in average exchange rates for these currencies ( assuming a simultaneous and immediate 10% ( 10 % ) change in all of such rates for the relevant period ) would have resulted in the following increase or ( decrease ) in our reported revenues for the years ended december 31 , 2017 , 2016 and 2015 ( in millions ) : .\n\ncurrency          | 2017 | 2016 | 2015 \n-------------------------- | ----- | ----- | -----\npound sterling       | $ 42 | $ 47 | $ 34 \neuro            | 35  | 38  | 33  \nreal            | 39  | 32  | 29  \nindian rupee        | 14  | 12  | 10  \ntotal increase or decrease | $ 130 | $ 129 | $ 106\n\nwhile our results of operations have been impacted by the effects of currency fluctuations , our international operations' revenues and expenses are generally denominated in local currency , which reduces our economic exposure to foreign exchange risk in those jurisdictions .\nrevenues included $ 16 million favorable and $ 100 million unfavorable and net earnings included $ 2 million favorable and $ 10 million unfavorable , respectively , of foreign currency impact during 2017 and 2016 resulting from changes in the u.s .\ndollar during these years compared to the preceding year .\nin 2018 , we expect minimal foreign currency impact on our earnings .\nour foreign exchange risk management policy permits the use of derivative instruments , such as forward contracts and options , to reduce volatility in our results of operations and/or cash flows resulting from foreign exchange rate fluctuations .\nwe do not enter into foreign currency derivative instruments for trading purposes or to engage in speculative activity .\nwe do periodically enter into foreign currency forward exchange contracts to hedge foreign currency exposure to intercompany loans .\nwe did not have any of these derivatives as of december 31 , 2017 .\nthe company also utilizes non-derivative net investment hedges in order to reduce the volatility in the income statement caused by the changes in foreign currency exchange rates ( see note 11 of the notes to consolidated financial statements ) .

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
