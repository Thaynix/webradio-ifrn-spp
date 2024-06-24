$(document).ready(function(){
    $(".carousel-imgs").owlCarousel({
        items: 1,
        loop: true,
        margin: 0,
        autoplay:true,
        autoplayTimeout:2500,
        autoplayHoverPause:false,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 1
            },
            1000: {
                items: 1
            }
        }
    });
  
    $(".carousel-cards").owlCarousel({
      items: 1,
      loop: false,
      margin: 10,
      autoHeight: false,
      autoHeightClass: 'owl-height',
      responsive: {
          0: {
              margin: 5,
              items: 1,
              autoHeight: true,
          },
          600: {
              items: 2,
              autoHeight: true,
          },
          1000: {
              items: 3
          }
      }
    });
    
    $('.carousel-cards-team').owlCarousel({
        loop:false,
        margin:5,
        nav:true,
        responsive:{
            0:{
                items:2
            },
            600:{
                items:3
            },
            1000:{
                items:5
            }
        }
    })
  });