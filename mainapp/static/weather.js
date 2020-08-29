const API_KEY = '0c584632a7b7d1d11a962fcc005458c6';
// const API_KEY = 'ec2e1a2fff61130a0460810ad0f94282';

function getURL(lat, lon){
    var weatherURL = "https://api.openweathermap.org/data/2.5/onecall";
    weatherURL += "?lat=" + lat + "&lon=" + lon;
    weatherURL += "&exclude=" + "minutely,daily";
    weatherURL += "&lang=kr";
    weatherURL += "&units=metric";
    weatherURL += "&appid="+API_KEY;

    return weatherURL;
}


function getWeather(lan,log) {
    $.ajax({
        url: getURL(lan,log),
        method: "GET",
        dataType: 'json',
        error: function(xhr, statud, error){
            alert(error);
        },
        success: function(json) {
            $("#popup-desc td").html(`
                <img class="weather-pic" src='http://openweathermap.org/img/wn/${json.current.weather[0].icon}.png'>
                &nbsp&nbsp${json.current.temp}˚C`);
            $("#popup-temp-h1 td").html(`
                <img class="weather-pic" src='http://openweathermap.org/img/wn/${json.hourly[1].weather[0].icon}.png'>
                &nbsp&nbsp${json.hourly[1].temp}˚C`);
            $("#popup-temp-h2 td").html(`
                <img class="weather-pic" src='http://openweathermap.org/img/wn/${json.hourly[2].weather[0].icon}.png'>
                &nbsp&nbsp${json.hourly[2].temp}˚C`);
            // $("#popup_temp > td").text(json.current.temp + "˚C");

            // document.writeln("<h2>1시간후 날씨</h2>");
            // // ***************** 59분이면? 몇분기준으로 가져와야하나??????
            // document.writeln("<h2>"+json.hourly[1].weather[0].description+"</h2>");
            // document.writeln("<h2>"+json.hourly[1].temp+"C</h2><hr>");

            // document.writeln("<h2>2시간후 날씨</h2>");
            // document.writeln("<h2>"+json.hourly[2].weather[0].description+"</h2>");
            // document.writeln("<h2>"+json.hourly[3].temp+"C</h2>");

        } //success func 종료
    });
}