from flask import Flask, request, jsonify
from flask.views import MethodView
from flask_cors import CORS
import sys
import collections

collections.Iterable = collections.abc.Iterable

sys.path.append('./datastructures')
from bloom_filter import BloomFilter

try:
    from collections.abc import Callable  # noqa
except ImportError:
    from collections import Callable  # noqa

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)


class BloomFilterView(MethodView):
    bloom_filter = BloomFilter(1000, 0.01)

    def post(self):
        if request.path == '/api/bloom-filter/settings':
            return self.new_bloom_filter()
        else:
            return self.add_item()

    def get(self):
        return self.check_item()

    def add_item(self):
        item = request.json.get('item')
        if item:
            self.bloom_filter.add(item)
            return jsonify({'message': 'Item added to bloom filter.'}), 200
        return jsonify({'message': 'Item not added to bloom filter.'}), 400

    def check_item(self):
        item = request.args.get('item')
        if item:
            exists = self.bloom_filter.exists(item)
            return jsonify({'exists': exists}), 200
        return jsonify({'exists': False}), 400

    def get_memory_size_of_bf(self):
        return sys.getsizeof(self.bloom_filter)

    def new_bloom_filter(self):
        capacity = request.json.get('capacity')
        fp_prob = request.json.get('falsePositiveRate')
        num_hash_functions = request.json.get('numHashFunctions')

        if capacity and fp_prob and num_hash_functions:
            self.bloom_filter = BloomFilter(capacity, fp_prob)
            return jsonify({'message': 'Settings updated successfully.'}), 200

        return jsonify({'message': 'Failed to update settings.'}), 400


app.add_url_rule('/api/bloom-filter',
                 view_func=BloomFilterView.as_view('bloom_filter'))

app.add_url_rule('/api/bloom-filter/settings',
                 view_func=BloomFilterView.as_view('bloom_filter_settings'))


@app.route('/api/bloom-filter/memory-size', methods=['GET'])
def get_memory_size_of_bf():
    return jsonify({'memorySize': BloomFilterView().get_memory_size_of_bf()
                   }), 200


if __name__ == '__main__':
    app.run(debug=True)