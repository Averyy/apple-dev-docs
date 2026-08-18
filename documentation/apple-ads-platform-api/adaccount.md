# AdAccount

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The account-level resource within an organization that contains campaigns and advertising settings.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AdAccount
```

#### Discussion

An `AdAccount` is the operational container for campaigns within an organization.

Each ad account is authorized for App Store or Apple Maps advertising, not both. You can’t combine the two on the same account.

`systemStatus` reflects operational readiness. If `INACTIVE`, check `systemStatusReasons`. Common causes include a missing payment method or pending tax verification.

##### Example

```json
{
  "id": 123456789,
  "name": "AwayFinder Ad Account",
  "orgId": 987654321,
  "timezone": "America/New_York",
  "currency": "USD",
  "paymentModel": "PAYG",
  "systemStatus": "ACTIVE",
  "systemStatusReasons": [],
  "delegations": [
    {
      "resourceId": "12345678",
      "resourceType": "CONTENT_PROVIDER",
      "resourceName": "AwayFinder Apps"
    }
  ],
  "productFeatures": [
    "APPSTORE_APP_MANUAL"
  ],
  "creationTime": "2025-01-10T08:00:00.000",
  "modificationTime": "2025-01-10T08:00:00.000"
}
```

## Topics

### Type Aliases
- [type AdAccount.Currency](adaccount/currency-data.typealias.md)
  The currency for the ad account, inherited from the parent org at creation.
- [type AdAccount.PaymentModel](adaccount/paymentmodel-data.typealias.md)
  The payment model for the ad account.
- [type AdAccount.SystemStatus](adaccount/systemstatus-data.typealias.md)
  `ACTIVE` on successful creation, transitioning to `INACTIVE` if issues arise.
- [type AdAccount.SystemStatusReasons](adaccount/systemstatusreasons-data.typealias.md)
  Populated when `systemStatus` is `INACTIVE`, identifying the specific blocking condition.

## Properties

- `id` (int64): System-assigned unique identifier for the ad account. Read-only.
- `name` (string): The name of the ad account. Must be unique within the parent org. Mutable.
- `orgId` (int64): The identifier of the parent organization. Read-only, inherited from the parent org.
- `timezone` (string): The time zone for the ad account, inherited from the parent org at creation. Example: `America/New_York`. Read-only.
- `currency` (AdAccount.Currency): The currency for the ad account. Supported values: `USD`, `EUR`, `GBP`, `JPY`, `AUD`, `CAD`, `MXN`, `NZD`, `RUB`, `CNY`, `RMB`, `INR`, `BRL`, `IDR`. See [`AdAccount.Currency`](adaccount/currency-data.typealias.md). Read-only, inherited from the parent org.
- `paymentModel` (AdAccount.PaymentModel): The payment model for the ad account. `LOC` (line of credit) enables budget orders and is invoiced monthly. `PAYG` (pay as you go) is charged per campaign spend. See [`AdAccount.PaymentModel`](adaccount/paymentmodel-data.typealias.md). Read-only, inherited from the parent org.
- `systemStatus` (AdAccount.SystemStatus): `ACTIVE` on successful creation. Transitions to `INACTIVE` if issues arise. See [`AdAccount.SystemStatus`](adaccount/systemstatus-data.typealias.md). Read-only.
- `systemStatusReasons` ([AdAccount.SystemStatusReasons]): Populated when `systemStatus` is `INACTIVE`. Possible values: `TAX_VERIFICATION_PENDING`, `ORG_NO_PAYMENT_METHOD_ON_FILE`, `NO_PAYMENT_METHOD_ON_FILE`, `CHARGE_BACK_DISPUTED`, `CREDIT_CARD_SUSPENDED`, `ORG_PAYMENT_TYPE_DECLINED`, `FRAUD`, `INVALID_PAYMENT_PROFILE`, `MSA_EXPIRED`, `MSA_NOT_RECEIVED`, `PAYMENT_DECLINED`, `PAYMENT_METHOD_CANCELED`, `PAYMENT_METHOD_ON_HOLD`, `PAYMENT_PENDING_CHARGES`, `LOC_EXHAUSTED`, `POLICY_VIOLATION`, `TERM_NOT_ACCEPTED`, `USER_REQUESTED_ACCOUNT_SUSPENSION`. See [`AdAccount.SystemStatusReasons`](adaccount/systemstatusreasons-data.typealias.md). Read-only.
- `delegations` ([Delegation]): Delegated resources associated with this ad account (brands, content providers). See [`Delegation`](delegation.md). Mutable.
- `productFeatures` ([ProductFeatures]): Defines whether the account is authorized for App Store or Apple Maps advertising. `APPSTORE_APP_MANUAL` enables App Store advertising. `BUSINESS_BRAND_MANUAL` enables Apple Maps. See [`ProductFeatures`](productfeatures.md) for details. Set at creation via `AdAccountCreate` (required).
- `creationTime` (date-time): Timestamp when the ad account was created. Read-only.
- `modificationTime` (date-time): Timestamp of the last modification to the ad account. Read-only.

## See Also

- [object AdAccountCreate](adaccountcreate.md)
  Request body for creating a new ad account under an organization.
- [object AdAccountUpdate](adaccountupdate.md)
  The request body you use to update an ad account.
- [object AdAccountResponse](adaccountresponse.md)
  The response envelope ad account operations return.
- [object AclAdAccount](acladaccount.md)
  Ad account details as returned in ACL responses.
- [object UserAcl](useracl.md)
  An access control entry for a single ad account that specifies the authenticated user’s assigned roles.
- [object UserAclListResponse](useracllistresponse.md)
  The response envelope for the Get User ACL endpoint, containing the list of user access control entries.
- [object UserAccessResult](useraccessresult.md)
  The result object returned when querying user ACL entries, containing the list of ad account access records.
- [object Delegation](delegation.md)
  Links an ad account to an external advertiser resource, such as a content provider or brand.
- [object DelegationCreate](delegationcreate.md)
  The request body for creating a delegation on an ad account.
- [object DelegationUpdate](delegationupdate.md)
  The request body for updating a delegation on an ad account.
- [object Me](me.md)
  The authenticated user’s identity information.
- [object MeResponse](meresponse.md)
  The response envelope for the Get Me Details endpoint, containing the authenticated user’s identity.
- [object Org](org.md)
  Represents an organization in the Apple Ads system.
- [object OrgResponse](orgresponse.md)
  The response envelope for a single organization lookup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adaccount)*