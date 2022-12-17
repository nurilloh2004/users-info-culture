(function ($) {
    "use strict";

    if ($('.searchByMonth-datepicker').length) {
        $('.searchByMonth-datepicker').datepicker({
            format: "MM - yyyy",
            minViewMode: 1
        });
    }

    if ($('.searchByDate-datepicker').length) {
        $('.searchByDate-datepicker').datepicker({
            format: "d - M - yyyy",
            startDate: "-3d",
            todayBtn: "linked",
            todayHighlight: true
        });
    }

    if ($('.plan-visit__tab-links').length) {
        var planVisitLink = $('.plan-visit__tab-links').find('.nav-link');
        planVisitLink.on('click', function (e) {
            var target = $(this).attr('data-target');
            // animate
            $('html, body').animate({
                scrollTop: $(target).offset().top - 50
            }, 1000);


            planVisitLink.removeClass('active');
            $(this).addClass('active');

            return false;
        })
    }
    if ($('.range-slider-price').length) {

        var priceRange = document.getElementById('range-slider-price');

        noUiSlider.create(priceRange, {
            start: [30, 150],
            limit: 200,
            behaviour: 'drag',
            connect: true,
            range: {
                'min': 10,
                'max': 200
            }
        });

        var limitFieldMin = document.getElementById('min-value-rangeslider');
        var limitFieldMax = document.getElementById('max-value-rangeslider');

        priceRange.noUiSlider.on('update', function (values, handle) {
            (handle ? $(limitFieldMax) : $(limitFieldMin)).text(values[handle]);
        });
    }
    ;

    if ($('.quantity-spinner').length) {
        $("input.quantity-spinner").TouchSpin({});
    }
    if ($('.contact-form-vaidated').length) {
        $('.contact-form-vaidated').validate({ // initialize the plugin
            rules: {
                name: {
                    required: true
                },
                fname: {
                    required: true
                },
                lname: {
                    required: true
                },
                email: {
                    required: true,
                    email: true
                },
                message: {
                    required: true
                },
                subject: {
                    required: true
                },
                booking_date: {
                    required: true
                }
            },
            submitHandler: function (form) {
                // sending value with ajax request
                $.post($(form).attr('action'), $(form).serialize(), function (response) {
                    $(form).parent().find('.result').append(response);
                    $(form).find('input[type="text"]').val('');
                    $(form).find('input[type="email"]').val('');
                    $(form).find('textarea').val('');
                });
                return false;
            }
        });
    }
    if ($('.datepicker').length) {
        $('.datepicker').datepicker();
    }
    if ($('.counter').length) {
        $('.counter').counterUp({
            delay: 10,
            time: 3000
        });
    }
    if ($('.img-popup').length) {
        var groups = {};
        $('.img-popup').each(function () {
            var id = parseInt($(this).attr('data-group'), 10);

            if (!groups[id]) {
                groups[id] = [];
            }

            groups[id].push(this);
        });


        $.each(groups, function () {

            $(this).magnificPopup({
                type: 'image',
                closeOnContentClick: true,
                closeBtnInside: false,
                gallery: {enabled: true}
            });

        });

    }
    ;
    if ($('.wow').length) {
        var wow = new WOW({
            boxClass: 'wow', // animated element css class (default is wow)
            animateClass: 'animated', // animation css class (default is animated)

            mobile: true, // trigger animations on mobile devices (default is true)
            live: true // act on asynchronously loaded content (default is true)
        });
        wow.init();
    }
    if ($('.main-navigation .navigation-box').length) {
        var subMenu = $('.main-navigation .submenu');
        subMenu.parent('li').children('a').append(function () {
            return '<button class="sub-nav-toggler"> <span class="sr-only">Toggle navigation</span> <span class="icon-bar"></span> <span class="icon-bar"></span> <span class="icon-bar"></span> </button>';
        });
        var mainNavToggler = $('.header-navigation .menu-toggler');
        var subNavToggler = $('.main-navigation .sub-nav-toggler');
        mainNavToggler.on('click', function () {
            var Self = $(this);
            var menu = Self.closest('.header-navigation').find(Self.data('target'));
            $(menu).slideToggle();
            $(menu).toggleClass('showen');
            return false;
        });
        subNavToggler.on('click', function () {
            var Self = $(this);
            Self.parent().parent().children('.submenu').slideToggle();
            return false;
        });
    }

    if ($('.video-popup').length) {
        $('.video-popup').magnificPopup({
            disableOn: 700,
            type: 'iframe',
            mainClass: 'mfp-fade',
            removalDelay: 160,
            preloader: true,

            fixedContentPos: false
        });
    }
    if ($('[data-toggle="tooltip"]').length) {
        $('[data-toggle="tooltip"]').tooltip();
    }
    if ($('.stricky').length) {
        $('.stricky').addClass('original').clone(true).insertAfter('.stricky').addClass('stricked-menu').removeClass('original');
    }
    if ($('.scroll-to-target').length) {
        $(".scroll-to-target").on('click', function () {
            var target = $(this).attr('data-target');
            // animate
            $('html, body').animate({
                scrollTop: $(target).offset().top
            }, 1000);

            return false;

        });
    }


    if ($('.side-menu__toggler').length) {
        $('.side-menu__toggler').on('click', function (e) {
            $('.side-menu__block').addClass('active');
            e.preventDefault();
        });
    }

    if ($('.side-menu__block-overlay').length) {
        $('.side-menu__block-overlay').on('click', function (e) {
            $('.side-menu__block').removeClass('active');
            e.preventDefault();
        });
    }


    if ($('.search-popup__toggler').length) {
        $('.search-popup__toggler').on('click', function (e) {
            $('.search-popup').addClass('active');
            e.preventDefault();
        });
    }

    if ($('.search-popup__overlay').length) {
        $('.search-popup__overlay').on('click', function (e) {
            $('.search-popup').removeClass('active');
            e.preventDefault();
        });
    }
    $(window).on('scroll', function () {
        if ($('.scroll-to-top').length) {
            var strickyScrollPos = 100;
            if ($(window).scrollTop() > strickyScrollPos) {
                $('.scroll-to-top').fadeIn(500);
            } else if ($(this).scrollTop() <= strickyScrollPos) {
                $('.scroll-to-top').fadeOut(500);
            }
        }
        if ($('.stricked-menu').length) {
            var headerScrollPos = 100;
            var stricky = $('.stricked-menu');
            if ($(window).scrollTop() > headerScrollPos) {
                stricky.addClass('stricky-fixed');
            } else if ($(this).scrollTop() <= headerScrollPos) {
                stricky.removeClass('stricky-fixed');
            }
        }
    });
    if ($('.accrodion-grp').length) {
        var accrodionGrp = $('.accrodion-grp');
        accrodionGrp.each(function () {
            var accrodionName = $(this).data('grp-name');
            var Self = $(this);
            var accordion = Self.find('.accrodion');
            Self.addClass(accrodionName);
            Self.find('.accrodion .accrodion-content').hide();
            Self.find('.accrodion.active').find('.accrodion-content').show();
            accordion.each(function () {
                $(this).find('.accrodion-title').on('click', function () {
                    if ($(this).parent().hasClass('active') === false) {
                        $('.accrodion-grp.' + accrodionName).find('.accrodion').removeClass('active');
                        $('.accrodion-grp.' + accrodionName).find('.accrodion').find('.accrodion-content').slideUp();
                        $(this).parent().toggleClass('active');
                        $(this).parent().find('.accrodion-content').slideDown();
                    }
                    ;
                });
            });
        });

    }
    ;

    $(document).on('ready', function () {
        if ($('.preloader').length) {
            $('.preloader').fadeOut('slow');
        }
    });

    $(window).on('load', function () {
        if ($('.collection-five__carousel').length) {
            $('.collection-five__carousel').owlCarousel({
                loop: true,
                margin: 0,
                nav: true,
                navText: [
                    '<i class="fa fa-angle-left"></i>',
                    '<i class="fa fa-angle-right"></i>'
                ],
                dots: false,
                autoWidth: false,
                autoplay: true,
                smartSpeed: 700,
                autoplayTimeout: 5000,
                autoplayHoverPause: true,
                responsive: {
                    0: {
                        items: 1,
                        slideBy: 1
                    },
                    480: {
                        items: 1,
                        slideBy: 1
                    },
                    600: {
                        items: 2,
                        slideBy: 2
                    },
                    991: {
                        items: 2,
                        slideBy: 2
                    },
                    1000: {
                        items: 2,
                        slideBy: 2
                    },
                    1200: {
                        items: 2,
                        slideBy: 2
                    }
                }
            });
        }
        if ($('.plan-visit__price-carousel').length) {
            $('.plan-visit__price-carousel').owlCarousel({
                loop: true,
                margin: 0,
                nav: false,
                navText: [
                    '<i class="fa fa-angle-left"></i>',
                    '<i class="fa fa-angle-right"></i>'
                ],
                dots: true,
                autoWidth: false,
                autoplay: true,
                smartSpeed: 700,
                autoplayTimeout: 5000,
                items: 1,
                autoplayHoverPause: true,
            });
        }
        if ($('.sidebar__post-carousel').length) {
            $('.sidebar__post-carousel').owlCarousel({
                loop: true,
                margin: 0,
                nav: false,
                navText: [
                    '<i class="fa fa-angle-left"></i>',
                    '<i class="fa fa-angle-right"></i>'
                ],
                dots: true,
                autoWidth: false,
                autoplay: true,
                smartSpeed: 700,
                autoplayTimeout: 5000,
                items: 1,
                autoplayHoverPause: true,
            });
        }
        if ($('.related-product__carousel').length) {
            $('.related-product__carousel').owlCarousel({
                loop: true,
                margin: 30,
                nav: true,
                navText: [
                    '<i class="fa fa-angle-left"></i>',
                    '<i class="fa fa-angle-right"></i>'
                ],
                dots: false,
                autoWidth: false,
                autoplay: true,
                smartSpeed: 700,
                autoplayTimeout: 5000,
                autoplayHoverPause: true,
                responsive: {
                    0: {
                        items: 1
                    },
                    480: {
                        items: 1
                    },
                    600: {
                        items: 2
                    },
                    991: {
                        items: 3
                    },
                    1000: {
                        items: 4
                    },
                    1200: {
                        items: 4
                    }
                }
            });
        }
        if ($('.venue-one__carousel').length) {
            $('.venue-one__carousel').owlCarousel({
                loop: true,
                margin: 30,
                nav: true,
                navText: [
                    '<i class="fa fa-angle-left"></i>',
                    '<i class="fa fa-angle-right"></i>'
                ],
                dots: false,
                autoWidth: false,
                autoplay: true,
                smartSpeed: 700,
                autoplayTimeout: 5000,
                autoplayHoverPause: true,
                responsive: {
                    0: {
                        items: 1
                    },
                    480: {
                        items: 1
                    },
                    600: {
                        items: 2
                    },
                    991: {
                        items: 2
                    },
                    1000: {
                        items: 3
                    },
                    1200: {
                        items: 3
                    }
                }
            });
        }
        if ($('.venue-two__carousel').length) {
            var venueTwoCarousel = $('.venue-two__carousel').owlCarousel({
                loop: true,
                margin: 0,
                nav: false,
                navText: [
                    '<i class="fa fa-angle-left"></i>',
                    '<i class="fa fa-angle-right"></i>'
                ],
                dots: false,
                autoWidth: false,
                autoplay: true,
                smartSpeed: 700,
                autoplayTimeout: 5000,
                autoplayHoverPause: true,
                responsive: {
                    0: {
                        items: 1
                    },
                    480: {
                        items: 1
                    },
                    600: {
                        items: 2
                    },
                    991: {
                        items: 2
                    },
                    1000: {
                        items: 3
                    },
                    1200: {
                        items: 3
                    }
                }
            });
            $('.venue-two__carousel-nav-left').on('click', function () {
                venueTwoCarousel.trigger('next.owl.carousel');
                return false;
            });
            $('.venue-two__carousel-nav-right').on('click', function () {
                venueTwoCarousel.trigger('prev.owl.carousel');
                return false;
            });
        }
        if ($('.brand-two__carousel').length) {
            $('.brand-two__carousel').owlCarousel({
                loop: true,
                margin: 120,
                nav: false,
                navText: [
                    '<i class="fa fa-long-arrow-left"></i>',
                    '<i class="fa fa-long-arrow-right"></i>'
                ],
                dots: false,
                autoWidth: false,
                autoplay: true,
                smartSpeed: 700,
                autoplayTimeout: 5000,
                autoplayHoverPause: true,
                responsive: {
                    0: {
                        items: 2,
                        margin: 30
                    },
                    480: {
                        items: 3,
                        margin: 40
                    },
                    600: {
                        items: 3,
                        margin: 50
                    },
                    991: {
                        items: 4
                    },
                    1000: {
                        items: 5
                    },
                    1200: {
                        items: 5
                    }
                }
            });
        }
        if ($('.blog-one__carousel').length) {
            $('.blog-one__carousel').owlCarousel({
                loop: true,
                margin: 30,
                nav: false,
                navText: [
                    '<i class="fa fa-long-arrow-left"></i>',
                    '<i class="fa fa-long-arrow-right"></i>'
                ],
                dots: true,
                autoWidth: false,
                autoplay: true,
                smartSpeed: 700,
                autoplayTimeout: 5000,
                autoplayHoverPause: true,
                responsive: {
                    0: {
                        items: 1
                    },
                    480: {
                        items: 1
                    },
                    600: {
                        items: 1
                    },
                    991: {
                        items: 2
                    },
                    1000: {
                        items: 2
                    },
                    1200: {
                        items: 2
                    }
                }
            });
        }
        if ($('.service-two__carousel').length) {
            $('.service-two__carousel').owlCarousel({
                loop: true,
                margin: 30,
                nav: false,
                navText: [
                    '<i class="fa fa-long-arrow-left"></i>',
                    '<i class="fa fa-long-arrow-right"></i>'
                ],
                dots: true,
                autoWidth: false,
                autoplay: true,
                smartSpeed: 700,
                autoplayTimeout: 5000,
                autoplayHoverPause: true,
                responsive: {
                    0: {
                        items: 1
                    },
                    480: {
                        items: 1
                    },
                    767: {
                        items: 1
                    },
                    991: {
                        items: 2
                    },
                    1000: {
                        items: 3
                    },
                    1200: {
                        items: 3
                    }
                }
            });
        }
        if ($('.testimonials-one__carousel').length) {
            if ($('.testimonials-one__carousel').data('carousel-margin') !== undefined) {
                var testicarouselMargin = $('.testimonials-one__carousel').data('carousel-margin');
            } else {
                var testicarouselMargin = 80;
            }
            var testiOneCarousel = $('.testimonials-one__carousel').owlCarousel({
                loop: true,
                margin: testicarouselMargin,
                nav: false,
                dots: true,
                autoWidth: false,
                autoplay: true,
                smartSpeed: 700,
                autoplayTimeout: 5000,
                autoplayHoverPause: true,
                responsive: {
                    0: {
                        items: 1
                    },
                    480: {
                        items: 1
                    },
                    600: {
                        items: 1
                    },
                    991: {
                        items: 1
                    },
                    1000: {
                        items: 1
                    },
                    1200: {
                        items: 1
                    }
                }
            });

            $('.testimonials-one__navbtn-left').on('click', function () {
                testiOneCarousel.trigger('next.owl.carousel');
                return false;
            });
            $('.testimonials-one__navbtn-right').on('click', function () {
                testiOneCarousel.trigger('prev.owl.carousel');
                return false;
            });

        }

        if ($('.side-menu__block-inner').length) {
            $('.side-menu__block-inner').mCustomScrollbar({
                axis: 'y',
                theme: 'dark'
            });
        }

        if ($('.custom-cursor__overlay').length) {

            // / cursor /
            var cursor = $(".custom-cursor__overlay .cursor"),
                follower = $(".custom-cursor__overlay .cursor-follower");

            var posX = 0,
                posY = 0;

            var mouseX = 0,
                mouseY = 0;

            TweenMax.to({}, 0.016, {
                repeat: -1,
                onRepeat: function () {
                    posX += (mouseX - posX) / 9;
                    posY += (mouseY - posY) / 9;

                    TweenMax.set(follower, {
                        css: {
                            left: posX - 22,
                            top: posY - 22
                        }
                    });

                    TweenMax.set(cursor, {
                        css: {
                            left: mouseX,
                            top: mouseY
                        }
                    });

                }
            });

            $(document).on("mousemove", function (e) {
                var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
                mouseX = e.pageX;
                mouseY = e.pageY - scrollTop;
            });
            $("button, a").on("mouseenter", function () {
                cursor.addClass("active");
                follower.addClass("active");
            });
            $("button, a").on("mouseleave", function () {
                cursor.removeClass("active");
                follower.removeClass("active");
            });
            $(".custom-cursor__overlay").on("mouseenter", function () {
                cursor.addClass("close-cursor");
                follower.addClass("close-cursor");
            });
            $(".custom-cursor__overlay").on("mouseleave", function () {
                cursor.removeClass("close-cursor");
                follower.removeClass("close-cursor");
            });
        }

        if ($('.slider-one__carousel').length) {
            var slideOneCarousel = $('.slider-one__carousel').owlCarousel({
                loop: true,
                items: 1,
                margin: 0,
                dots: true,
                nav: false,
                animateOut: 'slideOutDown',
                animateIn: 'fadeIn',
                active: true,
                smartSpeed: 1000,
                autoplay: 7000
            });
            $('.slide-one__left-btn').on('click', function (e) {
                slideOneCarousel.trigger('next.owl.carousel');
                e.preventDefault();
            });
            $('.slide-one__right-btn').on('click', function (e) {
                slideOneCarousel.trigger('prev.owl.carousel');
                e.preventDefault();
            });
        }

        if ($('.slider-two__carousel').length) {
            var slideTwoWrap = $('.slider-two');
            var slideTwoCarousel = $('.slider-two__carousel').owlCarousel({
                loop: true,
                items: 1,
                margin: 0,
                dots: false,
                nav: false,
                animateOut: 'slideOutDown',
                animateIn: 'fadeIn',
                active: true,
                smartSpeed: 1000,
                autoplay: 7000
            });
            slideTwoWrap.find('.slide-two__left-btn').on('click', function (e) {
                slideTwoCarousel.trigger('next.owl.carousel');
                e.preventDefault();
            });
            slideTwoWrap.find('.slide-two__right-btn').on('click', function (e) {
                slideTwoCarousel.trigger('prev.owl.carousel');
                e.preventDefault();
            });
        }
        if ($('.masonary-layout').length) {
            $('.masonary-layout').isotope({
                layoutMode: 'masonry',
                itemSelector: '.masonary-item',

            });
        }
        if ($('.masonary-layout-no-grid-width').length) {
            $('.masonary-layout-no-grid-width').isotope({
                layoutMode: 'masonry',
                itemSelector: '.masonary-item'
            });
        }

        if ($('.post-filter').length) {
            var postFilterList = $('.post-filter li');
            // for first init
            $('.filter-layout').isotope({
                filter: '.filter-item',
                animationOptions: {
                    duration: 500,
                    easing: 'linear',
                    queue: false
                }
            });
            // on click filter links
            postFilterList.children('a').on('click', function () {
                var Self = $(this);
                var selector = Self.parent().attr('data-filter');
                postFilterList.children('a').parent().removeClass('active');
                Self.parent().addClass('active');


                $('.filter-layout').isotope({
                    filter: selector,
                    animationOptions: {
                        duration: 500,
                        easing: 'linear',
                        queue: false
                    }
                });
                return false;
            });
        }

        if ($('.post-filter.has-dynamic-filter-counter').length) {
            // var allItem = $('.single-filter-item').length;

            var activeFilterItem = $('.post-filter.has-dynamic-filter-counter').find('li');

            activeFilterItem.each(function () {
                var filterElement = $(this).data('filter');
                var count = $('.gallery-content').find(filterElement).length;
                $(this).children('span').append('<span class="count"><b>' + count + '</b></span>');
            });
        }

        if ($('.team-three__carousel').length) {

            var teamThreeCarousel = $('.team-three__carousel').owlCarousel({
                loop: true,
                margin: 30,
                nav: false,
                navText: [
                    '<i class="fa fa-long-arrow-left"></i>',
                    '<i class="fa fa-long-arrow-right"></i>'
                ],
                dots: false,
                autoWidth: false,
                autoplay: true,
                smartSpeed: 700,
                autoplayTimeout: 5000,
                autoplayHoverPause: true,
                responsive: {
                    0: {
                        items: 1
                    },
                    480: {
                        items: 1
                    },
                    600: {
                        items: 2
                    },
                    991: {
                        items: 2
                    },
                    1200: {
                        items: 2
                    },
                    1440: {
                        items: 3
                    }
                }
            });
            $('.team-three__btn-left').on('click', function () {
                teamThreeCarousel.trigger('next.owl.carousel');
                return false;
            });
            $('.team-three__btn-right').on('click', function () {
                teamThreeCarousel.trigger('prev.owl.carousel');
                return false;
            });
        }

        if ($('.related-product__carousel').length) {
            $('.related-product__carousel').owlCarousel({
                loop: true,
                margin: 30,
                nav: false,
                navText: [
                    '<i class="fa fa-long-arrow-left"></i>',
                    '<i class="fa fa-long-arrow-right"></i>'
                ],
                dots: false,
                autoWidth: false,
                autoplay: true,
                smartSpeed: 700,
                autoplayTimeout: 5000,
                autoplayHoverPause: true,
                responsive: {
                    0: {
                        items: 1
                    },
                    480: {
                        items: 1
                    },
                    767: {
                        items: 2
                    },
                    991: {
                        items: 2
                    },
                    1000: {
                        items: 3
                    },
                    1200: {
                        items: 3
                    }
                }
            });
        }

        if ($('.project-two__carousel').length) {
            $('.project-two__carousel').owlCarousel({
                loop: true,
                margin: 0,
                nav: false,
                dots: true,
                autoWidth: false,
                autoplay: true,
                smartSpeed: 700,
                autoplayTimeout: 5000,
                autoplayHoverPause: true,
                responsive: {
                    0: {
                        items: 1
                    },
                    480: {
                        items: 1
                    },
                    600: {
                        items: 2
                    },
                    991: {
                        items: 3
                    },
                    1000: {
                        items: 4
                    },
                    1200: {
                        items: 4
                    }
                }
            });
        }

        if ($('.project-one__carousel').length) {
            if ($('.project-one__carousel').data('carousel-margin') !== undefined) {
                var projectCarouselMargin = $('.project-one__carousel').data('carousel-margin');
            } else {
                var projectCarouselMargin = 0;
            }
            $('.project-one__carousel').owlCarousel({
                loop: true,
                margin: projectCarouselMargin,
                nav: false,
                dots: true,
                autoWidth: false,
                autoplay: true,
                smartSpeed: 700,
                autoplayTimeout: 5000,
                autoplayHoverPause: true,
                responsive: {
                    0: {
                        items: 1
                    },
                    480: {
                        items: 1
                    },
                    600: {
                        items: 1
                    },
                    991: {
                        items: 2
                    },
                    1000: {
                        items: 3
                    },
                    1200: {
                        items: 3
                    }
                }
            });
        }

    });

})(jQuery);


