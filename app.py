from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/pool/<pool_type>/<rarity>')
def get_pool(pool_type, rarity):
    cot = json.load(open('./nonebot-plugin-azurlane-assistant-data/azurlane/pool.json', 'r', encoding='utf-8'))
    if(cot.get(pool_type) == None):
        return jsonify({'error': 'pool_type not found'})
    if(cot[pool_type].get(rarity) == None):
        return jsonify({'error': 'rarity not found'})
    return jsonify(cot[pool_type][rarity])