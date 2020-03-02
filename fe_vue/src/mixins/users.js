export default {
    methods: {
        async registeruser(params) {
            return new Promise((resolve,reject) => {
                this.$http.post('/register', params)
                .then(response => {
                    resolve(response.data)
                })
                .catch(error => {
                    reject(response.reason)
                })
            }) 
        },
        async loginuser(params) {
            return new Promise((resolve,reject) => {
                this.$http.post('/login', params)
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