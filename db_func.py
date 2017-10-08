def fetch(posts, db,issue_no):
     return (posts, db, posts.find_one({"issue_no" : issue_no}))

def update_tag(posts,db,issue_no,tag):
    print 'intial tag = ', posts.find_one({"issue_no": issue_no})[u'tag']
    db.posts.update_one({
        'issue_no': issue_no
    }, {
        '$set': {
            'tag'   :tag
        }
    }, upsert=False)
    print 'After Updating tags = ', posts.find_one({"issue_no": issue_no})[u'tag']
    return (posts,db)


def update_status( posts, db,issue_no,status):
    print 'initial status = ', posts.find_one({"issue_no": issue_no})[u'status']
    db.posts.update_one({
        'issue_no': issue_no
    }, {    
        '$set': {
            'status': status
        }
    }, upsert=False)
    print 'After updating status : ', posts.find_one({"issue_no": issue_no})[u'status']
    return (posts,db)