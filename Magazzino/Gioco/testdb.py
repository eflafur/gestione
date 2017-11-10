from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from django.contrib.auth.models import User



class MyPrint:


    def __init__(self, buffer, pagesize):
        self.buffer = buffer
        if pagesize == 'A4':
            self.pagesize = A4
        elif pagesize == 'Letter':
            self.pagesize = letter
        self.width, self.height = self.pagesize

    @staticmethod
    def _header_footer(canvas, doc):
        # Save the state of our canvas so we can draw on it
        canvas.saveState()
        styles = getSampleStyleSheet()

        # Header
        header = Paragraph('This is a multi-line header.  It goes on every page.   ' * 5, styles['Normal'])
        w, h = header.wrap(doc.width, doc.topMargin)
        header.drawOn(canvas, doc.leftMargin, doc.height + doc.topMargin - h)

        # Footer
        footer = Paragraph('This is a multi-line footer.  It goes on every page.   ' * 5, styles['Normal'])
        w, h = footer.wrap(doc.width, doc.bottomMargin)
        footer.drawOn(canvas, doc.leftMargin, h)

        # Release the canvas
        canvas.restoreState()


    def print_users(self):
        buffer = self.buffer
        doc = SimpleDocTemplate(buffer,
                                rightMargin=72,
                                leftMargin=72,
                                topMargin=72,
                                bottomMargin=72,
                                pagesize=self.pagesize)

        # Our container for 'Flowable' objects
        elements = []

        # A large collection of style sheets pre-made for us
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        users = User.objects.all()
        elements.append(Paragraph('My User Names', styles['Heading1']))
        for i, user in enumerate(users):
            elements.append(Paragraph(user.get_full_name(), styles['Normal']))

        doc.build(elements, onFirstPage=self._header_footer, onLaterPages=self._header_footer,
                  canvasmaker=NumberedCanvas)

        # Get the value of the BytesIO buffer and write it to the response.
        pdf = buffer.getvalue()
        buffer.close()
        return pdf

    '''
        Usage with django

    @staff_member_required
    def print_users(request):
        # Create the HttpResponse object with the appropriate PDF headers.
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="My Users.pdf"'

        buffer = BytesIO()

        report = MyPrint(buffer, 'Letter')
        pdf = report.print_users()

        response.write(pdf)
        return response
    '''


class NumberedCanvas(canvas.Canvas):


    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []


    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()


    def save(self):
        """add page info to each page (page x of y)"""
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)


    def draw_page_number(self, page_count):
        # Change the position of this to wherever you want the page number to be
        self.drawRightString(211 * mm, 15 * mm + (0.2 * inch),
                             "Page %d of %d" % (self._pageNumber, page_count))




#----------------------------------------------------------------

#from gestione.models import sp, ce,ivacliente,libro

#import reportlab
#from reportlab.pdfgen import canvas
#from reportlab.lib.pagesizes import letter, A4,inch
#from reportlab.lib.colors import pink, black, red, blue, green
##from reportlab.lib.units import inch
    

#class Pdf:
    #def __init__(self,filename,pagesize=A4,bottomup = 1,pageCompression=0,verbosity=0,encrypt=None):
        #self.filename=filename
        #self.psize=pagesize
    #def Do(self):
        #c=canvas.Canvas(self.filename,pagesize=A4)
        ##c.drawString(8.2*inch, 11.6*inch, "F")
        ##c.drawString(595, 842, "H")
        #num=0
        #x=300
        #y=830
        #size=5
        ##while (num<30):
            ##c.setFont("Helvetica", size)
            ##c.drawString(x,y, "adesso scrivo "+str(num))
            ##y-=10
            ##num+=1
            ##size+=1


        #invoice=c.beginText(x,y)
        #invoice.setFont("Helvetica",size)
        #num=0
        #while (num<10):
            ##invoice.setCharSpace(num)
            ##invoice.setWordSpace(num)
            ##invoice.setLeading(num+4)
            #invoice.textLine("adesso scrivo" +str(num))
            #num+=1
        ##c.setFont("Courier", 60)
        #c.setFillColorRGB(1, 0, 0)
        ##c.drawCentredString(letter[0] / 2, inch * 6, "CLASSIFIED")
        #c.drawText(invoice)
        #c.showPage()
        #c.save()
        



    