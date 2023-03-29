
    var player = document.getElementById('player');
    //значения параметров от 0 до 100
    var blur =0;       //0-дефолтное значение
    var sepia =0;       //0-дефолтное значение
    var brightness =50;  //50-дефолтное значение
    var contrast =50;   //50-дефолтное значение
    var grayscale =0;
    var saturate = 50;
    var huerotate=0;
    var invert =0;
    var opacity =0;

    var epilepsion = false;
    var daltonizm = false;

    var home = document.getElementById('home');
    var videos = document.getElementById('videos');
    var setting = document.getElementById('setting');
    var settingPresets = document.getElementById('settingPresets');
    var settingRangs = document.getElementById('settingRangs');
    var contact = document.getElementById('contact');
    var user = document.getElementById('user');
    var watch = document.getElementById('watch');
    var reformat = document.querySelectorAll('.reformat');

    var formRanges = document.getElementById('formRangs');

    var daltonicBlock = document.querySelectorAll('.daltonicBlock');

    // Создание контейнера для блоков
    var block;
    var title;
    var image;
    var button;
    var nBlocks = 5;

    CreateVideosBlocks();
    // Создание 3 блоков
    function CreateVideosBlocks(){
        for (let i = 1; i <= nBlocks; i++) {
          // Создание блока
          block = document.createElement('div');
          block.classList.add('blockProduct');

          // Создание заголовка
          title = document.createElement('p');
          title.innerText = `Фильм №${i}`;

          // Создание изображения
          image = document.createElement('img');
          image.classList.add('reformat');
          image.style.filter = 'blur(0px)';
          image.src = `/static/image/mem${i}.png`;
          //image.width = '90';


          // Создание кнопки
          button = document.createElement('input');
          button.type = 'button';
          button.classList.add('button');
          button.value = 'Смотреть';
          button.onclick = function() {
            DivVisible(document.getElementById('watch'), i);
          };

          // Добавление элементов в блок
          block.appendChild(title);
          block.appendChild(image);
          block.appendChild(button);
          // Добавление блока в контейнер
          videos.appendChild(block);
        }
        reformat = document.querySelectorAll('.reformat');
    }


    function Reformate()
    {
        for (let i = 0; i < reformat.length; i++)
        {
        reformat[i].style.filter = 'blur('+blur/10+'px)' +
                             'brightness('+brightness*2+'%)' +
                             'sepia('+ sepia/100 +')' +
                             'contrast('+ contrast/50 +')'+
                             'grayscale('+grayscale+'%)'+
                             'saturate('+saturate*2+'%)'+
                             'hue-rotate('+huerotate*3.6+'deg)'+
                             'invert('+invert+'%)'+
                             'opacity('+opacity+'%)';
        }
    }

    function valueElFilter(img,el)
    {
        str = img.style.filter;
        str1 = el;
        beg = str.indexOf(str1)+str1.length +1;

        if (str.indexOf(str1)>= 0)
        {
            end = beg + str.substring(beg).indexOf(')') -1;
            //document.write(str.substring(beg,end)," ",el,"      ");
            return (Number(str.substring(beg,end)));
        }
        else
        {
           //document.write(beg, "-beg; ",end, "-end; ",str.substring(beg,end), "-rez; ",str.indexOf(str1),"-flag; ",el,"-el; ",str,"-str; ");

           return ;
        }
    }

    function DoPreset(img)
    {
        if (valueElFilter(img,"contrast")!=undefined)
        contrast = valueElFilter(img,"contrast");
        else contrast =50;

        if (valueElFilter(img,"blur")!=undefined)
        blur = valueElFilter(img,"blur");
        else blur =0;

        if (valueElFilter(img,"sepia")!=undefined)
        sepia = valueElFilter(img,"sepia");
        else sepia =0;

        if (valueElFilter(img,"brightness")!=undefined)
        brightness = valueElFilter(img,"brightness");
        else brightness =50;

        if (valueElFilter(img,"grayscale")!=undefined)
        grayscale = valueElFilter(img,"grayscale");
        else grayscale =0;

        if (valueElFilter(img,"saturate")!=undefined)
        saturate = valueElFilter(img,"saturate");
        else saturate =50;

        if (valueElFilter(img,"huerotate")!=undefined)
        huerotate = valueElFilter(img,"huerotate");
        else huerotate =0;

        if (valueElFilter(img,"invert")!=undefined)
        invert = valueElFilter(img,"invert");
        else invert =0;

        if (valueElFilter(img,"opacity")!=undefined)
        opacity = valueElFilter(img,"opacity");
        else opacity =100;
        Reformate();
        for (let i = 0; i < reformat.length; i++)
        {
            reformat[i].style.filter = img.style.filter;
        }
        formRanges.contrast.value = contrast;
        formRanges.brightness.value = brightness;
        formRanges.sepia.value = sepia;
        formRanges.blur.value = blur;
        formRanges.saturate.value = saturate;
        formRanges.grayscale.value = grayscale;
        formRanges.huerotate.value = huerotate;
        formRanges.invert.value = invert;
        formRanges.opacity.value = opacity;
    }


     function DivVisible(ell, i = 0)
    {
        setting.style.display='none';
        videos.style.display= 'none';
        contact.style.display= 'none';
        user.style.display= 'none';
        watch.style.display= 'none';
        settingPresets.style.display= 'none';
        settingRangs.style.display= 'none';
        home.style.display= 'none';

        ell.style.display='block';
        switch(i)
        {
            case 1:  // if (x === 'value1')...
                player.poster ="static/image/mem1.png";
                if (epilepsion==false)
                {
                    player.src ="https://drive.google.com/uc?export=preview&id=1W0a-dOu5d_kt85S2iAUHDGzYPpnL10S7";
                }
                else
                {
                    player.src ="https://drive.google.com/uc?export=preview&id=1hZ7OD-eI-OrHNC9q6q6IhjBmFyS7IC-S";
                }
            break;
            case 2:  // if (x === 'value2') ...
                player.poster ="static/image/mem2.png";
                if (epilepsion==false)
                {
                    player.src ="https://drive.google.com/uc?export=preview&id=18f2piaXv0fwnif8XYoPN2T9uxm_KYdXu";
                }
                else
                {
                    player.src ="https://drive.google.com/uc?export=preview&id=1rGdu5eBYkR-qzefTme0KJ9l6SUQoyg1c";
                    //player.src ="https://drive.google.com/file/d/1rGdu5eBYkR-qzefTme0KJ9l6SUQoyg1c";
                    //player.src ="https://drive.google.com/uc?export=preview&id=18f2piaXv0fwnif8XYoPN2T9uxm_KYdXu";
                }

            break;
            case 3:  // if (x === 'value2') ...
                player.poster ="https://drive.google.com/uc?export=preview&id=1j52HifhieqAHYR7bZuRZKdbEjXsNY-3Z";
                if (epilepsion==false)
                {
                    player.src ="https://drive.google.com/uc?export=preview&id=1j52HifhieqAHYR7bZuRZKdbEjXsNY-3Z";
                }
                else
                {
                    player.src ="https://drive.google.com/uc?export=preview&id=19R5IYHJRBUPTJY5pvC7KqJeXcHniou51";
                    //player.src ="https://drive.google.com/uc?export=preview&id=1j52HifhieqAHYR7bZuRZKdbEjXsNY-3Z";
                }
            break;
            case 4:  // if (x === 'value2') ...
                player.poster ="https://drive.google.com/uc?export=preview&id=16bJTq_bcRJgObSYq93XudUtLR-Mf_zSh";
                if (epilepsion==false)
                {
                    player.src ="https://drive.google.com/uc?export=preview&id=16bJTq_bcRJgObSYq93XudUtLR-Mf_zSh";
                }
                else
                {
                    player.src ="https://drive.google.com/uc?export=preview&id=1icp7Vnso3OMGxfeE_dwSBXlsbNb1QfN4";
                }
            break;
            case 5:  // if (x === 'value2') ...
                player.poster ="https://drive.google.com/uc?export=preview&id=1EsebTzq4KV45mpjS4QnG76amTY_3kx0O";
                if (epilepsion==false)
                {
                    player.src ="https://drive.google.com/uc?export=preview&id=1EsebTzq4KV45mpjS4QnG76amTY_3kx0O";
                }
                else
                {
                    player.src ="https://drive.google.com/uc?export=preview&id=1IxNwaEmT8wX30fWNO-_BgFf7rPMlP1_D";
                }
            break;
            default:
                player.src = "";
                player.poster = "";
            break;
        }
    }




    /*!!!!!!!!!!ФОРМЫ JS!!!!!!!!!!!!*/
    function FormRangsProcessing (form)          //обработка формы
    {
        contrast = form.contrast.value;
        blur = form.blur.value;
        sepia = form.sepia.value;
        brightness = form.brightness.value;
        grayscale = form.grayscale.value;
        saturate = form.saturate.value;
        huerotate = form.huerotate.value;
        invert = form.invert.value;
        opacity = form.opacity.value;
        Reformate();
    }

    function FormProcessing (form)          //обработка формы
    {
        if (form.daltonizm.value == "Да")
        {
            daltonizm=true;
            for (let i = 0; i < daltonicBlock.length; i++)
            {
                daltonicBlock[i].style.display = 'block';
            }
        }
        else
        {
            daltonizm=false;
            for (let i = 0; i < daltonicBlock.length; i++)
            {
                daltonicBlock[i].style.display = 'none';
            }
        }
        if (form.epilepsion.value == "Да")
        {
            epilepsion=true;
        }
        else
        {
            epilepsion=false;
        }
    }


