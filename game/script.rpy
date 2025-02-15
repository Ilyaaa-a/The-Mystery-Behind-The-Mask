# Вы можете расположить сценарий своей игры в этом файле.
# Игра начинается здесь:

label start:
    scene bg rooftops 2 with fade 
    "Париж, современность..."   
    #show animation1 at left2 with dissolve ВОТ ТАК АНИМАЦИЮ МОЖНО ДЕЛАТЬ
    #show spin1 at left2 with dissolve 
    show mar happy at left2 with dissolve
    "Главные герои — Маринетт (Леди Баг)" 
    show adr happy at right2 with dissolve
    extend " и Адриан (Супер-Кот)." 
    
    scene bg rooftops with fade
    "История разворачивается в течение одного дня, когда в городе появляется новая злодейка..."
    scene bg panic city with fade
    show badgirlie at right2 with dissolve
    "Угрожающая раскрыть тайны жителей Парижа..."
    jump meet
    return

label meet:

    scene bg school with fade

    show mar happy at left2 
    with easeinleft
    mar "Ай! Ой, простите! Я не смотрела, куда..."

    show adr happy at right2
    with easeinright
    adr "Нет, это я виноват, я был в своих мыслях..."

    show mar hi
    mar " Адриан?!"

    show adr normal
    adr " Маринетт? Привет!"

    "За кого вы продолжите играть?"

    call screen choose_character

    return

###################################################################

label marinett:

    scene bg school with fade

    show mar happy at left2 
    show adr happy at right2
   

    "Привет! Я... я просто очень спешу, опаздываю на встречу с Алей, и..."
    extend " ой, мои эскизы!"

    show mar normal
    "(в мыслях) Я уронила свою папку с эскизами."

    adr punch "Давай я помогу!"
    hide adr with easeoutbottom
    #$ renpy.notify("Леди Баг запомнит это.") # уведомления слева сверху

    "(в мыслях) Где же этот эскиз? Он должен быть где-то здесь..."
    hide mar with easeoutbottom
    "Адриан, ты уверен, что не видел мой эскиз? Он очень важен для меня."

    show adr happy at left2 with easeinbottom
    adr "Это... это дизайн костюма? Он выглядит потрясающе!"
    show mar happy at right2 with easeinbottom
    "(в мыслях) Почему он так на меня смотрит? Может, он догадывается, что это дизайн для него"
    "Ой, нет, это просто... эээ... наброски! Ничего особенного!"
    "(в мыслях) Я не могу позволить ему увидеть этот эскиз! Он поймёт, что я делаю костюм для него..."

    adr normal "Не скромничай, Маринетт. Ты талантлива. Мне нравится, как ты играешь с формами и цветами."
    mar normal "Спасибо... это значит для меня многое."
    mar happy "Мне правда жаль, что я тебя задержала. Ты же опаздываешь на встречу?"
    mar hi "Удачи, Адриан! И... спасибо за помощь!"
    adr punch "Удачи, Маринетт!"
    hide adr with easeoutleft

    show tikki at left2 with easeintop
    tik "Маринетт, ты снова всё испортила! Почему ты всегда такая неуклюжая?!"

    hide mar with dissolve
    hide tikki with dissolve

    scene bg illusion with fade
    "Куда же на самом деле торопились Маринетт и Адриан?"
    "Давайте я вам расскажу, что поизошло до их встречи..."
    scene bg panic city with fade
    "Внезапно по всему Парижу разносится новость: появилась новая злодейка по имени Мираж, "
    extend "которая может создавать иллюзии, раскрывающие самые сокровенные тайны людей."
    "Город в панике."
    "Маринетт и Адриан понимают, что должны действовать." 
    "Они находят свои потерянные вещи и расходятся," 
    extend " чтобы превратиться в Леди Баг и Супер-Кота."

    scene bg rooftops 2 with fade
    "Леди Баг и Супер-Кот встречаются на крыше, чтобы обсудить план действий."
    "Они решают выследить Мираж, но сталкиваются с его иллюзиями," 
    extend " которые показывают их самые глубокие страхи и желания."

