const translations = {
  en: {
    home: 'Home',
    themes: 'Themes',
    language: 'Language',
    chineseZodiac: 'Chinese Zodiac',
    taylorSwift: 'Taylor Swift',
    welcome: 'Welcome to 2048 Game Series! Try our themed versions:',
    newGame: 'New Game',
    score: 'SCORE',
    best: 'BEST',
    gameOver: 'Game Over!',
    tryAgain: 'Try again',
    won: 'You win!',
    keepGoing: 'Keep going'
  },
  cn: {
    home: '首页',
    themes: '主题',
    language: '语言',
    chineseZodiac: '生肖版',
    taylorSwift: '泰勒斯威夫特版',
    welcome: '欢迎来到2048游戏系列！尝试我们的主题版本：',
    newGame: '新游戏',
    score: '得分',
    best: '最佳',
    gameOver: '游戏结束！',
    tryAgain: '再试一次',
    won: '你赢了！',
    keepGoing: '继续游戏'
  }
};

function getCurrentLanguage() {
  const path = window.location.pathname;
  const lang = path.split('/')[1];
  return translations[lang] ? lang : 'en';
}

function translate(key) {
  const lang = getCurrentLanguage();
  return translations[lang][key] || translations['en'][key];
}

// 页面加载完成��执行翻译
document.addEventListener('DOMContentLoaded', function() {
  const elements = document.querySelectorAll('[data-i18n]');
  elements.forEach(element => {
    const key = element.getAttribute('data-i18n');
    element.textContent = translate(key);
  });
}); 