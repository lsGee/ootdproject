// 지도 홈버튼(줌아웃)
L.Control.zoomHome = L.Control.extend({
    home: { lat:0, lng:0, zoom:0 },
    options: {
        position: 'topright',
        zoomHomeText: `
            <svg width="24px" height="24px" viewBox="0 0 16 16" class="bi bi-arrows-fullscreen" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd" d="M5.828 10.172a.5.5 0 0 0-.707 0l-4.096 4.096V11.5a.5.5 0 0 0-1 0v3.975a.5.5 0 0 0 .5.5H4.5a.5.5 0 0 0 0-1H1.732l4.096-4.096a.5.5 0 0 0 0-.707zm4.344 0a.5.5 0 0 1 .707 0l4.096 4.096V11.5a.5.5 0 1 1 1 0v3.975a.5.5 0 0 1-.5.5H11.5a.5.5 0 0 1 0-1h2.768l-4.096-4.096a.5.5 0 0 1 0-.707zm0-4.344a.5.5 0 0 0 .707 0l4.096-4.096V4.5a.5.5 0 1 0 1 0V.525a.5.5 0 0 0-.5-.5H11.5a.5.5 0 0 0 0 1h2.768l-4.096 4.096a.5.5 0 0 0 0 .707zm-4.344 0a.5.5 0 0 1-.707 0L1.025 1.732V4.5a.5.5 0 0 1-1 0V.525a.5.5 0 0 1 .5-.5H4.5a.5.5 0 0 1 0 1H1.732l4.096 4.096a.5.5 0 0 1 0 .707z"/>
            </svg>`,
        zoomHomeTitle: 'Zoom home'
    },

    onAdd: function (map) {
        var controlName = 'gin-control-zoom',
            container = L.DomUtil.create('div', controlName + ' leaflet-bar'),
            options = this.options;

        this._zoomHomeButton = this._createButton(options.zoomHomeText, options.zoomHomeTitle,
        controlName + '-home', container, this._zoomHome);

        return container;
    },

    onRemove: function (map) {
        map.off('zoomend zoomlevelschange', this._updateDisabled, this);
    },

    _zoomHome: function (e) {
        mymap.setView([this.home.lat, this.home.lng], this.home.zoom);
    },

    _createButton: function (html, title, className, container, fn) {
        var link = L.DomUtil.create('a', className, container);
        link.innerHTML = html;
        link.href = '#';
        link.title = title;

        L.DomEvent.on(link, 'mousedown dblclick', L.DomEvent.stopPropagation)
            .on(link, 'click', L.DomEvent.stop)
            .on(link, 'click', fn, this)
            .on(link, 'click', this._refocusOnMap, this);

        return link;
    },
});



// 팝업 정보 띄우기
// 날씨정보는 weater.js
function getInfo(layer, img, cd, url) {
    var msg = `
        <div><div><div class="popup info">
            <table class="table table-sm"><tbody>
                <tr>
                    <th class="table-secondary" colspan="2">${layer.feature.properties.SIG_KOR_NM}</th>
                </tr>
                <tr id="popup-desc">
                    <th class="first-col">현재</th>
                    <td>${img.spinner}</td>
                </tr>
                <tr id="popup-temp-h1">
                    <th class="first-col">1시간후</th>
                    <td>${img.spinner}</td>
                </tr>
                <tr id="popup-temp-h2">
                    <th class="first-col">2시간후</th>
                    <td>${img.spinner}</td>
                </tr>
            </tbody></table>
            ${img.best_img}<br>
        <div class="btn-group" role="group" aria-label="Large button group">
                <button type="button" class="btn btn-secondary" onclick="location.href='${url[0]}'">더보기</button>
                <button type="button" class="btn btn-secondary" onclick="location.href='${url[1]}'">사진 올리기</button>
        </div>
        </div></div></div>`;

        $("#map-cover, div.popup-area").css("display", "block");
        $("#map-popup").html(msg);
}



// 회색영역 클릭 시 팝업창 닫기
function closePopup() {
    e = event.target;
    var popup_area = document.querySelectorAll("#map-popup *");
    var popup = document.querySelectorAll("#map-cover, div.popup-area");

    for(var i in popup_area) {
        if(e == popup_area[i]) break;
        else if( i == popup_area.length - 1 ) {
            popup[0].setAttribute("style", "display:none;");
            popup[1].setAttribute("style", "display:none;");
        }
    }
}


// 튜토리얼 영역 생성
function openTutorial() {
    // 본문(지도+지역명검색+수치) 전체 높이
    var height = document.querySelector("body > section").offsetHeight;

    $("div.tutorial-area").css({
        height: height + "px",
        visibility: "visible",
        padding: "0px 7px"
    });
    $("body > section > div:nth-child(2)").css("top", -height + "px");
    $("section").css("height", height);

    // var h_maptitle = document.querySelector("#mapid").offsetTop;
    // var h_maparea = document.querySelector("#mapid").offsetHeight;
    
    // var h_h2 = document.querySelector("article.search-bar > h2").offsetHeight;
    // var h_search = document.querySelector("article.search-bar").offsetHeight - h_h2;
    

    // $("div.tutorial-area").html(`
    //     <div class="tutorial-map-title"></div>
    //     <div class="tutorial-map"><div>
    //         지도를 클릭하면<br>지역별 날씨 정보와<br>사용자들의 OOTD를<br>확인할 수 있습니다. 
    //     </div></div>
    //     <div class="tutorial-search-title"></div>
    //     <div class="tutorial-search"></div>
        
    // `);

    // $("div.tutorial-area > div:nth-child(1)").css("height", h_maptitle);

    // $("div.tutorial-map").css("height", h_maparea);

    // $("div.tutorial-area > div:nth-child(3)").css("height", h_h2);

    // $("div.tutorial-search").css({
    //     height: h_search,
    //     margin: "3px 30px"
    // });
}

function openTutorialMap() {
    openTutorial();

    $("div.tutorial-area").html(`
        <div class="tutorial tutorial-map">
            지도를 클릭하면<br>지역별 날씨 정보와<br>사용자들의 OOTD를<br>확인할 수 있습니다.
        </div>
    `)

    $("div.tutorial.tutorial-map").css({
        width: "200px",
        top: 10,
        left: $("svg.bi.bi-question-circle-fill.map").offset().left + 15
    });
}

function openTutorialSearch() {
    openTutorial();

    $("div.tutorial-area").html(`
        <div class="tutorial tutorial-search">
            지도를 클릭하면<br>지역 이름을 직접 선택해<br>사용자들의 OOTD를<br>확인할 수 있습니다.
        </div>
    `)

    $("div.tutorial.tutorial-search").css({
        width: "200px",
        top: $("article.search-bar > h2").offset().top - 50,
        left: $("svg.bi.bi-question-circle-fill.search").offset().left + 15
    });
}

function closeTutorial() {
    $("div.tutorial-area").removeAttr("style");
    $("div.tutorial-area").empty();
    $("body > section > div:nth-child(2)").removeAttr("style");
    $("section").removeAttr("style");
}

