class TradeInfo:
    def __init__(self, lists):
        self.total = 0
        self.trades = []
        self.__parse(lists)

    def __parse(self, lists):
        self.total = len(lists)
        self.trades = [self.__map_to_trade(single) for single in lists]

    def __map_to_trade(self, single):
        if single.create_time:
            time = single.create_datetime.strftime('%Y-%m-%d')
        else:
            time = '未知'
        return dict(
            user_name = single.user.nickname,
            time = time,
            id = single.id
        )
