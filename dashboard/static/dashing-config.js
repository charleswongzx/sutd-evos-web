var w = window.innerWidth;
var h = window.innerHeight;

var horizontal_res = 8;
var vertical_res = 5;

var mainDashboard = new Dashboard({'widgetBaseDimensions': [w/horizontal_res, h/vertical_res]});

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



//mainDashboard.addWidget('speed_widget', 'TelemetryGauge', {
//    getData: function () {
//        $.extend(this.scope, {
//            title: 'Speed',
//            detail: 'km/h',
//            value: d.getSeconds(),
//            data: {
//                angleArc: 280,
//                angleOffset: -140,
//                displayInput: true,
//                displayPrevious: true,
//                step: 1,
//                min: 1,
//                max: 70,
//                readOnly: true,
//                format: function(value) { return value; }
//            },
//            Dashing.utils.get('speed_widget', function(data) {
//            $.extend(self.scope, data);
//        });
//        });
//    },
//    interval: widget_refresh_rate
//});
