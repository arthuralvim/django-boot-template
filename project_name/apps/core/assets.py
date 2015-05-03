
PIPELINE_JS = {
    'vendor': {
        'source_filenames': (
            'jquery/dist/jquery.min.js',
            'bootstrap/dist/js/bootstrap.js',
            'backbone/backbone.js',
            'marionette/lib/backbone.marionette.js',
            'd3/d3.js',
            'c3/c3.js',
            'bootstrap-datepicker/js/bootstrap-datepicker.js',
            'bootstrap-datepicker/js/locales/bootstrap-datepicker.pt-BR.js',
            'selectize/dist/js/standalone/selectize.js',
        ),
        'output_filename': 'js/vendor.js',
    }
}


PIPELINE_CSS = {
    'base': {
        'source_filenames': (
            'bootstrap/dist/css/bootstrap.css',
            'font-awesome/css/font-awesome.css',
            'c3/c3.css',
            'bootstrap-datepicker/dist/css/bootstrap-datepicker3.css',
            'selectize/dist/css/selectize.bootstrap3.css',
        ),
        'output_filename': 'css/base.css',
    },
}
