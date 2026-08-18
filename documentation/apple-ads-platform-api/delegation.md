# Delegation

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Links an ad account to an external advertiser resource, such as a content provider or brand.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object Delegation
```

#### Discussion

`Delegation` links an ad account to an external advertiser resource: a `CONTENT_PROVIDER` (App Store) or a `BUSINESS_BRAND` (Apple Maps).

`Delegation` objects appear in `AdAccount.delegations`, and `GET /v1/advertiser-resources` returns them.

##### Example

```json
{
  "resourceId": "555666777",
  "resourceType": "CONTENT_PROVIDER",
  "resourceName": "AwayFinder"
}
```

## Topics

### Type Aliases
- [type Delegation.ResourceType](delegation/resourcetype-data.typealias.md)
  The type of the linked resource: `CONTENT_PROVIDER` or `BUSINESS_BRAND`.

## Properties

- `resourceId` (string): The ID of the delegated resource. For `CONTENT_PROVIDER`, this is the Content Provider ID (CPID). For `BUSINESS_BRAND`, this is the Brand ID.
- `resourceType` (Delegation.ResourceType): The type of the linked resource. Accepted values: `CONTENT_PROVIDER`, `BUSINESS_BRAND`. See [`Delegation.ResourceType`](delegation/resourcetype-data.typealias.md).
- `resourceName` (string): The display name of the delegated resource. For `BUSINESS_BRAND`, this is the brand name. For `CONTENT_PROVIDER`, this is the provider name from App Store Connect.

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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/delegation)*