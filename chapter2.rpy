label start2:
    stop music fadeout 1
    scene bg ch2 with fade
    pause 2.0
    scene black with fade
    e "{i}{color=#5200a5}Конечно, это моя вина. Здесь больше некому нести за что-либо ответственность.{/color}{/i}"
    scene bg shelf 
    show m norm:
        xalign 1.8
        yalign 1.0
    show p tired at left
    show pm norm:
        yalign -7.0
    play music musnorm
    with fade
    e '— Давайте проясним ситуацию, — сказал Гарри, — папа, если профессор действительно поднимет тебя в воздух, причём ты будешь знать, что нет никаких скрытых верёвок, то это будет считаться достаточным доказательством существования магии.'
    e 'Ты не будешь отпираться и называть происходящее обычными фокусами. Так будет честно. Если подобная демонстрация уже сейчас кажется тебе недостаточной, то мы можем придумать другой эксперимент.'
    h 'Отец Гарри, профессор Майкл Веррес-Эванс, закатил глаза:'
    m '— Да, Гарри'
    e '— Теперь ты, мама. Твоя теория заключается в том, что профессор сможет сделать это. Но если ничего не произойдёт, то ты признаешь, что ошибалась. '
    e 'И не будешь говорить, что магия не работает, когда люди настроены скептически, и тому подобное.'
    h 'Заместитель директора Минерва МакГонагалл с удивлением смотрела на Гарри. '
    h 'Одетая в чёрную мантию и остроконечную шляпу, она выглядела как настоящая ведьма, но разговаривала официальным тоном с шотландским акцентом, что совсем не вязалось с её внешним видом.'
    h 'На первый взгляд казалось, что она вот-вот разразится злобным хохотом и начнёт варить из младенцев жуткое зелье, но весь этот эффект испарялся, стоило ей открыть рот.'
    show pm answ
    pm '— Так этого будет достаточно, мистер Поттер? — уточнила волшебница. — Можно начинать демонстрацию?'
    e '— Достаточно? Скорее всего, нет, — ответил Гарри, — но это точно поможет. Начинайте, заместитель директора.'
    pm '— Можно просто «профессор», — сказала она. — Вингардиум левиоса.'
    show m shocked with easeintop:
        yalign 0.9

    h'Гарри посмотрел на отца.'
    e '— Гм.'
    h 'Тот посмотрел на него и повторил эхом:'
    m '— Гм.'
    h 'Затем профессор Веррес-Эванс перевёл взгляд на профессора МакГонагалл:'
    m '— Ладно, можете опустить меня вниз.'
    show m norm with easeouttop:
        yalign 1.0
    h 'Майкл Веррес-Эванс медленно приземлился на пол.'
    h 'Гарри взъерошил волосы. Может, дело было в том, что какая-то его часть заранее знала результат, но…'
    e '— Почему-то меня это не впечатлило, — сказал он. — Я думал, что моя реакция будет более драматичной, учитывая, что я стал свидетелем события бесконечно малой вероятности…'
    show m answ
    show pm answ
    show p conf
    h 'Он запнулся: мать, МакГонагалл и даже отец снова смотрели на него тем самым взглядом.'
    e '— Я имею в виду ситуацию, когда всё, во что веришь, оказывается ложью.'
    h 'В самом деле, увиденное должно было потрясти его гораздо сильнее. Сейчас мозгу Гарри следовало бы перебирать все возможные гипотезы об устройстве вселенной, которые говорили бы о невозможности того, что только что случилось.'
    h 'А вместо этого его рассудок говорил: «Ладно, я видел, как профессор из Хогвартса махнула палочкой и мой отец поднялся в воздух. И что тут такого?»'
    h 'Ведьма с довольно-таки весёлым видом добродушно улыбнулась.'
    show pm smile
    pm '— Вы хотели бы продолжить демонстрацию, мистер Поттер?'
    e '— Это не обязательно, — ответил Гарри, — мы провели достаточно убедительный эксперимент. Но…'
    h 'Он колебался. Хотелось увидеть больше. В конце концов, сейчас, учитывая обстоятельства, любопытство было правильным и уместным.'
    e '— Что ещё вы можете показать?'
    hide pm smile
    show pm cat with fade
    h 'Профессор МакГонагалл превратилась в кошку.'
    h 'Гарри отскочил назад так быстро, что споткнулся о стопку книг и звучно шмякнулся на пол. Не успев правильно выставить руки, он всем своим весом приземлился на плечо, и теперь оно болезненно ныло.'
    show pm ssmile with vpunch:
        yalign -7.0
    play sound punch
    h 'В тот же миг маленькая полосатая кошка вновь стала женщиной в чёрной мантии.'
    pm '— Извините, мистер Поттер, — в её голосе звучало искреннее сочувствие, но губы едва заметно улыбались. — Я должна была вас предупредить.'
    h 'Гарри еле дышал от потрясения:'
    e '— Как вы ЭТО сделали?!'
    pm '— Это просто трансфигурация, — ответила МакГонагалл. — Трансформация анимага, если говорить точно.'
    e '— Вы превратились в кошку! В МАЛЕНЬКУЮ кошку! Вы нарушили закон сохранения энергии! Это не какое-то условное правило. Энергия выражается с помощью квантового гамильтониана, а при нарушении закона сохранения теряется унитарность! '
    e 'Получается распространение сигналов быстрее скорости света! И кошки СЛОЖНЫЕ! Человеческий разум просто не в состоянии представить себе всю кошачью анатомию и всю кошачью биохимию, не говоря уже о неврологии. Как можно продолжать думать, используя мозг размером с кошачий?'
    h'Профессор МакГонагалл уже едва сдерживала улыбку:'
    show pm smile
    pm '— Магия.'
    e '— Магии для такого недостаточно. Для этого нужно быть богом!'
    show pm answ
    h'МакГонагалл моргнула:'
    pm '— Так меня ещё никто не называл.'
    h 'Взгляд Гарри затуманился, его разум принялся подсчитывать причинённый ущерб. '
    h 'Вся идея единообразной вселенной с математически обоснованными законами, все представления физики пошли коту (точнее, кошке) под хвост.'
    h 'Три тысячи лет люди по маленьким кусочкам складывали картину мира, узнавали, что музыка планет имеет ту же мелодию, что и падающее яблоко, искали истинные универсальные законы, для которых нет исключений и которые, принимая простую математическую форму, управляли даже мельчайшими частицами… '
    h 'И ещё тот факт, что сознание находится в мозге, и что мозг состоит из нейронов, и что мозг равен личности…'
    h 'А тут женщина превращается в кошку, только и всего.'
    h 'Гарри хотел задать тысячу вопросов, но в итоге вырвался один:'
    e '— Что это за словосочетание — «Вингардиум левиоса»? Кто придумывает слова к этим заклинаниям, дети дошкольного возраста?'
    show pm norm
    pm '— Закончим на этом, мистер Поттер, — решительно остановила его МакГонагалл, но в её глазах читался с трудом удерживаемый смех. — Если вы хотите изучать магию, нам необходимо обговорить все детали вашего поступления в Хогвартс.'
    e '— Верно, — задумчиво ответил Гарри. Он собрался с мыслями. Путь к знаниям придётся начинать заново, но у него ещё оставался экспериментальный метод, и об этом стоило помнить. — Так как же мне попасть в Хогвартс?'
    show pm ssmile
    h 'Сдавленный смешок вырвался изо рта ведьмы, будто его выдернули клещами.'
    show m answ
    m '— Подожди, Гарри, — вмешался его отец. — Ты же знаешь, по каким причинам ты до сих пор не посещаешь школу. Что будем делать с ними?'
    h 'МакГонагалл повернулась к Майклу:'
    show pm answ
    pm '— Какие причины? О чём вы говорите?'
    e '— У меня проблемы со сном, — сказал Гарри, беспомощно разводя руками. — В моих биологических сутках двадцать шесть часов, я каждый день ложусь спать на два часа позже. Десять вечера, двенадцать, два часа, четыре утра и так по кругу.'
    e 'Даже если я заставлю себя встать раньше, это не поможет, и весь следующий день я буду не в своей тарелке. Поэтому я до сих пор не хожу в обычную школу.'
    show p tired
    p '— Это одна из причин, — уточнила его мать, награждённая за это свирепым взглядом Гарри.'
    pm '— Хм-м, — протянула МакГонагалл. — Не сталкивалась с подобным прежде. Нужно будет спросить у мадам Помфри, знает ли она подходящее лекарство.'
    show pm norm
    h 'Её лицо смягчилось:'
    pm '— Но не думаю, что это может быть препятствием. Я найду решение вашей проблемы со временем, — она снова сдвинула брови. — Каковы же другие причины?'
    h 'Гарри наградил родителей ещё одним свирепым взглядом:'
    e '— Я сознательно возражаю против идеи обязательного посещения школы, основываясь на перманентной неспособности системы школьного образования предоставить мне учителей и учебные пособия минимально приемлемого уровня.'
    hide p tired
    show p2 at left
    show m condescending
    h 'Родители Гарри рассмеялись, как будто вдруг услышали отличную шутку.'
    m'— Ага, — сказал отец Гарри, сверкнув глазами, — теперь понятно, почему в третьем классе ты укусил свою учительницу математики.'
    e '— Она не знала, что такое логарифм!'
    p '— И, конечно, укусить её — весьма взрослый способ решения проблемы, — вторила мать.'
    h 'Отец Гарри кивнул:'
    m '— Продуманная стратегия в отношении учителей, которые не понимают логарифмов.'
    e '— Мне было семь лет! Как долго вы ещё собираетесь вспоминать тот случай?'
    p '— Да, всё понятно, — с участием в голосе сказала мать. — Ты укусил одного учителя математики, и теперь тебе этого никогда не забудут.'
    h 'Гарри повернулся к МакГонагалл:'
    e '— Вот видите, с чем мне приходится иметь дело?'
    p '— Извините, — сказала Петуния и выбежала за стеклянную дверь гостиной. Впрочем, её смех было слышно даже оттуда.'
    hide p2 with easeoutleft
    pm '— Гм, значит так, — по какой-то причине МакГонагалл было непросто продолжить разговор. — Никакого кусания учителей в Хогвартсе. Это понятно, мистер Поттер?'
    h'Гарри, насупившись, посмотрел на неё:'
    e '— Хорошо, я не стану никого кусать, пока меня самого не укусят.'
    h'Услышав это, профессор Майкл Веррес-Эванс тоже был вынужден покинуть комнату.'
    hide m condescending with easeoutright
    show p2 at left
    show m norm at right:
        xalign 1.8
        yalign 1.0
    with fade
    show pm ssmile
    pm '— Итак, — вздохнула МакГонагалл, дождавшись, пока родители Гарри возьмут себя в руки и вернутся. '
    pm '— Думаю, учитывая обстоятельства, стоит повременить с покупкой школьных принадлежностей. Займёмся этим за несколько дней до начала учебного года.'
    e '— Что? Почему? Ведь другие дети уже знакомы с магией! Я должен начать готовиться прямо сейчас!'
    pm '— Смею вас заверить, мистер Поттер, — ответила профессор МакГонагалл, — в Хогвартсе вы сможете начать обучение с самых основ.'
    pm 'К тому же, мистер Поттер, подозреваю, что если я оставлю вас на два месяца с вашими учебниками даже без волшебной палочки, то, вернувшись сюда, я найду лишь кратер, полный лилового дыма, опустевший город и полчища огненных зебр, терроризирующих остатки Англии.'
    h 'Мать и отец Гарри согласно кивнули.'
    e '— Мама! Папа!'
    stop music
    jump start3