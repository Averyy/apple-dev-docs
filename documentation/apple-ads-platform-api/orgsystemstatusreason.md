# OrgSystemStatusReason

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Reasons that can cause an organization’s system status to not be active.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string OrgSystemStatusReason
```

## Possible Values

- `CHARGE_BACK_DISPUTED`: A chargeback dispute is pending on the organization.
- `CREDIT_CARD_SUSPENDED`: The credit card on file has been suspended.
- `ORG_PAYMENT_TYPE_DECLINED`: The organization’s payment type was declined.
- `FRAUD`: The organization has been flagged for fraud.
- `LOC_EXHAUSTED`: The line of credit has been fully exhausted.
- `MSA_EXPIRED`: The Master Services Agreement has expired.
- `MSA_NOT_RECEIVED`: The Master Services Agreement has not been received.
- `NO_PAYMENT_METHOD_ON_FILE`: No payment method is on file for the organization.
- `PAYMENT_DECLINED`: The payment method was declined.
- `PAYMENT_METHOD_CANCELED`: The payment method has been canceled.
- `PAYMENT_METHOD_ON_HOLD`: The payment method is currently on hold.
- `PAYMENT_PENDING_CHARGES`: There are pending charges on the payment method.
- `POLICY_VIOLATION`: The organization has violated Apple Ads policies.
- `TAX_VERIFICATION_PENDING`: Tax verification is pending for the organization.
- `TERM_NOT_ACCEPTED`: Required terms of service have not been accepted.
- `USER_REQUESTED_ACCOUNT_SUSPENSION`: The organization was suspended at user request.

## See Also

- [type ProductFeatures](./productfeatures.md)
  Product features are the advertising capabilities for an ad account.
- [type OrgSystemStatus](./orgsystemstatus.md)
  System-derived operational status of an organization.
- [type AdAccountSystemStatus](./adaccountsystemstatus.md)
  System-derived operational status of an ad account.
- [type AdAccountSystemStatusReason](./adaccountsystemstatusreason.md)
  Enumeration of reasons that can cause an ad account’s system status to be `INACTIVE`.
- [object AdvertiserResourceListResponse](./advertiserresourcelistresponse.md)
  Response envelope for advertiser resource list requests.
- [type AdvertiserResourceType](./advertiserresourcetype.md)
  The type of advertiser resource you delegate to an ad account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/orgsystemstatusreason)*