$(document).ready(function() {
    // Make images fill width of block
    $('.page-wrapper img').addClass('img-fluid');

    document.querySelector('#language-selection-dropdown').addEventListener('change', function (e) {

        Cookies.set("lang", e.target.value)

        let p = window.location.pathname.split('/')
        p[1] = e.target.value
        window.location.pathname = p.join('/')

    });

    let language_dropdown = $('#language-selection-dropdown')

    const langs = {
        "en": "English",
        "ru": "Русский",
        "uz": "O'zbekcha"
    };

    const langCode = window.location.pathname.split('/')[1];
    language_dropdown.selectpicker(langCode, langs[langCode]);
    language_dropdown.selectpicker('render');

    // cookie
    if (!Cookies.get('lang')) {
        Cookies.set('lang', 'uz');
        window.location = window.location.origin + '/uz'
    }

    $('.side-menu__block-close').on('click', function () {
       $('.side-menu__block').removeClass('active');
    });


    const accordion = document.querySelectorAll('.person-detail__acc'),
    accordionHeader = document.querySelectorAll('.person-detail__header');

    accordionHeader.forEach(function(item) {
        item.addEventListener('click', function (e) {
            e.preventDefault();
            const target = e.target;
            accordion.forEach(function (subitem, n, e) {
                if(target && target.classList.contains('collapsed')) {
                    if(subitem == n) {
                        n.classList.remove('collapsed');
                    }
                }
            })
        })
    })

    $('.side-menu__block-inner .navigation-box').find('ul.submenu').siblings('a').each(function(i, a) {
        a.addEventListener('click', function(ev) {
            ev.preventDefault()
            $(a).siblings('ul.submenu').toggleClass('act')
            $(a).find('.fa-chevron-down').toggleClass('icon_active')
        })
    })

    if ($('ul.right-menu .collapse-menu-item').length) {
        $('.collapse-menu-item').on('click', function (e) {
            $(this).toggleClass('rotate');
            $(e.target).siblings('ul.submenu').toggleClass('open')
        })
    }

    /*
    if ($('.main-navigation .navigation-box').length) {
        var subMenu = $('.main-navigation .submenu');
        subMenu.parent('li').children('a').append(function() {
            return '<button class="sub-nav-toggler"> <span class="sr-only">Toggle navigation</span> <span class="icon-bar"></span> <span class="icon-bar"></span> <span class="icon-bar"></span> </button>';
        });
        var mainNavToggler = $('.header-navigation .menu-toggler');
        var subNavToggler = $('.main-navigation .sub-nav-toggler');
        mainNavToggler.on('click', function() {
            var Self = $(this);
            var menu = Self.closest('.header-navigation').find(Self.data('target'));
            $(menu).slideToggle();
            $(menu).toggleClass('showen');
            return false;
        });
        subNavToggler.on('click', function() {
            var Self = $(this);
            Self.parent().parent().children('.submenu').slideToggle();
            return false;
        });
    }
    */

});




/*
$(document).ready(function() {
    $('select').selectpicker();

    $('#language-selection-dropdown').on('change', function (e) {
        let newLang = '', oldLang = ('/' + window.location.pathname.split('/')[1] + '/');

        if (/(en|ru|uz)/.test(e.target.value)){
            newLang = '/' + e.target.value + '/';
        } else {
            newLang = '/en/';
        }

        window.location = window.location.href.replace(oldLang, newLang, 1);

    })

    loadGalleryImages(
        $('.fluid-this')
            .find('img')
    );

    setTimeout(function () {
        $('.fluid-this')
            .find('img')
            .addClass('img-fluid');
    }, 250);

});

function loadGalleryImages(container) {

    container
        .each(function (index, el) {
            const imgPath = el.attributes['src'].value,
                altText = el.attributes['alt'] && el.attributes['alt'].value ? el.attributes['alt'].value : null,
                imgWidth = el.attributes['width'] && el.attributes['width'].value ? el.attributes['width'].value : null,
                imgHeight = el.attributes['height'] && el.attributes['height'].value ? el.attributes['height'].value : null;

            const append = '' +
                '<a href="' + imgPath + '" data-fancybox="page-gallery" data-caption="' + (altText ? altText : "") + '" ' + (imgWidth ? 'width="' + imgWidth : "") + '"' + (imgHeight ? 'height="' + imgHeight : "") + '"' + '>' +
                    '<img src="' + imgPath + '" alt="' + (altText ? altText : "") + '" class="img-fluid" />' +
                '</a>';

            $(el).replaceWith(append);

        })

    $('[data-fancybox="page-gallery"]').fancybox();

}

function loadImageAsGallery(imageElement) {

    const imgPath = imageElement.attributes['src'].value,
        altText = imageElement.attributes['alt'] && imageElement.attributes['alt'].value ? imageElement.attributes['alt'].value : null,
        imgWidth = imageElement.attributes['width'] && imageElement.attributes['width'].value ? imageElement.attributes['width'].value : null,
        imgHeight = imageElement.attributes['height'] && imageElement.attributes['height'].value ? imageElement.attributes['height'].value : null,
        selector = imageElement.attributes['data-fancybox'].value;

    const append = '' +
        '<a href="' + imgPath + '" data-fancybox="' + selector + '" data-caption="' + (altText ? altText : "") + '" ' + (imgWidth ? 'width="' + imgWidth : "") + '"' + (imgHeight ? 'height="' + imgHeight : "") + '"' + '>' +
            '<img src="' + imgPath + '" alt="' + (altText ? altText : "") + '" class="img-fluid" />' +
        '</a>';

    $(imageElement).replaceWith(append).fancybox();

}
*/


let a = {
    "id": 0,
    "case_number": "64646-00003",
    "subject": "subject",
    "description": "description here",
    "type": {"id": 0, "name": "One of Problem/Demo Request/Feature Request/Question/Request etc"},
    "contact": {"id": 0, "name": "contact name"},
    "lead": {"id": 0, "name": "lead name"},
    "company": {"id": 0, "name": "company name"},
    "other": {
        "first_name": "John",
        "last_name": "Smith",
        "email": "john.smith@email.com",
        "phone": "phonenumber",
        "fax": "faxnumber",
        "company_name": "John Co"
    },
    "origin": {"id": 0, "name": "name", "code": "code"},
    "reason": {"id": 0, "name": "name", "code": "code"},
    "other_reason": "string",
    "priority": {"id": 0, "name": "name", "code": "code"},
    "status": {"id": 0, "name": "name", "code": "code"},
    "opportunity": {"id": 0, "name": "opportunity name"},
    "assignee": {"id": 0, "name": "assignee name"},
    "department": {"id": 0, "name": "department name"},
    "resolver": {"id": 0, "name": "resolver name"},
    "internal_status": {"id": 0, "name": "status"},
    "created_date": 1585228189327,
    "closed_date": 1585228189327,
    "internal_updated_date": 1585228189327,
    "notes": "notes here ..."
}

