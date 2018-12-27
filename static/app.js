new Vue({
    el: "#vue-app-one",
    data: {
        student: [],
        testvuejs: "at vue"
    },
    methods: {
        test: function () {
            alert(1)
        },
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
                .get('http://127.0.0.1:8000/polls/returnData')
                .then(function (data) {
                    for (var i = 0; i < data.body.length; i++) {
                        this.student[i] = data.body[i].fields
                    }
                    this.testvuejs = this.student
                }).catch((a) => {
                    console.log(a)
                });
        }
    }
});