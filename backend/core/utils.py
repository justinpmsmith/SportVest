from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A6
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO


class Utils:
    @staticmethod
    def generateReceipt(product_data, receipt_no, total_price):
        # Data for the table
        table_data = [
            ["Product Code", "Product Name", "Price (R)"],
        ]

        # Populate table_data with product details
        for product_code, product_info in product_data.items():
            product_name = product_info.get('name', '')
            product_price = product_info.get('price', 0)
            table_data.append([product_code, product_name, f"{product_price:.2f}"])

        # Add the total row to the table
        table_data.append(["", "", ""])
        table_data.append(["Total", '', f"{total_price:.2f}"])

        # Create a BytesIO buffer for in-memory PDF content
        pdf_buffer = BytesIO()

        # Create a Base Document Template of page size A4
        pdf = SimpleDocTemplate(pdf_buffer, pagesize=A6)

        # Standard stylesheet defined within reportlab itself
        styles = getSampleStyleSheet()

        # Fetching the style of Top-level heading (Heading1)
        title_style = styles["Heading1"]

        # Set the font size to a smaller value (e.g., 8)
        title_style.fontSize = 6

        # Alignment: 0 for left, 1 for center, 2 for right
        title_style.alignment = 1

        # Creating the paragraph with the heading text and passing the styles
        title = Paragraph(f"Receipt Number: {receipt_no}", title_style)

        # Creating a Table Style object and defining the styles row-wise
        style = TableStyle(
            [
                ("BOX", (0, 0), (-1, -1), 1, colors.black),
                ("GRID", (0, 0), (2, len(table_data) - 1), 1, colors.black),
                ("BACKGROUND", (0, 0), (2, 0), colors.gray),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
            ]
        )

        # Creating a table object and passing the style to it
        table = Table(table_data, style=style)

        # Building the actual PDF putting together all the elements
        pdf.build([title, table])

        # Get the PDF content from the buffer
        pdf_content = pdf_buffer.getvalue()

        # Close the buffer
        pdf_buffer.close()

        # Return the PDF content
        return pdf_content