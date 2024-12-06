#!/bin/bash

# 创建语言目录
mkdir -p cn en jp kr

# 将重定向页面放到根目录的index.html
cp redirect.html index.html

# 定义语言内容
declare -A translations
# 英文内容
translations[en.home]="Home"
translations[en.themes]="Themes"
translations[en.language]="Language"
translations[en.chineseZodiac]="Chinese Zodiac"
translations[en.taylorSwift]="Taylor Swift"
translations[en.welcome]="Welcome to 2048 Game Series! Try our themed versions:"
translations[en.newGame]="New Game"
translations[en.score]="SCORE"
translations[en.best]="BEST"
translations[en.gameOver]="Game Over!"
translations[en.tryAgain]="Try again"
translations[en.won]="You win!"
translations[en.keepGoing]="Keep going"
translations[en.howToPlay]="How to play"
translations[en.gameIntro]="Join numbers and get to the <strong>2048 tile!</strong>"
translations[en.gameExplanation]="Use your <strong>arrow keys</strong> to move the tiles. When two tiles with the same number touch, they <strong>merge into one!</strong>"
translations[en.about]="About 2048"
translations[en.aboutText]="2048 is an addictive puzzle game created by Gabriele Cirulli in March 2014. The game quickly became a worldwide phenomenon, spawning numerous variations and adaptations. The objective is simple yet challenging: combine matching numbers to create the tile with the number 2048."
translations[en.gameMechanics]="Game Mechanics"
translations[en.mechanicsText]="Players slide numbered tiles on a 4x4 grid using arrow keys. When two tiles with the same number collide, they merge into one tile with their sum. The game continues until you either create the 2048 tile (victory) or can no longer make any moves (game over)."
translations[en.themedVersions]="Our Themed Versions"
translations[en.shareTwitter]="Share on Twitter"
translations[en.shareXiaohongshu]="Share on Little Red Book"

# 中文内容
translations[cn.home]="首页"
translations[cn.themes]="主题"
translations[cn.language]="语言"
translations[cn.chineseZodiac]="生肖版"
translations[cn.taylorSwift]="泰勒斯威夫特版"
translations[cn.welcome]="欢迎来到2048游戏系列！尝试我们的主题版本："
translations[cn.newGame]="新游戏"
translations[cn.score]="得分"
translations[cn.best]="最佳"
translations[cn.gameOver]="游戏结束！"
translations[cn.tryAgain]="再试一次"
translations[cn.won]="你赢了！"
translations[cn.keepGoing]="继续游戏"
translations[cn.howToPlay]="游戏规则"
translations[cn.gameIntro]="合并数字，获得 <strong>2048</strong> 方块！"
translations[cn.gameExplanation]="使用<strong>方向键</strong>移动方块。当两个相同数字的方块相撞时，它们会<strong>合并成一个！</strong>"
translations[cn.about]="关于2048"
translations[cn.aboutText]="2048是由Gabriele Cirulli于2014年3月创建的一款令人上瘾的益智游戏。这个游戏迅速成为全球现象，衍生出众多变体和改编版本。游戏目标简单而具有挑战性：合并相同的数字以创建数字2048的方块。"
translations[cn.gameMechanics]="游戏机制"
translations[cn.mechanicsText]="玩家使用方向键在4x4网格上滑动数字方块。当两个相同数字的方块碰撞时，它们会合并成一个新的方块，数字为两者之和。游戏持续进行，直到你创建出2048方块（胜利）或无法继续移动（游戏结束）。"
translations[cn.themedVersions]="主题版本"
translations[cn.shareTwitter]="分享到推特"
translations[cn.shareXiaohongshu]="分享到小红书"

# 复制所有必要的文件和目录到每个语言目录
for lang in cn en; do
  # 复制静态资源
  cp -r js $lang/
  cp -r style $lang/
  cp -r themes $lang/
  cp -r meta $lang/
  cp favicon-16x16.ico $lang/
  
  # 生成对应语言的index.html
  cat > $lang/index.html << EOL
<!DOCTYPE html>
<html lang="${lang}">
<head>
  <meta charset="utf-8">
  <title>2048 Game Series | 2048 Fun Games</title>
  <meta name="description" content="${translations[$lang.welcome]}">
  <link href="themes/common.css" rel="stylesheet" type="text/css">
  <link href="style/main.css" rel="stylesheet" type="text/css">
  <link rel="apple-touch-icon" href="meta/apple-touch-icon.png">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black">
  <meta name="HandheldFriendly" content="True">
  <meta name="MobileOptimized" content="320">
  <meta name="viewport" content="width=device-width, target-densitydpi=160dpi, initial-scale=1.0, maximum-scale=1, user-scalable=no, minimal-ui">
  <link rel="icon" type="image/x-icon" href="favicon-16x16.ico">
  <link rel="shortcut icon" type="image/x-icon" href="favicon-16x16.ico">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
