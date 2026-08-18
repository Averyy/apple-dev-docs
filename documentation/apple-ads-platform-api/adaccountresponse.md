# AdAccountResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The response envelope ad account operations return.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AdAccountResponse
```

#### Discussion

`AdAccountResponse` wraps the result of create, read, and update operations on a single `AdAccount`. On success, the response populates `result` with the full `AdAccount` object and leaves `error` null. On failure, `error` describes the problem and `result` is null.

##### Example

```json
{
  "result": {
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
}
```

## Properties

- `result` (AdAccount): The ad account object the operation returns. See [`AdAccount`](adaccount.md). Read-only.
- `error` (Error): An error object present when the operation fails. See [`Error`](error.md). Read-only.

## See Also

- [object AdAccount](adaccount.md)
  The account-level resource within an organization that contains campaigns and advertising settings.
- [object AdAccountCreate](adaccountcreate.md)
  Request body for creating a new ad account under an organization.
- [object AdAccountUpdate](adaccountupdate.md)
  The request body you use to update an ad account.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adaccountresponse)*