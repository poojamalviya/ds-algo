def minCoin(coin, s):
    dp = [[0]*s for _ in range(len(coin))]
    for i in range(len(coin)): dp[i][0]=1
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if i==0:
                dp[i][j] = dp[i][j-i]+1
    print dp


coin =[1,2,5]
s = 11

print minCoin(coin, s)






Popular social networks contain millions and even billions of connections between individuals.

Design a system that allows a user to search for another person, and see the shortest path between the








// var mailMap = common.PropertyMap{}
	// var notificationObj = common.PropertyMap{}
	// var identifierDict = common.PropertyMap{}
	// var bill Bill
	// db.Find(&bill, "id = ?", data.billId).Error
	// balance, err = GetBalance(&corp, "", txn.billId, corporate.Status, db)
	// if err != nil {
	// 	common.GetLogger().Printf("error while getting payable amount of the bill %s", bill.ID)
	// 	continue
	// }
	// paidAmount, err := GetTotalPayments(corporate.ID, bill, db)
	// if err != nil {
	// 	common.GetLogger().Printf("error while calculating the total amount paid till now for bill %s: %s", bill.ID, err)
	// 	continue
	// }
	// identifier_dict["bill_id"] = txn.billId
	// identifier_dict["from_date"] = bill.FromDate
	// identifier_dict["to_date"] = bill.ToDate
	// identifier_dict["total_bill"] = paymentObj.Amount
	// identifier_dict["amount_received"] = paidAmount
	// identifier_dict["amount_pending"] = balance
	// identifier_dict["account_status"] = corp.Status
	// notification_obj["corp_id"] = corp.ID
	// mailMap["notification_obj"] = notification_obj
	// mailMap["not_id"] = "bill_payment"
	// main.callNotificationExpense(mailMap) 




{"amount": 65, "ref_id": "TT1231431", "bin_number": "99999", "currency_id": "USD", "corporate_id": "crp_c2c0fa0289e241758e0b2ed99a4c5e05", "nodal_account_id": "acc_15481ee1d71c41ae8c9ebd02d6c13f79", "charge_fee_account_id": "acc_15481ee1d71c41ae8c9ebd02d6c13f79"}



# bill_payment 
# 1. bill_number
# 2. bill_cycle
# 3. total_bill    payable_amount
# 4. amount_received  total_paid
# 5. amount_pending
# 6. account_status

# bill_overdue = 6 and 7
# 1. total_bill
# 2. amount_received
# 3. amount_pending
# 4. account_status

# bill_overdue_final
# 1. total_bill
# 2. amount_received
# 3. amount_pending
# 4. account_status

# bill_account_deactivated
# 1. total_bill
# 2. amount_received
# 3. amount_pending
# 4. account_status

# bill_generated/ bill_due/ bill_reminder
# 1. amount
# 2. amount_words
# 3. date
# 4. from_date
# 5. to_date
# 6. https://cards.uat.happay.in/balance/bil_61a2466080f346429259992ad50dbe05
# 7. total_bill
# 8. amount_received
# 9. amount_pending
# 10. account_status


# emp_invite
# 1. admin_name
# 2. company_name
# 3. link   bill_link

# emp_invite_followUp / emp_invite_followUp afpoter ==>2 days of invite
# 1. admin name
# 2. orgname
# 3. activation link

# expired
# 1. admin name



 <p>For queries, please email us at <u> <a href = "help@happay.in">help@happay.in</a></u></p>
<div style="text-align:center;margin: 30px 0px;">
	<a href="{{bill_link}}" style="mso-style-priority:100 !important;text-decoration:none;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:Montserrat, sans-serif;font-size:18px;color:#020A1C;border-style:solid;border-color:#80c5de;border-width:10px 20px 10px 20px;display:inline-block;background:#80c5de;border-radius:4px;font-weight:500;font-style:normal;line-height:22px;width:auto;text-align:center;">Pay Bill</a>
</div>
<p></p>


<p>Cheers,<br />
Happay Team</p>


game theory
1. nim game
2. grundy number
3. minmax



27 
28 
29 follow1
30 follow2
 fine follow1
28 expired



@shared_task(name='kyc_reminder_mail', queue=PROD_CELERY_QUEUE)
@track_celery_memory_usage
def kyc_reminder_mail():
    from datetime import datetime, timedelta
    import pytz
    from AccessControl.models import HappayUser
    from AccessControl.utils import simulateUser
    from NotificationEngine.interface import initiate_notification
    try:
        current_time = datetime.now(pytz.timezone("UTC"))
        from_date = current_time- timedelta(days=2)
        to_date = current_time- timedelta(days=1)
        users = HappayUser.objects.filter(date_created__gte=from_date, date_created__lte= to_date, kyc_status = 3)
        for user in users:
            email_dict = {}
            identifier_dict ={}
            not_id =''
            if user.is_superuser:
                not_id = "kyc_reminder_admin"
            else:
                not_id = "kyc_reminder_user"
            
            identifier_dict["name"] = user.first_name
            email_dict = {
                "identifier_dict":identifier_dict
            }
            org = Organisation.objects.get(pk=user.org_id)
            simulate_user = simulateUser(user.email_id, org, user.mobile_number)
            initiate_notification(not_id, simulate_user, None, None, email_dict)

    except Exception, e:
        import sys
        import traceback
        traceback = traceback.format_exc(sys.exc_info())
        email_text = str(e) + "\n" + traceback
        send_server_mail("Kyc Reminder Mail - "+str(datetime.now().date()), email_text, "hello@happay.in", ["abhishek.g@happay.in", "pooja.malviya@happay.in"], [], [])
        log_error(INFO, 'kyc_reminder_mail ', str(datetime.now().date()), traceback=traceback, exception=str(e))
    return



		# delete from "public"."AccessControl_role" where "admin_id" = 'HP2020921142463479452073HP'
	# delete from "public"."AccessControl_happayuser_permissions" where "happayuser_id" = 'HP2020921142463479452073HP'