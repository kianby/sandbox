var grunt = require('grunt');

grunt.loadNpmTasks('grunt-contrib-jshint');
grunt.loadNpmTasks('grunt-karma');

// Project configuration.
grunt.initConfig({
  jshint: {
    all: ['Gruntfile.js', 'lib/**/*.js', 'test/**/*.js']
  },
  karma: {
  unit: {
    options: {
      files: ['test/**/*.js']
    }
  }
}
});

grunt.registerTask('default', 'default task description', function(){
  console.log('Nothing to do');
  grunt.log.ok('Success');
});

