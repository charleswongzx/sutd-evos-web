
/* global Dashing */

Dashing.widgets.ButtonPanel = function(dashboard) {
    var self = this;
    self.__init__ = Dashing.utils.widgetInit(dashboard, 'button_panel');
    self.row = 4;
    self.col = 3;
//    self.color = '#96bf48';
    self.scope = {};
    self.getWidget = function () {
        return this.__widget__;
    };
    self.getData = function () {};
    self.interval = 1000;
};
