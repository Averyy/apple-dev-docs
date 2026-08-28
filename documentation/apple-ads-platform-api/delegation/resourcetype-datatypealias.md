# Delegation.ResourceType

**Framework**: Apple Ads Platform API  
**Kind**: typealias

The type of the linked resource: `CONTENT_PROVIDER` or `BUSINESS_BRAND`.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string Delegation.ResourceType
```

#### Discussion

This mirrors the `resourceType` set when the delegation was created or last updated, and continues to determine whether `resourceId` is a Content Provider ID or a Brand ID.

##### Example

```json
{
  "resourceId": "555666777",
  "resourceType": "CONTENT_PROVIDER"
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/delegation/resourcetype-data.typealias)*