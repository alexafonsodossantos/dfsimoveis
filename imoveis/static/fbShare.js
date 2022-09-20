
    window.fbAsyncInit = function() {
        FB.init({
            appId: '{599373841672782}',
            xfbml: true,
            version: 'v2.9'
        });
        FB.AppEvents.logPageView();
    };
    function isMobile() {
        const toMatch = [/Android/i, /webOS/i, /iPhone/i, /iPad/i, /iPod/i, /BlackBerry/i, /Windows Phone/i];
        return toMatch.some((toMatchItem) => {
            return navigator.userAgent.match(toMatchItem);
        });
    }
    function messengerShare() {
        url = 'https://dfsimoveis.herokuapp.com/detalhes/{{imovel.id}}';
        if (isMobile()) {
            window.location.href = "fb-messenger://share/?link=" + url;
        } else {
            FB.ui({
                method: 'send',
                link: url,
                redirect_uri: url
            });
        }
    }
