from yattag import Doc
import codecs
name_file = "enterNumberOfVehicle.html"
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
    <li><div id="num" class="buttonBlue">123</div></li>
    <li class="imgN"><input type="text" id="numberOfVehicle" placeholder="НОМЕР АВТО"></li>
    <li><img id="del" class="keyBtn" src="images/del.png"></li>
"""
context_li_operation_succesful = """
    <li class="keyHolder">
        <div class="keyBtn keyboard letter">й</div>
        <div class="keyBtn keyboard letter">ц</div>
        <div class="keyBtn keyboard letter">у</div>
        <div class="keyBtn keyboard letter">к</div>
        <div class="keyBtn keyboard letter">е</div>
        <div class="keyBtn keyboard letter">н</div>
        <div class="keyBtn keyboard letter">г</div>
        <div class="keyBtn keyboard letter">ш</div>
        <div class="keyBtn keyboard letter">щ</div>
        <div class="keyBtn keyboard letter">з</div>
        <div class="keyBtn keyboard letter">х</div>
        <div class="keyBtn keyboard letter">ї</div>
    </li>
    <li class="keyHolder">
        <div class="keyBtn keyboard letter">ф</div>
        <div class="keyBtn keyboard letter">и</div>
        <div class="keyBtn keyboard letter">в</div>
        <div class="keyBtn keyboard letter">а</div>
        <div class="keyBtn keyboard letter">п</div>
        <div class="keyBtn keyboard letter">р</div>
        <div class="keyBtn keyboard letter">о</div>
        <div class="keyBtn keyboard letter">л</div>
        <div class="keyBtn keyboard letter">д</div>
        <div class="keyBtn keyboard letter">ж</div>
        <div class="keyBtn keyboard letter">є</div>
    </li>
    <li class="keyHolder">
        <div class="keyBtn keyboard letter">ґ</div>
        <div class="keyBtn keyboard letter">я</div>
        <div class="keyBtn keyboard letter">ч</div>
        <div class="keyBtn keyboard letter">с</div>
        <div class="keyBtn keyboard letter">м</div>
        <div class="keyBtn keyboard letter">і</div>
        <div class="keyBtn keyboard letter">т</div>
        <div class="keyBtn keyboard letter">ь</div>
        <div class="keyBtn keyboard letter">б</div>
        <div class="keyBtn keyboard letter">ю</div>
        <div id="englB" class="buttonBlue">ENG</div>
    </li>
    <li id="buttonNumbers">
        <div class="keyBtn buttonNums keyboard">1</div>
        <div class="keyBtn buttonNums keyboard">2</div>
        <div class="keyBtn buttonNums keyboard">3</div>
        <div class="keyBtn buttonNums keyboard">4</div>
        <div class="keyBtn buttonNums keyboard">5</div>
        <div class="keyBtn buttonNums keyboard">6</div>
        <div class="keyBtn buttonNums keyboard">7</div>
        <div class="keyBtn buttonNums keyboard">8</div>
        <div class="keyBtn buttonNums keyboard">9</div>
        <div class="keyBtn buttonNums keyboard">0</div>
    </li>
"""
context_li_footer_bar = """
    <li id="numberParcomat"></li>
    <li class="forward"><a href="#" target="_blank"><img src="images/forward.png"></li></li>
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
            },
            keyBoard = document.querySelectorAll('.keyBtn');
            keyBoard.forEach(function(button, index) {
                button.addEventListener('click', function() {
                    document.getElementById('numberOfVehicle').value += this.innerHTML.toUpperCase();
                    if (button.id == "del") {
                        document.getElementById('numberOfVehicle').value = '';
                    }
                });
            });
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
            let letters = document.querySelectorAll('.letter');
            let keyNums = document.getElementById('buttonNumbers');
            let loop = 0;
            let englB = document.getElementById('englB');
            document.getElementById("num").onclick = ()=>{
                loop++;
                letters.forEach(function(button, index){
                    if(loop % 2 !== 0){
                        document.getElementById("num").innerHTML = "АБВ";
                        button.style.display = "none";
                        keyNums.style.display = "flex";
                        englB.style.display = "none";
                    }
                    else if(loop % 2 === 0){
                        document.getElementById("num").innerHTML = "123";
                        button.style.display = "block";
                        keyNums.style.display = "none";
                        englB.style.display = "flex";
                    }
                });
            }
    }
"""
doc.asis('<!DOCTYPE html>')
with tag('html', lang="en"):
    with tag('head'):
        doc.asis('<meta http-equiv="Content-Type" content="text/html; charset=utf-8">')
        doc.asis('<link rel="stylesheet" type="text/css" href="css/styleEnterNumberOfVehicle.css">')
        doc.asis('<title>Оплата успішна</title>')
    with tag('body'):
        with tag('div class="wrapper"'):
            doc.asis('<ul class="highBar">' + context_li_time_and_langtool + '</ul>')
            doc.asis('<ul class="spaceInput">' + context_textarea + '</ul>')
            doc.asis('<ul class="operationSuccesful">' + context_li_operation_succesful + '</ul>')
            doc.asis('<ul class="footerBar">' + context_li_footer_bar + '</ul>')
            doc.asis('<script>' + script_time_and_lang + '</script>')
result = doc.getvalue()
file = codecs.open(name_file, "a", "utf-8")
with open(name_file, "w"):
    pass
file.write(result)