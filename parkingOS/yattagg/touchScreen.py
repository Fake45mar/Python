from yattag import Doc
import codecs
name_file = "touchScreen.html"
doc, tag, text = Doc().tagtext()
context_li_time_and_langtool = """
    <li id='highBarTime'></li>
    <li id='highBarLangRus' class='active'>УКР</li>
    <li id="highBarLangEng">ENG</li>"""
context_li_operation_succesful = """
    <li id="touchScreen"><h2>Торкніться екрану</h2></li>
    <li class="imgN"><img id="handFing" src="images/handFing.png"</li>
"""
context_li_footer_bar = """
    <li id="numberParcomat"></li>
    <li class="serviceHelp"><a href="#" target="_blank">Служба підтримки</a></li>
"""
script_time_and_lang = """
    window.onload = ()=>{
        let date = new Date();
        document.getElementById('highBarTime').innerHTML = date.getHours() + ':' + date.getMinutes();
        let rus = document.getElementById('highBarLangRus'),
            eng = document.getElementById('highBarLangEng'),
            langArr = [rus, eng],
            parkRobot = {
                location:"Where is this robot locate?",
                numberParkRobot:360
            };
            document.getElementById('numberParcomat').innerHTML = "Паркомат №" +  parkRobot.numberParkRobot;
            for(var i = 0;i < langArr.length;i++){
                langArr[i].addEventListener('click', function(){
                    if(event.target.id == "highBarLangEng"){
                        eng.classList.add('active');
                        rus.classList.remove('active');
                    }
                    else if(event.target.id == "highBarLangRus"){
                        rus.classList.add('active');
                        eng.classList.remove('active');
                    }
                })
            }
    }
"""
doc.asis('<!DOCTYPE html>')
with tag('html', lang="en"):
    with tag('head'):
        doc.asis('<meta http-equiv="Content-Type" content="text/html; charset=utf-8">')
        doc.asis('<link rel="stylesheet" type="text/css" href="css/styleTouchScreen.css">')
        doc.asis('<title>Торкніться екрану</title>')
        with tag('body'):
            with tag('div class="wrapper"'):
                doc.asis('<ul class="highBar">' + context_li_time_and_langtool + '</ul>')
                doc.asis('<ul class="operationSuccesful">' + context_li_operation_succesful + '</ul>')
                doc.asis('<ul class="footerBar">' + context_li_footer_bar + '</ul>')
                doc.asis('<script>' + script_time_and_lang + '</script>')
result = doc.getvalue()
file = codecs.open(name_file, "a", "utf-8")
with open(name_file, "w"):
    pass
file.write(result)