from yattag import Doc
import codecs
name_file = "succesfulPayment.html"
doc, tag, text = Doc().tagtext()
context_li_time_and_langtool = """
    <li class='highBarTime'>qwe</li>
    <li class='highBarLang'>абв</li>"""
context_li_operation_succesful = """
    <li class="imgN"></li>
    <li><h2>оплата успішна</h2></li>
    <li><h3>не забудьте забрати чек</h3></li>
"""
context_li_footer_bar = """
    <li class="numberParcomat">Паркомат №</li>
    <li class="serviceHelp"><a href="#" target="_blank">Служба підтримки</a></li>
"""
doc.asis('<!DOCTYPE html>')
with tag('html', lang="en"):
    with tag('head'):
        doc.asis('<meta http-equiv="Content-Type" content="text/html; charset=utf-8">')
        doc.asis('<link rel="stylesheet" type="text/css" href="css/style.css">')
        doc.asis('<title>Оплата успішна</title>')
    with tag('body'):
        doc.asis('<ul class="highBar">' + context_li_time_and_langtool + '</ul>')
        doc.asis('<ul class="operationSuccesful">' + context_li_operation_succesful + '</ul>')
        doc.asis('<ul class="footerBar">' + context_li_footer_bar + '</ul>')
        doc.asis('<script></script>')
result = doc.getvalue()
file = codecs.open(name_file, "a", "utf-8")
with open(name_file, "w"):
    pass
file.write(result)