#########################

    scene bg rooftops 2 with fade
    show lady strange at left2 with dissolve
    "Супер-Кот, ты слышал о Мираж? Она создаёт иллюзии, которые раскрывают самые сокровенные тайны людей."
    
    show cat vibe at right2 with dissolve
    cat "Я знаю, Леди Баг. Её иллюзии опасны, но мы справимся. Мы всегда справляемся."

    show lady point
    "Мы должны остановить его, пока она не навредила ещё больше."

    cat normal "Ты права, мы должны действовать быстро. Но будь осторожна — она может играть на наших страхах."


    scene bg illusion with fade
    "Внезапно Леди Баг погружается в иллюзию под действием Мираж"

    show lady strange illusion at left2 with dissolve 
    "Где я...?"

    show cat strange illusion at right2 with dissolve
    cat "Маринетт? Это ты? Ты — Леди Баг?"

    hide lady strange illusion with dissolve
    show mar normal at left2 with dissolve 

    "Адриан, подожди! Это не так, как ты думаешь..."

    cat "Почему ты скрывала это от меня? Я думал, мы друзья."

    "(про себя) Это иллюзия... Это не настоящий Адриан. Я должна быть сильной!"
    
    cat "Ты обманывала меня всё это время... Я не могу тебе доверять."

    show tikki with dissolve
    tik "Маринетт, она не реальная! Это иллюзия!"
    hide tikki with dissolve

    menu optional_name:
        "Сопротивляться иллюзии?"
        "Найти в себе силы бороться":
            "Нет! Ты не настоящий! Это просто иллюзия!"
            show mar happy
            "(про себя) Я знаю, что он бы меня понял..."
            "(про себя) Я не позволю иллюзиям сломать меня. Я сильнее этого!"
            
            hide mar normal with dissolve 
            show lady illusion at left2 with dissolve

            "(кричит) Я — Леди Баг, и я не позволю тебе сломать меня!"
            show tikki with dissolve
            tik "Маринетт, ты прошла испытание!"
            hide tikki with dissolve

            jump final_fight

        "Поддаться иллюзии":
            "Адриан, прости меня... Я не хотела тебя обманывать."
            "(про себя) Может, он прав... Может, я действительно его подвела."
            "(Леди Баг теряет уверенность, её силы ослабевают)"
            
            hide mar normal with dissolve 
            show lady strange illusion at left2 with dissolve

            "Прости меня... Я не справилась..."
            $ renpy.notify("Иллюзия сильно повлияла на Маринетт") # уведомления слева сверху
            show tikki with dissolve
            tik "Маринетт, иллюзия надавила на твои слабости..."
            hide tikki with dissolve

            $ persistent.Good_Mar_end = True
            jump final_fight
                
    return

###############################################################

