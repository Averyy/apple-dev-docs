# Org.SystemStatus

**Framework**: Apple Ads Platform API  
**Kind**: typealias

System-derived operational status of the organization.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
string Org.SystemStatus
```

#### Discussion

This status reflects the organization as a whole; individual ad accounts under it carry their own separate [`AdAccount.SystemStatus`](adaccount/systemstatus-data.typealias.md).

##### Example

```json
{
  "systemStatus": "ACTIVE"
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/org/systemstatus-data.typealias)*