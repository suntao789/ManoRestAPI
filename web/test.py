import web

urls = (
    '/', 'hello',
    '/v3/auth/tokens','tokens',
    '/v2/vapps/instances/(\d+)/vm','queryvms'
)
app = web.application(urls, globals())

class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello, ' + name + '!'

class tokens:
    def POST(self):
        web.header("Content-Type","application/json") 
        web.header("X-Subject-Token","7099908ad96c4653acd181fc84214f3c") 
        render = open("templates/tokendata.txt",'r').readlines()
        return ''.join(i.strip("\n") for i in render)
    
class queryvms:
    def GET(self):
        render = open("templates/tokendata.txt",'r').readlines()
        return ''.join(i.strip("\n") for i in render)

if __name__ == "__main__":
    app.run()