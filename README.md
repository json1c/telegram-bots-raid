<h1>RaidBot</h1>
<em>Скрипт для рейда чатов в Telegram.</em>

<h2>Канал: https://t.me/huis_bn</h2>

<h1>Разработчик</h1>
<em>https://t.me/json1c</em>


<em>За основу взят код от http://github.com/KrasProject-2021, я лишь немного улучшил его. Точно так же и с README, но мне лень его переписывать, так что за ошибки не пинайте.</em>

<h1>Прошу Вас соблюдать лицензию.</h1>

<h1>Документация.</h1>
<em><p>[ 1 ] Открываем config.py.</p>
<p>[ 2 ] Начнем с разбора строк, в самом начале есть переменная ADMIN_ID там вместо единиц указываем свой телеграм id (получить можете через бота @username_to_id_bot).</p>
<p>[ 3 ] Далее где TOKENS внутри квадратных скобок вводим токены от @BotFather, обязательно в кавычках и через запятую, пример:</p>
<p><pre>
TOKENS [
    "TOKEN1",
    "TOKEN2"
]</pre></p>
<p>[ 4 ] Где MESSAGES точно так же как и в 3 пунтке вводим текст(ы) спама, если будет больше 1 текста то боты будут выбирать рандомный текст из листа и спамить.</p>
<p>[ 5 ] Если в чате есть слоумод, то в переменной DELAY необходимо указать задержку (в секнудах).</p>
<p>Теперь можем закрывать файл config.py и запускать raid.py.</p></em>

<h1>Установка. (Termux)</h1>
<em>
<p>[ 6 ] <pre><code>pkg -y update</code></pre></p>
<p>[ 7 ] <pre><code>pkg install -y git python</code></pre></p>
<p>[ 8 ] <pre><code>git clone https://github.com/json1c/telegram-bots-raid</code></pre></p>
<p>[ 9 ] <pre><code>cd RaidBot</code></pre></p>
<p>[ 10 ] <pre><code>pip install -r requirements.txt</code></pre></p>

<p>Запуск</p>

<p>[ 11 ] <pre><code>python raid.py</code></pre></p>

</em>
