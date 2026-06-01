import argparse
from datetime import datetime

def greet(name=None, lang="en"):
    # 语言映射
    greetings = {
        'en': {'morning': 'Good morning', 'afternoon': 'Good afternoon', 'evening': 'Good evening'},
        'zh': {'morning': '早上好', 'afternoon': '下午好', 'evening': '晚上好'}
    }
    
    # 获取时段
    hour = datetime.now().hour
    if hour < 12:
        period = 'morning'
    elif hour < 18:
        period = 'afternoon'
    else:
        period = 'evening'
    
    # 获取问候语
    prefix = greetings.get(lang, greetings['en'])[period]
    
    # 返回问候语
    if name:
        return f"{prefix}, {name}!"
    return f"{prefix}!"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', type=str, help='Your name')
    parser.add_argument('--lang', type=str, default='en', choices=['en', 'zh'])
    args = parser.parse_args()
    
    print(greet(args.name, args.lang))