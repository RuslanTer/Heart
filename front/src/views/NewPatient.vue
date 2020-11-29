<template lang="pug">
  v-card(flat style="background-color: rgba(0,0,0, 0)" height="90%" ).pa-15
    v-card-title.display-2 Новый пациент
    v-card-text(v-if="!check")
      v-row
        v-col(lg="4").align-content-center
          v-card.elevation-4
            v-card-title(@click="step = 1").text-style-patient ФИЗИЧЕСКИЕ ДАННЫЕ ПАЦИЕНТА
              v-spacer
              v-btn(text) Голосовой ввод
                v-icon mdi-microphone
            v-card-subtitle(v-if="step === 1") Шаг 1 из 2
            v-card-subtitle(v-if="step === 2") Шаг 2 из 2
            v-card-text(v-if="step === 1")
              v-row
                v-col(lg="6")
                  v-text-field(v-model="id"  outlined label="ID"  color="#19193E")
                  v-select(v-model="semya" outlined label="Семейное положение"  color="#19193E"  :items="semya_items")
                  v-select(v-model="nacionalnost" outlined label="Национальность" color="#19193E"  :items="nacionalnost_items")
                v-spacer
                v-col(lg="6")
                  v-select(v-model="sex" outlined label="Пол" color="#19193E"  :items="sex_items")
                  v-select(v-model="etnos" outlined label="Этнос" color="#19193E"  :items="etnos_items")
                  v-select(v-model="religiya" outlined label="Религия" color="#19193E"  :items="religiya_items")
              v-row
                v-col
                  v-select(v-model="mesto" outlined label="Место жительства" color="#19193E"  :items="mesto_items")
                  v-select(v-model="obrazovanie" outlined label="Образование" color="#19193E"  :items="obrazovanie_items")
                  v-select(v-model="professiya" outlined label="Профессия" color="#19193E" :items="professiya_items")
              v-row
                v-col(lg="6")
                  v-checkbox(v-model="work" label="Пациент работает" color="#19193E")
                  v-checkbox(v-model="dontwork" label="Прекращение работы по болезни" color="#19193E")
                  v-checkbox(v-model="gip" label="Альтериальная гипертензия" color="#19193E")
                  v-checkbox(v-model="sten" label="Стенокардия, ИБС,инфаркт миокарда" color="#19193E")
                  v-checkbox(v-model="other" label="Прочие заболевания сердца" color="#19193E")
                v-col(lg="6")
                  v-checkbox(v-model="old" label="Выход на пенсию" color="#19193E")
                  v-checkbox(v-model="sugar" label="Сахарный диабет" color="#19193E")
                  v-checkbox(v-model="onmk" label="ОНМК" color="#19193E")
                  v-checkbox(v-model="heart" label="Сердечная недостаточность" color="#19193E")
              v-row
                v-col
                  v-text-field(v-model="bol" v-if="dontwork" outlined label="Болезнь"  color="#19193E")
                  v-text-field(v-model="dlit_hiper" v-if="gip" outlined label="Длительность альтериальной гипертензии"  color="#19193E" )
                  v-text-field(v-model="dlit_steno" v-if="sten" outlined label="Длительность стенокардии, ИБС,инфаркт миокарда" color="#19193E" )
                  v-text-field(v-model="bol_other" v-if="other" outlined label="Какие заболевания сердца? "  color="#19193E")
                  v-text-field(v-model="dlit_diabet" v-if="sugar" outlined label="Длительность сахарного диабета" color="#19193E" )
                  v-text-field(v-model="dlit_omnk" v-if="onmk" outlined label="Длительность  ОМНК"  color="#19193E")
                  v-text-field(v-model="dlit_serdned" v-if="heart" outlined label="Длительность сердечной недостаточности" color="#19193E" )
              v-row.align-content-center.justify-center
                v-btn(text outlined width="50%" @click="step=2" dark style="background-color: #19193E").text-btn Далее
            v-card-text(v-if="step === 2")
              v-col
                v-row
                  v-col(lg="6")
                    v-text-field(v-model="sad1" color="#19193E" outlined label="САД1" )
                    v-text-field(v-model="sad2" color="#19193E" outlined label="САД2" )
                    v-text-field(v-model="chss1" color="#19193E" outlined label="ЧСС1" )
                    v-text-field(v-model="ot1" color="#19193E" outlined label="ОТ1" suffix="см")
                    v-text-field(v-model="ob1" color="#19193E" outlined label="ОБ1" suffix="см")
                    v-text-field(v-model="ves" color="#19193E" outlined label="Вес" suffix="кг")
                    v-text-field(v-model="plecho" color="#19193E" outlined label="Плечо" suffix="см")
                    v-text-field(v-model="golova" color="#19193E" outlined label="Голова" suffix="см")
                    v-text-field(v-model="silal2" color="#19193E" outlined label="Сила левая2" )
                    v-text-field(v-model="silar1" color="#19193E" outlined label="Сила правая1" )
                    v-text-field(v-model="silar3" color="#19193E" outlined label="Сила правая3" )
                    v-text-field(v-model="fev1" color="#19193E" outlined label="FEV1%" )
                    v-text-field(v-model="pefr1" color="#19193E" outlined label="PEFR%" )
                    v-text-field(v-model="holesterin" color="#19193E" outlined label="Холестирин" )
                    v-text-field(v-model="lpvp" color="#19193E" outlined label="ЛПВП" )
                  v-col(lg="6")
                    v-text-field(v-model="dad1" color="#19193E" outlined label="ДАД1" )
                    v-text-field(v-model="dad2" color="#19193E" outlined label="ДАД2" )
                    v-text-field(v-model="chss2" color="#19193E" outlined label="ЧСС2" )
                    v-text-field(v-model="ot2" color="#19193E" outlined label="ОТ2" suffix="см")
                    v-text-field(v-model="ob2" color="#19193E" outlined label="ОБ2" suffix="см")
                    v-text-field(v-model="rost" color="#19193E" outlined label="Рост" suffix="см")
                    v-text-field(v-model="golen" color="#19193E" outlined label="Голень" suffix="см")
                    v-text-field(v-model="silal1" color="#19193E" outlined label="Сила левая1" )
                    v-text-field(v-model="silal3" color="#19193E" outlined label="Сила левая3" )
                    v-text-field(v-model="silar2" color="#19193E" outlined label="Сила правая2" )
                    v-text-field(v-model="fev" color="#19193E" outlined label="FEV1" )
                    v-text-field(v-model="pefr" color="#19193E" outlined label="PEFR" )
                    v-text-field(v-model="glukoza" color="#19193E" outlined label="Глюкоза" )
                    v-text-field(v-model="triglic" color="#19193E" outlined label="Триглицериды" )
                    v-text-field(v-model="lpnp" color="#19193E" outlined label="ЛПНВ" )
                v-row.align-content-center.justify-center
                  v-btn(text outlined width="50%" @click="step=3" dark style="background-color: #19193E").text-btn Продолжить
                v-row.align-content-center.justify-center
                  v-btn(text width="50%" @click="step=1"  coloк="#19193E").text-btn Назад
        v-spacer
        v-col(lg="4").align-content-center
          v-card.elevation-4
            v-card-title(@click="step = 3").text-style-patient СОЦИАЛЬНЫЕ ДАННЫЕ ПАЦИЕНТА
              v-spacer
              v-btn(text) Голосовой ввод
                v-icon mdi-microphone
            v-card-subtitle(v-if="step === 3") Шаг 1 из 2
            v-card-subtitle(v-if="step === 4") Шаг 2 из 2
            v-card-text(v-if="step === 3")
              v-row
                v-col
                  v-subheader.title.black--text.pb-0 Люди обычно честные
                  v-radio-group(v-model="ludi_ob")
                    v-row
                      v-col(lg="3")
                        v-radio(label="Полностью согласен" value="Полностью согласен" color="#19193E")
                      v-col(lg="3")
                        v-radio(label="Частично согласен" value="Частично согласен" color="#19193E")
                      v-col(lg="3")
                        v-radio(label="Частично не согласен"  value="Частично не согласен"  color="#19193E")
                      v-col(lg="3")
                        v-radio(label="Полностью не согласен" value="Полностью не согласен" color="#19193E")
                  v-subheader.title.black--text.pb-0 Если я делаю...
                  v-radio-group(v-model="esli_ya")
                    v-row
                      v-col(lg="3")
                        v-radio(label="Полностью согласен" value="Полностью согласен" color="#19193E")
                      v-col(lg="3")
                        v-radio(label="Частично согласен" value="Частично согласен" color="#19193E")
                      v-col(lg="3")
                        v-radio(label="Частично не согласен"  value="Частично не согласен"  color="#19193E")
                      v-col(lg="3")
                        v-radio(label="Полностью не согласен" value="Полностью не согласен" color="#19193E")
                  v-subheader.title.black--text.pb-0 Реклама масла
                  v-radio-group(v-model="maslo")
                    v-row
                      v-col(lg="3")
                        v-radio(label="Полностью согласен" value="Полностью согласен" color="#19193E")
                      v-col(lg="3")
                        v-radio(label="Частично согласен" value="Частично согласен" color="#19193E")
                      v-col(lg="3")
                        v-radio(label="Частично не согласен"  value="Частично не согласен"  color="#19193E")
                      v-col(lg="3")
                        v-radio(label="Полностью не согласен" value="Полностью не согласен" color="#19193E")
                  v-subheader.title.black--text.pb-0 Реклама, мука
                  v-radio-group(v-model="muka")
                    v-row
                      v-col(lg="3")
                        v-radio(label="Полностью согласен" value="Полностью согласен" color="#19193E")
                      v-col(lg="3")
                        v-radio(label="Частично согласен" value="Частично согласен" color="#19193E")
                      v-col(lg="3")
                        v-radio(label="Частично не согласен"  value="Частично не согласен"  color="#19193E")
                      v-col(lg="3")
                        v-radio(label="Полностью не согласен" value="Полностью не согласен" color="#19193E")
                  v-subheader.title.black--text.pb-0 Реклама, рис
                  v-radio-group(v-model="ris")
                    v-row
                      v-col(lg="3")
                        v-radio(label="Полностью согласен" value="Полностью согласен" color="#19193E")
                      v-col(lg="3")
                        v-radio(label="Частично согласен" value="Частично согласен" color="#19193E")
                      v-col(lg="3")
                        v-radio(label="Частично не согласен"  value="Частично не согласен"  color="#19193E")
                      v-col(lg="3")
                        v-radio(label="Полностью не согласен" value="Полностью не согласен" color="#19193E")
                  v-subheader.title.black--text.pb-0 Реклама, безалкоголь
                  v-radio-group(v-model="bezalko")
                    v-row
                      v-col(lg="3")
                        v-radio(label="Полностью согласен" value="Полностью согласен" color="#19193E")
                      v-col(lg="3")
                        v-radio(label="Частично согласен" value="Частично согласен" color="#19193E")
                      v-col(lg="3")
                        v-radio(label="Частично не согласен"  value="Частично не согласен"  color="#19193E")
                      v-col(lg="3")
                        v-radio(label="Полностью не согласен" value="Полностью не согласен" color="#19193E")
                  v-subheader.title.black--text.pb-0 Реклама, снеки
                  v-radio-group(v-model="sneki")
                    v-row
                      v-col(lg="3")
                        v-radio(label="Полностью согласен" value="Полностью согласен" color="#19193E")
                      v-col(lg="3")
                        v-radio(label="Частично согласен" value="Частично согласен" color="#19193E")
                      v-col(lg="3")
                        v-radio(label="Частично не согласен"  value="Частично не согласен"  color="#19193E")
                      v-col(lg="3")
                        v-radio(label="Полностью не согласен" value="Полностью не согласен" color="#19193E")
                  v-subheader.title.black--text.pb-0 Реклама, сигареты
                  v-radio-group(v-model="sigarety")
                    v-row
                      v-col(lg="3")
                        v-radio(label="Полностью согласен" value="Полностью согласен" color="#19193E")
                      v-col(lg="3")
                        v-radio(label="Частично согласен" value="Частично согласен" color="#19193E")
                      v-col(lg="3")
                        v-radio(label="Частично не согласен"  value="Частично не согласен"  color="#19193E")
                      v-col(lg="3")
                        v-radio(label="Полностью не согласен" value="Полностью не согласен" color="#19193E")
                  v-subheader.title.black--text.pb-0 Реклама, алкоголь
                  v-radio-group(v-model="alko")
                    v-row
                      v-col(lg="3")
                        v-radio(label="Полностью согласен" value="Полностью согласен" color="#19193E")
                      v-col(lg="3")
                        v-radio(label="Частично согласен" value="Частично согласен" color="#19193E")
                      v-col(lg="3")
                        v-radio(label="Частично не согласен"  value="Частично не согласен"  color="#19193E")
                      v-col(lg="3")
                        v-radio(label="Полностью не согласен" value="Полностью не согласен" color="#19193E")
                  v-select(v-model="pom_oo" outlined label="Помощь общ. органам" color="#19193E" :items="['да','нет']")
                  v-select(v-model="pom_ro" outlined label="Помощь религ. органам" color="#19193E" :items="['да','нет']")
                  v-row
                    v-col(lg="6")
                      v-checkbox(v-model="poterya" label="Потеря работы" color="#19193E")
                      v-checkbox(v-model="bankrot" label="Банкротство" color="#19193E")
                      v-checkbox(v-model="razvod" label="Развод" color="#19193E")
                      v-checkbox(v-model="bolezn" label="Болезнь" color="#19193E")
                    v-col(lg="6")
                      v-checkbox(v-model="pensiua" label="Выход на пенсию" color="#19193E")
                      v-checkbox(v-model="grab" label="Грабеж" color="#19193E")
                      v-checkbox(v-model="konflict" label="Конфликт в семье" color="#19193E")

                  v-row.align-content-center.justify-center
                    v-btn(text outlined width="50%" @click="step=4" dark style="background-color: #19193E").text-btn Продолжить
                  v-row.align-content-center.justify-center
                    v-btn(text width="50%" @click="step=2"  coloк="#19193E").text-btn Назад
            v-card-text(v-if="step===4")
              v-row
                v-col(lg="6")
                  v-checkbox(v-model="mashina" label="Машина" color="#19193E")
                  v-checkbox(v-model="ferma" label="Ферма" color="#19193E")
                  v-checkbox(label="Другое" color="#19193E" v-model="other_step2")
                v-col(lg="6")
                  v-checkbox(v-model="garazh" label="Гараж" color="#19193E")
                  v-checkbox(v-model="lavka" label="Лавка" color="#19193E")
              v-row
                v-col
                  v-text-field(v-model="drugoe" outlined v-if="other_step2" label="Укажите" color="#19193E")
              v-row
                v-col
                  v-subheader.title.black--text Часть дохода на еду
                  v-radio-group.pr-4.pl-4(v-model="dohod_eda")
                    v-row
                      v-col(lg="3")
                        v-radio(label="1/2" value="1/2" color="#19193E")
                      v-col(lg="3")
                        v-radio(label="1/3" value="1/3" color="#19193E")
                      v-col(lg="3")
                        v-radio(label="1/4" value="1/4" color="#19193E")
                      v-col(lg="3")
                        v-radio(label="1/10 и менее" value="1/10 и менее" color="#19193E")
                  v-textarea(v-model="dohod_eda_comm" outlined label="Комментарий"  color="#19193E" full-width)
              v-row
                v-col
                  v-subheader.title.black--text Достаток по сравнению с другими
                  v-radio-group.pr-4.pl-4(v-model="dohod_eda_drug")
                    v-row
                      v-col(lg="6")
                        v-radio(label="очень низкий" value="очень низкий" color="#19193E")
                      v-col(lg="6")
                        v-radio(label="низкий" value="низкий" color="#19193E")
                      v-col(lg="6")
                        v-radio(label="средний" value="средний" color="#19193E")
                      v-col(lg="6")
                        v-radio(label="выше среднего" value="выше среднего" color="#19193E")
              v-row
                v-col
                  v-subheader.title.black--text Тип жилья
                  v-radio-group.pr-4.pl-4(v-model="tip_zhilya")
                    v-row
                      v-col(lg="4")
                        v-radio(label="Квартира" value="Квартира" color="#19193E")
                      v-col(lg="4")
                        v-radio(label="Частный дом" value="Частный дом" color="#19193E")
                  v-text-field(v-model="komnat" outlined label="Количество комнат"  color="#19193E")
                  v-text-field(v-model="ploshad" outlined label="Площадь (кв.м.)"  color="#19193E")
              v-row.align-content-center.justify-center
                v-btn(text outlined width="50%" @click="step=5" dark style="background-color: #19193E").text-btn Продолжить
              v-row.align-content-center.justify-center
                v-btn(text width="50%" @click="step=3"  coloк="#19193E").text-btn Назад
        v-spacer
        v-col(lg="4").align-content-center
          v-card.elevation-4
            v-card-title(@click="step = 5").text-style-patient ДОПОЛНИТЕЛЬНЫЕ ДАННЫЕ
              v-spacer
              v-btn(text  ) Голосовой ввод
                v-icon mdi-microphone
            v-card-text(v-if="step === 5")
              v-row
                v-col
                  v-subheader.title.black--text.pb-0 Замечания курящим детям
                  v-radio-group(v-model="kur_det")
                    v-row
                      v-col(lg="3")
                        v-radio(label="обычное явление" value="обычное явление" color="#19193E")
                      v-col(lg="3")
                        v-radio(label="некоторые взрослые" value="некоторые взрослые" color="#19193E")
                      v-col(lg="3")
                        v-radio(label="редко, но возможно" value="редко, но возможно" color="#19193E")
                      v-col(lg="3")
                        v-radio(label="такого не было" value="такого не было" color="#19193E")
                  v-subheader.title.black--text.pb-0 Замечания курящим подросткам
                  v-radio-group(v-model="kur_pod")
                    v-row
                      v-col(lg="3")
                        v-radio(label="обычное явление" value="обычное явление" color="#19193E")
                      v-col(lg="3")
                        v-radio(label="некоторые взрослые" value="некоторые взрослые" color="#19193E")
                      v-col(lg="3")
                        v-radio(label="редко, но возможно" value="редко, но возможно" color="#19193E")
                      v-col(lg="3")
                        v-radio(label="такого не было" value="такого не было" color="#19193E")
                  v-subheader.title.black--text.pb-0 Замечания нездоровой еды / дети
                  v-radio-group(v-model="nexd_eda_det")
                    v-row
                      v-col(lg="3")
                        v-radio(label="обычное явление" value="обычное явление" color="#19193E")
                      v-col(lg="3")
                        v-radio(label="некоторые взрослые" value="некоторые взрослые" color="#19193E")
                      v-col(lg="3")
                        v-radio(label="редко, но возможно" value="редко, но возможно" color="#19193E")
                      v-col(lg="3")
                        v-radio(label="такого не было" value="такого не было" color="#19193E")
                  v-subheader.title.black--text.pb-0 Замечания нездоровой еды / подростки
                  v-radio-group(v-model="nexd_eda_pod")
                    v-row
                      v-col(lg="3")
                        v-radio(label="обычное явление" value="обычное явление" color="#19193E")
                      v-col(lg="3")
                        v-radio(label="некоторые взрослые" value="некоторые взрослые" color="#19193E")
                      v-col(lg="3")
                        v-radio(label="редко, но возможно" value="редко, но возможно" color="#19193E")
                      v-col(lg="3")
                        v-radio(label="такого не было" value="такого не было" color="#19193E")
                  v-subheader.title.black--text.pb-0 Советы физ. активности / дети
                  v-radio-group(v-model="sovet_det")
                    v-row
                      v-col(lg="3")
                        v-radio(label="обычное явление" value="обычное явление" color="#19193E")
                      v-col(lg="3")
                        v-radio(label="некоторые взрослые" value="некоторые взрослые" color="#19193E")
                      v-col(lg="3")
                        v-radio(label="редко, но возможно" value="редко, но возможно" color="#19193E")
                      v-col(lg="3")
                        v-radio(label="такого не было" value="такого не было" color="#19193E")
                  v-subheader.title.black--text.pb-0 Советы физ. активности / подростки
                  v-radio-group(v-model="sovet_pod")
                    v-row
                      v-col(lg="3")
                        v-radio(label="обычное явление" value="обычное явление" color="#19193E")
                      v-col(lg="3")
                        v-radio(label="некоторые взрослые" value="некоторые взрослые" color="#19193E")
                      v-col(lg="3")
                        v-radio(label="редко, но возможно" value="редко, но возможно" color="#19193E")
                      v-col(lg="3")
                        v-radio(label="такого не было" value="такого не было" color="#19193E")
              v-row.align-content-center.justify-center.pt-3
                v-btn(text outlined width="50%" @click="createPatient" dark style="background-color: #19193E").text-btn Создать анализ
              v-row.align-content-center.justify-center
                v-btn(text width="50%" @click="step=4"  coloк="#19193E").text-btn Назад

    v-card-text(v-else)
      v-card(flat style="background-color: rgba(0,0,0, 0)").elevation-0
        v-row
          v-col(lg="5")
            v-card.elevation-0
              v-card-title.text-style-patient.pt-6 ПЕРСОНАЛЬНЫЕ РЕКОМЕНДАЦИИ
              v-card-text.pt-12  {{rec}}
          v-col(lg="7")
            v-row
              v-col(lg="6").pt-0
                v-card().elevation-0
                  v-card-title Артериальная гипертензия
                  v-card-text
                    v-sparkline(:value="[bols.model1/2, bols.model1]"
                      :gradient="gradient"
                      :smooth="radius || false"
                      :padding="padding"
                      :line-width="width"
                      :stroke-linecap="lineCap"
                      :gradient-direction="gradientDirection"
                      :fill="fill"
                      :type="type"
                      :auto-line-width="autoLineWidth"
                      auto-draw)
                      template(v-slot:label="item") {{ item.value }}
              v-col(lg="6").pt-0
                v-card().elevation-0
                  v-card-title ОНМК
                  v-card-text
                    v-sparkline(:value="[bols.model2/2, bols.model2]"
                      :gradient="gradient"
                      :smooth="radius || false"
                      :padding="padding"
                      :line-width="width"
                      :stroke-linecap="lineCap"
                      :gradient-direction="gradientDirection"
                      :fill="fill"
                      :type="type"
                      :auto-line-width="autoLineWidth"
                      auto-draw)
                      template(v-slot:label="item") {{ item.value }}
              v-col(lg="6").pt-0
                v-card().elevation-0
                  v-card-title Сердечная недостаточность
                  v-card-text
                    v-sparkline(:value="[bols.model3/2, bols.model3]"
                      :gradient="gradient"
                      :smooth="radius || false"
                      :padding="padding"
                      :line-width="width"
                      :stroke-linecap="lineCap"
                      :gradient-direction="gradientDirection"
                      :fill="fill"
                      :type="type"
                      :auto-line-width="autoLineWidth"
                      auto-draw)
                      template(v-slot:label="item") {{ item.value }}
              v-col(lg="6").pt-0
                v-card().elevation-0
                  v-card-title Стенокардия/ИБС/Инфаркт миокарда
                  v-card-text
                    v-sparkline(:value="[bols.model4/2, bols.model4]"
                      :gradient="gradient"
                      :smooth="radius || false"
                      :padding="padding"
                      :line-width="width"
                      :stroke-linecap="lineCap"
                      :gradient-direction="gradientDirection"
                      :fill="fill"
                      :type="type"
                      :auto-line-width="autoLineWidth"
                      auto-draw)
                      template(v-slot:label="item") {{ item.value }}
              v-col(lg="6").pt-0
                v-card().elevation-0
                  v-card-title Прочие заболевания сердца
                  v-card-text
                    v-sparkline(:value="[bols.model5/2, bols.model5]"
                      :gradient="gradient"
                      :smooth="radius || false"
                      :padding="padding"
                      :line-width="width"
                      :stroke-linecap="lineCap"
                      :gradient-direction="gradientDirection"
                      :fill="fill"
                      :type="type"
                      :auto-line-width="autoLineWidth"
                      auto-draw)
                      template(v-slot:label="item") {{ item.value }}
