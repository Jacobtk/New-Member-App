from api.models import Member
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.pdfmetrics import stringWidth

lineSeparator = .3 * inch
margin = inch * .75


def generate_header(pdf, id, remaining_space):
    width, height = remaining_space
    member = Member.objects.get(id=id)
    print inch
    title = "New Member Information Form: " + member.full_name
    pdf.drawCentredString(width/2, height - .25*inch, title)

    return width, height - inch * .7


def add_entry(pdf, position, data):
    width, height = position

    pdf.drawString(margin, height, data)
    return width, height - lineSeparator


def generate_core_data_entries(pdf, id, remaining_space):
    width, height = remaining_space
    member = Member.objects.get(id=id)
    pdf.setFont('Times-Bold', 12)
    remaining_space = add_entry(pdf, remaining_space, "Personal")
    pdf.setFont('Times-Roman', 12)
    remaining_space = add_entry(pdf, remaining_space, "Full Name: " + member.full_name)
    remaining_space = add_entry(pdf, remaining_space, "Preferred Name: " + (member.preferred_name if member.preferred_name is not None else "None"))
    remaining_space = add_entry(pdf, remaining_space, "Phone Number: " + member.phone)
    remaining_space = add_entry(pdf, remaining_space, "Address: " + member.address)
    remaining_space = add_entry(pdf, remaining_space, "Date of Birth: " + member.date_of_birth)
    remaining_space = add_entry(pdf, remaining_space, "Email: " + (member.email if member.email else "None"))

    return remaining_space


def generate_custom_fields(pdf):
    pass


def generate_footer(pdf):
    pass

def generate_pdf(response, id):
    # Create the PDF object, using the response object as its "file."
    pdf = canvas.Canvas(response, pagesize=letter)
    width, height = letter

    remaining_space = letter
    # print pdf.getAvailableFonts()
    pdf.setFont('Times-Roman', 15)
    remaining_space = generate_header(pdf, id, remaining_space)
    remaining_space = generate_core_data_entries(pdf, id, remaining_space)
    generate_custom_fields(pdf)
    generate_footer(pdf)

    pdf.showPage()
    pdf.save()


