var tag = document.createElement('script');
tag.src = "http://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
var current_idx = 0;
var current_videoid = '';


/**
 * onYouTubeIframeAPIReady 함수는 필수로 구현해야 한다.
 * 플레이어 API에 대한 JavaScript 다운로드 완료 시 API가 이 함수 호출한다.
 * 페이지 로드 시 표시할 플레이어 개체를 만들어야 한다.
 */
var player;
var playerState;

function onYouTubeIframeAPIReady() {
    player = new YT.Player('player', {
        height: '100%',
        width: '100%',
        videoId: '',
        playerVars: {
            rel : 0,          //0으로 해놓아야 재생 후 관련 영상이 안뜸, 이제 적용 안됨.
            showinfo: 0,
            autoplay: 1
        },
        events: {
            'onReady': onPlayerReady,               // 플레이어 로드가 완료되고 API 호출을 받을 준비가 될 때마다 실행
            'onStateChange': onPlayerStateChange    // 플레이어의 상태가 변경될 때마다 실행
        }
    });
}
function onPlayerReady(event) {
    console.log('onPlayerReady 실행');
}
function onPlayerStateChange(event) {
    playerState = event.data;

    if (playerState== YT.PlayerState.ENDED) {
        var max = table.rows.length - 1;
        if (current_idx < max)
            current_idx += 1;
        else
            current_idx = 0;

        changeVideoAndStart(table.rows[current_idx].id);
        updateTable();
    } 
//   if (playerState== YT.PlayerState.PLAYING) alert('재생 중');
//  if (event.data == YT.PlayerState.PAUSED) alert('일시중지 됨');
//    if (event.data == YT.PlayerState.BUFFERING) alert('버퍼링 중');
//   if (event.data == YT.PlayerState.CUED) alert('재생준비 완료됨');
//  if (event.data == -1) alert('예외');

    console.log('onPlayerStateChange 실행: ' + playerState);

    // 재생여부를 통계로 쌓는다.
    collectPlayCount(event.data);
}

function playYoutube() {
    // 플레이어 자동실행 (주의: 모바일에서는 자동실행되지 않음)
    player.playVideo();
}
function pauseYoutube() {
    player.pauseVideo();
}
function stopYoutube() {
    player.seekTo(0, true);     // 영상의 시간을 0초로 이동시킨다.
    player.stopVideo();
}
var played = false;
function collectPlayCount(data) {
    if (data == YT.PlayerState.PLAYING && played == false) {
        // todo statistics
        played = true;
        console.log('statistics');
    }
}

// 영상을 재생한다.
function changeVideoAndStart(id) {
    current_vid = id;
    player.loadVideoById(id, 0, "large");
    insertVideoToHistory();     // 시청기록에 추가한다.
}

// 재생목록을 선택한다.
function selectPlaylist(id)
{
	postForm.setAttribute('method', 'post');
	postForm.setAttribute('action', '/youtube/playlist/'+ id + '/');
	postForm.submit();
}

// 재생목록을 추가한다.
function insertPlaylist()
{
    openForm("popupInsert");
}

// 재생목록의 이름을 변경한다
function renamePlaylist()
{
    openForm("popupRename");
}

// 재생목록을 삭제한다.
function deletePlaylist()
{
    openForm("popupDelete");
}

// 시청 기록을 가져온다
function selectHistory()
{
	postForm.setAttribute('method', 'post');
	postForm.setAttribute('action', '/youtube/history/');
	postForm.submit();
}

// 플레이중인 영상을 시청기록에 추가한다.
function insertVideoToHistory() {
    $.ajax({
        type: "POST",
        url: "/youtube/history/insert_video/",
        dataType: "text",
        data: {
            'videoid': current_vid, 
            'csrfmiddlewaretoken': '{{ csrf_token }}'
        },
        success: function(response){ 
        },
        error: function(request, status, error){
        },
    });
}