label adrian:

    scene bg school with fade

    show mar happy at left2 
    show adr happy at right2
   
    "Привет! Я просто опаздываю на тренировку, и..."
    show adr normal
    extend " мое кольцо!"
    show mar normal
    "(про себя) Где же это кольцо? Отец будет в ярости, если я его потеряю."

    "Маринетт, ты не видела маленькое серебряное кольцо? Оно очень важно для меня."
    show adr punch
    "Это подарок от отца... он не любит, когда я теряю его вещи."

    mar normal "Давай я помогу поискать!"
    hide mar with easeoutbottom
    show adr happy
    "Спасибо, Маринетт. Ты всегда такая отзывчивая."
    hide adr with easeoutbottom

    mar "Ну, знаешь... это же ничего такого. Ты ведь тоже всегда помогаешь другим."
    "(про себя) Я не могу позволить отцу узнать, что я потерял кольцо. Он и так считает меня неудачником."

    show mar happy at right2 with easeinbottom
    mar "Нашла! Оно было где-то в траве."
    show adr happy at left2 with easeinbottom
    "(про себя) Она нашла его... Надеюсь, она не заметила, как я переживаю."
    "Да, это оно! Спасибо, Маринетт!"
    mar normal "Оно такое красивое... Должно быть, оно действительно важно для тебя."
    show adr normal
    "Это просто... эээ... старый подарок. Ничего особенного."
    mar happy "Ты сказал, это подарок от отца? Он, наверное, очень гордится тобой."
    show adr punch
    "Может, мы уже пойдём? Я не хочу тебя больше задерживать."
    mar hi "Удачи, Адриан!"
    "О чёрт, мне нужно бежать. Удачи, Маринетт!"
    hide mar with easeoutright

    show plug at right2 with easeintop
    plug "Ты чуть все не испортил!!"

    hide adr with dissolve
    hide plug with dissolve

    scene bg illusion with dissolve
    "Куда же на самом деле торопились Маринетт и Адриан?"
    "Давайте я вам расскажу, что поизошло до их встречи..."

    scene bg panic city with dissolve
    "Внезапно по всему Парижу разносится новость: появилась новая злодейка по имени Мираж, "
    extend "которая может создавать иллюзии, раскрывающие самые сокровенные тайны людей."
    "Город в панике."
    "Маринетт и Адриан понимают, что должны действовать." 
    "Они находят свои потерянные вещи и расходятся," 
    extend " чтобы превратиться в Леди Баг и Супер-Кота."

    scene bg rooftops 2 with dissolve
    "Леди Баг и Супер-Кот встречаются на крыше, чтобы обсудить план действий."
    "Они решают выследить Мираж, но сталкиваются с её иллюзиями," 
    extend " которые показывают их самые глубокие страхи и желания."

#################

    scene bg rooftops 2 with fade
    show lady strange at left2 with dissolve
    show cat vibe at right2 with dissolve

    mar "Супер-Кот, ты слышал о Мираж? Она создаёт иллюзии, которые раскрывают самые сокровенные тайны людей."
    
    "Я знаю, Леди Баг. Её иллюзии опасны, но мы справимся. Мы всегда справляемся."

    show lady point
    mar "Мы должны остановить её, пока она не навредила ещё больше."

    show cat normal
    "Ты права, мы должны действовать быстро. Но будь осторожна — она может играть на наших страхах."

####

    scene bg illusion with fade
    "Внезапно Супер-Кот погружается в иллюзию под действием Мираж"

    show cat strange illusion at right2 with dissolve 
    "Где я...?"

    show gabr at left2 with dissolve
    gabr "Адриан? Ты — Супер-Кот? Ты всё это время обманывал меня?"

    hide cat strange illusion with dissolve
    show adr normal at right2 with dissolve 

    "Отец... это не так, как ты думаешь..."

    gabr "Ты думал, что сможешь скрывать это вечно? Ты позоришь нашу семью."

    "(про себя) Это иллюзия... Это не настоящий отец. Я должен быть сильным!"
    "Нет! Ты не настоящий! Это просто иллюзия!"

    gabr "Ты никогда не был достойным сыном."

    show plug with dissolve
    plug "Адриан, он не реальный! Это иллюзия!"
    hide plug with dissolve

    menu optional_name2:
        "Сопротивляться иллюзии?"
        "Найти в себе силы бороться":
            hide adr normal with dissolve
            show cat illusion at right2 with dissolve
            "Нет! Ты не настоящий отец! Я знаю, что он бы гордился мной."
            "(про себя) Я не позволю иллюзиям сломать меня. Я сильнее этого!"
            "(Супер-Кот становится сильнее, его уверенность растёт.)"
            
            show plug with dissolve
            plug "Адриан, ты прошел испытание!"
            hide plug with dissolve

            jump final_fight

        "Поддаться иллюзии":
            "Отец, прости меня... Я не хотел тебя подвести."
            hide adr normal with dissolve
            show cat strange illusion at right2 with dissolve
            "(про себя) Может, он прав... Может, я действительно его разочаровал."
            "(Супер-Кот теряет уверенность, его силы ослабевают.)"
            $ renpy.notify("Иллюзия сильно повлияла на Адриана") # уведомления слева сверху
            show plug with dissolve
            tik "Адриан, иллюзия была очень сильна..."
            hide plug with dissolve
            hide cat strange illusion with dissolve

            $ persistent.Good_Adr_end = True
            jump final_fight
    return

