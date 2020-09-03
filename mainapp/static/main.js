// 지도 사이즈 제한
// $(window).resize(function() {
//     $("article.map-area").css("display", "none");
// })


// 지도 홈버튼(줌아웃)
L.Control.zoomHome = L.Control.extend({
    home: { lat:0, lng:0, zoom:0 },
    options: {
        position: 'topright',
        zoomHomeText: `
            <svg width="20px" height="20px" viewBox="0 0 16 16" class="bi bi-arrows-fullscreen" fill="darkgrey" xmlns="http://www.w3.org/2000/svg">
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
        $(".name-area > h2").text("지역을 선택해 주세요");
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
                <button type="button" onclick="location.href='${url[0]}'">더보기</button>
                <button type="button" class="button primary" onclick="location.href='${url[1]}'">사진 올리기</button>
        </div></div></div>`;

        $("#map-cover, div.popup-area").css("display", "block");
        $("#map-popup").html(msg);
}



// 다른 영역 클릭 시 팝업창 닫기
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