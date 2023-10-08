$(document).ready(function () {
    const total = $("#id_category-TOTAL_FORMS").val()

    for (let i = 0; i < total; i++) {
        const type = $("#id_category-" + i + "-type")
        const value = type.val();
        const values = $("#id_category-" + i + "-values");
        const btn_add = $("#add_id_category-"+i+"-values");

        if (value === 'char' || value === 'text' || value === 'date' || value === 'time') {
            values.prop('disabled', true);
            btn_add.prop('disabled', true);
            values.val([]).trigger('change');
        } else {
            values.prop('disabled', false);
            btn_add.prop('disabled', false);
        }
    }

    $(".field-type").change(function () {
        const type = $(this).children();
        const id = type.attr('id').match(/\d+/)[0];
        const value = type.val();
        const values = $("#id_category-" + id + "-values");
        const btn_add = $("#add_id_category-"+id+"-values");


        if (value === 'char' || value === 'text' || value === 'date' || value === 'time') {
            values.prop('disabled', true);
            btn_add.hide();
            values.val([]).trigger('change');
        } else {
            values.prop('disabled', false);
            btn_add.show();
        }
    });
});