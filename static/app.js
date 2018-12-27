new Vue({
    el: "#vue-app-one",
    data: {
        blog: {
            title: "",
            author: "",
            context: ""
        },
        testvuejs: "at vue"
    },
    methods: {
        addData: function () {
            this.$http
                .post('http://127.0.0.1:8000/polls/getData', {
                    title: this.blog.title,
                    author: this.blog.author,
                    tel: this.blog.context
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