label final_fight:

    scene bg panic city with fade
    "Леди Баг и Супер-Кот находят Мираж и вступают с ней в бой."
    if persistent.Good_Adr_end:
        "Супер-Кот пытается прийти в себя после иллюзии..."
    elif persistent.Good_Mar_end:
        "Маринетт пытается прийти в себя после иллюзии..."

    "Злодей использует их слабости, создавая иллюзии, где они видят друг друга без масок."

    show cat normal at left2 with dissolve
    show lady strange at right2 with dissolve

    bad "Вы не сможете спрятаться от своих страхов! Я покажу вам правду!"
    bad "Ваши тайны разрушат вас. Сдавайтесь!"



    scene bg illusion with fade
    "Леди Баг и Супер-Кот переносятся в иллюзию..."
    "Где видят друг друга без масок."
    show adr normal at left2 with dissolve
    show mar happy at right2 with dissolve

    mar "Адриан? Ты... ты Супер-Кот?"
    adr "Маринетт? Ты... ты Леди Баг?"
    mar normal "(про себя) Это правда? Он всегда был рядом со мной?"
    adr punch "(про себя) Это правда? Она всегда была рядом со мной?"
    mar happy "Но... почему ты никогда не сказал мне?"
    adr happy "Но... почему ты никогда не сказала мне?"

    hide adr normal with dissolve
    hide mar normal with dissolve

    show badgirlie at right2 with dissolve
    bad "Кажется они были совсем не готовы к этому!"
    bad "На это я и рассчитывала!"
    bad "АХАХАХАХА!!"
    hide badgirlie with dissolve

    "Смогут ли они принять этот факт?"
    "От этого зависит судьба всего Парижа..."

    menu optional_name3:
        "Как поступят Леди Баг и Супер-Кот?"
        "Объединить силы":
            show adr punch at left2 with dissolve
            show mar happy at right2 with dissolve
            lady "Адриан, теперь, когда мы знаем правду, мы можем стать ещё сильнее."
            cat "Ты права, Маринетт. Вместе мы непобедимы."
            scene bg panic city with fade
            show cat vibe at left2 with dissolve
            show lady point at right2 with dissolve

            if persistent.Good_Adr_end:
                "Начинается финальная битва."
                "Супер_Кот чувствует слабость..."
                "Леди Баг толкает его и защищает от удара Мираж!"
                "(Они объединяют свои силы и атакуют Миража вместе.)"
            elif persistent.Good_Mar_end:
                "Начинается финальная битва."
                "Леди Баг чувствует слабость..."
                "Супер-Кот понял, что Мираж будет атаковать Леди Баг, потому что она слаба..."
                "Он защищает Леди Баг от атак Мираж"
                "(Они объединяют свои силы и атакуют Миража вместе.)"
            else:
                "(Они объединяют свои силы и атакуют Миража вместе.)"
            

            if persistent.Good_Adr_end:
                jump good_adr_end
            elif persistent.Good_Mar_end:
                jump good_mar_end
            else:
                jump best_end

        "Действовать в одиночку":
            show adr normal at left2 with dissolve
            show mar normal at right2 with dissolve
            lady "Я... я не могу сейчас это обсуждать. Давай просто победим Миража."
            cat "Ты права. Сейчас важнее остановить его."
            show cat normal at left2 with dissolve
            show lady normal at right2 with dissolve
            "Командная работа была бы намного эффективнее..."
            "Мираж пользуется их слабостями и атакует их по-одиночке..."
            jump bad_end

    return

