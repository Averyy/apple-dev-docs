# Org

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Represents an organization in the Apple Ads system.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object Org
```

#### Discussion

An `Org` is the top-level entity that owns ad accounts, manages users, and groups all advertising activity under a single billing relationship. It’s the root entity in the account hierarchy, with ad accounts, campaigns, and user memberships all existing beneath it.

The `systemStatus` field reflects whether the org is `ACTIVE` or `INACTIVE`. An inactive org prevents all campaigns under it from serving. Check `systemStatusReasons` for the specific cause.

To discover which organizations the current API token can access, use `GET /v1/acls`. Then, to retrieve full details, use `GET /v1/orgs/{orgId}`.

##### Example

```json
{
  "name": "AwayFinder",
  "currency": "USD",
  "timezone": "America/Los_Angeles",
  "paymentModel": "PAYG",
  "systemStatus": "ACTIVE",
  "systemStatusReasons": [],
  "id": 123456789
}
```

## Topics

### Type Aliases
- [type Org.Currency](org/currency-data.typealias.md)
  The currency used by the organization.
- [type Org.PaymentModel](org/paymentmodel-data.typealias.md)
  The payment model set through Apple Ads.
- [type Org.SystemStatus](org/systemstatus-data.typealias.md)
  System-derived operational status of the organization.
- [type Org.SystemStatusReasons](org/systemstatusreasons-data.typealias.md)
  Reasons that can cause the organization’s system status to be `INACTIVE`.

## Properties

- `name` (string): The name of the organization.
- `currency` (Org.Currency): The currency used by the organization. See [`Org.Currency`](org/currency-data.typealias.md).
- `timezone` (string): The timezone associated with the organization.
- `paymentModel` (Org.PaymentModel): The payment model for the organization. `LOC` (line of credit) enables budget orders and is invoiced monthly. `PAYG` (pay as you go) is charged per campaign spend. See [`Org.PaymentModel`](org/paymentmodel-data.typealias.md).
- `systemStatus` (Org.SystemStatus): The system-assigned status of the organization. See [`Org.SystemStatus`](org/systemstatus-data.typealias.md).
- `systemStatusReasons` ([Org.SystemStatusReasons]): Reasons associated with the current system status. See [`Org.SystemStatusReasons`](org/systemstatusreasons-data.typealias.md).
- `id` (int64): The unique identifier for the organization.

## See Also

- [object AdAccount](adaccount.md)
  The account-level resource within an organization that contains campaigns and advertising settings.
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
- [object OrgResponse](orgresponse.md)
  The response envelope for a single organization lookup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/org)*