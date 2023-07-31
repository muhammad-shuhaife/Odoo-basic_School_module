odoo.define('student.tag_client_action',function (require) {
'use  strict';

    var core = require('web.core');
    var AbstractAction = require('web.AbstractAction');
    var DisplayCustomMessageAction = AbstractAction.extend({
    //template: ''
          start: function(){
            alert('This is warning message');
            }
    });
    core.action_registry.add('tag_client_action',DisplayCustomMessageAction);
    return DisplayCustomMessageAction;
    });