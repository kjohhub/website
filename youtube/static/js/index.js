

/**
 * Youtube API 로드
 */
var tag = document.createElement('script');
tag.src = "http://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
var current_idx = 0;

/**
 * onYouTubeIframeAPIReady 함수는 필수로 구현해야 한다.
 * 플레이어 API에 대한 JavaScript 다운로드 완료 시 API가 이 함수 호출한다.
 * 페이지 로드 시 표시할 플레이어 개체를 만들어야 한다.
 */
var player;
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
var playerState;
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


/**
 * loadVideoById 함수는 지정한 동영상을 로드하고 재생한다.
 * 인수구문: loadVideoByUrl(mediaContentUrl:String, startSeconds:Number, suggestedQuality:String):Void
 * 개체구문: loadVideoByUrl({mediaContentUrl:String, startSeconds:Number, endSeconds:Number, suggestedQuality:String}):Void
 * loadVideoById 함수 뿐만 아니라 다른 대체적인 함수들도 개체구문이 기능이 더 많다.
 */
function changeVideoAndStart(id) {
    player.loadVideoById(id, 0, "large");
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

function updateTable() {
    var rows = document.getElementById("table").getElementsByTagName("tr");
    for (var i = 0; i < rows.length; i++) {
        if (i == current_idx)
            rows[i].classList.add("selected");
        else
            rows[i].classList.remove("selected");
    }
}

function sendPost(action, params) {

	var form = document.createElement('form');
	form.setAttribute('method', 'post');
	form.setAttribute('action', action);
	document.charset = "utf-8";
	for ( var key in params) {

		var hiddenField = document.createElement('input');
		hiddenField.setAttribute('type', 'hidden');
		hiddenField.setAttribute('name', key);
		hiddenField.setAttribute('value', params[key]);
		form.appendChild(hiddenField);
	}

	document.body.appendChild(form);
	form.submit();
}


/*
function selectedRow() {
    var index,
    table = document.getElementById("table");
    
    for (var i = 0; i < table.rows.length; i++)
    {
        table.rows[i].onclick = function()
        {
        if (typeof index !== "undefined") {
            table.rows[index].classList.toggle("selected");
        }
        index = this.rowIndex;

        //var video = document.video_list(index);
       
        this.classList.toggle("selected");
        };
    }
}

*/

/*
// 테이블의 Row 클릭시 값 가져오기
$("#example-table-1 tr").click(function(){

  alert("aaaaa");
    var str = ""
    var tdArr = new Array();    // 배열 선언

    // 현재 클릭된 Row(<tr>)
    var tr = $(this);
    var td = tr.children();

    // tr.text()는 클릭된 Row 즉 tr에 있는 모든 값을 가져온다.
    alert("클릭한 Row의 모든 데이터 : "+tr.text());

    // 반복문을 이용해서 배열에 값을 담아 사용할 수 도 있다.
    td.each(function(i){
        tdArr.push(td.eq(i).text());
    });

    alert("배열에 담긴 값 : "+tdArr);

    // td.eq(index)를 통해 값을 가져올 수도 있다.

    var no = td.eq(0).text();
    var userid = td.eq(1).text();
    var name = td.eq(2).text();
    var email = td.eq(3).text();


    str +=    " * 클릭된 Row의 td값 = No. : <font color='red'>" + no + "</font>" +
            ", 아이디 : <font color='red'>" + userid + "</font>" +
            ", 이름 : <font color='red'>" + name + "</font>" +
            ", 이메일 : <font color='red'>" + email + "</font>";

    $("#ex1_Result1").html(" * 클릭한 Row의 모든 데이터 = " + tr.text());
    $("#ex1_Result2").html(str);

});
*/