JSON.parse(localStorage.getItem("isDarkMode")) && document.querySelector("html").classList.add("filter"),
    JSON.parse(localStorage.getItem("fontSizeRelative")) ? (Number.parseInt(JSON.parse(localStorage.getItem("fontSizeRelative"))),
        $("h1, h2, h3, h4, h5, h6, p, a, span").animate({
            "font-size": "+=" + JSON.parse(localStorage.getItem("fontSizeRelative"))
        })) : localStorage.setItem("fontSizeRelative", "0"),

document.querySelector("#blackmode").addEventListener("click", function (t) {
    t.preventDefault(),
        localStorage.setItem("isDarkMode", document.querySelector("html").classList.toggle("filter"))
}),
    $("#plsfont, #minfont, #resfont").on("click", function () {
        $("#plsfont, #minfont, #resfont").removeClass("active")
    }),
    $("#plsfont").on("click", function (t) {
        Number.parseInt(localStorage.getItem("fontSizeRelative")) <= 9 && (localStorage.setItem("fontSizeRelative", Number.parseInt(localStorage.getItem("fontSizeRelative")) + 1),
            $("h1, h2, h3, h4, h5, h6, p, a, span").animate({
                "font-size": "+=1"
            }, 1),
            t.target.classList.add("active"))
    }),
    $("#minfont").on("click", function (t) {
        -9 <= Number.parseInt(localStorage.getItem("fontSizeRelative")) && (localStorage.setItem("fontSizeRelative", Number.parseInt(localStorage.getItem("fontSizeRelative")) - 1),
            $("h1, h2, h3, h4, h5, h6, p, a, span").animate({
                "font-size": "-=1"
            }, 1),
            t.target.classList.add("active"))
    }),
    $("#resfont").on("click", function (t) {
        $("h1, h2, h3, h4, h5, h6, p, a, span").removeAttr("style"),
            localStorage.setItem("fontSizeRelative", "0")
    });

