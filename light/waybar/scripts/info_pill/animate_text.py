import sys
import pickle
import time

TMP = "/tmp/waybar-custom-animate_text"
TIME = 1

def anim_trim(text):
    if len(text) > 0:
        return text[1:-1]
    return ""
    
def anim_expand(text,i):
    i = (len(text)//2) - i
    if i <= 0:
        return text
    return text[i:-i]

def anim(text, _id):
    try:
        with open(TMP,"rb") as f:
            prev = pickle.load(f)
    except FileNotFoundError:
        prev = {}

    if prev.get(_id):
        tmp_text = prev[_id]
        for _ in range(len(prev[_id])//2):
            tmp_text = anim_trim(tmp_text)
            yield (tmp_text)
            time.sleep((TIME/(len(prev[_id])//2)))

    tmp_text = ""
    for i in range((len(text)//2)+1):
        tmp_text = anim_expand(text,i)
        yield (tmp_text)
        time.sleep(TIME/(len(text)//2))

    prev[_id] = text

    with open(TMP, 'wb') as f:
        pickle.dump(prev,f)
        
    
if __name__ == "__main__":
    for i in anim(sys.argv[1],sys.argv[2]):
        print(i)