// 플레이중인 영상을 재생목록에 추가한다.
function insertVideoToPlaylist(listid) {
    var videoid = current_vid
    $.ajax({
        type: "POST",
        url: "/youtube/playlist/insert_video/",
        data: {
            'listid': listid, 
            'videoid': videoid, 
            'csrfmiddlewaretoken': '{{ csrf_token }}'
        },
        dataType: "text",
        success: function(response){ 
        },
        error: function(request, status, error){ 
        },
    });
}

// 재생목록에서 비디오를 삭제한다
function deleteVideoFromPlaylist(listid, videoid) {
    $.ajax({
        type: "POST",
        url: "/youtube/playlist/delete_video/",
        data: {
            'listid': listid, 
            'videoid': videoid, 
            'csrfmiddlewaretoken': '{{ csrf_token }}'
        },
        dataType: "text",
        success: function(response){ 
        },
        error: function(request, status, error){ 
        },
    });
}

// 시청기록에서 비디오를 삭제한다
function deleteVideoFromHistory(videoid) {
    $.ajax({
        type: "POST",
        url: "/youtube/history/delete_video/",
        data: {
            'videoid': videoid, 
            'csrfmiddlewaretoken': '{{ csrf_token }}'
        },
        dataType: "text",
        success: function(response){ 
        },
        error: function(request, status, error){ 
        },
    });
}


function changeVideoObjectAndStart() {
    // 0초부터 10초까지 재생을 시킨다.
    player.loadVideoById({
        'videoId': 'bHQqvYy5KYo',
        'startSeconds': 0,
        'endSeconds': 10
    });
}

/**
 * loadPlaylist 함수는 지정한 재생목록을 로드하고 재생한다.
 * 인수구문: loadPlaylist(playlist:String|Array, index:Number, startSeconds:Number, suggestedQuality:String):Void
 * 개체구문: loadPlaylist({list:String, listType:String, index:Number, startSeconds:Number, suggestedQuality:String}):Void
 * [주의: 개체구문의 loadPlaylist 함수에서의 재생목록ID 와 동영상ID 의 사용방법이 다르다.]
 */
function changeVideoListAndStart() {
    player.loadPlaylist(['wcLNteez3c4', 'LOsNP2D2kSA', 'rX372ZwXOEM'], 0, 0, 'large');
}
function changeVideoListObjectAndStart() {
    player.loadPlaylist({
        'playlist': ['9HPiBJBCOq8', 'Mp4D0oHEnjc', '8y1D8KGtHfQ', 'jEEF_50sBrI'],
        'listType': 'playlist',
        'index': 0,
        'startSeconds': 0,
        'suggestedQuality': 'small'
    });
}
function changeVideoListObjectAndStart2() {
    player.loadPlaylist({
        'list': 'UUPW9TMt0le6orPKdDwLR93w',
        'listType': 'playlist',
        'index': 0,
        'startSeconds': 0,
        'suggestedQuality': 'small'
    });
}

function itemClicked(tr) {
    current_idx = tr.rowIndex;
    changeVideoAndStart(tr.id);
    updateTable();
}

function itemDelete(type, listid, videoid) {
    //alert(type + "," + listid + "," + videoid);
    if  (type == 'history') {
        deleteVideoFromHistory(videoid);
    }
    else if (type == 'playlist') {
        deleteVideoFromPlaylist(listid, videoid);
    }
    // 테이블에서 삭제
    for (var i = 0; i < table.rows.length; i++) {
        if (table.rows[i].id == videoid) {
            table.deleteRow(i);
            break;
        }  
    }
}

function delete_row() {
    alert(table.rows.length);
    if (table.rows.length < 1) 
        return;
    table.deleteRow( table.rows.length-1 ); // 하단부터 삭제
}

function updateTable() {
    var rows = document.getElementById("table").getElementsByTagName("tr");
    for (var i = 0; i < rows.length; i++) {
        if (i == current_idx)
            rows[i].classList.add("selected");
        else
            rows[i].classList.remove("selected");
    }
}

function openForm(formid) {
    document.getElementById(formid).style.display = "block";
}

function closeForm(formid) {
    document.getElementById(formid).style.display = "none";
}