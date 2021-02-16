$(document).ready(function(){
  $( "#btn" ).click( function() {

    //버튼클릭 이벤트가 뜨고 난 후 검색어를 저장해야 초기값(빈 값)으로 되돌아가지 않음
    var playlist_code = $("#playlist_code").val();
    var count = 1;
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
                      let title = items.snippet.title.replace("'", "-");
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


  $("#btnSave").click(function() {

    var checkbox = $("input[name=checkbox]:checked");
    var success = 0;
    var failed = 0;

    if(confirm("정말 등록하시겠습니까?") == true) {
      checkbox.each(function(i) {
        // checkbox.parent() : checkbox의 부모는 <td>이다.
        // checkbox.parent().parent() : <td>의 부모이므로 <tr>이다.
        var tr = checkbox.parent().parent().eq(i);
        var td = tr.children();
  
        // td.eq(0)은 체크박스 이므로  td.eq(1)의 값부터 가져온다.
        var title = td.eq(1).find('input[type="text"]').val();
        var videoid = td.eq(2).find('input[type="text"]').val();
  
        $.ajax({
          type: "POST",
          url: "/youtube/manage_video/insert/",
          data: {
              'videoid': videoid,
              'title': title
          },
          async: false,
          dataType: "text",
          success: function(response){
            success+=1;
          },
          error: function(request, status, error){
            failed+=1;
            
          },
        });
      });
      
      alert("성공: " + success + ", 실패: " + failed);
    }
  });
});

//크롤링한 데이터를 테이블로 출력
function proc(videoInfo) {
  deleteAll();

  $.each(videoInfo, function (index, item) {
    let str =
      "<tr>" +
      "<td><input type='checkbox' name='checkbox'></td>" +
      "<td><input class='table_item' type='text' style='width: 900px;' name='title' value='"+ item.title + "'></td>" +
      "<td><input class='table_item' type='text' style='width: 200px;' name='title' value='"+ item.videoId + "' disabled></td>" +
    "</tr>";
    $("table").append(str);
    console.log(item);
    });
}

//테이블 데이터(행) 전체삭제
function deleteAll() {
  $("#result tr").remove();
}

//체크박스 전체선택/해제
function selectAll(selectAll)  {
  const checkboxes
     = document.querySelectorAll('input[type="checkbox"]');

  checkboxes.forEach((checkbox) => {
    checkbox.checked = selectAll.checked
  })
}
