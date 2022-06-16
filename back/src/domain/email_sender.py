# from __future__ import print_function
# import time
# import sib_api_v3_sdk
# from sib_api_v3_sdk.rest import ApiException
# from pprint import pprint


# class Email:
#     def send_email(seller_info):
#         # Configure API key authorization: api-key
#         configuration = sib_api_v3_sdk.Configuration()
#         configuration.api_key[
#             "api-key"
#         ] = "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"

#         # Uncomment below lines to configure API key authorization using: partner-key
#         # configuration = sib_api_v3_sdk.Configuration()
#         # configuration.api_key['partner-key'] = 'YOUR_API_KEY'

#         # create an instance of the API class
#         api_instance = sib_api_v3_sdk.SMTPApi(sib_api_v3_sdk.ApiClient(configuration))
#         send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
#             to=[
#                 {
#                     "email": seller_info["seller_email"],
#                     "name": seller_info["seller_name"],
#                 }
#             ],
#             template_id=1,
#             params=seller_info,
#             headers={
#                 "X-Mailin-custom": "custom_header_1:custom_value_1|custom_header_2:custom_value_2|custom_header_3:custom_value_3",
#                 "charset": "iso-8859-1",
#             },
#         )  # SendSmtpEmail | Values to send a transactional email

#         try:
#             # Send a transactional email
#             api_response = api_instance.send_transac_email(send_smtp_email)
#             pprint(api_response)
#         except ApiException as e:
#             print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