$(".closemodal").on("click", function() {
    $(".error-text").removeClass("active"),
    $(".call-request").removeClass("active")
});

$("#request-call").on("click", function() {
    $(".call-request").addClass("active")
});

window.addEventListener("keydown", function (t) {
    "" != window.getSelection().toString() && t.ctrlKey && 13 == t.keyCode && (document.querySelector(".error-text").classList.add("active"),
        document.querySelector(".error__href").value = window.location.href,
        document.querySelector(".error__value").value = window.getSelection().toString()),
    27 === t.keyCode && "Escape" === t.key && ($(".error-text").removeClass("active"),
        $(".call-request").removeClass("active"))
});
const postData = async function (t, e) {
    var n = document.cookie.split("; ").filter(t => "csrftoken" === t.split("=")[0])[0].split("=")[1];
    const i = await fetch(t, {
        method: "POST",
        body: e,
        mode: "same-origin",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": n
        }
    });
    return await i.json()
}
    , formTypo = document.querySelector(".form__typo")
    , errorText = document.querySelector(".error-text");

function bindData(n, i, o) {
    n.addEventListener("submit", function (t) {
        t.preventDefault();
        const e = new FormData(n);
        t = JSON.stringify(Object.fromEntries(e.entries()));
        document.querySelector(".spinner").classList.add("show"),
            postData(o, t).then(function (t) {
                i.classList.remove("active");
                document.querySelector(".spinner").classList.remove("show");
                window.swal({
                    title: `${message.title}`,
                    icon: "info",
                    position: "center",
                    timer: 3e3,
                    html: `<p>${message.success}</p> `
                })
            }).catch(function () {
                i.classList.remove("active"),
                    document.querySelector(".spinner").classList.remove("show");
                    window.swal({
                        title: `${message.title}`,
                        icon: "error",
                        position: "center",
                        timer: 3e3,
                        html: `<p>${message.failure}</p> `
                    });
            }).finally(function () {
                n.reset()
            })
    })
}

