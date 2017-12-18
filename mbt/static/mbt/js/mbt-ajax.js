$(document).ready(function(){
   $("#like_btn").click(function(){
        var dishid;
        dishid = $(this).attr("data-id");
        //alert(dishid)
        $.get("/like_dish",{d_id:dishid},function(data){
            $('#dsp_like').html(data);
            $('#like_btn').hide();
            }



        );

   });

});
