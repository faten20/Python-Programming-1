#!/usr/bin/env python
# coding: utf-8

# In[5]:


import requests 
from bs4 import BeautifulSoup 
  
URL = " https://scratch.mit.edu/studios/1817151/  "
a = requests.get(URL) 
  
soup = BeautifulSoup(a.content) # If this line causes an error, run 'pip install html5lib' or install html5lib 
print(soup.prettify())


# In[6]:


#find the title from a given html document.
from bs4 import BeautifulSoup
html_doc = """
<!DOCTYPE html>
<html>
 <head>
  <meta content="IE=Edge" http-equiv="X-UA-Compatible"/>
  <meta content="m_3TAXDreGTFyoYnEmU9mcKB4Xtw5mw6yRkuJtXRKxM" name="google-site-verification"/>
  <title>
   Scratch - Imagine, Program, Share
  </title>
  <link href="//cdn.scratch.mit.edu/scratchr2/static/__ad0074bbd02c73bcc1e3fe1856f1e8b0__/vendor/redmond/jquery.ui.all.css" rel="stylesheet"/>
  <link href="//cdn.scratch.mit.edu/scratchr2/static/__ad0074bbd02c73bcc1e3fe1856f1e8b0__/css/main.css" rel="stylesheet" type="text/css"/>
  <link href="//cdn.scratch.mit.edu/scratchr2/static/__ad0074bbd02c73bcc1e3fe1856f1e8b0__//css/handheld.css" media="handheld, only screen and (max-device-width:480px)" rel="stylesheet"/>
  <link href="//cdn.scratch.mit.edu/scratchr2/static/__ad0074bbd02c73bcc1e3fe1856f1e8b0__/css/pages/http-errors.css" rel="stylesheet"/>
  <script src="//cdn.scratch.mit.edu/scratchr2/static/__ad0074bbd02c73bcc1e3fe1856f1e8b0__//js/jquery.min.js" type="text/javascript">
  </script>
  <script src="//cdn.scratch.mit.edu/scratchr2/static/__ad0074bbd02c73bcc1e3fe1856f1e8b0__/js/lib/underscore-min.js" type="text/javascript">
  </script>
  <script>
   window.console||(window.console={log:$.noop,error:$.noop,debug:$.noop}); // ensure console fails gracefully when missing
      // define _gaq here to log errors with GA. ga.js script gets loaded furthe down
      var sessionCookieName = 'scratchsessionsid';
      var _gaq = window._gaq || [];
      _gaq.push(['_setAccount', 'UA-30688952-1']);
      _gaq.push(['_setSampleRate', '10']);
      _gaq.push(['_trackPageview']);
  </script>
  <script type="text/javascript">
   function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }

        function setCookie(name, value, days) {
            var expires;

            if (days) {
                var date = new Date();
                date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
                expires = "; expires=" + date.toGMTString();
            } else {
                expires = "";
            }
            document.cookie = escape(name) + "=" + escape(value) + expires + "; path=/";
        }
  </script>
  <script>
   var Scratch = Scratch || {};
Scratch.INIT_DATA = Scratch.INIT_DATA || {};



Scratch.INIT_DATA.ADMIN = false;
Scratch.INIT_DATA.LOGGED_IN_USER = {
  
  options: {
    
    
  }
};
Scratch.INIT_DATA.comment_posting = true;

Scratch.INIT_DATA.BROWSERS_SUPPORTED = {

  chrome: 35,
  firefox: 31,
  msie: 8,
  safari: 7
};

Scratch.INIT_DATA.TEMPLATE_CUES = {

  unsupported_browser: true,
  welcome: true,
  confirmed_email: false
};







Scratch.INIT_DATA.IS_IP_BANNED = false;

Scratch.INIT_DATA.GLOBAL_URLS = {
  'media_url': '//uploads.scratch.mit.edu/',
  'static_url': '//cdn.scratch.mit.edu/scratchr2/static/__ad0074bbd02c73bcc1e3fe1856f1e8b0__/',
  'static_path': '/scratchr2/static/__ad0074bbd02c73bcc1e3fe1856f1e8b0__/'
}

Scratch.INIT_DATA.IS_SOCIAL = false;
  </script>
  <meta content="website" property="og:type"/>
  <meta content="Make games, stories and interactive art with Scratch. (scratch.mit.edu)" property="og:description"/>
  <meta content="Scratch - Imagine, Program, Share" property="og:title"/>
  <meta content="https://scratch.mit.edu/studios/1817151/%20%20" property="og:url"/>
 </head>
 <body class="">
  <!--[if lte IE 8]>
  <div class="unsupported-browser banner" data-cue="unsupported_browser">
    <div class="container">
      <span>Scratch supports Internet Explorer 9+. We suggest you upgrade to <a href="/info/faq/#requirements">a supported browser</a>, <a href="/scratch2download/">download the offline editor</a>, or <a href="https://en.scratch-wiki.info/wiki/List_of_Bug_Workarounds">read about common workarounds</a>.</span>
    </div>
  </div>
  <![endif]-->
  <div id="pagewrapper">
   <div id="topnav">
    <div class="innerwrap">
     <div class="container">
      <a class="logo" href="/">
       <span class="scratch">
       </span>
      </a>
      <ul class="site-nav">
       <li>
        <a href="/projects/editor/?tip_bar=home" id="project-create">
         Create
        </a>
       </li>
       <li>
        <a href="/explore/projects/all">
         Explore
        </a>
       </li>
       <li>
        <a href="/ideas">
         Ideas
        </a>
       </li>
       <li class="last">
        <a href="/about/">
         About
        </a>
       </li>
      </ul>
      <form action="/search/projects" class="search" method="get">
       <input class="glass" type="submit" value=""/>
       <input id="search-input" name="q" placeholder="Search" type="text"/>
      </form>
      <ul class="account-nav">
      </ul>
      <script id="template-account-nav-logged-out" type="text/template">
       <ul class="account-nav" >
              <li class="join-scratch"><a href="/join">Join Scratch</a></li><li id="login-dropdown" class="sign-in dropdown"><span data-toggle="dropdown" class="dropdown-toggle"><span>Sign in</span></span><div class="popover bottom dropdown-menu"><div class="arrow"></div><div class="popover-content" ><form method="post" id="login" action="#"><label for="username">Username</label><input type="text" id="login_dropdown_username" name="username" maxlength="30" class="wide username" /><label for="password" class="password">Password</label><input type="password" name="password" class="wide password" /><div class="ajax-loader" style="display:none; float: left;"></div><button type="submit">Sign in</button><span class="forgot-password"><a href="/accounts/password_reset/">Need help?</a></span><div class="error"></div></form></div></div></li><li data-control="modal-login" class="sign-in mobile"><span>Sign in</span></li>
          </ul>
      </script>
      <script id="template-account-nav-logged-in" type="text/template">
       <ul class="account-nav logged-in"><li class="messages"><a title="messages - updates and notices" href="/messages" class="messages-icon"><span class="notificationsCount none">0</span></a></li><li class="my-stuff"><a title="my stuff - manage projects and studios" href="/mystuff/" class="mystuff-icon"></a></li><li class="logged-in-user dropdown"><span class="user-name dropdown-toggle" data-toggle="dropdown"><img class="user-icon" src="<%- LOGGED_IN_USER.model.thumbnail_url %>" width="24" height="24"><%- LOGGED_IN_USER.model.username_truncated %><span class="caret"></span></span><div class="dropdown-menu blue" ><ul class="user-nav"><li><a href="<%- LOGGED_IN_USER.model.profile_url %>">Profile</a></li><li><a href="/mystuff/">My Stuff</a></li><% if (LOGGED_IN_USER.model.is_educator){ %><li><a href="/educators/classes/">My Classes</a></li><% } %><% if (LOGGED_IN_USER.model.is_student){ %><li><a href="/classes/<%- LOGGED_IN_USER.model.classroom_id %>/">My Class</a></li><% } %><li><a href="/accounts/settings/">Account settings</a></li><li id="logout" class="logout divider"><form method="post" action="/accounts/logout/"><input type='hidden' name='csrfmiddlewaretoken' value='JRTIagjqHCyRPqxlPlWpq7FhpsWtRdaH' /><input type="submit" value="Sign out"></form></li></ul></div></li></ul>
      </script>
      <script src="//cdn.scratch.mit.edu/scratchr2/static/__ad0074bbd02c73bcc1e3fe1856f1e8b0__/js/account-nav.js" type="text/javascript">
      </script>
     </div>
     <iframe class="iframeshim" frameborder="0" scrolling="no">
      &lt;html&gt;&lt;head&gt;&lt;/head&gt;&lt;body&gt;&lt;/body&gt;&lt;/html&gt;
     </iframe>
    </div>
    <!-- innerwrap -->
   </div>
   <div class="confirm-email banner" data-cue="confirmed_email" style="display:none;">
    <div class="container">
     <span>
      <a href="#" id="confirm-email-popup">
       Confirm your email
      </a>
      to enable sharing.
      <a href="/help/faq/#accounts">
       Having trouble?
      </a>
     </span>
     <div class="close">
      x
     </div>
    </div>
   </div>
   <div class="email-outage banner" style="display:none; background-color:#FF661A;">
    <div class="container">
     <span>
      We are experiencing a disruption with email delivery. If you are not receiving emails from us, please try after 8am EST.
     </span>
     <div class="close">
      x
     </div>
    </div>
   </div>
   <div class="container" id="content">
    <div id="alert-view">
    </div>
    <!-- templates/404.html block main-content -->
    <div class="box" id="page-404">
     <div class="box-head">
     </div>
     <div class="box-content">
      <img src="//cdn.scratch.mit.edu/scratchr2/static/__ad0074bbd02c73bcc1e3fe1856f1e8b0__/images/404-giga.png" style="margin:20px;padding: 10px;"/>
      <div class="box-header">
       <h1>
        Whoops! Our server is Scratch'ing its head
       </h1>
      </div>
      <p>
       We couldn't find the page you're looking for. Check to make sure you've typed the url correctly.
       <br/>
       You can try searching for what you're looking for here:
      </p>
      <form action="/search/projects" class="search" method="get">
       <span class="glass">
        <i>
        </i>
       </span>
       <input name="q" placeholder="Search" type="text"/>
      </form>
      <p>
      </p>
      <h3 class="status-code">
       404
      </h3>
     </div>
    </div>
    <!-- end block main-content -->
   </div>
  </div>
  <div id="footer">
   <div class="container">
    <style>
     #footer ul.footer-col li {
            list-style-type:none;
            display: inline-block;
            width: 184px;
            text-align: left;
            vertical-align: top;
          }

          #footer ul.footer-col li h4 {
            font-weight: bold;
            font-size: 14px;
            color: #666;
          }
    </style>
    <ul class="clearfix footer-col">
     <li>
      <h4>
       About
      </h4>
      <ul>
       <li>
        <a href="/about/">
         About Scratch
        </a>
       </li>
       <li>
        <a href="/parents/">
         For Parents
        </a>
       </li>
       <li>
        <a href="/educators/">
         For Educators
        </a>
       </li>
       <li>
        <a href="/developers">
         For Developers
        </a>
       </li>
       <li>
        <a href="/info/credits/">
         Credits
        </a>
       </li>
       <li>
        <a href="/jobs/">
         Jobs
        </a>
       </li>
       <li>
        <a href="https://www.scratchfoundation.org/media-kit/">
         Press
        </a>
       </li>
      </ul>
     </li>
     <li>
      <h4>
       Community
      </h4>
      <ul>
       <li>
        <a href="/community_guidelines/">
         Community Guidelines
        </a>
       </li>
       <li>
        <a href="/discuss/">
         Discussion Forums
        </a>
       </li>
       <li>
        <a href="http://wiki.scratch.mit.edu/">
         Scratch Wiki
        </a>
       </li>
       <li>
        <a href="/statistics/">
         Statistics
        </a>
       </li>
      </ul>
     </li>
     <li>
      <h4>
       Support
      </h4>
      <ul>
       <li>
        <a href="/ideas">
         Ideas
        </a>
       </li>
       <li>
        <a href="/info/faq/">
         FAQ
        </a>
       </li>
       <li>
        <a href="/download">
         Offline Editor
        </a>
       </li>
       <li>
        <a href="/contact-us/">
         Contact Us
        </a>
       </li>
       <li>
        <a href="/store">
         Scratch Store
        </a>
       </li>
       <li>
        <a href="https://secure.donationpay.org/scratchfoundation/">
         Donate
        </a>
       </li>
      </ul>
     </li>
     <li>
      <h4>
       Legal
      </h4>
      <ul>
       <li>
        <a href="/terms_of_use/">
         Terms of Use
        </a>
       </li>
       <li>
        <a href="/privacy_policy/">
         Privacy Policy
        </a>
       </li>
       <li>
        <a href="/DMCA/">
         DMCA
        </a>
       </li>
      </ul>
     </li>
     <li>
      <h4>
       Scratch Family
      </h4>
      <ul>
       <li>
        <a href="http://scratched.gse.harvard.edu/">
         ScratchEd
        </a>
       </li>
       <li>
        <a href="http://www.scratchjr.org/">
         ScratchJr
        </a>
       </li>
       <li>
        <a href="http://day.scratch.mit.edu/">
         Scratch Day
        </a>
       </li>
       <li>
        <a href="/conference/">
         Scratch Conference
        </a>
       </li>
       <li>
        <a href="http://www.scratchfoundation.org/">
         Scratch Foundation
        </a>
       </li>
      </ul>
     </li>
    </ul>
    <ul class="clearfix" id="footer-menu">
     <li>
      <form action="/i18n/setlang/" id="lang-dropdown" method="post">
       <select id="language-selection" name="language">
        <option value="ab">
         Аҧсшәа
        </option>
        <option value="ar">
         العربية
        </option>
        <option value="am">
         አማርኛ
        </option>
        <option value="az">
         Azeri
        </option>
        <option value="id">
         Bahasa Indonesia
        </option>
        <option value="be">
         Беларуская
        </option>
        <option value="bg">
         Български
        </option>
        <option value="ca">
         Català
        </option>
        <option value="cs">
         Česky
        </option>
        <option value="cy">
         Cymraeg
        </option>
        <option value="da">
         Dansk
        </option>
        <option value="de">
         Deutsch
        </option>
        <option value="et">
         Eesti
        </option>
        <option value="el">
         Ελληνικά
        </option>
        <option selected="" value="en">
         English
        </option>
        <option value="es">
         Español
        </option>
        <option value="es-419">
         Español Latinoamericano
        </option>
        <option value="eu">
         Euskara
        </option>
        <option value="fa">
         فارسی
        </option>
        <option value="fr">
         Français
        </option>
        <option value="ga">
         Gaeilge
        </option>
        <option value="gd">
         Gàidhlig
        </option>
        <option value="gl">
         Galego
        </option>
        <option value="ko">
         한국어
        </option>
        <option value="hy">
         Հայերեն
        </option>
        <option value="he">
         עִבְרִית
        </option>
        <option value="hr">
         Hrvatski
        </option>
        <option value="zu">
         isiZulu
        </option>
        <option value="is">
         Íslenska
        </option>
        <option value="it">
         Italiano
        </option>
        <option value="ka">
         ქართული ენა
        </option>
        <option value="sw">
         Kiswahili
        </option>
        <option value="ht">
         Kreyòl ayisyen
        </option>
        <option value="ku">
         Kurdî
        </option>
        <option value="ckb">
         کوردیی ناوەندی
        </option>
        <option value="lv">
         Latviešu
        </option>
        <option value="lt">
         Lietuvių
        </option>
        <option value="hu">
         Magyar
        </option>
        <option value="mi">
         Māori
        </option>
        <option value="mn">
         Монгол хэл
        </option>
        <option value="nl">
         Nederlands
        </option>
        <option value="ja">
         日本語
        </option>
        <option value="ja-Hira">
         にほんご
        </option>
        <option value="nb">
         Norsk Bokmål
        </option>
        <option value="nn">
         Norsk Nynorsk
        </option>
        <option value="uz">
         Oʻzbekcha
        </option>
        <option value="th">
         ไทย
        </option>
        <option value="km">
         ភាសាខ្មែរ
        </option>
        <option value="pl">
         Polski
        </option>
        <option value="pt">
         Português
        </option>
        <option value="pt-br">
         Português Brasileiro
        </option>
        <option value="rap">
         Rapa Nui
        </option>
        <option value="ro">
         Română
        </option>
        <option value="ru">
         Русский
        </option>
        <option value="sk">
         Slovenčina
        </option>
        <option value="sl">
         Slovenščina
        </option>
        <option value="sr">
         Српски
        </option>
        <option value="fi">
         Suomi
        </option>
        <option value="sv">
         Svenska
        </option>
        <option value="vi">
         Tiếng Việt
        </option>
        <option value="tr">
         Türkçe
        </option>
        <option value="uk">
         Українська
        </option>
        <option value="zh-cn">
         简体中文
        </option>
        <option value="zh-tw">
         繁體中文
        </option>
       </select>
      </form>
     </li>
    </ul>
   </div>
  </div>
  <!-- templates/modal-login.html block -->
  <div class="modal hide fade in" id="login-dialog" style="width: 450px">
   <form action="/login/" method="post">
    <fieldset>
     <div class="modal-header">
      <a class="close" data-dismiss="modal" href="#">
       x
      </a>
      <h3>
       Sign in
      </h3>
     </div>
     <div class="modal-body">
      <div class="control-group">
       <label class="control-label" for="username">
        Username
       </label>
       <div class="controls">
        <input class="username" maxlength="30" name="username" type="text"/>
       </div>
      </div>
      <div class="control-group">
       <label class="control-label" for="password">
        Password
       </label>
       <div class="controls">
        <input class="password" name="password" type="password"/>
       </div>
      </div>
     </div>
     <div class="modal-footer">
      <span class="error">
      </span>
      <div class="buttons-right">
       <button class="button primary" type="submit">
        Sign in
       </button>
       <a data-control="registration">
        Or Join Scratch
       </a>
      </div>
     </div>
    </fieldset>
   </form>
   <iframe class="iframeshim" frameborder="0" scrolling="no">
    &lt;html&gt;&lt;head&gt;&lt;/head&gt;&lt;body&gt;&lt;/body&gt;&lt;/html&gt;
   </iframe>
  </div>
  <!-- end templates/modal-login.html -->
  <div class="registration modal hide fade" data-backdrop="static" id="registration">
   <iframe class="iframeshim" frameborder="0" scrolling="no">
    &lt;html&gt;&lt;head&gt;&lt;/head&gt;&lt;body&gt;&lt;/body&gt;&lt;/html&gt;
   </iframe>
  </div>
  <script src="//cdn.scratch.mit.edu/scratchr2/static/__ad0074bbd02c73bcc1e3fe1856f1e8b0__//js/jquery-ui.min.js" type="text/javascript">
  </script>
  <script charset="utf-8" src="//cdn.scratch.mit.edu/scratchr2/static/__ad0074bbd02c73bcc1e3fe1856f1e8b0__/js/main.js" type="text/javascript">
  </script>
  <script type="text/javascript">
   // load gaq script
    (function() {
      var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
      ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
      var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
    })();
  </script>
  <script charset="utf-8" src="//cdn.scratch.mit.edu/scratchr2/static/__ad0074bbd02c73bcc1e3fe1856f1e8b0__/js/base.js" type="text/javascript">
  </script>
  <script charset="utf-8" src="//cdn.scratch.mit.edu/scratchr2/static/__ad0074bbd02c73bcc1e3fe1856f1e8b0__/js/lazyload.js" type="text/javascript">
  </script>
  <script id="template-collection-count" type="text/template">
   <%- count %>
  </script>
  <script id="template-comment-actions" type="text/template">
   <% if (can_delete) { %>
  <% if (is_staff && comment_user == current_user) { %>
    <span data-control="delete" class="actions report">Delete</span>
  <% } else if (type != "gallery" || comment_user == current_user) { %>
    <span data-control="delete" class="actions report">Delete</span>
  <% } %>
<% } %>
<% if (current_user != comment_user) { %>
  <span data-control="report" class="actions report">
  <% if (student_of_educator) { %>
    Delete
  <% } else { %>
    Report
  <% } %></span>
<% } %>
  </script>
  <script id="template-modal-login" type="text/template">
   <div class="modal hide fade in" id="login-dialog" style="width: 450px">
  <form method="post" action="/login/">
    <fieldset>
      <div class="modal-header">
        <a href="#" data-dismiss="modal" class="close">x
        </a>
        <h3>Login</h3>
      </div>
      <div class="modal-body">
        <div class="control-group">
        <label class="control-label" for="username">Username
          </label>
          <div class="controls">
            <input id="username" type="text" name="username" maxlength="30" />
          </div>
        </div>
        <div class="control-group">
        <label class="control-label" for="password">Password
          </label>
          <div class="controls">
            <input type="password" name="password" id="password" />
          </div>
        </div>
      </div>
      <div class="modal-footer">
        <span class="error">
        </span>
        <span class="button primary" id="sign-in" data-control="site-login">
        <span>{% trans "Sign in" $}
          </span>
        </span>
      </div>
    </fieldset>
  </form>
</div>
  </script>
  <script id="template-comment-reply" type="text/template">
   <form>
    <div class="control-group tooltip right">
      <textarea name="content"></textarea>
      
      <span class="hovertext error" data-control="error" data-content="comment-error"><span class="arrow"></span><span class="text"></span></span>
      <span class="small-text">You have <span id="chars-left-<%- comment_id %>">500</span> characters left.</span>
    </div>
    <div class="control-group">
        <div class="button small" data-parent-thread="<%- thread_id %>" data-commentee-id="<%- commentee_id %>" data-control="modal-login"><a href="#null">Post</a></div>
        <div class="button small grey" data-control="cancel"><a href="#null">Cancel</a></div>
      <span class="notification"></span>
    </div>
  </form>
  </script>
  <script id="template-deletion-canceled" type="text/template">
   <div class="deletion-canceled">
  <div class="form">
    <p>
    Your account was scheduled for deletion but you logged in. Your account has been reactivated. If you didn’t request for your account to be deleted, you should <a href="/accounts/password_change/">change your password</a> to make sure your account is secure. 
    </p>
  </div>
</div>
  </script>
  <script id="template-unsupported-browser" type="text/template">
   <div class="unsupported-browser banner" data-cue="unsupported_browser">
    <div class="container">
      <span>Scratch works best on newer browsers. We suggest you upgrade to <a href="/info/faq/#requirements">a supported browser</a>, <a href="/scratch2download/">download the offline editor</a>, <a href="https://en.scratch-wiki.info/wiki/List_of_Bug_Workarounds">or read about common workarounds</a>.</span>
      <div class="close">x</div>
    </div>
  </div>
  </script>
  <script id="template-unsupported-msie" type="text/template">
   <div class="unsupported-browser banner" data-cue="unsupported_browser">
    <div class="container">
      <span>Scratch will stop supporting Internet Explorer 8 on April 30, 2015. We suggest you upgrade to <a href="/info/faq/#requirements">a supported browser</a>, <a href="/scratch2download/">download the offline editor</a>, or <a href="https://en.scratch-wiki.info/wiki/List_of_Bug_Workarounds">read about common workarounds</a>.</span>
      <div class="close">x</div>
    </div>
  </div>
  </script>
  <!-- load javascript translation catalog, and javascript fuzzy date library -->
  <script src="/jsi18n/" type="text/javascript">
  </script>
  <script src="//cdn.scratch.mit.edu/scratchr2/static/__ad0074bbd02c73bcc1e3fe1856f1e8b0__/js/lib/jquery.timeago.settings.js" type="text/javascript">
  </script>
  <script src="//cdn.scratch.mit.edu/scratchr2/static/__ad0074bbd02c73bcc1e3fe1856f1e8b0__//js/apps/registration/main.js" type="text/javascript">
  </script>
  <script src="//cdn.scratch.mit.edu/scratchr2/static/__ad0074bbd02c73bcc1e3fe1856f1e8b0__//js/apps/global.js" type="text/javascript">
  </script>
  <script>
   Scratch.NotificationPollTime = 300000;
  </script>
  <script>
   $(document).on("accountnavready", function(e){
        $('#topnav .messages').notificationsAlert();
    });
  </script>
 </body>
 <!-- Site Version: 3.2021.01.28_2021_01_28_10_20 -->
</html>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
print("Title of the document:")
print(soup.find("title"))


# In[ ]:




