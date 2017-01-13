from util.hook import *
from util import web


@hook(cmds=['chuck', 'cn'], rate=10)
def chuck(code, input):
    """Get random Chuck Norris facts. I bet he's better than you."""
    try:
        if input.group(2) and input.group(2).isdigit():
            data = web.json('http://api.icndb.com/jokes/' + input.group(2))
        else:
            data = web.json('http://api.icndb.com/jokes/random')
    except:
        return code.say('Chuck seems to be in the way. I\'m not fucking with him.')
    code.say('#{blue}%s{c} - %s' % (data['value']['id'], web.escape(data['value']['joke'])))
