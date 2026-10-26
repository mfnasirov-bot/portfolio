"""Generates sample invoice PDFs (different layouts) for testing and demos."""

from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

OUT = Path(__file__).parent / "sample_invoices"

INVOICES = [
    {
        "file": "acme_supplies.pdf",
        "vendor": "Acme Office Supplies Ltd.",
        "lines": [
            "INVOICE", "Invoice No: INV-2026-0412", "Date: 14 October 2026", "Due: 13 November 2026",
            "", "Bill to: Northwind Trading LLC",
            "", "Printer paper A4 (20 boxes)          $180.00",
            "Toner cartridges (6)                   $420.00",
            "", "Subtotal: $600.00", "Tax (10%): $60.00", "TOTAL DUE: $660.00",
        ],
    },
    {
        "file": "baku_logistics.pdf",
        "vendor": "Baku Logistics MMC",
        "lines": [
            "Hesab-faktura / Invoice", "No. BL-7781", "Issued: 2026-10-02",
            "Payment terms: 15 days",
            "", "Customer: Caspian Retail Group",
            "", "Freight Baku -> Ganja, 3 pallets      1 250,00 AZN",
            "Insurance                              75,00 AZN",
            "", "VAT 18%: 238,50 AZN", "Grand total: 1 563,50 AZN",
        ],
    },
    {
        "file": "cloudhost_eu.pdf",
        "vendor": "CloudHost Europe GmbH",
        "lines": [
            "Rechnung / Invoice", "Invoice #: CH-EU-90215", "Invoice date: 01.10.2026",
            "", "Customer ID: 55120",
            "", "Dedicated server (October)            EUR 249,00",
            "Backup storage 2 TB                    EUR 39,00",
            "", "Net: EUR 288,00", "VAT 19%: EUR 54,72", "Amount due: EUR 342,72",
        ],
    },
]


def main() -> None:
    OUT.mkdir(exist_ok=True)
    for inv in INVOICES:
        c = canvas.Canvas(str(OUT / inv["file"]), pagesize=A4)
        _, height = A4
        c.setFont("Helvetica-Bold", 18)
        c.drawString(60, height - 70, inv["vendor"])
        c.setFont("Helvetica", 11)
        y = height - 110
        for line in inv["lines"]:
            c.drawString(60, y, line)
            y -= 18
        c.save()
        print(f"Created {OUT / inv['file']}")


if __name__ == "__main__":
    main()
