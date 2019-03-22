from collections import OrderedDict
# import json
#
# a = [{   'line3' : {'1' : 'a','2' : 'b', '3' : 'c'}, 'line4' : {'4' : 'd','5' : 'e','6' : 'f'}   }]
#
# with open('temp_data.json', 'w', encoding='utf-8') as file:
#     json.dump(a, file, ensure_ascii=False, indent='\t')
#
# with open('temp_data.json','r', encoding='utf-8') as file:
#     root = json.load(file)
#
# print(root)
# print(a[0]['line3'])

data = [
        {
         '3': {'번호': '402187', '분류': '인권/성평등', '제목': '포항 약국 칼부림 사건의 가해 남성을 제대로 처벌하라.', '링크': 'https://www1.president.go.kr/petitions/410261', '청원인': 'twitter - ***', '청원기간': '18.10.18 ~ 18.11.17', '참여인원': '197,343명'},
         '4': {'번호': '402186', '분류': '기타', '제목': '인천 여중생 자살 가해자 강력처벌 희망 요망', '링크': 'https://www1.president.go.kr/petitions/347470', '청원인': 'facebook - ***', '청원기간': '18.08.19 ~ 18.09.18', '참여인원': '176,493명'},
         '5': {'번호': '402185', '분류': '인권/성평등', '제목': '이수역 폭행사건의 철저한 수사와 진상 규명을 촉구하며, 가해여성의 성추행과 모욕죄 처벌을 요청합니다.', '링크': 'https://www1.president.go.kr/petitions/443174', '청원인': 'facebook - ***', '청원기간': '18.11.15 ~ 18.12.15', '참여인원': '171,347명'},
         '6': {'번호': '402184', '분류': '정치개혁', '제목': '불법폭력조직 코마트레이드와 연루된 성남시장 은수미와 경기도지사 이재명 즉각 사퇴하라', '링크': 'https://www1.president.go.kr/petitions/314212', '청원인': 'ver - ***', '청원기간': '18.07.22 ~ 18.08.21', '참여인원': '163,917명'},
         '7': {'번호': '402183', '분류': '육아/교육', '제목': '아동학대로 오해받던 교사가 자살했습니다', '링크': 'https://www1.president.go.kr/petitions/407079', '청원인': 'facebook - ***', '청원기간': '18.10.15 ~ 18.11.14', '참여인원': '156,237명'},
         '8': {'번호': '402182', '분류': '정치개혁', '제목': ' 자유한국당 해산심판 요청', '링크': 'https://www1.president.go.kr/petitions/214435', '청원인': 'facebook - ***', '청원기간': '18.04.28 ~ 18.05.28', '참여인원': '153,735명'},
         '9': {'번호': '402181', '분류': '안전/환경', '제목': '"감옥에 갔다 와서 칼로 죽여버리겠다"', '링크': 'https://www1.president.go.kr/petitions/294032', '청원인': 'ver - ***', '청원기간': '18.07.03 ~ 18.08.02', '참여인원': '147,885명'},
         '10': {'번호': '402180', '분류': '교통/건축/국토', '제목': '경사진주차장에 경고문구 의무화와 자동차 보조제동장치 의무화를 요청합니다', '링크': 'https://www1.president.go.kr/petitions/26517', '청원인': 'ver - ***', '청원기간': '17.11.06 ~ 17.12.06', '참여인원': '146,068명'}
        },
        {
         '1': {'번호': '402179', '분류': '인권/성평등', '제목': '포항 약국 칼부림 사건의 가해 남성을 제대로 처벌 하라.', '링크': 'https://www1.president.go.kr/petitions/445550', '청원인': 'twitter - ***', '청원기간': '18.11.18 ~ 18.12.18', '참여인원': '142,715명'},
         '2': {'번호': '402178', '분류': '기타', '제목': '대한항공 개인회사의 "대한" , 영문명 "korean air" 의 명칭 사용금지 요청', '링크': 'https://www1.president.go.kr/petitions/198071', '청원인': 'ver - ***', '청원기간': '18.04.13 ~ 18.05.13', '참여인원': '135,212명'},
         '3': {'번호': '402177', '분류': '육아/교육', '제목': '교원 성과급 폐지를 강력히 요청합니다.', '링크': 'https://www1.president.go.kr/petitions/50257', '청원인': 'kakao - ***', '청원기간': '17.11.24 ~ 17.12.24', '참여인원': '134,637명'},
         '4': {'번호': '402176', '분류': '행정', '제목': "유튜버 '유정호'에 대한 감형및 판결근거를 정확하게 제시해주세요", '링크': 'https://www1.president.go.kr/petitions/507782', '청원인': 'ver - ***', '청원기간': '19.01.26 ~ 19.02.25', '참여인원': '133,546명'},
         '5': {'번호': '402175', '분류': '보건복지', '제목': '희귀난치병 보험혜택 절실합니다. 다른 병들과 똑같이 생사가 걸린 문제입니다.', '링크': 'https://www1.president.go.kr/petitions/311939', '청원인': 'facebook - ***', '청원기간': '18.07.19 ~ 18.08.18', '참여인원': '132,423명'},
         '6': {'번호': '402174', '분류': '인권/성평등', '제목': '청소년이란 이유로 보호법을 악용하는 잔인무도한 청소년들이 늘어나고있습니다. 반드시 [소년법]은 폐지해야합니다.', '링크': 'https://www1.president.go.kr/petitions/1798', '청원인': 'ver - ***', '청원기간': '17.09.03 ~ 17.11.02', '참여인원': '125,343명'},
         '7': {'번호': '402173', '분류': '기타', '제목': "'일간베스트'사이트를 폐지해주세요", '링크': 'https://www1.president.go.kr/petitions/19313', '청원인': 'facebook - ***', '청원기간': '17.10.05 ~ 17.11.04', '참여인원': '123,530명'},
         '8': {'번호': '402172', '분류': '인권/성평등', '제목': '해외 사이트를 기반으로 한 무분별한 일반인 모욕 사진의 유포를 처벌해주세요.', '링크': 'https://www1.president.go.kr/petitions/55256', '청원인': 'kakao - ***', '청원기간': '17.11.30 ~ 17.12.30', '참여인원': '123,288명'},
         '9': {'번호': '402171', '분류': '외교/통일/국방', '제목': '남성만의 실질적 독박 국방의무 이행에서 벗어나 여성도 의무 이행에 동참하도록 법률개정이 되어야 합니다.', '링크': 'https://www1.president.go.kr/petitions/899', '청원인': 'ver - ***', '청원기간': '17.08.30 ~ 17.09.14', '참여인원': '123,204명'},
         '10': {'번호': '402170', '분류': '보건복지', '제목': '35세 산모가  자연분만하다가 하늘나라로 갔습니다.(남편입니다) 의료 과실치사 진상조사바랍니다.', '링크': 'https://www1.president.go.kr/petitions/388917', '청원인': 'ver - ***', '청원기간': '18.09.23 ~ 18.10.23', '참여인원': '116,779명'}
         },
         {
          '1': {'번호': '402169', '분류': '문화/예술/체육/언론', '제목': '청와대 기자단, 해외 수행 기자단 제도의 폐지를 청원합니다.','링크': 'https://www1.president.go.kr/petitions/66242', '청원인': 'facebook - ***', '청원기간': '17.12.14 ~ 18.01.13','참여인원': '115,453명'},
          '2': {'번호': '402168', '분류': '정치개혁', '제목': '나경원 특검(혹은 국정조사)으로 나경원 원내 표님의 억울함을 풀어드리고 싶습니다.','링크': 'https://www1.president.go.kr/petitions/500653', '청원인': 'twitter - ***', '청원기간': '19.01.19 ~ 19.02.18','참여인원': '114,053명'},
          '3': {'번호': '402167', '분류': '행정', '제목': '귀화가 아닌 3년거주 외국인의 지방선거 선 거참여 당장 철회해 주세요!','링크': 'https://www1.president.go.kr/petitions/270378', '청원인': 'ver - ***','청원기간': '18.06.14 ~ 18.07.14', '참여인원': '112,124명'},
          '4': {'번호': '402166', '분류': '인권/성평등', '제목': '이성은 경찰청 성평등정책담당관의 해임을 청원합니다.','링크': 'https://www1.president.go.kr/petitions/289685', '청원인': 'ver - ***', '청원기간': '18.06.29 ~ 18.07.29','참여인원': '111,233명'},
          '5': {'번호': '402165', '분류': '경제민주화', '제목': '김기식 금감원장님을 무슨일이 있어도 지켜주세요!!','링크': 'https://www1.president.go.kr/petitions/193553', '청원인': 'ver - ***','청원기간': '18.04.10 ~ 18.05.10', '참여인원': '110,641명'},
          '6': {'번호': '402164', '분류': '인권/성평등', '제목': '개헌안, 차별금지법의 독소조항이 포함된 <국가인권정책 기본계획>을 즉각 철회해 주십시오.','링크': 'https://www1.president.go.kr/petitions/286759', '청원인': 'ver - ***', '청원기간': '18.06.27 ~ 18.07.27',' 참여인원': '110,110명'},
          '7': {'번호': '402163', '분류': '외교/통일/국방', '제목': '남북정상 담소 장면을 찍으며 "지*하네"라고 말한 카메라 기자를 엄벌해 주십시오.','링크': 'https://www1.president.go.kr/petitions/387845', '청원인': 'ver - ***', '청원기간': '18.09.22 ~ 18.10.22','참여인원': '109,917명'},
          '8': {'번호': '402162', '분류': '인권/성평등', '제목': '남녀 동일가치노동에서 동일임금지불과 더불어 임금 공개 의무화를 통한 임금격차 해소','링크': 'https://www1.president.go.kr/petitions/159655', '청원인': 'ver - ***', '청원기간': '18.03.06 ~ 18.04.05','참여인원': '107,512명'},
          '9': {'번호': '402161', '분류': '외교/통일/국방', '제목': 'k9자주포 폭발사고 진실을 규명해주세요','링크': 'https://www1.president.go.kr/petitions/218377', ' 청원인': 'ver - ***','청원기간': '18.05.01 ~ 18.05.31', '참여인원': '106,291명'},
          '10': {'번호': '402160', '분류': '정치개혁', '제목': '이명박 전 대통령 출국 금지 청원','링크': 'https://www1.president.go.kr/petitions/31254', '청원인': 'ver - ***', '청원기간': '17.11.10 ~ 17.12.10','참여인원': '105,942명'}
          },
        ]