</template>

<script>
import Analys from "@/views/Analys";
import axios from "axios";
const gradients = [
  ['#222'],
  ['#42b3f4'],
  ['red', 'orange', 'yellow'],
  ['purple', 'violet'],
  ['#00c6ff', '#F0F', '#FF0'],
  ['#f72047', '#ffd200', '#1feaea'],
]
export default {
  name: "NewPatient",
  components: {Analys},
  data: () => ({
    bols: {model1: 12, model2: 13, model3: 13, model4: 13, model5: 13},
    picker: new Date().toISOString().substr(0, 7),
    width: 2,
    radius: 10,
    padding: 8,
    lineCap: 'round',
    gradient: gradients[5],
    gradientDirection: 'top',
    gradients,
    fill: false,
    type: 'trend',
    autoLineWidth: false,
    rec: " Первичная профилактика инсульта – это комплекс мероприятий направленных на предотвращение развития острых нарушений церебрального кровообращения – геморрагического инсульта или инфаркта мозга (ишемического инсульта) - ведение здорового образа жизни, рациональное питание, поддержание адекватной массы тела, воздержание от курения и адекватное медикаментозное лечение заболеваний сердца и сосудов, сахарного диабета и других заболеваний.",
    work: false,
    check:false,
    dontwork: false,
    gip: false,
    sten: false,
    other: false,
    old: false,
    sugar: false,
    onmk: false,
    heart: false,
    step: 1,
    other_step2: false,
    id: null,
    sex: null,
    semya: null,
    etnos: null,
    nacionalnost: null,
    religiya: null,
    mesto: null,
    obrazovanie: null,
    professiya: null,
    dlit_omnk: "",
    dlit_serdned: "",
    dlit_steno: "",
    dlit_serd: "",
    dlit_hiper: "",
    bol_other: "",
    bol: "",
    dlit_diabet: "",
    sad1: null,
    sad2: null,
    dad1: null,
    dad2: null,
    chss1: null,
    chss2: null,
    ot1: null,
    ot2: null,
    ob1: null,
    ob2: null,
    ves: null,
    rost: null,
    plecho: null,
    golen: null,
    golova: null,
    silal1: null,
    silal2: null,
    silal3: null,
    silar1: null,
    silar2: null,
    silar3: null,
    fev: null,
    fev1: null,
    fvc: null,
    pefr: null,
    pefr1: null,
    glukoza: null,
    holesterin: null,
    triglic: null,
    lpvp: null,
    lpnp: null,
    semya_items: [
      'никогда не был(а) в браке',
      'в разводе',
      'в браке в настоящее время', '' +
      'вдовец / вдова',
      'гражданский брак / проживание с партнером',
      'раздельное проживание (официально не разведены)'],
    etnos_items: ['европейская', 'другая'],
    religiya_items: ['Христианство', 'Ислам', 'Буддизм', 'Атеизм', 'Нет', 'Другое'],
    nacionalnost_items: ['Русские', 'Белорусы', 'Татары', 'Удмурты', 'Казахи', 'Украинцы', 'Немцы', 'Другие национальности'],
    mesto_items: ['Город', 'Село'],
    sex_items: ['Мужчина', 'Женщина'],
    professiya_items: [
      'вооруженные силы',
      'дипломированные специалисты',
      'служащие',
      'низкоквалифицированные работники',
      'представители   законодат.   органов   власти,  высокопостав. долж.лица и менеджеры',
      'ведение домашнего хозяйства',
      'ремесленники и представители других отраслей промышленности',
      'работники,  занятые в сфере обслуживания, торговые работники магазинов и рынков',
      'техники и младшие специалисты',
      'операторы и монтажники установок и машинного оборудования',
      'квалифицированные работники сельского хозяйства и рыболовного',
      'Другое',
    ],
    obrazovanie_items: ['незаконченное основное общее', 'основное общее (9 кл.)', ' средняя школа / закон.среднее / выше среднего', 'профессиональное училище', 'ВУЗ'],
    ludi_ob: '',
    esli_ya: '',
    maslo: '',
    muka: '',
    ris: '',
    bezalko: '',
    alko: '',
    sneki: '',
    sigarety: '',
    pom_oo: '',
    pom_ro: '',
    poterya: false,
    pensiua: false,
    bankrot: false,
    grab: false,
    razvod: false,
    konflict: false,
    bolezn: false,
    mashina: false,
    garazh: false,
    ferma: false,
    drugoe: '',
    lavka: false,
    dohod_eda: '',
    dohod_eda_comm: '',
    dohod_eda_drug: '',
    tip_zhilya: '',
    komnat: '',
    ploshad: '',
    kur_det: false,
    kur_pod: false,
    nexd_eda_det: false,
    nexd_eda_pod: false,
    sovet_det: false,
    sovet_pod: false,
  }),
  methods: {
    async createPatient() {
      this.check=true
      const {data} = await axios.put('http://194.67.116.92:8080/api/patient/', {
        ID_0_0: this.id ,
        Pol_1_1: this.sex ,
        Semya_2_1: this.semya ,
        Etnos_3_1: this.etnos ,
        Nacionalnost_4_1: this.nacionalnost ,
        Religiya_5_1: this.religiya ,
        Mesto_prozhivaniya_1gorod_2selo_1_0: this.mesto ,
        Obrazovanie_6_1: this.obrazovanie ,
        Professiya_7_1: this.professiya ,
        Vy_rabotaete_8_1: this.work ,
        Vyhod_na_pensiu_9_1: this.old ,
        Prekraschenie_raboty_po_bolezni_10_1: this. dontwork,
        Saharnyi_diabet_11_1: this.sugar ,
        Dlitelnost_saharnogo_diabeta_12_1: this.dlit_diabet ,
        Arterialnaya_gipertenziya_13_1: this.gip ,
        Dlitelnost_arterialnoi_gipertenzii_14_1: this.dlit_hiper ,
        ONMK_15_1: this.onmk ,
        Danost_ONMK_16_1: this.dlit_omnk ,
        Stenokardiya_IBS_infarkt_miokarda_17_1: this.sten ,
        Dlitelnost_stenokardii_IBS_infarkta_miokarda_18_1: this.dlit_steno ,
        Serdechnaya_nedostatochnost_19_1: this.heart ,
        Dlitelnost_serdechnoi_nedostatochnosti_20_1: this.dlit_serd ,
        Prochie_zabolevaniya_serdca_21_1: this.other ,
        SAD1_1_3: this.sad1,
        SAD1_2_3: this.sad2 ,
        DAD1_1_3: this.dad1 ,
        DAD1_2_3: this.dad2 ,
        CHSS1_5_3: this.chss1 ,
        CHSS2_5_3: this.chss2 ,
        OT1_7_3: this.ot1 ,
        OT2_8_3: this.ot2 ,
        OB1_9_3: this.ob1 ,
        OB2_10_3: this.ob2 ,
        Ves_11_3: this.ves ,
        Rost_12_3: this.rost ,
        Plecho_13_3: this.plecho ,
        Golen_14_3: this.golen ,
        Golova_15_3: this.golova ,
        Sila_levaya1_16_3: this.silal1 ,
        Sila_levaya2_17_3: this.silal2 ,
        Sila_levaya3_18_3: this.silal3 ,
        Sila_pravaya1_19_3: this.silar1 ,
        Sila_pravaya2_19_3: this.silar2 ,
        Sila_pravaya3_19_3: this.silar3 ,
        FEV1_22_3: this.fev ,
        FEV1p_23_3: this.fev1 ,
        FVC_24_3: this.fvc ,
        PEFR_26_3: this.pefr ,
        PEFRp_27_3: this.pefr1 ,
        Glukoza_28_3: this.glukoza ,
        Holesterin_29_3: this.holesterin ,
        Trigliceridy_30_3: this.triglic ,
        LPVP_31_3: this.lpvp ,
        LPNP_32_3: this.lpnp ,
        Ludi_obychno_chestnye_1_2: this.ludi_ob,
        Esli_ya_delau_2_2: this.esli_ya ,
        Reklama_maslo_3_2: this.maslo ,
        Reklama_muka_4_2: this.muka ,
        Reklama_ris_5_2: this.ris ,
        Reklama_bezalkogol_6_2: this.bezalko ,
        Reklama_sneki_7_2: this.sneki ,
        Reklama_sigarety_8_2: this.sigarety ,
        Reklama_alkogol_9_2: this.alko ,
        Pomosch_obsch_organ_10_2: this.pom_oo ,
        Pomosch_OO_kolvo_11_2: null ,
        Pomosch_relig_organ_12_2: this.pom_ro ,
        Poterya_raboty36_17_2: this.poterya ,
        Vyhod_na_pensiu36_18_2: this.pensiua ,
        Bankrotstvo36_19_2: this.bankrot ,
        Grabezh36_20_2: this.grab ,
        Razvod36_21_2: this.razvod ,
        Konflikt_v_seme36_22_2: this.konflict ,
        Bolezn36_24_2: this.bolezn ,
        Mashina_43_5: this.mashina ,
        Garazh_44_5: this.garazh ,
        Ferma_45_5: this.ferma ,
        Lavka_46_5: this.lavka ,
        Drugoe_47_5: this.drugoe ,
        CHast_dohoda_na_edu_49_5: this.dohod_eda ,
        CHast_dohoda_na_edu_49_5_50_5: this.dohod_eda_comm ,
        Dostatok_po_srav_s_drug_51_5: this.dohod_eda_drug ,
        Tip_zhilya_52_5: this.tip_zhilya ,
        CHislo_komnat_53_5: this.komnat,
        Ploschad_zhilya_54_5: this.ploshad ,
        Zamechaniya_kuryaschim_detyam20_166_10: this.kur_det ,
        Zamechaniya_kuryaschim_podrostkam20_167_10: this.kur_pod ,
        Zamechaniya_nezdorovoi_edy_deti21_168_10: this.nexd_eda_det ,
        Zamechaniya_nezdorovaya_eda_podrostki21_169_10: this.nexd_eda_pod ,
        Sovety_fiz_aktivnosti_deti22_170_10: this.sovet_det ,
        Sovety_fiz_aktivnosti_podrostki22_171_10: this.sovet_pod ,
      })
      if (data!==null)

      {this.models = data}
    }
  }
}
</script>

<style scoped>

.text-style-patient {
  font-family: Roboto, sans-serif;
  font-size: 12px;
  font-style: normal;
  font-weight: 500;
  line-height: 14px;
  letter-spacing: 0.02em;
  text-align: left;

}
</style>
