/* global $, rivets, Dashing */

Dashing.widgets.TelemetryWidget = function(dashboard) {
    var self = this,
        widget;
    self.__init__ =  Dashing.utils.widgetInit(dashboard, 'telemetry_widget', {
        require: ['jqueryKnob']
    });
    this.row = 1;
    this.col = 1;
    this.scope = {};
    this.getWidget = function () {
        return widget;
    };
    this.getData = function () {};
    this.interval = 10000;
};

rivets.binders['telemetry_widget'] = function binder(el, data) {
    if (!data) return;
    if (!$.fn.knob) {
        $(document).on('libs/jqueryKnob/loaded', binder.bind(this, el, data));
        return;
    }
    if (!el.init) {
        $(el).knob(data);
        el.init = true;
    }
    else {
        $(el).trigger('configure', data);
    }
    $(el).val(this.model.value).trigger('change');
};
