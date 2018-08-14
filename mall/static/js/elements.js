var toPassword = function (name, displayName, value) {
    var html = document.getElementById("element-password").innerHTML;
    html = html.replace(/elementName/g, name)
        .replace(/displayName/g, displayName).replace(/elementValue/g, value);
    return html;
};
var appendPassword = function (name, displayName, value) {
    document.write(toPassword(name, displayName, value));
};
var toText = function (name, displayName, value) {
    var html = document.getElementById("element-text").innerHTML;
    html = html.replace(/elementName/g, name)
        .replace(/displayName/g, displayName).replace(/elementValue/g, value);
    return html;
};

var appendText = function (name, displayName, value) {
    document.write(toText(name, displayName, value));
};

var toSelect = function (name, displayName, value, options) {
    var html = document.getElementById("element-select").innerHTML;
    html = html.replace(/elementName/g, name)
        .replace(/displayName/g, displayName).replace(/elementValue/g, value);
    //var optionsHtml="<option></option>";
    var optionsHtml = "";
    for (var v in options) {
        var selected = value == v ? "selected" : "";
        optionsHtml += "<option value='" + v + "' " + selected + " >" + options[v] + "</option>\n";
    }
    html = html.replace(/optionsReplaceMe/g, optionsHtml);
    return html;
};

var appendSelect = function (name, displayName, value, options) {
    document.write(toSelect(name, displayName, value, options));
};

var toHotSelect = function (name, displayName, value) {
    var options = {};
    for (var i = 0; i <= 10; i++) {
        options[i] = i;
    }
    return toSelect(name, displayName, value, options);
};
var appendHotSelect = function (name, displayName, value) {
    document.write(toHotSelect(name, displayName, value));
};

var toYesNoSelect = function (name, displayName, value) {
    var options = {"true": "是", "false": "否"};
    return toSelect(name, displayName, value, options);
};

var appendYesNoSelect = function (name, displayName, value) {
    document.write(toYesNoSelect(name, displayName, value));
};

var appendActions = function () {
    var html = document.getElementById("element-form-actions").innerHTML;
    document.write(html);
};

var toHidden = function (name, value) {
    var html = document.getElementById("element-hidden").innerHTML;
    html = html.replace(/elementName/g, name).replace(/elementValue/g, value);
    return html;
};

var appendHidden = function (name, value) {
    document.write(toHidden(name, value));
};

var appendIndexActions = function (id) {
    var html = document.getElementById("index-actions").innerHTML;
    html = html.replace(/elementValue/g, id);
    document.write(html);
};

var appendCreateAction = function () {
    var html = document.getElementById("create-div").innerHTML;
    document.write(html);
};
