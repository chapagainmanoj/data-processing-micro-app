Docker<!doctype html><!-- start coded_template: id:4381928064 path:generated_layouts/4381928059.html --><!--[if lt IE 7]> <html class="no-js lt-ie9 lt-ie8 lt-ie7" lang="en" > <![endif]--><!--[if IE 7]>    <html class="no-js lt-ie9 lt-ie8" lang="en" >        <![endif]--><!--[if IE 8]>    <html class="no-js lt-ie9" lang="en" >               <![endif]--><!--[if gt IE 8]><!--><html class="no-js" lang="en"><!--<![endif]--><head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="author" content="Quid">
    <meta name="description" content="">
    <title>Docker Labs</title>
    <link rel="shortcut icon" href="http://go.quid.com/hubfs/Favicon-1.png?t=1505946174087">

    <script src="//static.hsstatic.net/jquery-libs/static-1.4/jquery/jquery-1.11.2.js"></script>
    <script type="text/javascript">hsjQuery = window['jQuery']</script>
    <link href="//static.hsstatic.net/content_shared_assets/static-1.4047/css/public_common.css" rel="stylesheet">

<!-- /Added by GoogleAnalytics integration -->



    <!--[if lt IE 9]>
    <script src="https://static.hsstatic.net/content_shared_assets/static-1.4047/js/css3-mediaqueries.js"></script>
    <![endif]-->
    <meta name="viewport" content="width=device-width, initial-scale=1">
<link href="//cdn2.hubspot.net/hub/-1/hub_generated/template_assets/1495141902003/hubspot_default/shared/responsive/layout.min.css" rel="stylesheet">


    <!-- The style tag has been deprecated. Attached stylesheets are included in the required_head_tags page variable. -->
    <!--[if lte IE 8]>
