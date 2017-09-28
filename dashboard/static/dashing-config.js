var mainDashboard = new Dashboard({"widgetBaseDimensions":[368,207]});


mainDashboard.addWidget('customWidget', 'Number', {
    getData: function () {
        var self = this;
        Dashing.utils.get('test_widget', function(data) {
            $.extend(self.scope, data);
        });
    },
    interval: 3000
});

mainDashboard.addWidget('speed_widget', 'Knob', {
    getData: function () {
        $.extend(this.scope, {
            title: 'Speed',
            detail: 'km/h',
            value: '35',
            data: {
                angleArc: 280,
                angleOffset: -140,
                displayInput: true,
                displayPrevious: true,
                step: 1,
                min: 1,
                max: 70,
                readOnly: true,
                format: function(value) { return value; }
            }
        });
    }
});
