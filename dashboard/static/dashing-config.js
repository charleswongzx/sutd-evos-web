var mainDashboard = new Dashboard();

//mainDashboard.addWidget('new_users_widget', 'Number', {
//    getData: function () {
//        var self = this;
//        Dashing.utils.get('new_users_widget', function(scope) {
//            $.extend(self.scope, scope);
//        });
//    },
//    interval: 5000
//});

widget_refresh_rate = 1000

mainDashboard.addWidget('clock_widget', 'Clock');


mainDashboard.addWidget('speed_widget', 'Knob', {
    getData: function () {
        var self = this;
        Dashing.utils.get('speed_widget', function(data) {
            $.extend(self.scope, data);
        });
    },
    interval: widget_refresh_rate,
    detail: 'km/h'
});

mainDashboard.addWidget('rpm_widget', 'Knob', {
    getData: function () {
        var self = this;
        Dashing.utils.get('rpm_widget', function(data) {
            $.extend(self.scope, data);
        });
    },
    interval: widget_refresh_rate,
    detail: 'RPM'
});


mainDashboard.addWidget('temp_widget', 'Knob', {
    getData: function () {
        var self = this;
        Dashing.utils.get('temp_widget', function(data) {
            $.extend(self.scope, data);
        });
    },
    interval: widget_refresh_rate,
    detail: 'deg'
});

mainDashboard.addWidget('pressure_widget', 'Knob', {
    getData: function () {
        var self = this;
        Dashing.utils.get('pressure_widget', function(data) {
            $.extend(self.scope, data);
        });
    },
    interval: widget_refresh_rate,
    detail: 'psi'
});

mainDashboard.addWidget('mileage_widget', 'Knob', {
    getData: function () {
        var self = this;
        Dashing.utils.get('mileage_widget', function(data) {
            $.extend(self.scope, data);
        });
    },
    interval: widget_refresh_rate,
    detail: 'km/l'
});



//mainDashboard.addWidget('speed_widget', 'Knob', {
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
