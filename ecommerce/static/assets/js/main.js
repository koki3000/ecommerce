var slide_number = 0;
var timer1 = 0;
var timer2 = 0;
var slides_tab = ['Aeropress', 'Comandante', 'Ekspres kolbowy', 'Waga', 'Zielona']
var slide_nav = '';

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
    
function setup()
{
    for (let index = 0; index < slides_tab.length; index++) {
        slide_nav = slide_nav + "<span id=\"slide"+ index +"\" style=\"cursor: pointer;\">["+ (index + 1) +"]</span>";
    }
    $('#slide_nav').html(slide_nav);
    for (let index = 0; index < slides_tab.length; index++) {
        document.getElementById('slide'+index).addEventListener('click', function(){
            set_slide(index);
        });
    }
    slides();
}

window.onload = setup;