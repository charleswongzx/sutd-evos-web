
/* global Dashing */

Dashing.widgets.Banner = function(dashboard) {
    var self = this;
    self.__init__ = Dashing.utils.widgetInit(dashboard, 'banner');
    self.row = 2;
    self.col = 20;
//    self.color = '#96bf48';
    self.scope = {};
    self.getWidget = function () {
        return this.__widget__;
    };
    self.getData = function () {};
    self.interval = 1000;
};
