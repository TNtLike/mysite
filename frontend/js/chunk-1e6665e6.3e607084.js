(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-1e6665e6"],{"2b27":function(e,t,n){(function(){var t={expires:"1d",path:"; path=/"},n={install:function(e){e.prototype.$cookies=this,e.cookies=this},config:function(e,n){e&&(t.expires=e),n&&(t.path="; path="+n)},get:function(e){var t=decodeURIComponent(document.cookie.replace(new RegExp("(?:(?:^|.*;)\\s*"+encodeURIComponent(e).replace(/[\-\.\+\*]/g,"\\$&")+"\\s*\\=\\s*([^;]*).*$)|^.*$"),"$1"))||null;if(t&&"{"===t.substring(0,1)&&"}"===t.substring(t.length-1,t.length))try{t=JSON.parse(t)}catch(n){return t}return t},set:function(e,n,s,a,i,o){if(!e)throw new Error("cookie name is not find in first argument");if(/^(?:expires|max\-age|path|domain|secure)$/i.test(e))throw new Error("cookie key name illegality ,Cannot be set to ['expires','max-age','path','domain','secure']\t","current key name: "+e);n&&n.constructor===Object&&(n=JSON.stringify(n));var r="";if(s=void 0===s?t.expires:s,s&&0!=s)switch(s.constructor){case Number:r=s===1/0||-1===s?"; expires=Fri, 31 Dec 9999 23:59:59 GMT":"; max-age="+s;break;case String:if(/^(?:\d{1,}(y|m|d|h|min|s))$/i.test(s)){var c=s.replace(/^(\d{1,})(?:y|m|d|h|min|s)$/i,"$1");switch(s.replace(/^(?:\d{1,})(y|m|d|h|min|s)$/i,"$1").toLowerCase()){case"m":r="; max-age="+2592e3*+c;break;case"d":r="; max-age="+86400*+c;break;case"h":r="; max-age="+3600*+c;break;case"min":r="; max-age="+60*+c;break;case"s":r="; max-age="+c;break;case"y":r="; max-age="+31104e3*+c;break;default:new Error("unknown exception of 'set operation'")}}else r="; expires="+s;break;case Date:r="; expires="+s.toUTCString();break}return document.cookie=encodeURIComponent(e)+"="+encodeURIComponent(n)+r+(i?"; domain="+i:"")+(a?"; path="+a:t.path)+(o?"; secure":""),this},remove:function(e,n,s){return!(!e||!this.isKey(e))&&(document.cookie=encodeURIComponent(e)+"=; expires=Thu, 01 Jan 1970 00:00:00 GMT"+(s?"; domain="+s:"")+(n?"; path="+n:t.path),this)},isKey:function(e){return new RegExp("(?:^|;\\s*)"+encodeURIComponent(e).replace(/[\-\.\+\*]/g,"\\$&")+"\\s*\\=").test(document.cookie)},keys:function(){if(!document.cookie)return[];for(var e=document.cookie.replace(/((?:^|\s*;)[^\=]+)(?=;|$)|^\s*|\s*(?:\=[^;]*)?(?:\1|$)/g,"").split(/\s*(?:\=[^;]*)?;\s*/),t=0;t<e.length;t++)e[t]=decodeURIComponent(e[t]);return e}};e.exports=n,"undefined"!==typeof window&&(window.$cookies=n)})()},"6d6e":function(e,t,n){},a3a6:function(e,t,n){"use strict";var s=n("6d6e"),a=n.n(s);a.a},b3e3:function(e,t,n){"use strict";n.r(t);var s=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"entMain"},[n("div",{staticClass:"content"},[n("el-row",{attrs:{gutter:20}},[n("el-col",{attrs:{span:12,offset:5}},[n("div",{staticClass:"content-left"},[n("div",{staticClass:"title"},[n("span",[n("b",[e._v("面试邀请")]),e._v("\n              ("+e._s(e.sentJob.length)+")\n            ")])]),0==e.sentJob.length?n("div",[n("p",[e._v("暂无邀请")])]):n("el-table",{staticStyle:{width:"100%"},attrs:{data:e.tempList,stripe:"",size:"small"}},[n("el-table-column",{attrs:{prop:"sendTime",label:"日期",sortable:"",width:"120"}}),n("el-table-column",{attrs:{prop:"jobName",label:"职位",width:"120"}}),n("el-table-column",{attrs:{prop:"entName",label:"公司"}}),n("el-table-column",{attrs:{prop:"status",label:"状态"}}),n("el-table-column",{attrs:{label:"操作",width:"100"},scopedSlots:e._u([{key:"default",fn:function(t){return[n("el-button",{staticStyle:{color:"#f56c6c"},attrs:{type:"text",size:"small"},on:{click:function(n){e.funClose(t.row)}}},[e._v("拒绝邀请")]),n("router-link",{attrs:{to:{name:"singlejob",query:{jobid:t.row.jobid,entid:t.row.entid,resumeid:t.row.resumeid}},target:"_blank"}},[n("el-button",{attrs:{type:"text",size:"small"},on:{click:function(n){e.funShow(t.row)}}},[e._v("查看职位")])],1),n("el-button",{staticStyle:{color:"#67c23a"},attrs:{type:"text",size:"small"},on:{click:function(n){e.funPass(t.row)}}},[e._v("接受邀请")])]}}])})],1),n("el-pagination",{staticClass:"page",staticStyle:{"text-align":"center"},attrs:{layout:"prev, pager, next",total:e.sentJob.length,"current-page":e.currentPage,"page-size":e.pageSize},on:{"size-change":e.funSizeChange,"current-change":e.funCurrentChange}})],1)])],1)],1)])},a=[],i=n("2b27"),o=n.n(i),r={name:"entMain",data:function(){return{sentJob:[],entJobInfo:[],currentPage:1,pageSize:10,tempList:[]}},created:function(){var e=this;this.axios.post("getSentJob",{psnid:o.a.get("psnid"),entid:""}).then(function(t){if("ok"==t.data.status){var n=JSON.parse(t.data.msg);for(var s in n)"面试邀请"==n[s].fields.status&&e.sentJob.push(n[s].fields);e.tempList=e.sentJob.slice(0,10)}})},methods:{funClose:function(e){var t=this;this.sentJob.splice(this.sentJob.indexOf(e),1),this.axios.post("closeSent",{msg:{jobid:e.jobid,resumeid:e.resumeid,entid:e.entid,psnid:e.psnid}}).then(function(e){"ok"==e.data.status&&(t.$message({type:"success",message:e.data.msg}),t.tempList=t.sentJob.slice(0,10))})},funPass:function(e){var t=this;this.sentJob.splice(this.sentJob.indexOf(e),1),this.axios.post("passSent",{msg:{jobid:e.jobid,resumeid:e.resumeid,entid:e.entid,psnid:e.psnid}}).then(function(e){"ok"==e.data.status&&(t.$message({type:"success",message:e.data.msg}),t.tempList=t.sentJob.slice(0,10))})},funDelJob:function(e,t){var n=this;this.entJobInfo.splice(t,1),this.axios.post("delEntJobInfo",{msg:e}).then(function(e){"ok"==e.data.status&&n.$message({type:"success",message:e.data.msg})})},funSizeChange:function(e){this.pageSize=e,this.funCurrentChange(this.currentPage)},funCurrentChange:function(e){this.currentPage=e,this.currentChangePage(this.sentJob,e)},currentChangePage:function(e,t){var n=(t-1)*this.pageSize,s=t*this.pageSize;for(this.tempList=[];n<s;n++)e[n]&&this.tempList.push(e[n])}},computed:{}},c=r,u=(n("a3a6"),n("2877")),l=Object(u["a"])(c,s,a,!1,null,"3405e76a",null);l.options.__file="recJob.vue";t["default"]=l.exports}}]);
//# sourceMappingURL=chunk-1e6665e6.3e607084.js.map