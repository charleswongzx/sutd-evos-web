var w = window.innerWidth;
var h = window.innerHeight;

var horizontal_res = 23;
var vertical_res = 16;

var mainDashboard = new Dashboard({'widgetBaseDimensions': [w/horizontal_res, h/vertical_res], 'widgetMargins': [10,10]});

widget_refresh_rate = 500

//mainDashboard.addWidget('telemetry', 'TelemetryGauge', {
//    getData: function () {
//        var self = this;
//        Dashing.utils.get('telemetry', function(data) {
//            $.extend(self.scope, data);
//        });
//    },
//    interval: widget_refresh_rate,
//    detail: 'km/h'
//});


mainDashboard.addWidget('banner_widget', 'Banner');


mainDashboard.addWidget('fuel_graph_widget', 'FuelGraph', {
    getData: function () {
        var self = this;
        Dashing.utils.get('fuel_graph_widget', function(data) {
            $.extend(self.scope, data);
        });
    },
    interval: 500,
    detail: 'laps'
});





mainDashboard.addWidget('speed_widget', 'TelemetryGauge', {
    getData: function () {
        var self = this;
        Dashing.utils.get('speed_widget', function(data) {
            $.extend(self.scope, data);
        });
    },
    interval: widget_refresh_rate,
    detail: 'km/h'
});

mainDashboard.addWidget('rpm_widget', 'TelemetryGauge', {
    getData: function () {
        var self = this;
        Dashing.utils.get('rpm_widget', function(data) {
            $.extend(self.scope, data);
        });
    },
    interval: widget_refresh_rate,
    detail: 'RPM'
});


mainDashboard.addWidget('temp_widget', 'TelemetryGauge', {
    getData: function () {
        var self = this;
        Dashing.utils.get('temp_widget', function(data) {
            $.extend(self.scope, data);
        });
    },
    interval: widget_refresh_rate,
    detail: 'deg'
});

//mainDashboard.addWidget('pressure_widget', 'TelemetryGauge', {
//    getData: function () {
//        var self = this;
//        Dashing.utils.get('pressure_widget', function(data) {
//            $.extend(self.scope, data);
//        });
//    },
//    interval: widget_refresh_rate,
//    detail: 'psi'
//});

mainDashboard.addWidget('mileage_widget', 'TelemetryGauge', {
    getData: function () {
        var self = this;
        Dashing.utils.get('mileage_widget', function(data) {
            $.extend(self.scope, data);
        });
    },
    interval: widget_refresh_rate,
    detail: 'km/l'
});


mainDashboard.addWidget('lap_widget', 'Number', {
    getData: function () {
        var self = this;
        Dashing.utils.get('lap_widget', function(data) {
            $.extend(self.scope, data);
        });
    },
    interval: widget_refresh_rate,
    detail: 'laps'
});

mainDashboard.addWidget('fuel_graph_widget', 'FuelGraph', {
    getData: function () {
        var self = this;
        Dashing.utils.get('fuel_graph_widget', function(data) {
            $.extend(self.scope, data);
        });
    },
    interval: 500,
    detail: 'laps'
});



mainDashboard.addWidget('button_panel_widget', 'ButtonPanel', {
    getData: function () {
        var self = this;
        Dashing.utils.get('button_panel_widget', function(data) {
            $.extend(self.scope, data);
        });
    },
    interval: widget_refresh_rate,
    detail: 'Control Panel'
});
