/* global $, rivets, Dashing */

Dashing.widgets.TelemetryGauge = function(dashboard) {
    var self = this,
        widget;
    self.__init__ =  Dashing.utils.widgetInit(dashboard, 'telemetry', {
        require: ['jqueryKnob']
    });
    this.row = 3;
    this.col = 2;
    this.scope = {};
    this.getWidget = function () {
        return widget;
    };
    this.getData = function () {};
    this.interval = 10000;
};

rivets.binders['telemetry'] = function binder(el, data) {
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
