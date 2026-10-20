# AdAccountSystemStatusReason

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Enumeration of reasons that can cause an ad account’s system status to be `INACTIVE`.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string AdAccountSystemStatusReason
```

## Possible Values

- `CHARGE_BACK_DISPUTED`: A chargeback dispute is pending on the account.
- `CREDIT_CARD_SUSPENDED`: The credit card on file has been suspended.
- `ORG_PAYMENT_TYPE_DECLINED`: The organization’s payment type was declined.
- `FRAUD`: The account has been flagged for fraud.
- `INVALID_PAYMENT_PROFILE`: The payment profile associated with the account is invalid.
- `MSA_EXPIRED`: The Master Services Agreement has expired.
- `MSA_NOT_RECEIVED`: The Master Services Agreement has not been received.
- `NO_PAYMENT_METHOD_ON_FILE`: No payment method is on file for the ad account.
- `ORG_NO_PAYMENT_METHOD_ON_FILE`: The parent organization has no payment method on file.
- `PAYMENT_DECLINED`: The payment method was declined.
- `PAYMENT_METHOD_CANCELED`: The payment method has been canceled.
- `PAYMENT_METHOD_ON_HOLD`: The payment method is currently on hold.
- `PAYMENT_PENDING_CHARGES`: There are pending charges on the payment method.
- `LOC_EXHAUSTED`: The line of credit has been fully exhausted.
- `POLICY_VIOLATION`: The account has violated Apple Ads policies.
- `TAX_VERIFICATION_PENDING`: Tax verification is pending for the account.
- `TERM_NOT_ACCEPTED`: Required terms of service have not been accepted.
- `USER_REQUESTED_ACCOUNT_SUSPENSION`: The account was suspended at user request.

## See Also

- [type ProductFeatures](./productfeatures.md)
  Product features are the advertising capabilities for an ad account.
- [type OrgSystemStatus](./orgsystemstatus.md)
  System-derived operational status of an organization.
- [type OrgSystemStatusReason](./orgsystemstatusreason.md)
  Reasons that can cause an organization’s system status to not be active.
- [type AdAccountSystemStatus](./adaccountsystemstatus.md)
  System-derived operational status of an ad account.
- [object AdvertiserResourceListResponse](./advertiserresourcelistresponse.md)
  Response envelope for advertiser resource list requests.
- [type AdvertiserResourceType](./advertiserresourcetype.md)
  The type of advertiser resource you delegate to an ad account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adaccountsystemstatusreason)*