require(['jQuery', 'boostrap', 'jquery.easing'], function($){


	var submitForm = function(e) {
	    e.preventDefault();
	    var self = $(this);
	    $("#send-button").attr('disabled', true);
	    $("#wait-message").prepend('<span>Sending message, please wait... </span>');
	    $.post(
	        self.attr('action'),
	        self.serializeArray(),
	        function(data) {
            	if (data.response.status === 'success') {
            		$('#success').removeClass('hidden');
            		return;
            	}
	            $.each(data.errors, function(d) {
	            	$('input[name=' + d + ']').addClass('alert-danger');
	            	data.errors[d].forEach(function(d2) {
	            		var span = $('<span>');
	            		span.addClass('error')
	            		span.text(d2);
	            		$('input[name=' + d + '], textarea[name=' + d + ']').next('p').append(span);
	            	});
	            });
	        }
	    );
	};

	$( document ).ready(function() {

		// jQuery for page scrolling feature - requires jQuery Easing plugin
		$('a.page-scroll').bind('click', function(event) {
		    var $anchor = $(this);
		    $('html, body').stop().animate({
		        scrollTop: ($($anchor.attr('href')).offset().top - 50)
		    }, 1250, 'easeInOutExpo');
		    event.preventDefault();
		});

		// Highlight the top nav as scrolling occurs
		$('body').scrollspy({
		    target: '.navbar-fixed-top',
		    offset: 51
		});

		// Closes the Responsive Menu on Menu Item Click
		$('.navbar-collapse ul li a').click(function(){ 
		        $('.navbar-toggle:visible').click();
		});

		// Offset for Main Navigation
		$('#mainNav').affix({
		    offset: {
		        top: 100
		    }
		})

		$("#contact-form").submit(submitForm);

		$("#myModal").on("hidden.bs.modal", function () {
		    // put your default event here
		    console.log('nun')
		    // $("#myModal .modal-content").html("");
		    $(this).removeData();
		});

	});

	console.log('main.js loaded');
});