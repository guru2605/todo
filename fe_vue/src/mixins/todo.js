export default {
    methods: {
        async getTodoList(params) {
            return new Promise((resolve,reject) => {
                this.$http.post('/todo/get', params)
                .then(response => {
                    resolve(response.data)
                })
                .catch(error => {
                    reject(response.reason)
                })
            }) 
        },
        async storeTodo(params) {
            return new Promise((resolve,reject) => {
                this.$http.post('/todo/create', params)
                .then(response => {
                    resolve(response.data)
                })
                .catch(error => {
                    reject(response.reason)
                })
            }) 
        },
        async updateTodo(params) {
            return new Promise((resolve,reject) => {
                this.$http.post('/todo/update', params)
                .then(response => {
                    resolve(response.data)
                })
                .catch(error => {
                    reject(response.reason)
                })
            }) 
        },
        async deleteTodo(params) {
            return new Promise((resolve,reject) => {
                this.$http.post('/todo/delete', params)
                .then(response => {
                    resolve(response.data)
                })
                .catch(error => {
                    reject(response.reason)
                })
            }) 
        }
    }
}