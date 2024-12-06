#!/usr/bin/env python3
import os
import shutil
import re

# 定义翻译内容
translations = {
    'en': {
        'home': 'Home',
        'themes': 'Themes',
        'language': 'Language',
        'chineseZodiac': 'Chinese Zodiac',
        'taylorSwift': 'Taylor Swift',
        'welcome': 'Welcome to 2048 Game Series! Try our themed versions:',
        'newGame': 'New Game',
        'score': 'SCORE',
        'best': 'BEST',
        'gameOver': 'Game Over!',
        'tryAgain': 'Try again',
        'won': 'You win!',
        'keepGoing': 'Keep going',
        'howToPlay': 'How to play',
        'gameIntro': 'Join numbers and get to the <strong>2048 tile!</strong>',
        'gameExplanation': 'Use your <strong>arrow keys</strong> to move the tiles. When two tiles with the same number touch, they <strong>merge into one!</strong>',
        'about': 'About 2048',
        'aboutText': '2048 is an addictive puzzle game created by Gabriele Cirulli in March 2014. The game quickly became a worldwide phenomenon, spawning numerous variations and adaptations. The objective is simple yet challenging: combine matching numbers to create the tile with the number 2048.',
        'gameMechanics': 'Game Mechanics',
        'mechanicsText': 'Players slide numbered tiles on a 4x4 grid using arrow keys. When two tiles with the same number collide, they merge into one tile with their sum. The game continues until you either create the 2048 tile (victory) or can no longer make any moves (game over).',
        'themedVersions': 'Our Themed Versions',
        'shareTwitter': 'Share on Twitter',
        'shareXiaohongshu': 'Share on Little Red Book',
        # Zodiac主题特有的翻译
        'zodiacTitle': 'Chinese Zodiac 2048',
        'zodiacDescription': 'Experience the traditional Chinese zodiac cycle through gameplay.',
        'zodiacIntro': 'Combine zodiac animals to complete the cycle!',
        'zodiacStory': 'The Chinese Zodiac Story',
        'zodiacStoryText': 'The Chinese zodiac, known as Sheng Xiao (生肖), is a repeating 12-year cycle of animal signs. According to legend, the Jade Emperor held a great race across a river to determine the order of the zodiac animals. The clever Rat, hardworking Ox, brave Tiger, and nine other animals each earned their place in this ancient tradition.',
        'zodiacCycle': 'The Zodiac Cycle in Our Game',
        'zodiacCycleText': 'In this special edition of 2048, we\'ve incorporated all twelve zodiac animals in their traditional order:',
        'zodiacCycleList_0': 'Start with the Rat (鼠) and Ox (牛)',
        'zodiacCycleList_1': 'Combine them to create the Tiger (虎)',
        'zodiacCycleList_2': 'Progress through Rabbit (兔), Dragon (龙), Snake (蛇)',
        'zodiacCycleList_3': 'Continue with Horse (马), Goat (羊), Monkey (猴)',
        'zodiacCycleList_4': 'Finally reach Rooster (鸡), Dog (狗), and Pig (猪)',
        'culturalSignificance': 'Cultural Significance',
        'culturalSignificanceText': 'Each zodiac animal carries unique characteristics and symbolism in Chinese culture. As you play, you\'ll discover the complete cycle of these beloved zodiac animals, making this more than just a game - it\'s a journey through Chinese tradition.',
        'rat': 'Rat',
        'ox': 'Ox',
        'tiger': 'Tiger',
        'rabbit': 'Rabbit',
        'dragon': 'Dragon',
        'snake': 'Snake',
        'horse': 'Horse',
        'goat': 'Goat',
        'monkey': 'Monkey',
        'rooster': 'Rooster',
        'dog': 'Dog',
        'pig': 'Pig',
        # Taylor Swift主题特有的翻译
        'taylorTitle': 'Taylor Swift 2048',
        'taylorDescription': 'A special edition celebrating Taylor Swift through AI-generated artistic portraits.',
        'taylorIntro': 'Combine portraits to discover unique artistic interpretations of Taylor!',
        'eraDescription': 'Experience Taylor\'s artistic journey through AI-generated portraits.',
        'aiArtDescription': 'This special edition celebrates Taylor Swift through the lens of artificial intelligence. We\'ve used AI technology to create unique artistic interpretations of Taylor, each capturing different aspects of her style and personality.',
        'gameplayFeatures': 'Gameplay Features',
        'gameplayText': 'As you play, you\'ll discover various AI-generated portraits of Taylor:',
        'featuresList_0': 'Start with classic portrait styles of Taylor',
        'featuresList_1': 'Combine tiles to reveal more artistic interpretations',
        'featuresList_2': 'Progress through various artistic styles and moods',
        'featuresList_3': 'Experience different facets of Taylor\'s persona',
        'featuresList_4': 'Discover unique AI-generated artistic renditions',
        'featuresList_5': 'Reach the ultimate Taylor portrait at 2048',
        'forSwifties': 'For Swifties',
        'swiftiesText': 'This game is more than just a puzzle - it\'s an artistic tribute to Taylor Swift, combining modern AI technology with gaming. Each merge reveals a new AI-generated interpretation of Taylor, creating a unique blend of art, technology, and fandom.',
        'debut': 'Debut',
        'fearless': 'Fearless',
        'speakNow': 'Speak Now',
        'red': 'Red',
        '1989': '1989',
        'reputation': 'Reputation',
        'lover': 'Lover',
        'folklore': 'Folklore',
        'evermore': 'Evermore',
        'midnights': 'Midnights',
        'shareTwitter': 'Share on Twitter',
        'shareXiaohongshu': 'Share on Little Red Book'
    },
    'cn': {
        'home': '首页',
        'themes': '主题',
        'language': '语言',
        'chineseZodiac': '生肖版',
        'taylorSwift': '泰勒斯威夫特版',
        'welcome': '欢迎来到2048游戏系列！尝试我们的主题版本：',
        'newGame': '新游戏',
        'score': '得分',
        'best': '最佳',
        'gameOver': '游戏结束！',
        'tryAgain': '再试一次',
        'won': '你赢了！',
        'keepGoing': '继续游戏',
        'howToPlay': '游戏规则',
        'gameIntro': '合并数字，获得 <strong>2048</strong> 方块！',
        'gameExplanation': '使用<strong>方向键</strong>移动方块。当两个相同数字的方块相撞时，它们会<strong>合并成一个！</strong>',
        'about': '关于2048',
        'aboutText': '2048是由Gabriele Cirulli于2014年3月创建的一款令人上瘾的益智游戏。这个游戏迅速成为全球现象，衍生出众多变体和改编版本。游戏目标简单而具有挑战性合并相同的数字以创建数字2048的方块。',
        'gameMechanics': '游戏机制',
        'mechanicsText': '玩家使用方向键在4x4网格上滑动数字方块。当两个相同数字的方块碰撞时，它们会合并成一个新的方块，数字为两者之和。游戏持续进行，直到你创建出2048方块（胜利）或无法继续移动（游戏结束）。',
        'themedVersions': '主题版本',
        'shareTwitter': '分享到推特',
        'shareXiaohongshu': '分享到小红书',
        # Zodiac主题特有的翻译
        'zodiacTitle': '2048生肖版',
        'zodiacDescription': '体验传统中国生肖循环的游戏玩法。',
        'zodiacIntro': '合并生肖动物，完成十二生肖循环！',
        'zodiacStory': '生肖的故事',
        'zodiacStoryText': '中国生肖（Sheng Xiao，生肖）是一个12年为周期的动物符号循环。据传说，玉皇大帝举办了一场横渡河流的比赛来决定生肖的顺序。机智的老鼠、勤劳的牛、勇猛的虎，以及其他九种动物，都在这个古老的传统中赢得了各自的位置。',
        'zodiacCycle': '游戏中的生肖循环',
        'zodiacCycleText': '在这个特别版本中，我们融入了十二生肖的传统顺序：',
        'zodiacCycleList_0': '从鼠（鼠）和牛（牛）开始',
        'zodiacCycleList_1': '合并它们创造出虎（虎）',
        'zodiacCycleList_2': '继续通过兔（兔）、龙（龙）、蛇（蛇）',
        'zodiacCycleList_3': '然后是马（马）、羊（羊）、猴（猴）',
        'zodiacCycleList_4': '最后到达鸡（鸡）狗（狗）和猪（猪）',
        'culturalSignificance': '文化意义',
        'culturalSignificanceText': '每个生肖动物在中国文化中都承载着独特的特征和象征意义。在游戏过程中，你将发现这些备受喜爱的生肖动物的完整循环，这不仅仅是一个游戏 - 这是一次穿越中国传统的旅程。',
        'rat': '鼠',
        'ox': '牛',
        'tiger': '虎',
        'rabbit': '兔',
        'dragon': '龙',
        'snake': '蛇',
        'horse': '马',
        'goat': '羊',
        'monkey': '猴',
        'rooster': '鸡',
        'dog': '狗',
        'pig': '猪',
        # Taylor Swift主题特有的翻译
        'taylorTitle': '2048泰勒斯威夫特版',
        'taylorDescription': '通过AI生成的艺术肖像致敬泰勒斯威夫特的特别版本。',
        'taylorIntro': '合并肖像，探索泰勒独特的艺术诠释！',
        'eraDescription': '通过AI生成的艺术肖像体验泰勒的艺术之旅。',
        'aiArtDescription': '这个特别��本通过人工智能的视角致敬泰勒斯威夫特。我们使用AI技术创造了泰勒独特的艺术诠释，每一幅都捕捉了她不同风格和个性的特点。',
        'gameplayFeatures': '游戏特色',
        'gameplayText': '在游戏过程中，你将发现种AI生成的泰勒肖像：',
        'featuresList_0': '从泰勒的经典肖像风格开始',
        'featuresList_1': '合并方块揭示更多艺术诠释',
        'featuresList_2': '体验各种艺术风格和情绪',
        'featuresList_3': '感受泰勒不同面貌的魅力',
        'featuresList_4': '发现独特的AI生成艺术作品',
        'featuresList_5': '达到2048解锁终极泰勒肖像',
        'forSwifties': '献给泰勒粉丝',
        'swiftiesText': '这不仅仅是一个益智游戏 - 这是一份致敬泰勒斯威夫特的艺术作品，将现代AI技术与游戏完美结合。每次合并都会展现一幅新的AI生成的泰勒诠释，创造出艺术、技术与粉丝文化的独特融合。',
        'debut': '处女作',
        'fearless': '无畏',
        'speakNow': '立刻说',
        'red': '红色',
        '1989': '1989',
        'reputation': '名誉',
        'lover': '恋人',
        'folklore': '民谣',
        'evermore': '永恒',
        'midnights': '午夜',
        'shareTwitter': '分享到推特',
        'shareXiaohongshu': '分享到小红书'
    }
}

