var mainDashboard = new Dashboard({"widgetBaseDimensions":[368,207]});

//mainDashboard.addWidget('new_users_widget', 'Number', {
//    getData: function () {
//        var self = this;
//        Dashing.utils.get('new_users_widget', function(scope) {
//            $.extend(self.scope, scope);
//        });
//    },
//    interval: 5000
//});


mainDashboard.addWidget('speed_widget', 'Number', {
    getData: function () {
        var self = this;
        Dashing.utils.get('speed_widget', function(data) {
            $.extend(self.scope, data);
        });
    },
    interval: 100
});

//var d = new Date()

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
//            interval: 100
//        });
//    }
//});
