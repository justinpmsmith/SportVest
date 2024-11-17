from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle, Image, Spacer
from reportlab.lib import colors
from reportlab.lib.pagesizes import A6
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO
import os
from django.core.mail import EmailMessage
from .models import Product, Sold, Receipt

from django.conf import settings


class Utils:
    @staticmethod
    def generateReceipt(product_data, receipt_info):
        # Data for the table
        table_data = [
            ["Product Code", "Product Name", "Price (R)"],
        ]

        # Populate table_data with product details
        for product_code, product_info in product_data.items():
            product_name = product_info.get('name', '')
            product_price = product_info.get('price', 0)
            table_data.append([product_code, product_name, f"{product_price:.2f}"])

        table_data.append(["", "Shipping", str(receipt_info['shipping_fee'])])

        # Add the total row to the table
        table_data.append(["", "", ""])
        table_data.append(["Total", '', f"{receipt_info['total_price']:.2f}"])

        # Create a BytesIO buffer for in-memory PDF content
        pdf_buffer = BytesIO()

        # Create a Base Document Template of page size A6
        pdf = SimpleDocTemplate(pdf_buffer, pagesize=A6)

        # Standard stylesheet defined within reportlab itself
        styles = getSampleStyleSheet()

        # Fetching the style of Top-level heading (Heading1)
        title_style = styles["Heading1"]

        # Set the font size to a smaller value (e.g., 8)
        title_style.fontSize = 6

        # Alignment: 0 for left, 1 for center, 2 for right
        title_style.alignment = 0

        # Load the logo image from the file
        logo_path = os.path.join(os.path.dirname(__file__), 'assets', 'logo.png')
        logo = Image(logo_path, width=50, height=50)  # Adjust the width and height as needed

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

        # Creating the paragraph with the heading text and passing the styles
        title = Paragraph(f"Receipt Number: {receipt_info['receipt_no']} ", title_style)
        billed_to = Paragraph(f"Billed to: {receipt_info['customer_name']} ", title_style)

        delivery_address = Paragraph(f"Delivery Location: {receipt_info['delivery_location']} ", title_style)

        new_line = Spacer(0, -15)

        # Building the actual PDF putting together all the elements
        pdf.build([Spacer(0, -40),
                   logo,
                   Spacer(0, 15),
                   title,
                   new_line,
                   billed_to,
                   new_line,
                   delivery_address,
                   table])

        # Get the PDF content from the buffer
        pdf_content = pdf_buffer.getvalue()

        # Close the buffer
        pdf_buffer.close()

        # Return the PDF content
        return pdf_content

    @staticmethod
    def emailReceipt(pdf_receipt, info):
        subject = f"SportVest receipt {info['receipt_no']}"
        message = f"Dear {info['name']}, \n\nThank you for your purchase " \
                  f"\n\nIf you have chosen to collect your order we will be in contact shortly to make arrangements; " \
                  f"Otherwise you can expect your order 2-5 working days at the pudo locker you provided." \
                  f"\nLocation: {info['address']}" \
                  f"\nContact Cell: {info['cell']}" \
                  f"\n\nIf you have any queries please contact Cherise at " \
                  f"\nEmail: {settings.ADMIN_EMAIL}" \
                  f"\nCell: {settings.ADMIN_CELL}" \
                  f"\n\nThank you for your support"

        from_email = settings.EMAIL_HOST_USER
        to_email = [settings.ADMIN_EMAIL, info['email'], settings.BACKUP_ADMIN_EMAIL]

        email = EmailMessage(subject, message, from_email, to_email)

        # Attach the PDF to the email
        email.attach('SportVest_receipt.pdf', pdf_receipt, 'application/pdf')

        # Send the email
        email.send()

    @staticmethod
    def emailContactUsMessage(info):
        subject = f"Contact us message"
        message = f"Name {info['name']}" \
                  f"\nEmail: ${info['email']}" \
                  f"\nCell{info['cell']}" \
                  f"\n\nMessage: {info['message']}"

        from_email = settings.EMAIL_HOST_USER
        to_email = [settings.ADMIN_EMAIL, settings.BACKUP_ADMIN_EMAIL]

        email = EmailMessage(subject, message, from_email, to_email)
        email.send()

        pass

    @staticmethod
    def updateDb(info):
        products = info['products']
        # add to receipts table
        receipt_entry = Receipt(receiptNo=info['receipt_no'],
                                buyerName=info['name'],
                                cell=info['cell'],
                                email=info['email'],
                                address=info['address'],
                                totalPrice=info['totalPrice'])
        receipt_entry.save()
        for product in products.values():
            # remove Product from Produtcs table
            print("product number: " + product['prodCode'])
            db_product = Product.objects.get(prodCode=product['prodCode'])
            db_product.delete()

            # add to Sold table
            sold_entry = Sold(prodName=product['name'],
                              prodCode=product['prodCode'],
                              price=product['price'],
                              receipt=receipt_entry,
                              receiptNo=info['receipt_no'])
            sold_entry.save()
