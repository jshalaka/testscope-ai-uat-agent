# TestScope AI — UAT Test Design Agent

TestScope AI is a proof-of-concept AI agent that analyses software requirements, identifies ambiguities and generates structured, risk-based User Acceptance Testing (UAT) test cases.

> Project status: **Planning and design — Step 1: POC scope definition**

## Why this project?

Testers frequently receive requirements that contain incomplete business rules, unclear acceptance criteria or hidden assumptions. Analysing these gaps and producing a traceable UAT test pack is valuable but time-consuming work.

TestScope AI is intended to support that process by producing a reviewable first draft while keeping the tester in control of business decisions.

## POC objective

Build an AI-powered agent that can:

- analyse one business requirement and its acceptance criteria;
- extract explicit business rules;
- identify ambiguities, missing information and assumptions;
- generate clarification questions before test design;
- produce positive, negative, boundary and end-to-end UAT test cases;
- assign risk and priority;
- validate acceptance-criteria coverage; and
- allow the tester to review and export the generated test pack.

## Planned workflow

1. The tester enters a requirement and acceptance criteria.
2. The agent extracts business rules and risks.
3. The agent presents ambiguities and clarification questions.
4. The tester answers the questions or approves documented assumptions.
5. The agent generates structured UAT test cases.
6. Rule-based checks validate completeness and traceability.
7. The tester reviews, edits and exports the results.

## Human-in-the-loop principle

The agent will not silently invent missing business rules. Missing information must be shown as a clarification question or a clearly labelled assumption. Final approval remains with the tester or business stakeholder.

## Initial technology direction

| Area | Proposed technology |
|---|---|
| Language | Python |
| Interface | Streamlit |
| AI orchestration | OpenAI Agents SDK |
| Data validation | Pydantic |
| Test-pack processing | Pandas |
| Automated checks | Pytest |
| Export | CSV initially, Excel later |

Technology choices will be confirmed during the implementation-design stage.

## Documentation

- [Project overview](docs/project-overview.md)
- [Problem statement](docs/problem-statement.md)
- [POC scope](docs/poc-scope.md)

Future documents will cover the sample requirement, structured output schema, solution architecture, implementation plan and evaluation strategy.

## Roadmap

- [x] Create repository
- [x] Define the project problem and initial POC scope
- [ ] Finalise the sample banking requirement
- [ ] Define input and output schemas
- [ ] Design the solution architecture
- [ ] Build the command-line prototype
- [ ] Add rule-based validation
- [ ] Build the Streamlit interface
- [ ] Add CSV and Excel export
- [ ] Evaluate the agent using benchmark requirements
- [ ] Deploy the demonstration application

## Responsible use and data protection

This project will use synthetic or publicly shareable requirements only. API keys, personal data, customer data and confidential company requirements must never be committed to the repository.

## Author

**Shalaka Jaitapkar**

## Licence

This project is available under the [MIT License](LICENSE).
