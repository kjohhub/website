function proc(videoInfo) {
  $.each(videoInfo, function (index, item) {
    let str = "<tr><td>" + item.title + "</td>";
    str += "<td>" + item.videoId + "</td></tr>";
    $("table").append(str);
    console.log(item);
  });
}


$(document).ready(function(){
  $( "#btn" ).click( function() {
    //버튼클릭 이벤트가 뜨고 난 후 검색어를 저장해야 초기값(빈 값)으로 되돌아가지 않음
    var playlist_code = $("#playlist_code").val();
    //console.log(playlist_code);
      $.ajax({
            type: "GET",
            dataType: "JSON",
            //default:PLxCfRlqeGfGnXPhPQNG1Ac0fWLS1gYDjZ로 검색할 것
            url: "https://www.googleapis.com/youtube/v3/playlistItems?playlistId=" + playlist_code + "&part=snippet&maxResults=50&key=AIzaSyCZ2OTX5bKu60-32PRV5m9tUfjiD08L_q0",
            contentType: "application/json",
            success : function(jsonData) {
              let videoInfo = [];
                    for (let i = 0; i < jsonData.items.length; i++) {
                      let items = jsonData.items[i];
                      let title = items.snippet.title;
                      let videoId = items.snippet.resourceId.videoId;
                      let items_dict = {
                        title,
                        videoId,
                      };
                      videoInfo.push(items_dict);
                      //console.log("title : "+ title);
                      //console.log("videoId : "+ videoId);
                    }

                    proc(videoInfo);
              },

            complete : function(data) {
              },

            error : function(xhr, status, error) {
                console.log("유튜브 요청 에러: "+error);
              }
        });
    });
});


/*
$.ajax({
  type: "GET",
  dataType: "JSON",
  url: "https://www.googleapis.com/youtube/v3/playlistItems?playlistId=PLxCfRlqeGfGnXPhPQNG1Ac0fWLS1gYDjZ&part=snippet&maxResults=100&key=AIzaSyCZ2OTX5bKu60-32PRV5m9tUfjiD08L_q0",
  contentType: "application/json",
  success : function(jsonData) {

  for (var i = 0; i < jsonData.items.length; i++) {
    var items = jsonData.items[i];
    var title = items.snippet.title;
    var videoId = items.snippet.resourceId.videoId;
    console.log("title : "+ title);
    console.log("videoId : "+ videoId);
    }
  },

  complete : function(data) {
  },

  error : function(xhr, status, error) {
  console.log("유튜브 요청 에러: "+error);
  }
});
*/
