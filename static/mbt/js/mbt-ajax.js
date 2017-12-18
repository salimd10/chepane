$('#like_btn').click(function(){
    var dishid;
    dishid = $(this).attr("data-dishid");
    $.get('/like_dish/',{dish_id: dishid},function(data){
               $('#dsp_like').html(data);
               $('#like_btn').hide();
    });

});