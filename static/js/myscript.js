var swiper = new Swiper('.swiper-container', {
  slidesPerView: 1,
  spaceBetween: 30,
  loop: true,
  autoplay: {
    delay: 5000,
  },
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
  },
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
});
$(document).ready(function () {
  // Category filter
  $('.list-group-item').click(function () {
      var category = $(this).data('filter');
      if (category == 'all') {
          $('.card').show();
      } else {
          $('.card').hide();
          $('.card[data-category="' + category + '"]').show();
      }
  });
});