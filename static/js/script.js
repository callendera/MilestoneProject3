$(document).ready(function() {
            $('.sidenav').sidenav();
            // select option for recipe type
            $('select').formSelect();
            // for action button on view recipe page
            $('.fixed-action-btn').floatingActionButton();

            $('.modal').modal();
        });