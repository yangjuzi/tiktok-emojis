import os
import re

# 表情信息映射
# 表情信息映射
EMOJI_INFO = {
    'smile': {
        'name': 'Smile',
        'categories': ['Emotion', 'Positive', 'Expression'],
        'meaning': 'The smile emoji represents happiness, joy, or positivity.',
        'uses': [
            'Showing happiness',
            'Expressing joy',
            'Reacting to positive content',
            'Showing positivity'
        ],
        'usage_tips': [
            'In comments to show happiness',
            'In captions to express joy',
            'In reaction to positive content',
            'In cheerful messages'
        ],
        'related': ['happy', 'joyful', 'excited']
    },
    'happy': {
        'name': 'Happy',
        'categories': ['Emotion', 'Positive', 'Expression'],
        'meaning': 'The happy emoji represents joy, happiness, or contentment.',
        'uses': [
            'Showing joy',
            'Expressing happiness',
            'Reacting to positive content',
            'Showing contentment'
        ],
        'usage_tips': [
            'In comments to show joy',
            'In captions to express happiness',
            'In reaction to positive content',
            'In cheerful messages'
        ],
        'related': ['smile', 'joyful', 'excited']
    },
    'angry': {
        'name': 'Angry',
        'categories': ['Emotion', 'Negative', 'Expression'],
        'meaning': 'The angry emoji represents frustration, irritation, and strong negative emotions.',
        'uses': [
            'Frustration and annoyance',
            'Strong disagreement',
            'Intense negative emotions',
            'Expressing anger in a playful way'
        ],
        'usage_tips': [
            'In comments to express disagreement',
            'In captions to show frustration',
            'In reaction videos',
            'In humorous contexts'
        ],
        'related': ['rage', 'furious', 'annoyed']
    },
    'cry': {
        'name': 'Cry',
        'categories': ['Emotion', 'Sad', 'Expression'],
        'meaning': 'The cry emoji represents sadness, disappointment, or emotional pain.',
        'uses': [
            'Expressing sadness',
            'Showing disappointment',
            'Reacting to emotional content',
            'Expressing sympathy'
        ],
        'usage_tips': [
            'In comments to show sadness',
            'In captions to express disappointment',
            'In emotional reaction videos',
            'In supportive messages'
        ],
        'related': ['tears', 'weep', 'sad']
    },
    'embarrassed': {
        'name': 'Embarrassed',
        'categories': ['Emotion', 'Shy', 'Expression'],
        'meaning': 'The embarrassed emoji represents shyness, awkwardness, or feeling self-conscious.',
        'uses': [
            'Showing shyness',
            'Expressing awkwardness',
            'Reacting to embarrassing situations',
            'Showing self-consciousness'
        ],
        'usage_tips': [
            'In comments to show shyness',
            'In captions to express awkwardness',
            'In reaction to embarrassing content',
            'In self-deprecating messages'
        ],
        'related': ['blush', 'awkward', 'flushed']
    },
    'surprised': {
        'name': 'Surprised',
        'categories': ['Emotion', 'Shock', 'Expression'],
        'meaning': 'The surprised emoji represents shock, amazement, or unexpected reactions.',
        'uses': [
            'Showing shock',
            'Expressing amazement',
            'Reacting to surprises',
            'Showing unexpected reactions'
        ],
        'usage_tips': [
            'In comments to show shock',
            'In captions to express amazement',
            'In reaction to surprises',
            'In unexpected content'
        ],
        'related': ['shock', 'astonish', 'wow']
    },
    'wronged': {
        'name': 'Wronged',
        'categories': ['Emotion', 'Negative', 'Expression'],
        'meaning': 'The wronged emoji represents feeling hurt, betrayed, or unfairly treated.',
        'uses': [
            'Showing hurt feelings',
            'Expressing betrayal',
            'Reacting to unfair treatment',
            'Showing emotional pain'
        ],
        'usage_tips': [
            'In comments to show hurt feelings',
            'In captions to express betrayal',
            'In emotional reaction videos',
            'In supportive messages'
        ],
        'related': ['cry', 'sad', 'hurt']
    },
    'shout': {
        'name': 'Shout',
        'categories': ['Emotion', 'Intense', 'Expression'],
        'meaning': 'The shout emoji represents loud expression, excitement, or strong emotions.',
        'uses': [
            'Showing excitement',
            'Expressing strong emotions',
            'Reacting to intense content',
            'Showing enthusiasm'
        ],
        'usage_tips': [
            'In comments to show excitement',
            'In captions to express strong emotions',
            'In reaction to intense content',
            'In enthusiastic messages'
        ],
        'related': ['excited', 'scream', 'wow']
    },
    'flushed': {
        'name': 'Flushed',
        'categories': ['Emotion', 'Shy', 'Expression'],
        'meaning': 'The flushed emoji represents embarrassment, shyness, or feeling flustered.',
        'uses': [
            'Showing embarrassment',
            'Expressing shyness',
            'Reacting to awkward situations',
            'Showing being flustered'
        ],
        'usage_tips': [
            'In comments to show embarrassment',
            'In captions to express shyness',
            'In reaction to awkward content',
            'In self-conscious messages'
        ],
        'related': ['blush', 'embarrassed', 'awkward']
    },
    'yummy': {
        'name': 'Yummy',
        'categories': ['Food', 'Positive', 'Expression'],
        'meaning': 'The yummy emoji represents delicious food, enjoyment, or satisfaction.',
        'uses': [
            'Showing food enjoyment',
            'Expressing satisfaction',
            'Reacting to food content',
            'Showing appreciation'
        ],
        'usage_tips': [
            'In comments about food',
            'In captions about meals',
            'In food reaction videos',
            'In appreciation messages'
        ],
        'related': ['drool', 'happy', 'excited']
    },
    'complacent': {
        'name': 'Complacent',
        'categories': ['Emotion', 'Neutral', 'Expression'],
        'meaning': 'The complacent emoji represents satisfaction, contentment, or self-satisfaction.',
        'uses': [
            'Showing satisfaction',
            'Expressing contentment',
            'Reacting to achievements',
            'Showing self-satisfaction'
        ],
        'usage_tips': [
            'In comments to show satisfaction',
            'In captions to express contentment',
            'In achievement videos',
            'In self-satisfied messages'
        ],
        'related': ['smile', 'proud', 'happy']
    },
    'drool': {
        'name': 'Drool',
        'categories': ['Food', 'Desire', 'Expression'],
        'meaning': 'The drool emoji represents desire, craving, or strong interest.',
        'uses': [
            'Showing desire',
            'Expressing craving',
            'Reacting to attractive content',
            'Showing strong interest'
        ],
        'usage_tips': [
            'In comments about food',
            'In captions about desires',
            'In reaction to attractive content',
            'In craving messages'
        ],
        'related': ['yummy', 'greedy', 'excited']
    },
    'scream': {
        'name': 'Scream',
        'categories': ['Emotion', 'Intense', 'Expression'],
        'meaning': 'The scream emoji represents extreme emotions, shock, or intense reactions.',
        'uses': [
            'Showing extreme emotions',
            'Expressing shock',
            'Reacting to intense content',
            'Showing intense reactions'
        ],
        'usage_tips': [
            'In comments to show extreme emotions',
            'In captions to express shock',
            'In reaction to intense content',
            'In intense messages'
        ],
        'related': ['shock', 'surprised', 'wow']
    },
    'weep': {
        'name': 'Weep',
        'categories': ['Emotion', 'Sad', 'Expression'],
        'meaning': 'The weep emoji represents intense sadness, grief, or emotional pain.',
        'uses': [
            'Expressing intense sadness',
            'Showing grief',
            'Reacting to emotional content',
            'Expressing deep sympathy'
        ],
        'usage_tips': [
            'In comments to show intense sadness',
            'In captions to express grief',
            'In emotional reaction videos',
            'In supportive messages'
        ],
        'related': ['cry', 'tears', 'sad']
    },
    'speechless': {
        'name': 'Speechless',
        'categories': ['Emotion', 'Shock', 'Expression'],
        'meaning': 'The speechless emoji represents being at a loss for words, shock, or disbelief.',
        'uses': [
            'Showing being speechless',
            'Expressing shock',
            'Reacting to surprising content',
            'Showing disbelief'
        ],
        'usage_tips': [
            'In comments to show being speechless',
            'In captions to express shock',
            'In reaction to surprising content',
            'In shocked messages'
        ],
        'related': ['surprised', 'shock', 'astonish']
    },
    'funnyface': {
        'name': 'Funny Face',
        'categories': ['Emotion', 'Funny', 'Expression'],
        'meaning': 'The funny face emoji represents humor, playfulness, or making jokes.',
        'uses': [
            'Showing humor',
            'Expressing playfulness',
            'Reacting to funny content',
            'Making jokes'
        ],
        'usage_tips': [
            'In comments to show humor',
            'In captions to express playfulness',
            'In reaction to funny content',
            'In humorous messages'
        ],
        'related': ['laugh', 'hehe', 'smile']
    },
    'laughwithtears': {
        'name': 'Laugh with Tears',
        'categories': ['Emotion', 'Happy', 'Expression'],
        'meaning': 'The laugh with tears emoji represents extreme happiness, joy, or finding something very funny.',
        'uses': [
            'Showing extreme happiness',
            'Expressing joy',
            'Reacting to very funny content',
            'Showing intense amusement'
        ],
        'usage_tips': [
            'In comments to show extreme happiness',
            'In captions to express joy',
            'In reaction to very funny content',
            'In amused messages'
        ],
        'related': ['laugh', 'happy', 'joyful']
    },
    'wicked': {
        'name': 'Wicked',
        'categories': ['Emotion', 'Mischievous', 'Expression'],
        'meaning': 'The wicked emoji represents mischief, playfulness, or being up to no good.',
        'uses': [
            'Showing mischief',
            'Expressing playfulness',
            'Reacting to pranks',
            'Showing being up to no good'
        ],
        'usage_tips': [
            'In comments to show mischief',
            'In captions to express playfulness',
            'In prank videos',
            'In mischievous messages'
        ],
        'related': ['evil', 'mischievous', 'smirk']
    },
    'facewithrollingeyes': {
        'name': 'Face with Rolling Eyes',
        'categories': ['Emotion', 'Skeptical', 'Expression'],
        'meaning': 'The face with rolling eyes emoji represents skepticism, disbelief, or being unimpressed.',
        'uses': [
            'Showing skepticism',
            'Expressing disbelief',
            'Reacting to unimpressive content',
            'Showing being unimpressed'
        ],
        'usage_tips': [
            'In comments to show skepticism',
            'In captions to express disbelief',
            'In reaction to unimpressive content',
            'In skeptical messages'
        ],
        'related': ['side-eye', 'disdain', 'suspicious']
    },
    'sulk': {
        'name': 'Sulk',
        'categories': ['Emotion', 'Negative', 'Expression'],
        'meaning': 'The sulk emoji represents being in a bad mood, sulking, or feeling grumpy.',
        'uses': [
            'Showing bad mood',
            'Expressing sulking',
            'Reacting to negative situations',
            'Showing being grumpy'
        ],
        'usage_tips': [
            'In comments to show bad mood',
            'In captions to express sulking',
            'In reaction to negative content',
            'In grumpy messages'
        ],
        'related': ['angry', 'disdain', 'annoyed']
    },
    'thinking': {
        'name': 'Thinking',
        'categories': ['Emotion', 'Neutral', 'Expression'],
        'meaning': 'The thinking emoji represents contemplation, consideration, or being in thought.',
        'uses': [
            'Showing contemplation',
            'Expressing consideration',
            'Reacting to thoughtful content',
            'Showing being in thought'
        ],
        'usage_tips': [
            'In comments to show contemplation',
            'In captions to express consideration',
            'In reaction to thoughtful content',
            'In thoughtful messages'
        ],
        'related': ['confused', 'puzzled', 'curious']
    },
    'lovely': {
        'name': 'Lovely',
        'categories': ['Emotion', 'Positive', 'Expression'],
        'meaning': 'The lovely emoji represents love, affection, or endearment.',
        'uses': [
            'Showing love',
            'Expressing affection',
            'Reacting to cute content',
            'Showing endearment'
        ],
        'usage_tips': [
            'In comments to show love',
            'In captions to express affection',
            'In reaction to cute content',
            'In romantic messages'
        ],
        'related': ['loveface', 'happy', 'smile']
    },
    'greedy': {
        'name': 'Greedy',
        'categories': ['Emotion', 'Desire', 'Expression'],
        'meaning': 'The greedy emoji represents desire, wanting more, or being greedy.',
        'uses': [
            'Showing desire',
            'Expressing wanting more',
            'Reacting to desirable content',
            'Showing being greedy'
        ],
        'usage_tips': [
            'In comments to show desire',
            'In captions to express wanting more',
            'In reaction to desirable content',
            'In greedy messages'
        ],
        'related': ['drool', 'excited', 'happy']
    },
    'wow': {
        'name': 'Wow',
        'categories': ['Emotion', 'Surprise', 'Expression'],
        'meaning': 'The wow emoji represents amazement, admiration, or surprise.',
        'uses': [
            'Showing amazement',
            'Expressing admiration',
            'Reacting to impressive content',
            'Showing surprise'
        ],
        'usage_tips': [
            'In comments to show amazement',
            'In captions to express admiration',
            'In reaction to impressive content',
            'In amazed messages'
        ],
        'related': ['surprised', 'shock', 'astonish']
    },
    'joyful': {
        'name': 'Joyful',
        'categories': ['Emotion', 'Positive', 'Expression'],
        'meaning': 'The joyful emoji represents extreme happiness, delight, or elation.',
        'uses': [
            'Showing extreme happiness',
            'Expressing delight',
            'Reacting to exciting content',
            'Showing elation'
        ],
        'usage_tips': [
            'In comments to show extreme happiness',
            'In captions to express delight',
            'In reaction to exciting content',
            'In cheerful messages'
        ],
        'related': ['happy', 'smile', 'excited']
    },
    'hehe': {
        'name': 'Hehe',
        'categories': ['Emotion', 'Funny', 'Expression'],
        'meaning': 'The hehe emoji represents playful laughter, mischief, or being up to something.',
        'uses': [
            'Showing playful laughter',
            'Expressing mischief',
            'Reacting to funny content',
            'Showing being up to something'
        ],
        'usage_tips': [
            'In comments to show playful laughter',
            'In captions to express mischief',
            'In reaction to funny content',
            'In playful messages'
        ],
        'related': ['laugh', 'funnyface', 'smile']
    },
    'slap': {
        'name': 'Slap',
        'categories': ['Action', 'Negative', 'Expression'],
        'meaning': 'The slap emoji represents physical reaction, frustration, or wanting to hit something.',
        'uses': [
            'Showing physical reaction',
            'Expressing frustration',
            'Reacting to annoying content',
            'Showing wanting to hit something'
        ],
        'usage_tips': [
            'In comments to show physical reaction',
            'In captions to express frustration',
            'In reaction to annoying content',
            'In frustrated messages'
        ],
        'related': ['angry', 'rage', 'furious']
    },
    'tears': {
        'name': 'Tears',
        'categories': ['Emotion', 'Sad', 'Expression'],
        'meaning': 'The tears emoji represents crying, sadness, or emotional release.',
        'uses': [
            'Expressing deep sadness',
            'Showing emotional release',
            'Reacting to emotional content',
            'Expressing sympathy'
        ],
        'usage_tips': [
            'In comments to show deep sadness',
            'In captions to express emotional release',
            'In emotional reaction videos',
            'In supportive messages'
        ],
        'related': ['cry', 'weep', 'sad']
    },
    'stun': {
        'name': 'Stun',
        'categories': ['Emotion', 'Shock', 'Expression'],
        'meaning': 'The stun emoji represents being stunned, shocked, or overwhelmed.',
        'uses': [
            'Showing being stunned',
            'Expressing shock',
            'Reacting to overwhelming content',
            'Showing being overwhelmed'
        ],
        'usage_tips': [
            'In comments to show being stunned',
            'In captions to express shock',
            'In reaction to overwhelming content',
            'In shocked messages'
        ],
        'related': ['surprised', 'shock', 'astonish']
    },
    'cute': {
        'name': 'Cute',
        'categories': ['Character', 'Positive', 'Expression'],
        'meaning': 'The cute emoji represents adorableness, charm, and endearing qualities.',
        'uses': [
            'Showing adorableness',
            'Expressing charm',
            'Reacting to cute content',
            'Showing affection'
        ],
        'usage_tips': [
            'In comments to show adorableness',
            'In captions to express charm',
            'In reaction to cute content',
            'In affectionate messages'
        ],
        'related': ['lovely', 'happy', 'smile']
    },
    'blink': {
        'name': 'Blink',
        'categories': ['Emotion', 'Neutral', 'Expression'],
        'meaning': 'The blink emoji represents surprise, confusion, or being taken aback.',
        'uses': [
            'Showing surprise',
            'Expressing confusion',
            'Reacting to unexpected content',
            'Showing being taken aback'
        ],
        'usage_tips': [
            'In comments to show surprise',
            'In captions to express confusion',
            'In reaction to unexpected content',
            'In surprised messages'
        ],
        'related': ['surprised', 'confused', 'astonish']
    },
    'disdain': {
        'name': 'Disdain',
        'categories': ['Emotion', 'Negative', 'Expression'],
        'meaning': 'The disdain emoji represents contempt, scorn, or looking down on something.',
        'uses': [
            'Showing contempt',
            'Expressing scorn',
            'Reacting to disliked content',
            'Showing looking down on something'
        ],
        'usage_tips': [
            'In comments to show contempt',
            'In captions to express scorn',
            'In reaction to disliked content',
            'In disdainful messages'
        ],
        'related': ['side-eye', 'facewithrollingeyes', 'sulk']
    },
    'astonish': {
        'name': 'Astonish',
        'categories': ['Emotion', 'Surprise', 'Expression'],
        'meaning': 'The astonish emoji represents amazement, wonder, or awe.',
        'uses': [
            'Showing amazement',
            'Expressing wonder',
            'Reacting to amazing content',
            'Showing awe'
        ],
        'usage_tips': [
            'In comments to show amazement',
            'In captions to express wonder',
            'In reaction to amazing content',
            'In amazed messages'
        ],
        'related': ['surprised', 'shock', 'wow']
    },
    'rage': {
        'name': 'Rage',
        'categories': ['Emotion', 'Negative', 'Expression'],
        'meaning': 'The rage emoji represents extreme anger, fury, or intense frustration.',
        'uses': [
            'Showing extreme anger',
            'Expressing fury',
            'Reacting to frustrating content',
            'Showing intense frustration'
        ],
        'usage_tips': [
            'In comments to show extreme anger',
            'In captions to express fury',
            'In reaction to frustrating content',
            'In angry messages'
        ],
        'related': ['angry', 'furious', 'slap']
    },
    'cool': {
        'name': 'Cool',
        'categories': ['Emotion', 'Positive', 'Expression'],
        'meaning': 'The cool emoji represents being cool, calm, or collected.',
        'uses': [
            'Showing being cool',
            'Expressing calmness',
            'Reacting to cool content',
            'Showing being collected'
        ],
        'usage_tips': [
            'In comments to show being cool',
            'In captions to express calmness',
            'In reaction to cool content',
            'In cool messages'
        ],
        'related': ['smirk', 'proud', 'confident']
    },
    'excited': {
        'name': 'Excited',
        'categories': ['Emotion', 'Positive', 'Expression'],
        'meaning': 'The excited emoji represents enthusiasm, excitement, or anticipation.',
        'uses': [
            'Showing enthusiasm',
            'Expressing excitement',
            'Reacting to exciting content',
            'Showing anticipation'
        ],
        'usage_tips': [
            'In comments to show enthusiasm',
            'In captions to express excitement',
            'In reaction to exciting content',
            'In enthusiastic messages'
        ],
        'related': ['happy', 'joyful', 'smile']
    },
    'proud': {
        'name': 'Proud',
        'categories': ['Emotion', 'Positive', 'Expression'],
        'meaning': 'The proud emoji represents pride, accomplishment, or self-satisfaction.',
        'uses': [
            'Showing pride',
            'Expressing accomplishment',
            'Reacting to achievements',
            'Showing self-satisfaction'
        ],
        'usage_tips': [
            'In comments to show pride',
            'In captions to express accomplishment',
            'In achievement videos',
            'In proud messages'
        ],
        'related': ['smile', 'happy', 'confident']
    },
    'smileface': {
        'name': 'Smile Face',
        'categories': ['Emotion', 'Positive', 'Expression'],
        'meaning': 'The smile face emoji represents happiness, joy, or positivity.',
        'uses': [
            'Showing happiness',
            'Expressing joy',
            'Reacting to positive content',
            'Showing positivity'
        ],
        'usage_tips': [
            'In comments to show happiness',
            'In captions to express joy',
            'In reaction to positive content',
            'In cheerful messages'
        ],
        'related': ['smile', 'happy', 'joyful']
    },
    'evil': {
        'name': 'Evil',
        'categories': ['Character', 'Negative', 'Expression'],
        'meaning': 'The evil emoji represents mischief, wickedness, or playful villainy.',
        'uses': [
            'Showing mischief',
            'Expressing wickedness',
            'Reacting to pranks',
            'Showing playful villainy'
        ],
        'usage_tips': [
            'In comments to show mischief',
            'In captions to express wickedness',
            'In prank videos',
            'In playful villain contexts'
        ],
        'related': ['wicked', 'mischievous', 'devil']
    },
    'angel': {
        'name': 'Angel',
        'categories': ['Character', 'Positive', 'Expression'],
        'meaning': 'The angel emoji represents innocence, goodness, or being angelic.',
        'uses': [
            'Showing innocence',
            'Expressing goodness',
            'Reacting to pure content',
            'Showing being angelic'
        ],
        'usage_tips': [
            'In comments to show innocence',
            'In captions to express goodness',
            'In reaction to pure content',
            'In angelic messages'
        ],
        'related': ['lovely', 'happy', 'smile']
    },
    'laugh': {
        'name': 'Laugh',
        'categories': ['Emotion', 'Happy', 'Expression'],
        'meaning': 'The laugh emoji represents laughter, joy, or finding something funny.',
        'uses': [
            'Showing laughter',
            'Expressing joy',
            'Reacting to funny content',
            'Showing finding something funny'
        ],
        'usage_tips': [
            'In comments to show laughter',
            'In captions to express joy',
            'In reaction to funny content',
            'In happy messages'
        ],
        'related': ['happy', 'joyful', 'smile']
    },
    'pride': {
        'name': 'Pride',
        'categories': ['Emotion', 'Positive', 'Expression'],
        'meaning': 'The pride emoji represents pride, accomplishment, or self-satisfaction.',
        'uses': [
            'Showing pride',
            'Expressing accomplishment',
            'Reacting to achievements',
            'Showing self-satisfaction'
        ],
        'usage_tips': [
            'In comments to show pride',
            'In captions to express accomplishment',
            'In achievement videos',
            'In proud messages'
        ],
        'related': ['proud', 'happy', 'confident']
    },
    'nap': {
        'name': 'Nap',
        'categories': ['Action', 'Neutral', 'Expression'],
        'meaning': 'The nap emoji represents sleepiness, tiredness, or taking a rest.',
        'uses': [
            'Showing sleepiness',
            'Expressing tiredness',
            'Reacting to tiring content',
            'Showing taking a rest'
        ],
        'usage_tips': [
            'In comments to show sleepiness',
            'In captions to express tiredness',
            'In reaction to tiring content',
            'In tired messages'
        ],
        'related': ['sleepy', 'tired', 'relaxed']
    },
    'loveface': {
        'name': 'Love Face',
        'categories': ['Emotion', 'Love', 'Expression'],
        'meaning': 'The love face emoji represents love, adoration, or being smitten.',
        'uses': [
            'Showing love',
            'Expressing adoration',
            'Reacting to romantic content',
            'Showing being smitten'
        ],
        'usage_tips': [
            'In comments to show love',
            'In captions to express adoration',
            'In reaction to romantic content',
            'In romantic messages'
        ],
        'related': ['lovely', 'happy', 'smile']
    },
    'awkward': {
        'name': 'Awkward',
        'categories': ['Emotion', 'Uncomfortable', 'Expression'],
        'meaning': 'The awkward emoji represents awkwardness, discomfort, or social anxiety.',
        'uses': [
            'Showing awkwardness',
            'Expressing discomfort',
            'Reacting to awkward situations',
            'Showing social anxiety'
        ],
        'usage_tips': [
            'In comments to show awkwardness',
            'In captions to express discomfort',
            'In reaction to awkward content',
            'In uncomfortable messages'
        ],
        'related': ['embarrassed', 'flushed', 'uncomfortable']
    },
    'shock': {
        'name': 'Shock',
        'categories': ['Emotion', 'Surprise', 'Expression'],
        'meaning': 'The shock emoji represents surprise, astonishment, or disbelief.',
        'uses': [
            'Showing surprise',
            'Expressing astonishment',
            'Reacting to shocking content',
            'Showing disbelief'
        ],
        'usage_tips': [
            'In comments to show surprise',
            'In captions to express astonishment',
            'In reaction to shocking content',
            'In surprised messages'
        ],
        'related': ['surprised', 'astonish', 'wow']
    }
}
def read_template():
    with open('template.html', 'r', encoding='utf-8') as f:
        return f.read()

