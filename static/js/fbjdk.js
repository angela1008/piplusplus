    window.fbAsyncInit = function() {
            FB.init({
              appId      : '125287541296517',
              status: true, 
            cookie: true,
            oauth: true,
              xfbml      : true,
              version    : 'v2.8'
            });
    //     window.fbloaded();
    //     FB.AppEvents.logPageView();
    //   };
    
      FB.getLoginStatus(function(response) {
    statusChangeCallback(response);
    });
    
    };
      (function(d, s, id){
         var js, fjs = d.getElementsByTagName(s)[0];
         if (d.getElementById(id)) {return;}
         js = d.createElement(s); js.id = id;
         js.src = "//connect.facebook.net/en_US/sdk.js";
         fjs.parentNode.insertBefore(js, fjs);
       }(document, 'script', 'facebook-jssdk'));
       
        function testAPI() {
    console.log('Welcome!  Fetching your information.... ');
    FB.api('/me',{fields:"id,name,email"}, function(response) {
      console.log('Successful login for: ' + response.name);
      document.getElementById('status').innerHTML =
         '<img src="https://graph.facebook.com/'
      + response.id + '/picture">'+ '<br/>' + response.name+'<br/>' ;
      
       var facebookmail = response.emil;
       var facebookid = response.id;
    
    document.getElementById("id_email").value=response.email;

        
        
    });
    }