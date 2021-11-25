from payment.webpay import *

def form_to_newebpay(merchant_order_no, total, title):
    payment = NewWebPayment(
                merchant_order_no,
                total,
                title
                )
    raw_trade_info = payment.get_trade_info()
    raw_trade_info_pad = NewWebPayment.addpadding(raw_trade_info)
    trade_info = NewWebPayment.encrypt(
                    raw_trade_info_pad.encode('utf8'),
                    HASH_KEY.encode('utf8'),
                    HASH_IV.encode('utf8')
                    )
    raw_trade_sha = payment.get_trade_sha(
                        HASH_KEY,
                        HASH_IV,
                        trade_info
                        )
    trade_sha = NewWebPayment.sha256hex(raw_trade_sha)

    form_info = {
        'merchantid': MERCHANT_ID,
        'tradeinfo': trade_info,
        'tradesha': trade_sha,
        'version': VERSION
    }

    return form_info