var gulp = require('gulp'),
    rimraf = require('rimraf')
    watch = require('gulp-watch'),
    connect = require('gulp-connect'),
    open = require('gulp-open'),
    minifycss = require('gulp-minify-css'),
    less = require('gulp-less');

/**
 * ------------------------------------------------------------ The Webserver
 */

// Create a webserver
gulp.task('webserver', function() {
  connect.server({
    root: ['.'],
    port: 6007,
    livereload: true
  });
});

/**
 * ------------------------------------------------------------ Live Reload
 */

// Compile less files to css
gulp.task('less', function() {
  return gulp.src('less/styles.less')
      .pipe(less())
      .pipe(minifycss())
      .pipe(gulp.dest('css'))
});

gulp.task('watch', function() {
  gulp.watch('less/**', ['less']);
});

// Watch files for changes and reload our server
gulp.task('livereload', ['webserver'], function() {
  gulp.src(['*.html', 'css/*.css', 'js/*.js'])
    .pipe(watch())
    .pipe(connect.reload());
});

/**
 * ------------------------------------------------------------ Dev Task
 */

gulp.task('dev', ['less', 'watch', 'livereload'], function() {
  var options = {
    url: "http://localhost:6007/",
    app: "firefox"
  };

 // Any file that exists
  gulp.src("gulpfile.js")
      .pipe(open("", options));
});

gulp.task('default', ['dev']);