def generate_html(template_path, lang):
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()
    
    # 替换所有翻译内容
    html = template
    for key, value in translations[lang].items():
        pattern = r'\{' + re.escape(key) + r'\}'
        html = re.sub(pattern, value, html)
    
    # 替换语言标记
    html = html.replace('{lang}', lang)
    
    return html

def process_theme_page(theme_name, source_path, lang_dir, lang):
    # 确保主题目录存在
    theme_dir = os.path.join(lang_dir, 'themes')
    os.makedirs(theme_dir, exist_ok=True)
    
    # 复制主题相关的资源（如图片、样式等）
    theme_assets = os.path.join('themes', theme_name)
    if os.path.exists(theme_assets):
        dest_assets = os.path.join(theme_dir, theme_name)
        if os.path.exists(dest_assets):
            shutil.rmtree(dest_assets)
        
        # 创建目标目录
        os.makedirs(dest_assets)
        
        # 复制样式文件
        src_style = os.path.join(theme_assets, 'style.css')
        if os.path.exists(src_style):
            shutil.copy2(src_style, os.path.join(dest_assets, 'style.css'))
        
        # 复制图片目录
        src_images = os.path.join(theme_assets, 'images')
        if os.path.exists(src_images):
            dest_images = os.path.join(dest_assets, 'images')
            if os.path.exists(dest_images):
                shutil.rmtree(dest_images)
            shutil.copytree(src_images, dest_images)
    
    # 生成翻译后的HTML
    html_content = generate_html(source_path, lang)
    
    # 写入翻译后的HTML文件
    output_path = os.path.join(theme_dir, f'{theme_name}.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

def main():
    # 创建语言目录
    for lang in ['cn', 'en']:
        print(f"处理 {lang} 语言版本...")
        
        # 创建目录
        os.makedirs(lang, exist_ok=True)
        
        # 复制静态资源
        for resource in ['js', 'style', 'meta']:
            if os.path.exists(resource):
                dest = os.path.join(lang, resource)
                if os.path.exists(dest):
                    shutil.rmtree(dest)
                shutil.copytree(resource, dest)
        
        # 复制favicon
        if os.path.exists('favicon-16x16.ico'):
            shutil.copy2('favicon-16x16.ico', os.path.join(lang, 'favicon-16x16.ico'))
        
        # 生成主页HTML
        print(f"生成 {lang} 版本的主页...")
        html_content = generate_html('template.html', lang)
        with open(os.path.join(lang, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        # 处理主题页面
        print(f"生成 {lang} 版本的生肖主题...")
        process_theme_page('zodiac', 'themes/zodiac.html', lang, lang)
        print(f"生成 {lang} 版本的泰勒主题...")
        process_theme_page('taylorSwift', 'themes/taylorSwift.html', lang, lang)
    
    print("多语言目录结构设置完成！")

if __name__ == '__main__':
    main() 