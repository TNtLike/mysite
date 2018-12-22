new Vue({
    el: "#vue-app-one",
    data: {
        testvuej: "at vue"
    },
    methods: {
        testDjango: function () {
            this.$http
                .post('http://127.0.0.1:8000/polls/testVuejsandDjango')
                .then(function (data) {
                    console.log(data);
                }).catch((a) => {
                    console.log(a)
                });
        }
    }
});