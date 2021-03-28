import anvil.server



from flask import Flask, jsonify, request #import objects from the Flask model
app = Flask(__name__) #define app using Flask

anvil.server.connect("O6HUI7ZPHPGAUYQSLUMJSCO3-5ESUVNCA6HH7DJWQ")

languages = [{'name' : 'JavaScript'}, {'name' : 'Python'}, {'name' : 'Ruby'}]

@app.route('/', methods=['GET'])
def test():
	return jsonify({'message' : 'It works!'})

@app.route('/lang', methods=['GET'])
def returnAll():
	return jsonify({'languages' : languages})

@app.route('/lang/<string:name>', methods=['GET'])
def returnOne(name):
	langs = [language for language in languages if language['name'] == name]
	return jsonify({'language' : langs[0]})

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080) #run app on port 8080 in debug modes