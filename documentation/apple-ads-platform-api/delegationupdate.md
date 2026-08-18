# DelegationUpdate

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The request body for updating a delegation on an ad account.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object DelegationUpdate
```

#### Discussion

You only ever send `DelegationUpdate` entries as part of the `delegations` array on [`Update Ad Accounts`](put-ad-accounts-_id_.md), which uses full-replacement semantics: the array you send becomes the account’s complete set of delegations. There is no separate add or remove operation. The system keeps entries you include and removes entries you omit.

**Adding a new delegation**: include every existing delegation plus the new entry. All delegations on an ad account must share the same `resourceType`. You cannot mix `CONTENT_PROVIDER` and `BUSINESS_BRAND` delegations on the same account. For example, an ad account with an existing `CONTENT_PROVIDER` delegation that wants to add a second `CONTENT_PROVIDER` delegation sends both entries:

```json
PUT /v1/ad-accounts/{id}

{
  "delegations": [
    {
      "resourceId": "12345678",
      "resourceType": "CONTENT_PROVIDER"
    },
    {
      "resourceId": "9876543",
      "resourceType": "CONTENT_PROVIDER"
    }
  ]
}
```

**Removing a delegation**: send the array with the unwanted entry omitted. To remove the second `CONTENT_PROVIDER` delegation added above and keep only the first, send:

```json
PUT /v1/ad-accounts/{id}

{
  "delegations": [
    {
      "resourceId": "12345678",
      "resourceType": "CONTENT_PROVIDER"
    }
  ]
}
```

To remove all delegations, send an empty array.

##### Example

```json
{
  "delegations": []
}
```

## Topics

### Type Aliases
- [type DelegationUpdate.ResourceType](delegationupdate/resourcetype-data.typealias.md)
  The type of resource being delegated.

## Properties

- `resourceId` (string): The ID of the resource you’re delegating. For `CONTENT_PROVIDER`, this is the Content Provider ID (CPID). For `BUSINESS_BRAND`, this is the Brand ID.
- `resourceType` (DelegationUpdate.ResourceType): The type of resource you’re delegating. See [`DelegationUpdate.ResourceType`](delegationupdate/resourcetype-data.typealias.md).

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
- [object Me](me.md)
  The authenticated user’s identity information.
- [object MeResponse](meresponse.md)
  The response envelope for the Get Me Details endpoint, containing the authenticated user’s identity.
- [object Org](org.md)
  Represents an organization in the Apple Ads system.
- [object OrgResponse](orgresponse.md)
  The response envelope for a single organization lookup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/delegationupdate)*