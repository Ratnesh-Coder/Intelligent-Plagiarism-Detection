# ============================================================
# HTML REPORT GENERATION
# ============================================================

import json

def highlight_text(text, matches):

    highlighted = text

    for m in matches:
        sentence = m["source"]
        
        highlighted = highlighted.replace(
            sentence,
            f"<mark style='background-color:#ff9999'>{sentence}</mark>"
        )

    return highlighted

def generate_html_report(results, matches):

    labels = []
    scores = []
    
    for doc, score, *_ in results:
        labels.append(doc)
        scores.append(round(score, 2))
        
    labels_json = json.dumps(labels)
    scores_json = json.dumps(scores)
    
    top_score = scores[0] if scores else 0
    original_score = 100 - top_score
    
    pie_data = json.dumps([top_score, original_score])  

    html = f"""
        <html>
            <head>
            <title>Plagiarism Report</title>
            <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
            <style>
                body{{font-family:Arial;margin:40px}}
                table{{border-collapse:collapse;width:70%}}
                th,td{{border:1px solid #ccc;padding:10px}}
                th{{background:#f2f2f2}}
                .high{{color:red;font-weight:bold}}
                .match{{
                    border-left:5px solid #dc3545;
                    background:#fafafa;
                    padding:15px;
                    margin:15px 0;
                    box-shadow:0 2px 5px rgba(0,0,0,0.1)
                }}
            </style>
        </head>
        <body>
            <h1>Plagiarism Detection Report</h1>
                <button onclick="downloadReport()"
                    style="
                    padding:10px 15px;
                    background:#007bff;
                    color:white;
                    border:none;
                    border-radius:5px;
                    cursor:pointer;
                    margin-bottom:20px;">
                    Download Report
                </button>
            <h2>Document Similarity</h2>
            <div style="display:flex;gap:50px;align-items:center"></div>
            <div style="width:500px"><canvas id="similarityChart"></canvas></div>
            <div style="width:300px;margin-top:40px"><canvas id="pieChart"></canvas></div>
            <table>
                <tr>
                    <th>Document</th>
                    <th>Similarity</th>
                </tr>
            """
    if not results:
        html += """
            <tr>
                <td colspan="2" style="color:red;font-weight:bold;text-align:center;">
                    No similar documents were detected.
                </td>
            </tr>
            """

    # --------------------------------------------------------
    # HIGHLIGHTED DOCUMENT
    # --------------------------------------------------------

    if results:
        best_doc_text = results[0][3]
        highlighted_doc = highlight_text(best_doc_text, matches)
        html += f"""
            <h2>Highlighted Source Document</h2>
            <div style="
                line-height:1.6;
                border:1px solid #ccc;
                padding:15px;
                margin-top:20px;
                background:#ffffff">
                {highlighted_doc}
            </div>
            """

    # --------------------------------------------------------
    # TABLE CONTENT
    # --------------------------------------------------------
    
    for doc, score, *_ in results:
        style = "class='high'" if score > 70 else ""
        html += f"""
            <tr>
            <td>{doc}</td>
            <td {style}>{round(score,2)}%</td>
            </tr>
            """

    html += "</table>"

    # --------------------------------------------------------
    # MATCHED SENTENCES
    # --------------------------------------------------------

    html += "<h2>Detected Plagiarized Sentences</h2>"

    for m in matches:
        html += f"""
            <div class='match'>
                <p><b>Query Sentence:</b></p>
                <p style="background-color:#fff3cd;padding:8px;border-radius:5px">
                    {m['query']}
                </p>
                <p><b>Matched Source Sentence:</b></p>
                <p style="background-color:#f8d7da;padding:8px;border-radius:5px">
                    {m['source']}
                </p>
            <p><b>Similarity:</b> {round(m['score'],2)}</p>
            </div>
            """

    # --------------------------------------------------------
    # CHART SCRIPT
    # --------------------------------------------------------

    html += f"""
        <script>

            function downloadReport() {{
                const element = document.createElement('a');
                element.href = 'plagiarism_report.html';
                element.download = 'plagiarism_report.html';
                document.body.appendChild(element);
                element.click();
                document.body.removeChild(element);
            }}
            
            const ctx = document.getElementById('similarityChart');
            
            new Chart(ctx, {{
                type: 'bar',
                data: {{
                    labels: {labels_json},
                    datasets: [{{
                        label: 'Plagiarism Similarity (%)',
                        data: {scores_json},
                        backgroundColor: 'rgba(220,53,69,0.6)',
                        borderColor: 'rgba(220,53,69,1)',
                        borderWidth: 1
                    }}]
                }},

                options: {{
                    scales: {{
                        y: {{
                            beginAtZero: true,
                            max: 100
                        }}
                    }}
                }}
            }});
            
            const pieCtx = document.getElementById('pieChart');
            new Chart(pieCtx, {{
                type: 'pie',
                data: {{
                    labels: ['Plagiarized', 'Original'],
                    datasets: [{{
                        data: {pie_data},
                        backgroundColor: [
                            'rgba(220,53,69,0.8)',
                            'rgba(40,167,69,0.8)'
                        ]
                    }}]
                }}
            }});
            
        </script>
    </body>
</html>
"""

    # --------------------------------------------------------
    # SAVE REPORT
    # --------------------------------------------------------

    with open("plagiarism_report.html", "w", encoding="utf-8") as f:
        f.write(html)