label best_end:
    scene bg panic city with fade
    show badgirlie at right2 with dissolve
    bad "НЕТ!"
    bad "Как вам это удалось?"
    bad "Мой план был идеальным..."
    hide badgirlie with dissolve
    "Мираж оказалась заточенной в мираже"

    scene bg street
    "Нашим героям предстоит догий разговор..."
    show lady normal at left2 with dissolve
    show cat normal at right2 with dissolve
    lady "Спасибо, что был рядом, Адриан. Ты сделал этот день особенным."
    cat "Спасибо, что была рядом, Маринетт. Ты всегда была для меня важна."
    hide lady normal at left2 with dissolve
    hide cat normal at right2 with dissolve

    $ persistent.Best_end = True # постоянная переменная

    show adr happy with dissolve
    adr "(про себя) Однажды я скажу ей, как сильно она для меня значит."
    hide adr with dissolve
    
    show mar happy at right2 with dissolve
    mar "(про себя) Может быть, однажды я смогу сказать ему, что чувствую."
    hide mar  with dissolve

    scene bg house mar with fade
    show alya with dissolve
    alya "ПОДПИСЧИКИ!! Я тут такоооое узнала!"

    return

label good_mar_end:
    scene bg panic city with fade
    show badgirlie at right2 with dissolve
    bad "НЕТ!"
    bad "Как вам это удалось?"
    bad "Мой план был идеальным..."
    hide badgirlie with dissolve
    "Мираж оказалась заточенной в мираже"

    scene bg street
    "Нашим героям предстоит догий разговор..."
    show lady normal at left2 with dissolve
    show cat normal at right2 with dissolve
    lady "Спасибо, что был рядом, Адриан. Ты спас меня сегодня."
    cat "Ты всегда была для меня важна! Спасибо, что была рядом, Маринетт."
    hide lady normal at left2 with dissolve
    hide cat normal at right2 with dissolve

    show adr happy with dissolve
    adr "(про себя) Однажды я скажу ей, как сильно она для меня значит."
    hide adr with dissolve
    
    $ persistent.Good_Mar_end = True # постоянная переменная

    show mar happy at right2 with dissolve
    mar "(про себя) Может быть, однажды я смогу сказать ему, что чувствую."
    mar normal "(про себя) Сегодня он спас меня..."
    mar normal "(про себя) Значит я для него важна!"
    hide mar  with dissolve
    return

label good_adr_end:
    scene bg panic city with fade
    show badgirlie at right2 with dissolve
    bad "НЕТ!"
    bad "Как вам это удалось?"
    bad "Мой план был идеальным..."
    hide badgirlie with dissolve
    "Мираж оказалась заточенной в мираже"

    scene bg street
    "Нашим героям предстоит догий разговор..."
    show cat normal at right2 with dissolve
    show lady normal at left2 with dissolve
    cat "Спасибо, что была рядом, Маринетт. Без тебя..."
    cat "Ты меня спасла!"
    lady "Мы всегда помогаем друг другу!"
    
    hide lady normal at left2 with dissolve
    hide cat normal at right2 with dissolve

    show adr happy with dissolve
    adr "(про себя) Однажды я скажу ей, как сильно она для меня значит."
    adr "(про себя) Она спасла меня..."
    adr "(про себя) Значит я ей небезразличен!"
    hide adr with dissolve
    
    $ persistent.Good_Adr_end = True # постоянная переменная

    show mar happy at right2 with dissolve
    mar "(про себя) Может быть, однажды я смогу сказать ему, что чувствую."
    hide mar  with dissolve
    return

label bad_end:
    scene bg panic city with fade

    show mar normal at right2 with dissolve
    show adr normal at left2 with dissolve
    mar "Как ты мог..."
    adr "Почему ты скрывала это от меня? Как мне тебе доверять?"
    hide mar normal with dissolve
    hide adr normal with dissolve

    show badgirlie at right2 with dissolve
    bad "Кажется они были совсем не готовы к этому!"
    bad "На это я и рассчитывала!"
    bad "АХАХАХАХА!!"
    hide badgirlie with dissolve

    "В Париже хаос..."
    "Леди Баг и Супер-Кот под действием миража..."
    "Стали совсем слабы"
    extend " и не смогли противостоять"

    window hide # убрать диалоговое окно
    scene bg panic city with fade

    pause

    "Конец - Мираж победила"

    $ persistent.Bad_end = True # постоянная переменная

    return