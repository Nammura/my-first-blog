from django.shortcuts import render, render_to_response
from .forms import DistributeForm
from .forms import PlayerForm
from .models import (Sunday,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday)
from .models import Daytoday
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.template.context_processors import csrf



import re
import random
import pandas as pd
import datetime


def distribute(request):
    #parameterの定義
    params = {'distText':'', 'title': '割り振り', 'DistributeForm':DistributeForm(), 'PlayerForm':PlayerForm(), 'team':'', 'pk':''}
    
    #Daytodayモデルのpkを取得
    pk = Daytoday.objects.all()[0].pk

    #曜日の取得(モデル優先)
    week_num = 0
    x = 0
    if Daytoday.objects.all()[0].days in [['1'],['2'],['3'],['4'],['5'],['6'],['7']]:
        week_num = int(((Daytoday.objects.all())[0].days)[0])
        week_num += 5
        week_num = week_num % 7
    else:
        week_num = datetime.date.today().weekday()
    
    #対応チームの取得
    teamDict = {
        0:'月曜チーム',
        1:'火曜チーム',
        2:'水曜チーム',
        3:'木曜チーム',
        4:'金曜チーム',
        5:'土曜チーム',
        6:'日曜チーム'
    }
    team = teamDict[week_num]
    
    
    #該当曜日モデルの全てのオブジェクトをregistersに格納
    if week_num == 6:
        registers = Sunday.objects.all()
    elif week_num == 0:
        registers = Monday.objects.all()
    elif week_num == 1:
        registers = Tuesday.objects.all()
    elif week_num == 2:
        registers = Wednesday.objects.all()
    elif week_num == 3:
        registers = Thursday.objects.all()
    elif week_num == 4:
        registers = Friday.objects.all()
    else:
        registers = Saturday.objects.all()
        
    
    #選択肢の定義
    choice1 = []
    choiceDict = {}
    for i in range(len(registers)):
        choice1.append((str(i+1),registers[i].member_name))
        choiceDict[str(i+1)] = registers[i].member_name
    
  
    #入力があるかないかの分岐
    if request.method == 'POST':
    
        #DistributeFormの値を取得
        distText = request.POST['distText']
        
                
    
        #PlayerFormの値を取得
        listret = request.POST.getlist('player')
        
    
        #その日の対応者の取得
        activePlayer = []
        for i in listret:
            activePlayer.append(choiceDict[i])
        
        #全科目と理系科目の定義
        subjectList = ["英語", "中学数学", "高校数学", "化学", "物理", "中学理科"]
        ScienceSubject = ["高校数学", "中学数学", "物理", "化学", "中学理科"]
        
        #入力が適切かどうかの分岐
        if (len(re.findall(r"\d+", distText)) != len(subjectList)) and (len(re.findall(r"\d+", distText)) != len(subjectList) + 1):
            params['distText'] = ['入力が不適切です。']
            params['DistributeForm'] = DistributeForm(request.POST)
            params['PlayerForm'] = PlayerForm(request.POST)
            params['WeekForm'] = WeekForm(request.POST)
            params['team'] = team
            params['pk'] = pk
            
        else:
            #文系、文系プラス、理系の分類
            humanitiesDefault = []
            humanitiesPlusDefault = []
            ScienceDefault = []
            
            science_or_humanities = []
            
            for register in registers:
                if register.science_or_humanities == ['1']:
                    humanitiesDefault.append(register.member_name)
                elif register.science_or_humanities == ['2']:
                    humanitiesPlusDefault.append(register.member_name)
                else:
                    ScienceDefault.append(register.member_name)
                
            
            #その日の対応者の分類
            humanities = []
            humanitiesPlus = []
            Science = []
            
            for person in humanitiesDefault:
                if person in activePlayer:
                    humanities.append(person)
                    
            for person in humanitiesPlusDefault:
                if person in activePlayer:
                    humanitiesPlus.append(person)
                    
            for person in ScienceDefault:
                if person in activePlayer:
                    Science.append(person)
                    
            random.shuffle(humanities)
            random.shuffle(humanitiesPlus)
            random.shuffle(Science)
            Humanities = humanities + humanitiesPlus
            people = humanities + humanitiesPlus + Science
            n = len(people)

            #各々の対応科目を定義
            ScienceRangeDict = {}
            SubjectSelectDict = {'中学数学':'1', '物理':'2', '化学':'3', '中学理科':'4', '高校数学':'0'}
            for register in registers:
                patternList = [[],[]]
                for subject in ScienceSubject:
                    if SubjectSelectDict[subject] not in register.only_for_science_menber_impossible_subject:
                        patternList[1].append(subject)
                        if SubjectSelectDict[subject] not in register.only_for_science_menber_no_good_subject:
                            patternList[0].append(subject)
                ScienceRangeDict[register.member_name] = patternList
                    

            #理系科について、その科目に対応できる人のリスト
            ScienceSubjectDict = {"高校数学":[], "中学数学":[], "物理":[], "化学":[], "中学理科":[]}

            #その日の理系対応者
            for subject in ScienceSubject:
                for person in Science:
                    if subject in ScienceRangeDict[person][0]:
                        ScienceSubjectDict[subject].append(person)
                #対応者か0の科目があるとき、非常電源に切替
                if ScienceSubjectDict[subject] == []:
                    for person in Science:
                        if subject in ScienceRangeDict[person][1]:
                            ScienceSubjectDict[subject].append(person)
            
            #対応者が0の教科を探す
            errorSubject = []
            if len(Humanities) == 0:
                errorSubject.append('英語')
            for subject in ScienceSubject:
                if ScienceSubjectDict[subject] == []:
                    errorSubject.append(subject)
            
            #対応者が0の教科があるとき、エラーメッセージを出す
            if len(errorSubject) != 0:
                errorMessage = ''
                for subject in errorSubject:
                    errorMessage += subject + '、'
                errorMessage = errorMessage.rstrip('、')
                errorMessage += 'の対応者がいません。'
                
                #フォームの保持
                params['distText'] = [errorMessage]
                params['DistributeForm'] = DistributeForm(request.POST)
                
                form = PlayerForm()
                form.fields['player'].choices = choice1
                form.fields['player'].initial = listret
                params['PlayerForm'] = form
                params['registers'] = registers
                params['team'] = team
                params['pk'] = pk
             
            #対応者が0の教科がないとき、割り振り開始
            else:
                ScienceSubject.pop(0)


                #各人の各科目の対応数を格納するxDictを定義
                xDict = {}
                for person in people:
                    xDict[person] = {}
                    for subject in subjectList:
                        xDict[person][subject] = 0
                        
                        
                #qNumber関数を定義
                def qNumber(text):
                    
                    number = re.findall(r"\d+", text)
                    if len(number) == len(subjectList) + 1:
                        number.pop(0)
                    for i in range(len(number)):
                        number[i] = int(number[i])
                    
                    index = []
                    for i in subjectList:
                        index.append(text.find(i))
                        
                    indexDict = {}
                    for i in range(len(index)):
                        indexDict[index[i]] = subjectList[i]
                        
                    index.sort()
                    
                    qNumberDict = {}
                    for i in range(len(index)):
                        qNumberDict[indexDict[index[i]]] = number[i]
                        
                    return qNumberDict

                #Dist関数を定義
                def Dist(num, n):
                    dist = []
                    for i in range(n):
                        dist.append(num // n)
                    
                    balance = num - (num // n) * n
                    for i in reversed(range(n)):
                        if balance > 0:
                            dist[i] += 1
                            balance -= 1
                        else:
                            dist[i] += 0
                    
                    return dist


                #テキストの定義
                text = distText
                qNumber = qNumber(text)

                #各人の対応数を格納するEachDictを定義
                EachDict ={}
                Total = 0
                for i in subjectList:
                        Total += qNumber[i]
                for i in range(n):
                    EachDict[people[i]] = Dist(Total, n)[i]


                def HumanitiesDist():
                    total = 0
                    for i in subjectList:
                        total += qNumber[i]
                    HumanitiesCapa = 0
                    for i in Humanities:
                        HumanitiesCapa += EachDict[i]

                    humanitiesCapa = 0
                    for i in humanities:
                        humanitiesCapa += EachDict[i]


                    #分岐1 英語と中数が少なすぎて文系の対応数が理系の対応数より小さくなるパターン
                    if qNumber["英語"] + qNumber["中学数学"] < HumanitiesCapa:
                        for i in range(len(Humanities)):
                            EachDict[Humanities[i]] = Dist(qNumber["英語"] + qNumber["中学数学"], len(Humanities))[i]
                        HumanitiesCapa = 0
                        for i in Humanities:
                            HumanitiesCapa += EachDict[i]
                        humanitiesCapa = 0
                        for i in humanities:
                            humanitiesCapa += EachDict[i]

                        #分岐1-1 文系の枠を英語で埋め切れないパターン
                        if qNumber["英語"] < humanitiesCapa:
                            EnglishDist = Dist(qNumber["英語"], len(humanities))
                            JrMathDelta = 0
                            for i in range(len(humanities)):
                                xDict[humanities[i]]["英語"] = EnglishDist[i]
                                xDict[humanities[i]]["中学数学"] = EachDict[humanities[i]] - xDict[humanities[i]]["英語"]
                                JrMathDelta += xDict[humanities[i]]["中学数学"]
                            for i in humanitiesPlus:
                                xDict[i]["中学数学"] = EachDict[i]
                                JrMathDelta += xDict[i]["中学数学"]
                            qNumber["中学数学"] -= JrMathDelta
                            qNumber["英語"] = 0

                        #分岐1-2 文系の枠を英語で埋め切れるパターン
                        else:
                            EnglishDelta = 0
                            JrMathDelta = 0
                            for i in humanities:
                                xDict[i]["英語"] = EachDict[i]
                                EnglishDelta += xDict[i]["英語"]
                            qNumber["英語"] -= EnglishDelta
                            EnglishDist = Dist(qNumber["英語"], len(humanitiesPlus))
                            for i in range(len(humanitiesPlus)):
                                xDict[humanitiesPlus[i]]["英語"] = EnglishDist[i]
                                xDict[humanitiesPlus[i]]["中学数学"] = EachDict[humanitiesPlus[i]] - xDict[humanitiesPlus[i]]["英語"]
                                JrMathDelta += xDict[humanitiesPlus[i]]["中学数学"]
                            qNumber["中学数学"] -= JrMathDelta
                            qNumber["英語"] = 0

                        total = 0
                        for i in subjectList:
                            total += qNumber[i]
                        HumanitiesCapa = 0
                        for i in Humanities:
                            HumanitiesCapa += EachDict[i]
                        for i in range(len(Science)):
                            EachDict[Science[i]] = Dist(total, len(Science))[i]


                    #分岐2 英語が多すぎて文系の対応数が理系の対応数より大きくなるパターン
                    elif qNumber["英語"] > HumanitiesCapa:
                        EnglishDist = Dist(qNumber["英語"], len(Humanities))
                        random.shuffle(Humanities)
                        for i in range(len(Humanities)):
                            xDict[Humanities[i]]["英語"] = EnglishDist[i]

                        total -= qNumber["英語"]
                        for i in range(len(Science)):
                            EachDict[Science[i]] = Dist(total, len(Science))[i]




                    #分岐3 文系の枠を英語で埋め切れないパターン
                    elif (HumanitiesCapa - qNumber["中学数学"] <= qNumber["英語"]) and (qNumber["英語"] < humanitiesCapa)  :
                        EnglishDist = Dist(qNumber["英語"], len(humanities))
                        JrMathDelta = 0
                        for i in range(len(humanities)):
                            xDict[humanities[i]]["英語"] = EnglishDist[i]
                            xDict[humanities[i]]["中学数学"] = EachDict[humanities[i]] - xDict[humanities[i]]["英語"]
                            JrMathDelta += xDict[humanities[i]]["中学数学"]
                        for i in humanitiesPlus:
                            xDict[i]["中学数学"] = EachDict[i]
                            JrMathDelta += xDict[i]["中学数学"]
                        qNumber["中学数学"] -= JrMathDelta



                    #分岐4 文系の枠を英語で埋め切れるパターン
                    else:
                        EnglishDelta = 0
                        JrMathDelta = 0
                        for i in humanities:
                            xDict[i]["英語"] = EachDict[i]
                            EnglishDelta += xDict[i]["英語"]
                        qNumber["英語"] -= EnglishDelta
                        EnglishDist = Dist(qNumber["英語"], len(humanitiesPlus))
                        for i in range(len(humanitiesPlus)):
                            xDict[humanitiesPlus[i]]["英語"] = EnglishDist[i]
                            xDict[humanitiesPlus[i]]["中学数学"] = EachDict[humanitiesPlus[i]] - xDict[humanitiesPlus[i]]["英語"]
                            JrMathDelta += xDict[humanitiesPlus[i]]["中学数学"]
                        qNumber["中学数学"] -= JrMathDelta


                def ScienceDist():
                    for i in ScienceSubject:
                        random.shuffle(Science)
                        dist = Dist(qNumber[i], len(ScienceSubjectDict[i]))
                        for j in range(len(ScienceSubjectDict[i])):
                            xDict[ScienceSubjectDict[i][j]][i] = dist[j]
                        
                    minus = 0
                    for i in Science:
                        Delta = 0
                        for j in ScienceSubject:
                            Delta += xDict[i][j]
                        xDict[i]["高校数学"] = EachDict[i] - Delta
                        if Delta > EachDict[i]:
                            minus = 1
                    
                    #負の割り振りがある場合の対処、問題ありと問題なしのグループに分ける
                    if minus == 1:
                        noProblem = []
                        Problem = []
                        for i in Science:
                            if xDict[i]["高校数学"] < 0:
                                Problem.append(i)
                            else:
                                noProblem.append(i)
                        #問題ありの情報をまとめる
                        problemLength = []
                        problemSubject = []
                        for person in Problem:
                            length = 0
                            sub = []
                            for subject in ScienceSubject:
                                if person in ScienceSubjectDict[subject]:
                                    length += 1
                                    sub.append(subject)

                            problemLength.append(length)
                            problemSubject.append(sub)
                        problemDict = {'問題者':Problem, '対応科目数':problemLength, '対応科目':problemSubject}
                        problemDf = pd.DataFrame.from_dict(problemDict)
                        problemDf.sort_values('対応科目数', inplace=True)
                        problemDf.reset_index(drop=True,inplace=True)

                        #問題なしの情報をまとめる
                        noProblemLength = []
                        noProblemSubject = []
                        for person in noProblem:
                            length = 0
                            sub = []
                            for subject in ScienceSubject:
                                if person in ScienceSubjectDict[subject]:
                                    length += 1
                                    sub.append(subject)

                            noProblemLength.append(length)
                            noProblemSubject.append(sub)
                        noProblemDict = {'無問題者':noProblem, '対応科目数':noProblemLength, '対応科目':noProblemSubject}
                        noProblemDf = pd.DataFrame.from_dict(noProblemDict)
                        noProblemDf.sort_values('対応科目数', inplace=True)
                        noProblemDf.reset_index(drop=True,inplace=True)


                        #問題あり一人一人に対し処理をする
                        for i in problemDf.index:
                            co = []
                            for j in noProblemDf.index:
                                co.append([])
                            noProblemDf['共通科目'] = co
                            for j in noProblemDf.index:
                                for subject in noProblemDf['対応科目'][j]:
                                    if subject in problemDf['対応科目'][i]:
                                        noProblemDf['共通科目'][j].append(subject)
                            index = []
                            for j in noProblemDf.index:
                                if noProblemDf['共通科目'][j] != []:
                                    index.append(j)
                


                            for j in noProblemDf.index:
                                if  (xDict[problemDf['問題者'][i]]['高校数学'] == 0):
                                    break
                                else:

                                    for subject in noProblemDf['共通科目'][j]:
                                        if  (xDict[problemDf['問題者'][i]]['高校数学'] == 0):
                                            break
                                        else:

                                            for k in range(xDict[noProblemDf['無問題者'][j]]['高校数学']):
                                                if (xDict[problemDf['問題者'][i]]['高校数学'] == 0) or (xDict[problemDf['問題者'][i]][subject] == 0):
                                                    break
                                                else:
                                                    xDict[problemDf['問題者'][i]]['高校数学'] += 1
                                                    xDict[noProblemDf['無問題者'][j]]['高校数学'] -=1
                                                    xDict[problemDf['問題者'][i]][subject] -= 1
                                                    xDict[noProblemDf['無問題者'][j]][subject] +=1
                                                    
                        #それでもマイナスがある場合の最終処理
                        while True:
                            plus = []
                            minus = []
                            zero = []
                            for person in Science:
                                if xDict[person]["高校数学"] < 0:
                                    minus.append(person)
                                elif xDict[person]["高校数学"] > 0:
                                    plus.append(person)
                                else:
                                    zero.append(person)

                            if minus == []:
                                break

                            else:
                                random.shuffle(plus)

                                totalMinus = 0
                                for person in minus:
                                    totalMinus -= xDict[person]["高校数学"]
                                    xDict[person]["高校数学"] = 0

                                minusDist = Dist(totalMinus,len(plus))
                                for i in range(len(minusDist)):
                                    xDict[plus[i]]['高校数学'] -= minusDist[i]
                                        
                                    
                            
                                    

                            
                    
                    
                    sentence = []
                    for i in people:
                        s = i + "　"
                        for j in subjectList:
                            if xDict[i][j] != 0:
                                s += ( j + str(xDict[i][j])+"+")
                        s = s.rstrip("+")
                        sentence.append(s)
                        
                    return sentence
                

                
                HumanitiesDist()
                message = ScienceDist()
                message.insert(0,"本日は")
                message.insert(1,"")
                message.append("")
                message.append("でお願いします！")
                params['distText'] = message
                params['DistributeForm'] = DistributeForm(request.POST)
                
                form = PlayerForm()
                form.fields['player'].choices = choice1
                form.fields['player'].initial = listret
                params['PlayerForm'] = form
                params['team'] = team
                params['pk'] = pk


    else:
        #対応者フォーム
        form = PlayerForm()
        form.fields['player'].choices = choice1
        ini = []
        for i in range(len(choice1)):
            ini.append(str(i+1))
        form.fields['player'].initial = ini
        params['PlayerForm'] = form
        params['team'] = team
        params['pk'] = pk
        
        

        # CFRF対策（必須）
        params.update(csrf(request))

        
    return render(request, 'distribute/distribute.html', params)
