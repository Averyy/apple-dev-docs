# DelegationUpdate.ResourceType

**Framework**: Apple Ads Platform API  
**Kind**: typealias

The type of resource being delegated.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
string DelegationUpdate.ResourceType
```

#### Discussion

This value determines whether `resourceId` must refer to a Content Provider ID or a Brand ID.

##### Example

```json
{
  "resourceId": "555666777",
  "resourceType": "CONTENT_PROVIDER"
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/delegationupdate/resourcetype-data.typealias)*