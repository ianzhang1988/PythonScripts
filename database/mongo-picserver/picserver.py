# coding: utf-8

import tornado.ioloop
import tornado.web
import pymongo, os
import bson.binary
from cStringIO import StringIO

mongo_url = '10.10.65.135'

class UploadFileHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.mongodb_client = self.application.mongodb_client
        self.pic_collection = self.mongodb_client.picture.pic_file

    def get(self):
        self.write('''
        <html>
          <head><title>Upload File</title></head>
          <body>
            <form action='put' enctype="multipart/form-data" method='post'>
            <input type='file' name='file'/><br/>
            <input type='text' name='id'/><br/>
            <input type='submit' value='submit'/>
            </form>
          </body>
        </html>
        ''')

    def post(self):
        # content
        file_metas = self.request.files['file']
        id = self.get_argument('id', None)
        print 'id',id
        if id == None :
            print 'error. argument missed.'
            self.write('error. argument missed.')
            return

        try:
            for meta in file_metas:
                filename = meta['filename']
                content = StringIO(meta['body'])
                self.pic_collection.save(dict(
                    id = id,
                    filename = filename,
                    content = bson.binary.Binary(content.getvalue()),
                ))

        except Exception, ex:
            print 'error. %s' % str(ex)
            self.write('error. %s' % str(ex))
            return

        self.write('finished!')


class DownloadFileHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.mongodb_client = self.application.mongodb_client
        self.pic_collection = self.mongodb_client.picture.pic_file

    def get(self):
        id = self.get_argument('id', None).decode('utf-8')
        file = self.get_argument('file', None).decode('utf-8')

        print 'id',id
        print 'file',file

        if id == None or file == None:
            self.write('no pic.')
            return

        pic = self.pic_collection.find_one(
            dict(
                id = id,
                filename=file
            )
        )

        if not pic:
            self.write('no pic.')
            return

        pic = pic['content']

        self.write(pic)
        self.set_header('Content-Type', 'image/jpeg')
        return

    def post(self):
        pass

    def put(self):
        pass

def main():
    app = tornado.web.Application([
        (r'/put', UploadFileHandler),
        #(r'/pic/(.*)', tornado.web.StaticFileHandler, {'path': db_path}),
        (r'/get', DownloadFileHandler),
    ])

    app.mongodb_client = pymongo.MongoClient(host=mongo_url)

    port = 3000
    print 'pictures server listening port: %d' % port
    app.listen(port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()