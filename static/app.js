new Vue({
    el: "#vue-app-one",
    data: {
        testvuej: "at vue"
    },
    methods: {
        testDjango: function () {
            this.$http
                .post('polls/testVuejsandDjango')
                .then(function (data) {
                    console.log(data);
                }).catch((a) => {
                    console.log(a)
                });
        }
    }
});