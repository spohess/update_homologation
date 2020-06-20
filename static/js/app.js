function activateCurrentMenu() {
    let activatedPath = window.location.pathname;
    let targetAnchor = $('[href="' + activatedPath + '"]');
    let collapseAncestors = targetAnchor.parents('.collapse');
    targetAnchor.addClass('active');
    targetAnchor.parent('.nav-item').addClass('active');
    collapseAncestors.each(function () {
        $(this).addClass('show');
        $(this).parent('.nav-item').addClass('active');
        $('[data-target="#' + this.id + '"]').removeClass('collapsed');
    })
}

function startDatetimepicker() {
    $('.input-calendar').datetimepicker({
        locale: moment.locale('pt-br'),
        format: 'L'
    });

    $('.input-clock').datetimepicker({
        locale: moment.locale('pt-br'),
        format: 'LTS'
    });

    $('.input-calendarclock').datetimepicker({
        locale: moment.locale('pt-br'),
    });
}

$(document).ready(function () {

    startDatetimepicker()
    activateCurrentMenu()
})