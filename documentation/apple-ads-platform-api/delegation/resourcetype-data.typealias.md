# Delegation.ResourceType

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

The type of the linked resource: `CONTENT_PROVIDER` or `BUSINESS_BRAND`.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string Delegation.ResourceType
```

## Possible Values

- `CONTENT_PROVIDER`: A content provider resource associated with the ad account. Its `resourceId` is the Content Provider ID (CPID).
- `BUSINESS_BRAND`: A Brand resource delegated from an organization. Its `resourceId` is the Brand ID.

## Discussion

This mirrors the `resourceType` set when the delegation was created or last updated, and continues to determine whether `resourceId` is a Content Provider ID or a Brand ID.

### Example

```json
{
  "resourceId": "555666777",
  "resourceType": "CONTENT_PROVIDER"
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/delegation/resourcetype-data.typealias)*