def generate_emoji_page(emoji_code, template):
    if emoji_code not in EMOJI_INFO:
        return None
    
    info = EMOJI_INFO[emoji_code]
    
    # 替换模板中的占位符
    content = template
    content = content.replace('{{EMOJI_NAME}}', info['name'])
    content = content.replace('{{EMOJI_CODE}}', emoji_code)
    content = content.replace('{{EMOJI_IMAGE}}', f'{emoji_code}.png')
    content = content.replace('{{EMOJI_MEANING}}', info['meaning'])  # 添加meaning的替换
    
    # 生成分类标签
    category_tags = '\n'.join([f'<span class="category-tag">{cat}</span>' for cat in info['categories']])
    content = content.replace('{{CATEGORY_TAGS}}', category_tags)
    
    # 生成表情用途
    emoji_uses = '\n'.join([f'<li>{use}</li>' for use in info['uses']])
    content = content.replace('{{EMOJI_USES}}', emoji_uses)
    
    # 生成使用提示
    usage_tips = '\n'.join([f'<li>{tip}</li>' for tip in info['usage_tips']])
    content = content.replace('{{USAGE_TIPS}}', usage_tips)
    
    # 生成相关表情
    related_emojis = []
    for related in info['related']:
        if related in EMOJI_INFO:
            related_emojis.append(f'''
                <div class="related-emoji" onclick="window.location.href='{related}.html'">
                    <img src="./static/{related}.png" alt="{EMOJI_INFO[related]['name']} Emoji">
                    <p>{EMOJI_INFO[related]['name']}</p>
                </div>
            ''')
    content = content.replace('{{RELATED_EMOJIS}}', '\n'.join(related_emojis))
    
    return content

def main():
    # 读取模板
    template = read_template()
    
    # 为每个表情生成页面
    for emoji_code in EMOJI_INFO:
        content = generate_emoji_page(emoji_code, template)
        if content:
            # 写入文件
            with open(f'{emoji_code}.html', 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Generated {emoji_code}.html')

if __name__ == '__main__':
    main()