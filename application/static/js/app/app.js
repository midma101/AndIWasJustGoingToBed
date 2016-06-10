App = Ember.Application.create({
    LOG_TRASITIONS: true,
    LOG_TRASITIONS_INTO: true,
    LOG_VIEW_LOOKUPS: true,
    LOG_ACTIVE_GENERATION: true,
    LOG_BINDINGS: true,
});

App.TextField = Ember.TextField.extend({
    attributeBindings: ['class', 'placeholder']
});

App.ApplicationView = Ember.View.extend({
    didInsertElement : function(){
        
    }
});

App.ApplicationRoute = Ember.Route.extend({
    model: function(){
    }
});



App.RegisterUserView = Ember.View.extend({
    actions: {

    }

});