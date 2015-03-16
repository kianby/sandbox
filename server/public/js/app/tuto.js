// Filename: tuto.js

define([
  'jquery',
  'underscore',
  'backbone',
], function($, _, Backbone){
  var initialize = function(){

    var AppView = Backbone.View.extend({
      // el - stands for element. Every view has a element associate in with HTML
      //      content will be rendered.
      el: '#container',
      template: _.template("<h3>Hello <%= who %></h3>"),
      // It's the first function called when this view it's instantiated.
      initialize: function(){
        this.render();
      },
      // $el - it's a cached jQuery object (el), in which you can use jQuery functions
      //       to push content. Like the Hello World in this case.
      render: function(){
        this.$el.html(this.template({who: 'world!'}));
      }
    });

    var appView = new AppView();
  }

  return {
    initialize: initialize
  };
});

