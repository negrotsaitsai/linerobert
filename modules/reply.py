from linebot.models import (
    MessageEvent, TextMessage, StickerMessage, TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, TemplateSendMessage, ButtonsTemplate, PostbackAction, MessageAction, URIAction, CarouselTemplate, CarouselColumn, QuickReply, QuickReplyButton
)

# 官方文件
# https://github.com/line/line-bot-sdk-python

# 常見問答表
faq = {
    '貼圖': StickerSendMessage(
        package_id='1',
        sticker_id='1'
    ),
    '爸爸': TextSendMessage(text='請問您想了解甚麼？',
                          quick_reply=QuickReply(items=[
                              QuickReplyButton(action=MessageAction(
                                  label="工作", text="長春化工")
                              ),
                              QuickReplyButton(action=MessageAction(
                                  label="教育方式", text="對於成績十分講究，成績就是一切。")
                              )
                          ])
                          ),

    '媽媽': TextSendMessage(text='請問您想了解甚麼？',
                          quick_reply=QuickReply(items=[
                              QuickReplyButton(action=MessageAction(
                                  label="工作", text="護士")
                              ),
                              QuickReplyButton(action=MessageAction(
                                  label="教育理念", text="學習需要結合興趣，孩子不管想做甚麼行業都可以，能養活自己就好。"))
                          ])
                          ),
    '弟弟': TextSendMessage(text='請問您想了解甚麼？',
                          quick_reply=QuickReply(items=[
                              QuickReplyButton(action=MessageAction(
                                  label="就學區域", text="苗栗農工化工科")
                              ),
                              QuickReplyButton(action=MessageAction(
                                  label="興趣", text="改造家裡農地，跟我一樣喜歡做一些智能設備，以此增加生活機能。"))
                          ])
                          ),
    '籃球': TextSendMessage(
        text="最愛的NBA球星Stephen Curry，他的投籃準度十分厲害是我追求的目標(雖然達不到哈哈)，身高186的我從小就被逼著去打中鋒，但事實上我最愛的位子是控球後衛，在球隊後方成為球隊視野，並找出最好的進攻機會，不是很棒嘛!哈哈!"
    ),
    '排球': TextSendMessage(
        text="因為一部日本動畫而喜歡上的運動，我最喜歡的位子是二傳手，在每次進攻都擔任助攻的角色，它是球隊核心，但卻也是球場上不易得到注意的選手，雖然人們只會注意得分球員，但我依舊喜歡但任球隊的影子"
    )
}

# 主選單
menu = TemplateSendMessage(
    alt_text='Carousel template',
    template=CarouselTemplate(
        columns=[
            CarouselColumn(
                # 卡片一圖片網址
                thumbnail_image_url='https://picsum.photos/id/296/900/400',
                title='家庭背景',
                text='點選下方按鈕開始互動',
                actions=[
                    MessageAction(
                        label='爸爸',
                        text='爸爸'
                    ),
                    MessageAction(
                        label='媽媽',
                        text='媽媽'
                    ),
                    MessageAction(
                        label='弟弟',
                        text='弟弟'
                    )
                ]
            ),
            CarouselColumn(
                # 卡片二圖片網址
                thumbnail_image_url='https://picsum.photos/id/355/900/400',
                title='興趣',
                text='點選下方按鈕開始互動',
                actions=[
                    MessageAction(
                        label='籃球',
                        text='籃球'
                    ),
                    MessageAction(
                        label='排球',
                        text='排球'
                    ),
                    URIAction(
                        label='組裝機械',
                        uri='https://www.instagram.com/arduino.cc/'
                    )
                ]
            )
        ]
    )
)