bindData(formTypo, errorText, "/en/api/typo-report");


const voice = document.querySelector("#audio")
    , aside = document.querySelectorAll(".aside ul li")
    , ulAside = document.querySelector(".aside ul");

function removeClassActive() {
    aside.forEach(function (t) {
        t.classList.remove("active")
    })
}

function addClassActive(t = 0) {
    aside[t].classList.add("active")
}

removeClassActive();
ulAside.addEventListener("click", function (t) {
    t.preventDefault();
    const n = t.target;

    if (n && n.classList.contains('aside_li')) {
        aside.forEach(function (item, i) {
            if (n === item) {
                removeClassActive();
                addClassActive(i);
                $("#resfont").removeClass("active");

            }
        })
    }
});
voice.addEventListener("click", function () {
    var t = JSON.parse(localStorage.getItem("soundAssistantEnabled"));
    localStorage.setItem("soundAssistantEnabled", !t)
});

$(window).on("mouseup", function () {
    let lastSoundAssistantTimeout = null;
    const locales = {
        en: "US English Female",
        ru: "Russian Female",
        uz: "Russian Female"
    }

    if (JSON.parse(localStorage.getItem("soundAssistantEnabled"))) {
        let t = window.getSelection();
        "" !== t.toString() && (lastSoundAssistantTimeout = setTimeout(function (t) {
            responsiveVoice.isPlaying() && responsiveVoice.cancel(),
                responsiveVoice.speak(window.getSelection().toString(), locales[page_lang])
        }, 250))
    } else
        clearTimeout(lastSoundAssistantTimeout)
});
