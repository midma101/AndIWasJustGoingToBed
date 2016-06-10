App.User = DS.Model.extend({
    'email': DS.attr('string'),
    'id': DS.attr('number')
});

App.Store = DS.Store.extend({
    revision: 13,
});
App.Store = DS.Store;

App.ApplicationAdapter = DS.RESTAdapter.extend({
    namespace: 'api'
});