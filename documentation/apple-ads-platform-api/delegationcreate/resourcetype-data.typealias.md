# DelegationCreate.ResourceType

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

The type of resource you’re delegating.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string DelegationCreate.ResourceType
```

## Possible Values

- `CONTENT_PROVIDER`: A content provider resource associated with the ad account. Its `resourceId` is the Content Provider ID (CPID).
- `BUSINESS_BRAND`: A Brand resource delegated from an organization. Its `resourceId` is the Brand ID.

#### Discussion

Choosing `CONTENT_PROVIDER` or `BUSINESS_BRAND` here fixes which kind of identifier `resourceId` must supply.

##### Example

```json
{
  "resourceId": "555666777",
  "resourceType": "CONTENT_PROVIDER"
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/delegationcreate/resourcetype-data.typealias)*