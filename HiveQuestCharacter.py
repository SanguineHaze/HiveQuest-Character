import os
import re
import random
import json
import datetime

from beem import Hive
from beem.account import Account
from beem.blockchain import Blockchain
from beem.comment import Comment
from beem.instance import set_shared_blockchain_instance
from beem.utils import construct_authorperm

hive = Hive(node=['https://anyx.io/'], keys = ["Public Key"])
set_shared_blockchain_instance(hive)
chain = Blockchain()

print("Loading Bot")

def summoncharbot():
    print(f'[Starting Character Bot]')
    REGEX = '(?<=^|(?<=[^a-zA-Z0-9-.]))@([A-Za-z]+[A-Za-z0-9]+)'
    username = 'sanguinehaze'
    REGCHA = '(?<=^|(?<=[^a-zA-Z0-9-.]))!([A-Za-z]+[A-Za-z0-9]+)'
    newchar = 'generate'

    while True:
        try:
            for post in chain.stream(opNames="comment", threading=True, thread_num=5):
                mentions = re.findall(REGEX, post["body"])
                gen_new_char = re.findall(REGCHA, post["body"])
                comment = Comment(post)
                perm = comment.authorperm
                parent = construct_authorperm(
                    Comment(perm).parent_author, Comment(perm).parent_permlink)
                author = post['author']
                if Comment(perm).is_comment():
                    if username in mentions:
                        comment.reply("Character Generator Bot Summoned! \nUse `!generate` to create a random character.", "", username)
                        commentlink = comment.permlink
                        print("Mention found - Comment made: " + commentlink)
        finally:
            print("Exiting Bot")

summoncharbot()
