from yattag import Doc
import codecs
name_file = "amountParkingTime.html"
doc, tag, text = Doc().tagtext()
context_li_time_and_langtool = """
    <li><a href="#"><img src="images/back.png"></a></li>
    <li id='highBarTime'></li>
    <li id="langToolBar">
        <div id='highBarLangRus' class='active'>УКР</div>
        <div id='highBarLangEng'>ENG</div>
    </li>
    """
context_textarea = """
    <li><div class="diff" id="diffOne">-</div></li>
    <li><span class="amount" id="amountOne">00</span></li>
    <li><div class="plus" id="plusOne">+</div></li>
    <li><div class="diff" id="diffTwo">-</div></li>
    <li><span class="amount" id="amountTwo">00</span></li>
    <li><div class="plus" id="plusTwo">+</div></li>
"""
context_li_operation_succesful = """
    <li><h3>ДО СПЛАТИ</h3></li>
"""
context_text_under_butt = """
    <li class="textUnderButt">мінімум: 1 година</li>
    <li class="textUnderButt" id="rightText">крок: 15 хвилин</li>
"""
context_li_footer_bar = """
    <li id="numberParcomat"></li>
    <li class="forward"><a href="#" target="_blank"><img src="images/grn.png"></li></li>
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
            let looperOne = 0;
            let looperTwo = 0;
            let plusDiff = document.querySelectorAll('.diff, .plus');
            let amountOne = document.getElementById('amountOne');
            let amountTwo = document.getElementById('amountTwo');
            plusDiff.forEach(function(button, index){
                button.addEventListener('click', function(el){
                    if(button.id == "plusOne"){
                        looperOne++;
                        if(looperOne > 9){
                            amountOne.innerHTML = looperOne;
                        }
                        else{
                            amountOne.innerHTML = '0' +  looperOne;
                        }
                    }
                    else if(button.id == "diffOne"){
                        looperOne--;
                        if(looperOne < 0){
                            looperOne = 0;
                            amountOne.innerHTML = '00';
                        }
                        else{
                            amountOne.innerHTML = '0' +   looperOne;
                        }
                    }
                    else if(button.id == "plusTwo"){
                        looperTwo++;
                        if(looperTwo > 9){
                            amountOne.innerHTML = looperTwo;
                        }
                        else{
                            amountTwo.innerHTML = '0' +   looperTwo;
                        }
                    }
                    else if(button.id == "diffTwo"){
                        looperTwo--;
                        if(looperTwo < 0){
                            looperTwo = 0;
                            amountTwo.innerHTML = '00';
                        }
                        else{
                            amountTwo.innerHTML = '0' +   looperTwo;
                        }
                    }
                })
            })
    }
"""
doc.asis('<!DOCTYPE html>')
with tag('html', lang="en"):
    with tag('head'):
        doc.asis('<meta http-equiv="Content-Type" content="text/html; charset=utf-8">')
        doc.asis('<link rel="stylesheet" type="text/css" href="css/styleAmountParkingTime.css">')
        doc.asis('<title>Оплата успішна</title>')
    with tag('body'):
        with tag('div class="wrapper"'):
            doc.asis('<ul class="highBar">' + context_li_time_and_langtool + '</ul>')
            doc.asis('<ul class="spaceInput">' + context_textarea + '</ul>')
            doc.asis('<ul class="textUnderButt">' + context_text_under_butt + '</ul>')
            doc.asis('<ul class="operationSuccesful">' + context_li_operation_succesful + '</ul>')
            doc.asis('<ul class="footerBar">' + context_li_footer_bar + '</ul>')
            doc.asis('<script>' + script_time_and_lang + '</script>')
result = doc.getvalue()
file = codecs.open(name_file, "a", "utf-8")
with open(name_file, "w"):
    pass
file.write(result)