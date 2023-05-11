var slide_number = 0;
var timer1 = 0;
var timer2 = 0;
var slides_tab = ['Aeropress', 'Comandante', 'Ekspres kolbowy', 'Waga', 'Zielona']

const hide = () =>
{
    $("#slider").fadeOut(500);
}

const slides = () =>
{
    var file = "<a href=\"/slider/"+ slides_tab[slide_number] +"/\"><img src=\"/static/assets/img/"+ slides_tab[slide_number] +".jpg\"></a>";
    slide_number++;
    if (slide_number>4) slide_number=0;
    document.getElementById("slider").innerHTML = file;
    $("#slider").fadeIn(500);
    timer1 = setTimeout("slides()", 5000);
    timer2 = setTimeout("hide()", 4500);
}

const set_slide = (nr) => 
{
    clearTimeout(timer1);
    clearTimeout(timer2);
    slide_number = nr;
    hide();
    setTimeout("slides()", 500);
}

window.onload = slides;