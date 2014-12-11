from django.views.generic.base import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from api.models import Member
from api.serializers import UserSerializer
from authentication import QuietBasicAuthentication
from easy_pdf.views import PDFTemplateView

from reportlab.pdfgen import canvas
from django.http import HttpResponse

from pdf_generator import generate_pdf


class IndexView(TemplateView):
    template_name = "index.html"


class AuthView(APIView):
    authentication_classes = (QuietBasicAuthentication,)
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return Response(self.serializer_class(request.user).data)


class HelloPDFView(PDFTemplateView):
    template_name = "pdf_template.html"


def pdf_view(request, pk):
    member = Member.objects.get(id=pk)

    # import pdb; pdb.set_trace()
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    # # Create the PDF object, using the response object as its "file."
    # p = canvas.Canvas(response)
    #
    # # Draw things on the PDF. Here's where the PDF generation happens.
    # # See the ReportLab documentation for the full list of functionality.
    # p.drawString(100, 100, "Hello world.")
    #
    # # Close the PDF object cleanly, and we're done.
    # p.showPage()
    # p.save()
    generate_pdf(response, pk)

    return response