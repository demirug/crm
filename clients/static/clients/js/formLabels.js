//Создание поля по параметрам path value
function addField(path, value="") {
    var el = $("<div class='form-input'><div class='input-group'>" +
        "  <input type='text' class='form-control' value='" + value + "'>" +
        "  <span class='input-group-btn'>" +
        "    <button class='btn btn-danger remove-btn' type='button'>X</button>" +
        "  </span>" +
        "</div></div>")
    //Добовление удаления поля по нажатию кнопки "Удалить"
    el.find('span>button').click(function () {
            if($(this).parents().eq(3).children().length > 1) {
                $(this).parents().eq(2).remove();
            }
    })
    $(path).append(el);
}

$(document).ready(function () {
    //Парсинг email из общего текстового поля и добавления данных как отдельных полей
    {
        data = $('#id_emails').val().split(' ');
        for (id in data) {
            if(data[id]) {
                addField('#emails>.vals', data[id]);
            }
        }

        //Если номеров нет (при пустой форме) добовление пустого поля
        if(data == "") {
             addField('#emails>.vals');
        }
    }
    //Парсинг телефонных номер из общего текстового поля и добавления данных как отдельных полей
    {
        data = $('#id_phones').val().split(' ');
        for (id in data) {
            if(data[id]) {
                addField('#phones>.vals', data[id]);
            }
        }

        //Если номеров нет (при пустой форме) добовление пустого поля
        if(data == "") {
             addField('#phones>.vals');
        }
    }

    //Добовление пустого поля
    $('.add-btn').click(function () {
        addField($(this).parent().children('.vals'))
    });


    $('#submit-btn').click(function () {
        let phones = "";
        let emails = "";

        //Сбор номеров телефона со всех полей в 1 строку
        $('#phones>.vals>.form-input>.input-group>input[type=text]').each(function () {
            if($(this).val()) {
              phones += $(this).val() + ' ';
            }
        })

        //Сбор email-ов со всех полей в 1 строку
         $('#emails>.vals>.form-input>.input-group>input[type=text]').each(function () {
            if($(this).val()) {
              emails += $(this).val() + ' ';
            }
         })

        //Установка новых значений полям
        $('#id_phones').val(phones);
        $('#id_emails').val(emails);

        //Установка полю текста из CKEditor-а
        $('#id_comp_description').val(CKEDITOR.instances.id_comp_description.getData());
        $('form').submit();

    })

})