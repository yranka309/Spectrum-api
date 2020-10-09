
 $(document).ready(function(){
  // Add smooth scrolling to all links
  $("a").on('click', function(event) {

    // Make sure this.hash has a value before overriding default behavior
    if (this.hash !== "") {
      // Prevent default anchor click behavior
      event.preventDefault();

      // Store hash
      var hash = this.hash;

      // Using jQuery's animate() method to add smooth page scroll
      // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 800, function(){

        // Add hash (#) to URL when done scrolling (default click behavior)
        window.location.hash = hash;
      });
    } // End if
  });
});


function showfunc1(){
  var x=document.getElementById("aboutvibhav");
  var y=document.getElementById("aboutees");
    x.style.display="block";
    y.style.display="none";
    $('#av').addClass('active');
    $('#ae').removeClass('active');
}
function showfunc2(){
  var x=document.getElementById("aboutvibhav");
  var y=document.getElementById("aboutees");
    x.style.display="none";
    y.style.display="block";
    $('#av').removeClass('active');
    $('#ae').addClass('active')
  
}

function showday1(){
  var x=document.getElementById("day1");
  var y=document.getElementById("day2");
    x.style.display="block";
    y.style.display="none";
    $('#d1').addClass('active');
    $('#d2').removeClass('active');
}
function showday2(){
  var x=document.getElementById("day1");
  var y=document.getElementById("day2");
    x.style.display="none";
    y.style.display="block";
    $('#d1').removeClass('active');
    $('#d2').addClass('active')
  
}
// 
/* $(document).ready(function(){
  if(window.innerWidth<800){
    $('.timeline li').addClass('timeline-inverted')
  }
});

$(window).resize(function(){
  if(window.innerWidth < 800){
    $('.timeline li').addClass('timeline-inverted')
  }else{

  }
}); */
// star rating
$(document).ready(function(){
  
  /* 1. Visualizing things on Hover - See next part for action on click */
  $('#stars li').on('mouseover', function(){
    var onStar = parseInt($(this).data('value'), 10); // The star currently mouse on
   
    // Now highlight all the stars that's not after the current hovered star
    $(this).parent().children('li.star').each(function(e){
      if (e < onStar) {
        $(this).addClass('hover');
      }
      else {
        $(this).removeClass('hover');
      }
    });
    
  }).on('mouseout', function(){
    $(this).parent().children('li.star').each(function(e){
      $(this).removeClass('hover');
    });
  });
  
  
  /* 2. Action to perform on click */
  $('#stars li').on('click', function(){
    var onStar = parseInt($(this).data('value'), 10); // The star currently selected
    var stars = $(this).parent().children('li.star');
    
    for (i = 0; i < stars.length; i++) {
      $(stars[i]).removeClass('selected');
    }
    
    for (i = 0; i < onStar; i++) {
      $(stars[i]).addClass('selected');
    }
    
    // JUST RESPONSE (Not needed)
    var ratingValue = parseInt($('#stars li.selected').last().data('value'), 10);
    $.ajax({
      type:'POST',
      url:'/web/rating',
      data:{
        rvalue:ratingValue,
        event:$('#stardata').val(),
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
      },
      success:function(response){
        if(response=='Success'){
          
          $('#stars').css('display','none')
          $('#success-box').css('display','block')
          msg='You Rated '+ratingValue+' out of 5';
          $('.success-box div.text-message').html("<span>" + msg + "</span>");
        }
        else{
        alert("Invalid operation");
        }
      },
      error:function(xhr){
        alert(`An error occcured: `+xhr.status+" "+ xhr.statusText+" "+xhr.responseText);
      }
    })
    
  });
  
  
});


function responseMessage(msg) {
  $('.success-box').fadeIn(200);  
  $('.success-box div.text-message').html("<span>" + msg + "</span>");
}

$(document).ready(function(){
  $('.customer-logos').slick({
      slidesToShow: 6,
      slidesToScroll: 1,
      autoplay: true,
      autoplaySpeed: 1500,
      arrows: false,
      dots: false,
      pauseOnHover: false,
      responsive: [{
          breakpoint: 768,
          settings: {
              slidesToShow: 4
          }
      }, {
          breakpoint: 520,
          settings: {
              slidesToShow: 3
          }
      }]
  });
});