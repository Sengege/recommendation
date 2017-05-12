from init import app
#from ui import index
from api import (
 douban
)


if __name__ == '__main__':
    app.run(debug=True,port=5050)
