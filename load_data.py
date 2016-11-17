import pandas as pd
import ujson as json


def pct_to_int(pct):
    try:
        return int(pct)
    except ValueError:
        return 0


def load_cnn_data(fd):
    data = json.load(fd)
    for poll in data['polls']:
        d = {
            'question': poll['question'].lower(),
            'num_respondents': poll['numrespondents'],
            'question_name': poll['pollname'],
            'qid': poll['qid'],
        }
        leader_lookup = {c['id']: c['fname'].strip() or "N/A"
                         for c in poll['candidates']}
        for ans in poll['answers']:
            d.update({
                'answer': ans['answer'],
                'answer_percent': pct_to_int(ans['pct']),
            })
            for a in ans['candidateanswers']:
                d['candidate'] = leader_lookup[a['id']]
                d['candidate_pct'] = pct_to_int(a['pct'])
                yield d
                d = d.copy()


def cnn_dataframe(fd):
    data_iter = load_cnn_data(fd)
    data = pd.DataFrame.from_dict(data_iter)
    data['candidate'] = data['candidate'].astype('category')
    return data


if __name__ == "__main__":
    # cnn_data.json comes from:
    # http://data.cnn.com/ELECTION/2016/US/xpoll/Pfull.json
    with open("cnn_data.json") as fd:
        data = cnn_dataframe(fd)

