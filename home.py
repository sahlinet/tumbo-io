def func(self):
	code = '''<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- apy Werbung -->
<ins class="adsbygoogle"
     style="display:inline-block;width:970px;height:90px"
     data-ad-client="ca-pub-3510032019858405"
     data-ad-slot="6183480971"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>'''
	print code
	template = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>apy.io</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
	<!-- favicon.ico -->
	<link rel="shortcut icon" href="/fastapp/apy/static/favicon.ico" type="image/x-icon">
	<link rel="icon" href="/fastapp/apy/static/favicon.ico" type="image/x-icon">
    <!-- Loading Bootstrap 
    <link href="%(STATIC_DIR)s/bootstrap/css/bootstrap.css" rel="stylesheet">-->
	<link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
	<!--
    <link href="%(STATIC_DIR)s/bootstrap/css/bootstrap-responsive.css" rel="stylesheet">
	-->
    <!-- Loading Flat UI -->
    <link href="%(STATIC_DIR)s/css/flat-ui.css" rel="stylesheet">
	<link href="%(STATIC_DIR)s/css/apy.css" rel="stylesheet">

  
    <!-- HTML5 shim, for IE6-8 support of HTML5 elements. All other JS at the end of file. -->
    <!--[if lt IE 9]>
      <script src="js/html5shiv.js"></script>
    <![endif]-->
	
  </head>
  <body>
  <header>
   <nav class="navbar navbar-default" role="navigation">
  <div class="container-fluid">
    <!-- Brand and toggle get grouped for better mobile display -->
    <div class="navbar-header">
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="http://apy.io">apy.io</a>
    </div>

    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
 
      <ul class="nav navbar-nav navbar-right">
        <li><a href="#" data-loc="home">Home</a></li>
		<li><a href="#" data-loc="features">Features</a></li>
		<li><a href="#" data-loc="testers">Testers</a></li>
      </ul>
    </div>
  </div>
</nav>
</header>
<div class="container">
	<section id="home" class="ourpanel">
		<div class="jumbotron jumbotron-midnight text-centered">
			<h1>apy.io</h1>
			<p>
				The Python Fiddling Platform
			</p>
		</div>
	</section>
	<section id="features" class="ourpanel">
		<div class="jumbotron jumbotron-midnight text-centered">
			<h1>Features</h1>
		</div>

		<div class="jumbotron jumbotron-midnight text-centered">
			<div class="row">
				<div class="showcase-item col-md-4">
					<div class="showcase-item-box">
						<img src="%(STATIC_DIR)s/images/icons/Pencil@2x.png"/>
						<h2>Fiddling</h2>

						<p>It was never easier to write and execute Python code in the browser.</p>
					</div>
				</div>
				
				<div class="showcase-item col-md-4">
					<div class="showcase-item-box">
					<img src="%(STATIC_DIR)s/images/icons/Arrow@2x.png"/>
						<h2>API</h2>
						<p>Create micro APIs based on Python. Directly published on our platform.</p>
					</div>
				</div>
				
				<div class="showcase-item col-md-4">
					<div class="showcase-item-box">
					<img src="%(STATIC_DIR)s/images/icons/Dude@2x.png"/>
						<h2>Sharing</h2>
						<p>Share your code with your friends or let them just use the API with a share link.</p>
					</div>
				</div>
			</div>
		</div>
		
	</section>
	<section id="testers" class="ourpanel">
			<div class="jumbotron jumbotron-midnight text-centered">
				<h1>Testers needed!</h1>
				<p>Do you want to help apy.io in the closed beta phase?</p><p>Drop us your name and your email address and </br>the reason why you are interested to see apy.io.</p>
				
			</div>

			<div class="jumbotron jumbotron-midnight text-centered">
				<div class="col-md-6 col-md-offset-3" id="interested">

					<form id="interested" name="interested">

						<!-- name -->
						<div class="form-group">
							<label for="name" class="col-sm-2 control-label">Name</label>
							<div class="col-sm-10">
								<input type="text" name="name" id="name" class="form-control"/>
							</div>
						</div>

						<!-- email -->
						<div class="form-group">
							<label for="email" class="col-sm-2 control-label">Email</label>
							<div class="col-sm-10">
								<input type="text" name="email" id="email" class="form-control"/>
							</div>
						</div>

						<!-- why -->
						<div class="form-group">
							<label for="why" class="col-sm-2 control-label">Why</label>
							<div class="col-sm-10">
								<input type="text" name="why" id="why" class="form-control" required />
							</div>
						</div>

						<!-- submit -->
						<div class="form-group">
							<div class="col-sm-offset-2 col-sm-10">
								<button class="testers btn btn-lg btn-primary-btn-embossed pull-left">Submit</button>
							</div>
						</div>


					</form>
				</div>
			
			</div>
	</section>
	
	<div class="container">	
	<section id="campaign" class="ourpanel">
			<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- apy Werbung -->
