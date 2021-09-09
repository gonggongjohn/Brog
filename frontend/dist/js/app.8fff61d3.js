(function(t){function e(e){for(var o,i,s=e[0],l=e[1],u=e[2],c=0,d=[];c<s.length;c++)i=s[c],Object.prototype.hasOwnProperty.call(r,i)&&r[i]&&d.push(r[i][0]),r[i]=0;for(o in l)Object.prototype.hasOwnProperty.call(l,o)&&(t[o]=l[o]);f&&f(e);while(d.length)d.shift()();return a.push.apply(a,u||[]),n()}function n(){for(var t,e=0;e<a.length;e++){for(var n=a[e],o=!0,i=1;i<n.length;i++){var l=n[i];0!==r[l]&&(o=!1)}o&&(a.splice(e--,1),t=s(s.s=n[0]))}return t}var o={},r={app:0},a=[];function i(t){return s.p+"js/"+({about:"about"}[t]||t)+"."+{about:"a42e7236"}[t]+".js"}function s(e){if(o[e])return o[e].exports;var n=o[e]={i:e,l:!1,exports:{}};return t[e].call(n.exports,n,n.exports,s),n.l=!0,n.exports}s.e=function(t){var e=[],n=r[t];if(0!==n)if(n)e.push(n[2]);else{var o=new Promise((function(e,o){n=r[t]=[e,o]}));e.push(n[2]=o);var a,l=document.createElement("script");l.charset="utf-8",l.timeout=120,s.nc&&l.setAttribute("nonce",s.nc),l.src=i(t);var u=new Error;a=function(e){l.onerror=l.onload=null,clearTimeout(c);var n=r[t];if(0!==n){if(n){var o=e&&("load"===e.type?"missing":e.type),a=e&&e.target&&e.target.src;u.message="Loading chunk "+t+" failed.\n("+o+": "+a+")",u.name="ChunkLoadError",u.type=o,u.request=a,n[1](u)}r[t]=void 0}};var c=setTimeout((function(){a({type:"timeout",target:l})}),12e4);l.onerror=l.onload=a,document.head.appendChild(l)}return Promise.all(e)},s.m=t,s.c=o,s.d=function(t,e,n){s.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:n})},s.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},s.t=function(t,e){if(1&e&&(t=s(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var n=Object.create(null);if(s.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var o in t)s.d(n,o,function(e){return t[e]}.bind(null,o));return n},s.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return s.d(e,"a",e),e},s.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},s.p="/",s.oe=function(t){throw console.error(t),t};var l=window["webpackJsonp"]=window["webpackJsonp"]||[],u=l.push.bind(l);l.push=e,l=l.slice();for(var c=0;c<l.length;c++)e(l[c]);var f=u;a.push([0,"chunk-vendors"]),n()})({0:function(t,e,n){t.exports=n("56d7")},"034f":function(t,e,n){"use strict";n("85ec")},"56d7":function(t,e,n){"use strict";n.r(e);n("e260"),n("e6cf"),n("cca6"),n("a79d");var o,r,a=n("2b0e"),i=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{attrs:{id:"app"}},[n("router-view")],1)},s=[],l=(n("034f"),n("2877")),u={},c=Object(l["a"])(u,i,s,!1,null,null,null),f=c.exports,d=(n("d3b7"),n("3ca3"),n("ddb0"),n("8c4f")),m=function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("div",{staticClass:"container"},[o("img",{staticClass:"mb-4",staticStyle:{"max-width":"100px","margin-top":"5%"},attrs:{alt:"brog logo",src:n("cf05")}}),o(t.component_show,{tag:"component",on:{change:t.onChangeComponent}})],1)},p=[],g=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"container"},[n("b-card",{attrs:{"border-variant":"info"}},[n("h1",[t._v("用户登录界面")]),n("b-form",{on:{submit:t.onLogin}},[n("b-form-group",{staticClass:"row mb-4",attrs:{id:"group-username","label-cols-sm":"2",label:"用户名：","label-for":"input-username"}},[n("b-form-input",{attrs:{id:"input-username",placeholder:"请输入用户名",required:""},model:{value:t.login_form.username,callback:function(e){t.$set(t.login_form,"username",e)},expression:"login_form.username"}})],1),n("b-form-group",{staticClass:"row mb-4",attrs:{id:"group-password","label-cols-sm":"2",label:"密码：","label-for":"input-password"}},[n("b-form-input",{attrs:{id:"input-password",placeholder:"请输入密码",required:""},model:{value:t.login_form.password,callback:function(e){t.$set(t.login_form,"password",e)},expression:"login_form.password"}})],1),n("b-form-checkbox",{staticClass:"mb-3",model:{value:t.rem_flag,callback:function(e){t.rem_flag=e},expression:"rem_flag"}},[t._v("记住用户名和密码")]),n("b-button",{staticStyle:{"margin-right":"50px"},attrs:{type:"submit",size:"lg",variant:"outline-primary"}},[t._v("登录")]),n("b-button",{attrs:{size:"lg",variant:"outline-success"},on:{click:t.jumpRegister}},[t._v("注册账户")])],1)],1)],1)},b=[],h={name:"LoginCard",data:function(){return{login_form:{username:"",password:""},rem_flag:!1}},mounted:function(){var t=localStorage.getItem("username"),e=localStorage.getItem("password");t&&(this.login_form.username=t),e&&(this.login_form.password=e)},methods:{getHostUrl:function(){var t=window.document.location.href,e=t.indexOf("://"),n=t.substring(0,e),o=t.substring(e+3),r=this.$route.path,a=o.indexOf(r),i=o.substring(0,a);console.log(t);var s=i.lastIndexOf(":"),l=i.substring(0,s);return n+"://"+l},onLogin:function(){var t=this,e=this.getHostUrl()+":5000/user/login/";this.axios.post(e,this.login_form).then((function(e){void 0!=e.data&&"200"==e.data.status&&(t.rem_flag&&(localStorage.setItem("username",t.login_form.username),localStorage.setItem("password",t.login_form.password)),t.$router.push("/dashboard"))})).catch((function(t){console.log(t)}))},jumpRegister:function(){this.$emit("change","register")}}},v=h,_=Object(l["a"])(v,g,b,!1,null,"0d84d1b4",null),w=_.exports,x=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"container"},[n("b-card",{attrs:{"border-variant":"info"}},[n("h1",[t._v("用户注册界面")]),n("b-form",{on:{submit:t.onRegister}},[n("b-form-group",{staticClass:"row mb-4",attrs:{id:"group-username","label-cols-sm":"2",label:"用户名：","label-for":"input-username"}},[n("b-form-input",{attrs:{id:"input-username",placeholder:"请输入用户名",required:""},model:{value:t.register_form.username,callback:function(e){t.$set(t.register_form,"username",e)},expression:"register_form.username"}})],1),n("b-form-group",{staticClass:"row mb-4",attrs:{id:"group-password","label-cols-sm":"2",label:"密码：","label-for":"input-password"}},[n("b-form-input",{attrs:{id:"input-password",placeholder:"请输入密码",required:""},model:{value:t.register_form.password,callback:function(e){t.$set(t.register_form,"password",e)},expression:"register_form.password"}})],1),n("b-form-group",{staticClass:"row mb-4",attrs:{id:"group-email","label-cols-sm":"2",label:"邮箱：","label-for":"input-email"}},[n("b-form-input",{attrs:{id:"input-email",type:"email",placeholder:"请输入邮箱",required:""},model:{value:t.register_form.email,callback:function(e){t.$set(t.register_form,"email",e)},expression:"register_form.email"}})],1),n("b-button",{staticStyle:{"margin-right":"50px"},attrs:{type:"submit",size:"lg",variant:"outline-primary"}},[t._v("注册")]),n("b-button",{attrs:{size:"lg",variant:"outline-success"},on:{click:t.jumpLogin}},[t._v("返回")])],1)],1)],1)},y=[],C={name:"RegisterCard",data:function(){return{register_form:{username:"",password:"",email:""}}},methods:{getHostUrl:function(){var t=window.document.location.href,e=t.indexOf("://"),n=t.substring(0,e),o=t.substring(e+3),r=this.$route.path,a=o.indexOf(r),i=o.substring(0,a),s=i.lastIndexOf(":"),l=i.substring(0,s);return n+"://"+l},onRegister:function(){var t=this.getHostUrl()+":5000/user/register/";this.axios.post(t,this.register_form).then((function(t){void 0!=t.data&&"200"==t.data.status&&console.log(t)})).catch((function(t){console.log(t)}))},jumpLogin:function(){this.$emit("change","login")}}},k=C,O=Object(l["a"])(k,x,y,!1,null,"7dbc93e4",null),S=O.exports,j={name:"Sign",data:function(){return{component_show:w}},methods:{onChangeComponent:function(t){"register"==t?this.component_show=S:"login"==t&&(this.component_show=w)}}},$=j,P=Object(l["a"])($,m,p,!1,null,null,null),E=P.exports,U=function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("div",{staticClass:"row"},[o("b-navbar",{attrs:{type:"light"}},[o("img",{staticStyle:{"max-width":"60px"},attrs:{alt:"brog logo",src:n("cf05")}}),o("h3",[t._v("书蛙")]),o("b-navbar-nav",{staticClass:"ml-auto"},[o("b-nav-item-dropdown",{attrs:{text:"我的",right:""}})],1)],1),o("b-card",{staticClass:"col-3",attrs:{"no-body":""}},[o("b-nav",{attrs:{vertical:"",tabs:""}},[o("b-nav-item",{on:{click:t.onSwitchShelf}},[t._v("书架")]),o("b-nav-item",{on:{click:t.onSwitchCommunity}},[t._v("社区")])],1)],1),o(t.component_show,{tag:"component",staticClass:"col",on:{change:t.onChangePage}})],1)},H=[],L=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"container"},[n("div",{staticClass:"container"},[n("h4",[t._v("贡献资源")]),n("b-form-file",{attrs:{plain:"",accept:".pdf"},model:{value:t.upload_file,callback:function(e){t.upload_file=e},expression:"upload_file"}}),n("b-button",{attrs:{variant:"outline-success"},on:{click:t.onUploadFile}},[t._v("上传文件")])],1),n("div",{staticClass:"container mt-2"},[n("h4",[t._v("可用资料")]),n("b-list-group",t._l(t.book_list,(function(e,o){return n("b-list-group-item",{key:e},[n("div",{staticClass:"row"},[n("p",{staticClass:"col"},[t._v("资料名："+t._s(e.name))]),n("p",{staticClass:"col"},[t._v("贡献者："+t._s(e.contributor))]),n("b-button",{staticClass:"col-3",attrs:{variant:"outline-primary"},on:{click:function(e){return t.onAddToShelf(o)}}},[t._v("添加到书架")])],1)])})),1)],1)])},I=[],R=(n("159b"),{name:"CommunityPage",data:function(){return{upload_file:null,book_list:[{uuid:1,name:"1234",contributor:"1234"}]}},mounted:function(){this.getBookList()},methods:{getHostUrl:function(){var t=window.document.location.href,e=t.indexOf("://"),n=t.substring(0,e),o=t.substring(e+3),r=this.$route.path,a=o.indexOf(r),i=o.substring(0,a);console.log(t);var s=i.lastIndexOf(":"),l=i.substring(0,s);return n+"://"+l},getBookList:function(){var t=this,e=this.getHostUrl+":5000/file/list_all/";this.axios.get(e).then((function(e){if(e.data&&"200"==e.data.status){var n=e.data.result;n.forEach((function(e){t.book_list.push({uuid:e.id,name:e.filename,contributor:e.contributor})}))}})).catch((function(t){console.log(t)}))},onUploadFile:function(){var t=this.getHostUrl()+":5000/file/upload/",e=new FormData;e.append("file",this.upload_file);var n={headers:{"Content-Type":"multipart/form-data"}};this.axios.post(t,e,n).then((function(t){console.log(t)})).catch((function(t){console.log(t)}))},onAddToShelf:function(t){var e=this.getHostUrl()+":5000/file/add/",n={id:this.book_list[t].uuid};this.axios.post(e,n).then((function(t){void 0!=t.data&&"200"==t.data.status&&alert("添加成功!")})).catch((function(t){console.log(t)}))}}}),T=R,q=Object(l["a"])(T,L,I,!1,null,null,null),B=q.exports,A=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"container"},[n("h3",[t._v("我的书架")]),n("b-button",{attrs:{variant:"outline-success"},on:{click:t.onAddBook}},[t._v("添加书籍")]),n("div",{staticClass:"row row-cols-3",staticStyle:{"margin-top":"3%"}},t._l(t.book_list,(function(e,o){return n("div",{key:e.name,staticClass:"container"},[n("b-card",[n("h3",[t._v(t._s(e.name))]),n("b-button",{attrs:{variant:"outline-primary"},on:{click:function(e){return t.onReadingBook(o)}}},[t._v("进入阅读")])],1)],1)})),0)],1)},z=[],M={name:"ShelfPage",data:function(){return{book_list:[{uuid:1,name:"1234"},{uuid:2,name:"5678"},{uuid:3,name:"2351"}]}},mounted:function(){},methods:{getHostUrl:function(){var t=window.document.location.href,e=t.indexOf("://"),n=t.substring(0,e),o=t.substring(e+3),r=this.$route.path,a=o.indexOf(r),i=o.substring(0,a);console.log(t);var s=i.lastIndexOf(":"),l=i.substring(0,s);return n+"://"+l},onAddBook:function(){this.$emit("change","community")},onReadingBook:function(t){this.$router.push({path:"/reader",query:{uuid:this.book_list[t].uuid}})}}},F=M,D=Object(l["a"])(F,A,z,!1,null,null,null),J=D.exports,G={name:"Sign",data:function(){return{component_show:J}},methods:{onSwitchShelf:function(){this.component_show=J},onSwitchCommunity:function(){this.component_show=B},onChangePage:function(t){"community"==t&&(this.component_show=B)}}},K=G,N=Object(l["a"])(K,U,H,!1,null,null,null),Q=N.exports,V={},W=Object(l["a"])(V,o,r,!1,null,null,null),X=W.exports;a["default"].use(d["a"]);var Y=[{path:"/",name:"Sign",component:E},{path:"/dashboard",name:"DashBoard",component:Q},{path:"/reader",name:"Reader",component:X},{path:"/about",name:"About",component:function(){return n.e("about").then(n.bind(null,"f820"))}}],Z=new d["a"]({routes:Y}),tt=Z,et=n("2f62");a["default"].use(et["a"]);var nt=new et["a"].Store({state:{},mutations:{},actions:{},modules:{}}),ot=n("5f5b"),rt=(n("f9e3"),n("2dd8"),n("bc3a")),at=n.n(rt),it=n("2106"),st=n.n(it);a["default"].use(ot["a"]),a["default"].use(st.a,at.a),a["default"].config.productionTip=!1,new a["default"]({router:tt,store:nt,render:function(t){return t(f)}}).$mount("#app")},"85ec":function(t,e,n){},cf05:function(t,e,n){t.exports=n.p+"img/logo.57790d17.png"}});
//# sourceMappingURL=app.8fff61d3.js.map