import redis
from flask import Flask

app=Flask(__name__)
db_cache = redis.Redis(host='redis',port=6379)
# db_cache = redis.Redis()

def web_hit_count():
    return db_cache.incr('hits')

@app.route('/')
def home():
    cnt = web_hit_count()
    return '''
            <h1> Docker compose app </h1>
            <p> Web access count : {} times </p>'''.format(cnt)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)