<ins class="adsbygoogle"
     style="display:inline-block;width:970px;height:90px"
     data-ad-client="ca-pub-3510032019858405"
     data-ad-slot="6183480971"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
	</section>
	</div>
	</div>
<div class="bottom-menu bottom-menu-inverse">
        <div class="container">
          <div class="row">
            <div class="col-md-2 brand">
              <a href="http://apy.io">apy.io</a>
            </div>

            <div class="col-md-8">
              <ul class="bottom-links">
				<li><a href="#" data-loc="home">Home</a></li>
				<li><a href="#" data-loc="features">Features</a></li>
				<li><a href="#" data-loc="testers">Testers</a></li>
              </ul>
            </div>

            <div class="col-md-2">
              <ul class="bottom-icons">
                <li><a href="https://twitter.com/philipsahli" class="fui-twitter"></a></li>
                <li><a href="https://plus.google.com/+PhilipSahli/posts" class="fui-googleplus"></a></li>
                <li><a href="http://www.linkedin.com/in/philipsahli" class="fui-linkedin"></a></li>
              </ul>
            </div>
          </div>
        </div>
      </div>

    <!-- Load JS here for greater good =============================-->
    <script src="%(STATIC_DIR)s/js/jquery-1.8.3.min.js"></script>
    <script src="%(STATIC_DIR)s/js/jquery-ui-1.10.3.custom.min.js"></script>
    <script src="%(STATIC_DIR)s/js/jquery.ui.touch-punch.min.js"></script>
	<!--
    <script src="%(STATIC_DIR)s/js/bootstrap.min.js"></script>
    <script src="%(STATIC_DIR)s/js/bootstrap-select.js"></script>
    <script src="%(STATIC_DIR)s/js/bootstrap-switch.js"></script>
	-->
	<script src="//netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <script src="%(STATIC_DIR)s/js/flatui-checkbox.js"></script>
    <script src="%(STATIC_DIR)s/js/flatui-radio.js"></script>
    <script src="%(STATIC_DIR)s/js/jquery.tagsinput.js"></script>
    <script src="%(STATIC_DIR)s/js/jquery.placeholder.js"></script>
    <script src="%(STATIC_DIR)s/js/jquery.stacktable.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-scrollTo/1.4.11/jquery.scrollTo.min.js"></script>
	
		<script type="text/javascript">
	$(function() {
  		$("button.testers").click(function(event) {
			form_s = $("form#interested").serialize();
			event.preventDefault();
			$(this).parent().find('input,textarea').prop('disabled', true);
			$(this).prop('disabled', true);
	$.get("fastapp/tumbo-landingpage/exec/send_mail/", form_s, function(data) {
			console.log(data);
			msg = '<div class="col-md-6 col-md-offset-3" style="margin-top: 20px"><div class="alert alert-success"><strong>Thank you '+data['?name']+'! </strong> We will contact you when the platform is ready. Please be patient!</div></div>';
			$($("div#interested")[0]).after(msg);
			});
		});
		
		$("ul.nav, ul.bottom-links").on('click', 'li a', function() {
		
			var $clickedAnchor = $(this),
			  	$panelToScrollTo = $("#" + $clickedAnchor.data('loc'));
			console.log($($panelToScrollTo[0]));
			$.scrollTo($panelToScrollTo[0], 800);
		});
		
	});
	</script>
	
	<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-26689283-3', 'apy.io');
  ga('send', 'pageview');

</script>
  </body>
</html>""" % self.settings
	return self.responses.HTMLResponse(template)