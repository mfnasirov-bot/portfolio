# AI Invoice Extractor

Reads PDF invoices with Claude AI and puts the key data into an Excel file, in any layout and any language.

**Extracted fields:** vendor, invoice number, invoice date, due date, total amount, currency.

**Safety net:** if a field is missing or unclear, the AI does not guess. The row is highlighted yellow in Excel with a "Needs review" reason, so no wrong numbers slip through.

## Setup

```bash
pip install -r requirements.txt
```

Set your Anthropic API key (get one at https://console.anthropic.com):

```powershell
$env:ANTHROPIC_API_KEY = "your-key-here"
```

## Usage

```bash
# Create 3 sample invoices (USD, AZN, EUR, in different layouts)
python make_samples.py

# Extract all invoices in a folder into Excel
python invoice_extractor.py sample_invoices -o invoices.xlsx

# Or a single file
python invoice_extractor.py path/to/invoice.pdf
```

## How it works

1. Each PDF is sent to Claude, which reads it directly, including scanned PDFs.
2. Claude returns the data in a fixed, validated structure (structured outputs).
3. The results are written to Excel with formatted headers; uncertain rows are highlighted.

Cost: roughly $0.01–0.03 per invoice, so 200 invoices a month cost a few dollars.