dict = {'0' :  ['500653'], '1' : ['159655'], '2' : ['66242'], '3' : ['19313'], '4' : ['55256']}
temp_list = []

for i in range(len(dict)):
    temp_list.append(dict.get(str(i)))

historylist = [y for x in temp_list for y in x]
print(historylist)

temp_dict = {}
newnum = 1
i = 0
while i < 3:
    for key,value in data[i].items():
        for j in range(len(dict)):
            if historylist[j] in value['링크'][39:]:
                temp_dict[str(newnum)] = value
                newnum += 1
    i += 1
print(temp_dict)
history_dict = {}

for key,value in temp_dict.items():
    for k in range(len(historylist)):
        if historylist[k] == value['링크'][39:]:
           history_dict[str(k+1)] = value

s = sorted(history_dict.items())

finaldict = {}

for i in range(len(s)):
    finaldict[str(s[i][0])] = s[i][1]
print(finaldict)

# history_dict = {}
# history_dict['1'] = temp_dict['3']
# history_dict['2'] = temp_dict['5']
# history_dict['3'] = temp_dict['1']
# history_dict['4'] = temp_dict['2']
# history_dict['5'] = temp_dict['4']
#
# print(history_dict)

#for key,value in data[0].items():
#    print(key,' : ',value)
# keyword = '다'
# tempdict1 = {}
# tempdict2 = {}
# num = 1
#
# for i in range(len(data[0])):
#     if keyword in data[0][str(i+3)]['제목']:
#         tempdict1[str(num)] = data[0][str(i+3)]
#         num += 1
# print(tempdict1)
#
# print('-----------------------------------------------------')
#
# a = 1
# while a < 3:
#     for i in range(len(data[a])):
#         if keyword in data[a][str(i+1)]['제목']:
#             tempdict2[str(num)] = data[a][str(i+1)]
#             num += 1
#     a += 1
#
# print(tempdict2)
# tempdict1.update(tempdict2)
# print(tempdict1)