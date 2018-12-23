new Vue({
    el: "#vue-app-one",
    data: {
        student: {
            name: "",
            age: 0,
            sexes: "",
            tel: ""
        },
        testvuejs: "at vue"
    },
    methods: {
        addData: function () {
            this.$http
                .post('http://127.0.0.1:8000/polls/getData', {
                    name: this.student.name,
                    age: this.student.age,
                    sex: this.student.sexes,
                    tel: this.student.tel
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