$('a[data-toggle="formtab"]').click(function(){
    var targetId = $(this).attr('href');

    $('.tabs-panels').removeClass('active')
    $('a[data-toggle="formtab"]').removeClass('active');
    
    $(targetId).addClass('active');
	$('a[href="'+targetId+'"]').addClass('active')

	

});