<script charset="utf-8" type="text/javascript" src="//js.hsforms.net/forms/v2-legacy.js"></script>
<![endif]-->
<script charset="utf-8" type="text/javascript" src="//js.hsforms.net/forms/v2.js"></script>
<link href="//fonts.googleapis.com/css?family=Roboto:300,400" rel="stylesheet">
<link href="//cdnjs.cloudflare.com/ajax/libs/select2/4.0.3/css/select2.min.css" rel="stylesheet" />
<style type="text/css">
  @font-face{font-family:'Futura-Heavy';src:url(http://go.quid.com/hubfs/fonts/Futura_Std_Heavy/Futura-Std-Heavy.woff?t=1478892595119) format('woff')}@font-face{font-family:'Futura-Medium';src:url(http://go.quid.com/hubfs/fonts/Futura_Std_Medium/Futura-Std-Medium.woff?t=1478892595119) format('woff')}@font-face{font-family:'Futura-Book';src:url(http://go.quid.com/hubfs/fonts/Futura_Std_Book/Futura-Std-Book.woff?t=1478892595119) format('woff')}@font-face{font-family:'Baskerville';src:url(http://go.quid.com/hubfs/fonts/Baskerville/Baskerville-Regular-webfont.woff?t=1478892595119) format('woff')}.clearfix:before,.clearfix:after{content:'\0020';display:block;overflow:hidden;visibility:hidden;width:0;height:0}.clearfix:after{clear:both}.clearfix{zoom:1}*,*::before,*::after{box-sizing:border-box}img{height:auto;max-width:100%}html,body{font-family:'Futura-Heavy';background:#252525;margin:0;letter-spacing:.05em}.row-fluid [class*="span"]{min-height:0 !important}.header-container,.form-layer-container{background-color:#1c1c1c;background-size:cover;background-position:50% 100%;padding-bottom:20px}#Header{border-bottom:2px solid #616161;margin:0 auto;max-width:1180px;padding:28px 10px 12px}#Header .site-id{float:left}#Header .site-address{float:right}#Header .site-address a{color:#fff;display:inline-block;font-size:13px;margin-top:22px;text-transform:uppercase;text-decoration:none}#Mast,#FormLayer{margin:0 auto;max-width:1180px;padding:28px 10px 70px}#Mast,#FormLayer.bottom-border{border-bottom:1px solid #616161}#Mast h1,#FormLayer h1{color:#1ed7d1;font-size:70px;letter-spacing:10px;line-height:75px;text-align:center}#Mast h3,#FormLayer h3{color:#e6e6e6;font-family:'Baskerville';font-size:28px;font-weight:normal;line-height:40px;margin-top:0}#Mast p,#FormLayer p{color:#e6e6e6;font-family:'Baskerville';font-size:28px;font-weight:normal;line-height:40px;margin-top:0}#Mast .mast-content,#FormLayer .layer-content{float:left;width:65%}#Mast .mast-content p:last-of-type,#FormLayer .layer-content p:last-of-type{margin-bottom:0}#Mast .mast-right-content,#FormLayer .layer-right-content{float:right;width:32%}#Mast .mast-form,#FormLayer .form-layer-form{width:100%}#Mast .mast-footer,#FormLayer .layer-footer{clear:both;padding-top:20px}#Mast .mast-footer p:last-of-type,#FormLayer .layer-footer p:last-of-type{margin-bottom:0}#Mast .mast-form .form-container,#FormLayer .form-layer-form .form-container{background:#1ed7d1;border-radius:5px;padding:20px 40px}#Mast .mast-form h4,#FormLayer .form-layer-form h4{color:#252525;font-size:28px;font-weight:normal;line-height:32px;margin:0 0 14px;text-align:center;text-transform:uppercase}#Mast .mast-form .field label,#Mast .mast-form .field>label,#FormLayer .form-layer-form .field label,#FormLayer .form-layer-form .field>label{color:#252525;display:none}#Mast .mast-form .hs-form .hs-error-msgs,#FormLayer .form-layer-form .hs-form .hs-error-msgs{padding-top:10px}#Mast .mast-form .hs-form .hs-error-msgs label,#FormLayer .form-layer-form .hs-form .hs-error-msgs label{color:#ff64a6;display:block}#Mast .mast-form .hs-form .hs-error-msgs li,#FormLayer .form-layer-form .hs-form .hs-error-msgs li{margin-bottom:10px;margin-left:0;margin-right:0}#Mast .mast-form input,#Mast .mast-form select,#FormLayer .form-layer-form input,#FormLayer .form-layer-form select{border:2px solid #fff;border-radius:5px;box-shadow:none;box-sizing:border-box;color:#252525;font-family:'Futura-Book';font-size:16px;font-weight:normal;height:auto;padding:13px 20px;width:100%}#Mast .mast-form input.error,#Mast .mast-form input.invalid,#FormLayer .form-layer-form input.error,#FormLayer .form-layer-form input.invalid{border:2px solid #ff64a6;color:#ff64a6}#Mast .mast-form .hs-form.stacked .field,#FormLayer .form-layer-form .hs-form.stacked .field{margin-bottom:6px}#Mast .mast-form select,#FormLayer .form-layer-form select{-webkit-appearance:none;-moz-appearance:none;appearance:none;background:#fff url("http://quid.com/assets/down-arrow.svg") no-repeat scroll 92% center}#Mast .mast-form .hs-form label,#FormLayer .form-layer-form .hs-form label{color:#252525;font-weight:normal}#Mast .mast-form .hs_submit,#FormLayer .form-layer-form .hs_submit{margin-top:13px}#Mast .mast-form input.hs-button,#FormLayer .form-layer-form input.hs-button{background-size:200% 100%;background-image:linear-gradient(to left,#fff 50%,#252525 50%);border:0;color:#fff;display:block;font-size:13px;max-width:500px;padding:17px 20px;text-align:center;text-transform:uppercase;text-shadow:none;width:100%;white-space:normal}#Mast .mast-form input.hs-button:hover,#FormLayer .form-layer-form input.hs-button:hover{background-position:-100% 0;color:#252525}#Mast .mast-form .hs-form.stacked .actions,#FormLayer .form-layer-form .hs-form.stacked .actions{margin:0;padding:0}#Mast .mast-form .hs-form .checkbox-field-container label,#FormLayer .form-layer-form .checkbox-field-container label{display:block}#Mast .mast-form .hs-form .checkbox-field-container .hs-error-msgs,#FormLayer .form-layer-form .checkbox-field-container .hs-error-msgs{padding:0}#Mast .mast-form .hs-form .checkbox-field-container .hs-error-msgs li,#FormLayer .form-layer-form .checkbox-field-container .hs-error-msgs li{margin-left:0}#Mast .mast-form .hs-form li.hs-form-checkbox,#FormLayer .form-layer-form li.hs-form-checkbox{margin-bottom:10px;margin-left:0}#Mast .mast-form .hs-form li.hs-form-checkbox label,#FormLayer .form-layer-form li.hs-form-checkbox label{display:block}#Mast .mast-form .hs-form li.hs-form-checkbox input,#FormLayer .form-layer-form li.hs-form-checkbox input{float:left;width:7% !important}#Mast .mast-form .hs-form li.hs-form-checkbox input,#FormLayer .form-layer-form li.hs-form-checkbox input{float:left;padding-left:2%;width:91%}.layer{background:#1c1c1c;padding-top:100px}.layer .container{margin:0 auto;max-width:1180px;padding:0 10px 100px}.layer .bottom-border{border-bottom:1px solid #616161}.layer .two-col .column{width:45%}.layer .two-col .column.first{float:left}.layer .two-col .column.last{float:right}.layer h2{color:#1ed7d1;font-size:36px;font-weight:normal;letter-spacing:2.3px;line-height:43px;margin:0 0 12px;text-transform:uppercase}.layer p{color:#e6e6e6;font-family:'Baskerville';font-size:28px;line-height:34px;margin-top:0}ul{padding:20px 0 0 0;margin:0}ul li{color:#e6e6e6;font-family:'Baskerville';font-size:28px;line-height:34px;margin-bottom:20px;margin-left:45px}ul.checkmark li{background:url(http://go.quid.com/hubfs/images/landing-page/checkmark.png?t=1478892595119) no-repeat 0 5px;list-style-type:none;margin-left:0;padding-left:45px}.quote-layer{background:url(http://go.quid.com/hubfs/images/landing-page/quote-layer-bg.jpg?t=1478892595119) no-repeat 50% 0;background-size:cover}.quote-layer .container{text-align:center}.quote-layer .quote{color:#252525;display:block;font-family:'Baskerville';font-size:48px;line-height:59px;padding-top:20px}.quote-layer cite{color:#252525;display:block;font-size:15px;font-style:normal;padding-bottom:20px;padding-top:36px;text-transform:uppercase}.centered-layer{text-align:center}.layer a.cta{background-size:200% 100%;background-image:linear-gradient(to left,#fff 50%,#1ed7d1 50%);border-radius:5px;color:#252525;display:inline-block;font-size:13px;font-family:'Futura-Heavy';letter-spacing:1.7px;line-height:17px;padding:20px 55px 17px;text-decoration:none;text-transform:uppercase;text-shadow:none}.layer a.cta:hover{background-position:-100% 0}.footer-container{border-top:1px solid #616161}.footer{max-width:1180px;margin:0 auto;padding:35px 10px}.footer__links-wrapper{display:flex;justify-content:space-between;margin-bottom:12px}.footer__links,.footer__social{display:inline-block;list-style:outside none none;margin:0;padding:0}.footer__links li{margin:0 13px}.footer__links li,.footer__social li{display:inline-block;position:relative}.footer__social li{display:inline-block;margin-left:21px}.footer__links li:first-child,.footer__social li:first-child{margin-left:0}.footer__links li:nth-of-type(3){margin-right:26px}.footer__links li:nth-of-type(3)::after{background:#959595 none repeat scroll 0 0;content:"";height:9px;position:absolute;right:-32px;top:50%;transform:translateY(-50%);width:2px}.footer__links li:nth-of-type(4){margin-left:26px}.link-one{color:#959595;text-transform:uppercase}.link{text-decoration:none}.link{font:12px/1 "Futura-Heavy";letter-spacing:1.7px}.link:hover{color:#fff}.footer__social li svg path,.footer__social li svg polygon{transition:fill .2s}.footer__social li svg:hover path,.footer__social li svg:hover polygon{fill:white}.footer__copy-right,.footer__trademark{color:#959595;font:12px/1 "Futura-Medium";margin:0}.footer__trademark{margin:10px 0 0}@media(max-width:1020px) and (min-width:881px){.footer__links li{margin:0 5px}.footer__links li:nth-of-type(3){margin-right:5px}.footer__links li:nth-of-type(3)::after{display:none}.footer__links li:nth-of-type(4){margin-left:5px}.footer__social li{margin-left:10px}.footer__social li.footer__social-facebook{margin-left:4px}}@media(max-width:880px){.footer__links-wrapper,.footer__links,.footer__social{display:block;width:100%}.footer__social{margin-top:12px}}@media(max-width:768px){#Mast .mast-content,#Mast .mast-right-content,#FormLayer .layer-content,#FormLayer .layer-right-content{float:none;width:100%}div.input{text-align:center}#Mast h1,#FormLayer h1{font-size:50px;line-height:55px}#Mast .mast-form input.hs-button,#FormLayer .form-layer-form input.hs-button{margin:0 auto}.mast-content h3,.mast-content p,.mast-right-content,.mast-footer,#FormLayer .layer-content h3,#FormLayer .layer-content p,#FormLayer .layer-right-content,#FormLayer .layer-footer{text-align:center}.layer .two-col .column{float:none !important;width:100% !important;text-align:center}ul,ul.checkmark{margin:0 auto;text-align:left;width:70%}.footer__links,.footer__social,.footer__copy-right,.footer__trademark{text-align:center}.footer__links li{margin:0 !important;width:100%}.footer__links li:nth-of-type(3)::after{display:none}#submitbutton{letter-spacing:normal}}@media(max-width:480px){#Mast h1,#Mast h1{font-size:34px;line-height:39px}#Mast h3,#FormLayer h3{font-size:28px;line-height:32px}#Mast .mast-form h4,#FormLayer .form-layer-form h4{font-size:24px;line-height:28px}.layer{padding-top:50px}.layer .container{padding-bottom:50px}.layer h2{font-size:28px;line-height:32px}.layer p{font-size:24px;line-height:30px}ul,ul.checkmark{width:100%}ul li{font-size:24px;line-height:30px}ul.checkmark li{background:url(http://go.quid.com/hubfs/images/landing-page/checkmark.png?t=1478892595119) no-repeat 0 2px}}.embed-container,.hs-responsive-embed{position:relative;padding-bottom:56.25%;height:0;overflow:hidden;max-width:100%;height:auto}.embed-container iframe,.embed-container object,.embed-container embed,.hs-responsive-embed iframe,.hs-responsive-embed object,.hs-responsive-embed embed{position:absolute;top:0;left:0;width:100%;height:100%}
</style>
<style>
.process-btn{
  padding: 10px 50px;
  background: #1ed7d1;
  font-family: 'Roboto', sans-serif;
  font-size: 18px;
  color: #FFF;
  margin-top: 20px;
  border: 0px;
  cursor: pointer;
  border-radius: 5px;
  float: right;
}
.select2-container{
  width: 100% !important;
  max-width: 1180px !important;
  font-size: 18px;
}
.select2-results ul li{
  margin-left: 0px;
  margin-bottom: 0px;
  font-size: 16px;
  padding: 5px 20px;
  background: #fff !important;
  color: #747474 !important;
}
.select2-container--default .select2-selection--single{
  padding: 12px 10px;
    height: 48px;
}
.select2-container--default .select2-selection--single .select2-selection__arrow{
  height: 48px;
  right: 10px;
}
.quid-wrap{
  color: white;
  font-family: 'Roboto', sans-serif !important;
}
.quid-wrap h3{
  margin: 0px;
  padding: 10px 0px;
}
.quid-wrap .quid-item{
  background: #333;
  padding: 15px 15px 10px;
  margin-bottom: 10px;
}
.quid-wrap .quid-item:hover{
  background: #444;
  cursor: pointer;
}
.quid-wrap .quid-item.active{
  background: #222;
  cursor: default;
  border: solid 1px #444;
}
.quid-wrap .quid-item h4{
  font-family: 'Roboto', sans-serif;
  margin: 0px;
}
.quid-wrap .quid-item p{
    font-size: 14px !important;
    font-family: 'Roboto', sans-serif !important;
    line-height: 18px !important;
    margin: 0px;
    margin-bottom: 10px;
}
.quid-wrap .quid-item p a{
  color: white;
}

/*Check*/

.quid-item{
  color: #AAAAAA;
  display: block;
  position: relative;
  float: left;
  width: 100%;
  border-bottom: 1px solid #333;
}

.quid-item input[type=radio]{
  position: absolute;
  visibility: hidden;
}

.quid-item label{
  display: block;
  position: relative;
  font-weight: 300;
  padding: 0px 0px 0px 50px;
  margin: 10px auto;
  z-index: 9;
  cursor: pointer;
  -webkit-transition: all 0.25s linear;
}

.quid-item:hover label{
  color: #FFFFFF;
}

.quid-item .check{
  display: block;
  position: absolute;
  border: 5px solid #AAAAAA;
  border-radius: 100%;
  height: 25px;
  width: 25px;
  top: 30px;
  left: 20px;
  z-index: 5;
  transition: border .25s linear;
  -webkit-transition: border .25s linear;
}

.quid-item:hover .check {
  border: 5px solid #FFFFFF;
}

.quid-item .check::before {
  display: block;
  position: absolute;
  content: '';
  border-radius: 100%;
  height: 10px;
  width: 10px;
  top: 3px;
  left: 3px;
  margin: auto;
  transition: background 0.25s linear;
  -webkit-transition: background 0.25s linear;
}

input[type=radio]:checked ~ .check {
  border: 5px solid #0DFF92;
}

input[type=radio]:checked ~ .check::before{
  background: #0DFF92;
}

input[type=radio]:checked ~ label{
  color: #0DFF92;
}
.file-upload{
  background: #444;
  display: inline-block;
  width: 100%;
}
.inputfile{
  display: inline-block;
  width: 100%;
  padding: 20px 30px;
  border: dotted 2px #666;
}
</style>


</head>
<body class="   hs-content-id-5253337811 hs-landing-page hs-page " style="">
    <div class="header-container-wrapper">
    <div class="header-container container-fluid">

<div class="row-fluid-wrapper row-depth-1 row-number-1 ">
<div class="row-fluid ">
<div class="span12 widget-span widget-type-custom_widget " style="" data-widget-type="custom_widget" data-x="0" data-w="12">
<div class="cell-wrapper layout-widget-wrapper">
<span id="hs_cos_wrapper_module_14721572480401357" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_custom_widget" style="" data-hs-cos-general-type="widget" data-hs-cos-type="custom_widget">
    <div class="header-container" style="">

        <div id="Header" class="clearfix">
          <div class="site-id">
            <a href="http://docker.com/"><img src="https://pbs.twimg.com/profile_images/862037907862765568/pYgBswUk.jpg" alt="Docker"></a>
          </div>
        </div> <!-- #Header -->

        <div id="Mast" class="clearfix">
          <h1>Docker LABS</h1>
          <hr>
              <div class="quid-wrap">
                <!--h3>Step 1: Choose Script</h3 !-->
                <!-- %for item in menu: -->
                <form class="" id="id" action="/" method="post" enctype="multipart/form-data">
                <div class="quid-item">
                    <h2>Bla</h2>
                </div>
              </form>
              <!-- %end -->
                <!--div class="second-option">
                  <h3>Step 2: Choose Input File</h3>
                  <div class="file-upload">
                    <label> default Input
                    <input type="file" name="data" id="file1" class="inputfile" placeholder="Input 1" required="" />
                  </label>
                  </div>
                </div-->

        </div> <!-- #Mast -->
    </div> <!-- .header-container -->
    <script type="text/javascript">
      $(document).ready(function() {
        setTimeout(function() {
          $('li.hs-form-checkbox').each(function() {
            $(this).parent().parent().parent().addClass('checkbox-field-container');
          });
        }, 1000);
      });
    </script>
    </span></div><!--end layout-widget-wrapper -->
</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

    </div><!--end header -->
</div><!--end header wrapper -->

<div class="body-container-wrapper">
    <div class="body-container container-fluid">


    </div><!--end body -->
</div><!--end body wrapper -->


<script type="text/javascript" src="//static.hsstatic.net/content_shared_assets/static-1.4047/js/public_common.js"></script>

<script src="//cdnjs.cloudflare.com/ajax/libs/select2/4.0.3/js/select2.min.js"></script>
<script type="text/javascript">
    $("select").select2({
      minimumResultsForSearch: Infinity
    });
    function submit_run(id) {
      x = document.getElementById(id);
      x.submit();
    }
</script>





    <!-- Generated by the HubSpot Template Builder - template version 1.03 -->
<!-- Editor Styles -->
<style id="hs_editor_style" type="text/css">
#hs_cos_wrapper_module_14721572480401357  { margin-left: 12px !important; margin-right: 12px !important; margin-bottom: 12px !important; margin-top: 12px !important; display: block !important }

</style>

<!-- end coded_template: id:4381928064 path:generated_layouts/4381928059.html -->
</body></html>
