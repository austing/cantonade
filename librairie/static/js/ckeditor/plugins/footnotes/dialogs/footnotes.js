﻿CKEDITOR.dialog.add("footnotesDialog",function(c){return{editor_name:!1,title:"Gérer les notes en bas de page",minWidth:400,minHeight:200,footnotes_el:!1,contents:[{id:"tab-basic",label:"Basic Settings",elements:[{type:"textarea",id:"new_footnote","class":"footnote_text",label:"Nouvelle note en bas de page:",inputStyle:"height: 100px"},{type:"text",id:"footnote_id",name:"footnote_id",label:"Aucune note en bas de page",setup:function(){var d=this.getDialog();$el=jQuery("#"+this.domId);d.footnotes_el=$el;c=d.getParentEditor();$footnotes=
jQuery("#"+c.id+"_contents iframe").contents().find(".footnotes ol");$this=this;if(0<$footnotes.length){0==$el.find("p").length?$el.append('<p style="margin-bottom: 10px;"><strong>Ou bien:</strong> Choisir note en bas de page:</p><ol></ol>'):$el.find("ol").empty();var a="";$footnotes.find("li").each(function(){$item=jQuery(this);var b=$item.attr("data-footnote-id");a+='<li style="margin-left: 15px;"><input type="radio" name="footnote_id" value="'+b+'" id="fn_'+b+'" /> <label for="fn_'+b+'" style="white-space: normal; display: inline-block; padding: 0 25px 0 5px; vertical-align: top; margin-bottom: 10px;">'+
$item.find("cite").text()+"</label></li>"});$el.children("label,div").css("display","none");$el.find("ol").html(a);$el.find(":radio").change(function(){$el.find(":text").val(jQuery(this).val())})}else $el.children("div").css("display","none")}}]}],onShow:function(){this.setupContent();var c=this;CKEDITOR.on("instanceLoaded",function(a){c.editor_name=a.editor.name});CKEDITOR.replaceAll(function(a,b){if(!a.className.match(/footnote_text/))return!1;b.toolbarGroups=[{name:"editing",groups:["undo","find",
"selection","spellchecker"]},{name:"clipboard",groups:["clipboard"]},{name:"basicstyles",groups:["basicstyles","cleanup"]}];b.allowedContent="br em strong; a[!href]";b.enterMode=CKEDITOR.ENTER_BR;b.autoParagraph=!1;b.height=80;b.resize_enabled=!1;b.autoGrow_minHeight=80;b.removePlugins="footnotes";b.on={focus:function(a){a=jQuery("#"+a.editor.id+"_contents");a.parents("tr").next().find(":checked").attr("checked",!1);a.parents("tr").next().find(":text").val("")}};return!0})},onOk:function(){var d=
CKEDITOR.instances[this.editor_name],a=this.getValueOf("tab-basic","footnote_id");c.fire("saveSnapshot");if(""==a){a=d.getData();if(""==a)return;c.plugins.footnotes.build(a,!0,c)}else c.plugins.footnotes.build(a,!1,c);d.destroy()}}});