</head>
<body>
  <div class="nav-container">
    <div class="nav-menu">
      <div class="site-title">2048+</div>
      <div class="nav-item">
        <a href="index.html" style="color: #f9f6f2; text-decoration: none; display: block;">${translations[$lang.home]}</a>
      </div>
      <div class="nav-item">
        <span>${translations[$lang.themes]}</span>
        <div class="dropdown-content">
          <a href="themes/zodiac.html">${translations[$lang.chineseZodiac]}</a>
          <a href="themes/taylorSwift.html">${translations[$lang.taylorSwift]}</a>
        </div>
      </div>
    </div>
    <div class="language-selector nav-item">
      <span>${translations[$lang.language]}</span>
      <div class="dropdown-content">
        <a href="/cn/index.html">简体中文</a>
        <a href="/en/index.html">English</a>
        <a href="/jp/index.html">日本語</a>
        <a href="/kr/index.html">한국어</a>
      </div>
    </div>
  </div>

  <div class="container">
    <div class="heading">
      <h1 class="title">2048</h1>
      <div class="scores-container">
        <div class="score-container">0</div>
        <div class="best-container">0</div>
      </div>
    </div>

    <p class="theme-intro">
      ${translations[$lang.welcome]}
    </p>

    <div class="above-game">
      <p class="game-intro">${translations[$lang.gameIntro]}</p>
      <a class="restart-button">${translations[$lang.newGame]}</a>
    </div>

    <div class="game-container">
      <div class="game-message">
        <p></p>
        <div class="social-sharing">
          <a href="#" class="twitter-share" onclick="shareOnTwitter()">
            <i class="fab fa-twitter"></i> ${translations[$lang.shareTwitter]}
          </a>
          <a href="#" class="xiaohongshu-share" onclick="shareOnXiaohongshu()">
            <i class="fas fa-heart"></i> ${translations[$lang.shareXiaohongshu]}
          </a>
        </div>
        <div class="lower">
          <a class="keep-playing-button">${translations[$lang.keepGoing]}</a>
          <a class="retry-button">${translations[$lang.tryAgain]}</a>
        </div>
      </div>

      <div class="grid-container">
        <div class="grid-row">
          <div class="grid-cell"></div>
          <div class="grid-cell"></div>
          <div class="grid-cell"></div>
          <div class="grid-cell"></div>
        </div>
        <div class="grid-row">
          <div class="grid-cell"></div>
          <div class="grid-cell"></div>
          <div class="grid-cell"></div>
          <div class="grid-cell"></div>
        </div>
        <div class="grid-row">
          <div class="grid-cell"></div>
          <div class="grid-cell"></div>
          <div class="grid-cell"></div>
          <div class="grid-cell"></div>
        </div>
        <div class="grid-row">
          <div class="grid-cell"></div>
          <div class="grid-cell"></div>
          <div class="grid-cell"></div>
          <div class="grid-cell"></div>
        </div>
      </div>

      <div class="tile-container">
      </div>
    </div>

    <p class="game-explanation">
      <strong class="important">${translations[$lang.howToPlay]}:</strong> ${translations[$lang.gameExplanation]}
    </p>
    <hr>
    <div class="game-description">
      <h2>${translations[$lang.about]}</h2>
      <p>${translations[$lang.aboutText]}</p>
      
      <h3>${translations[$lang.gameMechanics]}</h3>
      <p>${translations[$lang.mechanicsText]}</p>
      
      <h3>${translations[$lang.themedVersions]}</h3>
      <p>${translations[$lang.welcome]}</p>
      <ul>
        <li><strong><a href="themes/zodiac.html">${translations[$lang.chineseZodiac]}</a></strong></li>
        <li><strong><a href="themes/taylorSwift.html">${translations[$lang.taylorSwift]}</a></strong></li>
      </ul>
    </div>
  </div>

  <script src="js/bind_polyfill.js"></script>
  <script src="js/classlist_polyfill.js"></script>
  <script src="js/animframe_polyfill.js"></script>
  <script src="js/keyboard_input_manager.js"></script>
  <script src="js/html_actuator.js"></script>
  <script src="js/grid.js"></script>
  <script src="js/tile.js"></script>
  <script src="js/local_storage_manager.js"></script>
  <script src="js/game_manager.js"></script>
  <script src="js/application.js"></script>
  <script>
    function shareOnTwitter() {
      const text = "${translations[$lang.welcome]}";
      const url = window.location.href;
      window.open(\`https://twitter.com/intent/tweet?text=\${encodeURIComponent(text)}&url=\${encodeURIComponent(url)}\`, '_blank');
    }

    function shareOnXiaohongshu() {
      const text = "${translations[$lang.welcome]} " + window.location.href;
      navigator.clipboard.writeText(text).then(() => {
        alert("${translations[$lang.shareXiaohongshu]}");
      });
    }
  </script>
</body>
</html>
EOL

done

echo "多语言目录结构设置完成！" 