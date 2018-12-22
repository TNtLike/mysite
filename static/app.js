new Vue({
    el: "#vue-app-one",
    data: {
        testvuejs: "at vue"
    },
    methods: {
        addData: function () {
            this.$http
                .post('http://127.0.0.1:8000/polls/getdata',{
                })
                .then(function (data) {
                    console.log(data);
                }).catch((a) => {
                    console.log(a)
                });
        },
        getData: function () {
            this.$http
                .post('http://127.0.0.1:8000/polls/returnData')
                .then(function (data) {
                    console.log(data);
                }).catch((a) => {
                    console.log(a)
                });
        }
    }
});