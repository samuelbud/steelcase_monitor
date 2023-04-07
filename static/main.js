function get_icon_url(icon) {
    return `http://openweathermap.org/img/w/${icon}.png`;
}

function autoChangeRoute() {
  setInterval(function() {
    if (window.location.pathname === '/') {
      window.location.pathname = '/video';
    } else if (window.location.pathname === '/video') {
      window.location.pathname = '/weather';
    } else if (window.location.pathname === '/weather') {
      window.location.pathname = '/funfact';
    } else if (window.location.pathname === '/funfact') {
      window.location.pathname = 'riddle';
    } else if (window.location.pathname === '/riddle') {
      window.location.pathname = '/';
    } else {
      window.location.pathname = '/';
    }
  }, 240000);
}


autoChangeRoute();

