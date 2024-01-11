from flask import Flask
from flask_restful import Api, Resource, reqparse
import os
import signal
 
#Create instance for server
app = Flask(__name__)
api = Api(app)

#Request parser for getting input from requester
parser = reqparse.RequestParser()
 
#Check if server still running
class CheckServerStatus(Resource):
    def get(self):
        return {"Python Sever is running": True}
    def post(self):
        return self.get()

#For shutting down RESTful API server
class ShutdownServer(Resource):
    def get(self):
        os.kill(os.getpid(),signal.SIGTERM)
        return{}
    def post(self):
        self.get()
        return {}
    
class TestPassingData(Resource):
    def post(self):
        parser.add_argument('text')
        parser.add_argument('intnum')
        parser.add_argument('floatnum')
        parser.add_argument('boolean')
        args = parser.parse_args()
        text = args.text
        num = args.intnum
        numdec = args.floatnum
        boolean = args.boolean
        return {
            "text" : str(text),
            "intnum" : int(num),
            "floatnum" : float(numdec),
            "boolean" : bool(boolean)
            }

#Add resource in API and URL for requesting information
api.add_resource(CheckServerStatus, '/CheckServerStatus')
api.add_resource(ShutdownServer, '/PythonShutdown')
api.add_resource(TestPassingData,'/TestPassingData')
 
#Start server
if __name__ == "__main__":
    app.run(debug=True)