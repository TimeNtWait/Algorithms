# https://leetcode.com/problems/the-number-of-full-rounds-you-have-played/
# 1904 . Количество сыгранных вами полных раундов
class Solution:
    def parse_time(self, str_time):
        hh, mm = str_time.split(":")
        return int(hh), int(mm)

    def next_nearest_round(self, hh, mm):
        if mm in {0, 15, 30, 45}:
            return hh, mm
        elif 45 < mm <= 59:
            return (hh + 1), 0
        else:
            return hh, (int(mm / 15) + 1) * 15
        return hh, mm

    def numberOfRounds(self, loginTime, logoutTime):
        bh, bm = self.parse_time(loginTime)
        eh, em = self.parse_time(logoutTime)

        count_round = 0
        if eh < bh or (eh == bh and em < bm):
            bh, bm = self.next_nearest_round(bh, bm)
            count_round += int(((23 - bh) * 60 + (60 - bm)) / 15)
            count_round += int((eh * 60 + em) / 15)
        else:
            bh, bm = self.next_nearest_round(bh, bm)
            count_round += int(((eh - bh) * 60 + (em - bm)) / 15)
        return count_round


if __name__ == "__main__":
    loginTime = "21:30"
    logoutTime = "03:00"
    res = Solution().numberOfRounds(loginTime, logoutTime)
    print(res)
