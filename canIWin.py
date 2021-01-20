# myLookUp =[]
# def can_i_win(ops, s):
#     if s == 0:
#         return True
#     if len(myLookUp) == desiredvallue and s >= 0:
#         return False

#     for i in range(maxChoosable, -1, -1):

#         print i
#         if i not in myLookUp:
#             can_i_win(ops-1, s-i)
#             myLookUp.append(i)
#         else:
#             can_i_win(ops[len(ops)- 1], s)


def can_i_win(t, m, c):
    if m > t :
        can_i_win(t, m-1, c)
    if t == 0 :
        return c
    can_i_win(t-m, m, c+1)


maxChoosable = 10
desiredvallue = 11

print can_i_win(desiredvallue, maxChoosable, 0)







{"AID": "089472", "MCC": "6011", "MID": "BESTAVARIPETA 2", "POS": {"COUNTRY": "356", "POSTAL_CODE": "523334    ", "CARD_PRESENCE": "CARD_PRESENT", "ATTENDED_TERMINAL": "FALSE", "TERMINAL_LOCATION": "OFF_PREMISES_REMOTE_LOCATION", "PREAUTH_LIFE_CYCLE": "00", "TRANSACTION_STATUS": "NORMAL_REQUEST", "CARDHOLDER_PRESENCE": "CARDHOLDER_PRESENT", "TRANSACTION_SECURITY": "NO_CONCERN", "CARD_CAPTURE_CAPABILITY": "FALSE", "TERMINAL_INPUT_CAPABILITY": "MAGSTRIPE", "CARDHOLDER_ACTIVATED_TERMINAL_TYPE": "AUTH_1_AUTO_DISPENSING_WITH_PIN"}, "RRN": "684         ", "TID": "12921002", "STAN": "187606", "BILLING": {"AMOUNT": "000000150000", "CURRENCY": "356"}, "CHANNEL": "ATM", "TXN_AMT": {"AMOUNT": "000000150000", "CURRENCY": "356"}, "MERCHANT": {"CITY": "PRAKASHAM    ", "NAME": "BESTAVARIPETA 2ND ATM ", "COUNTRY": "IND"}, "TXN_TYPE": "AUTH", "PIN_BLOCK": "3F6D15B2B696985B", "SETTLEMENT": {"AMOUNT": "000000002112", "CURRENCY": "840"}, "TRANS_TYPE": "CARD_TRANSACTION", "PAN_ENTRY_MODE": "FULL_MAGSTRIPE_READ", "TO_ACCOUNT_TYPE": "UNSPECIFIED", "TRANSACTION_CODE": "DEBIT", "FROM_ACCOUNT_TYPE": "SAVING", "PIN_ENTRY_CAPABILITY": "PIN_ENTRY_CAPABLE", "TRANSMISSION_DATE_TIME": "20190927092947"}