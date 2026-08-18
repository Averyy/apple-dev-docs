# ChangeDetails.EntityMetaData

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A key-value map of entity metadata captured at the time of the change, such as entity name and parent IDs.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object ChangeDetails.EntityMetaData
```

#### Discussion

Each key is a metadata attribute name, such as `name` or `campaignId`, not a fixed field name. `entityMetaData` is a free-form map rather than an object with named properties, so the reference page labels this key `Any Key`. Both keys and values are strings, and the set of keys present varies by `entityType`. For example, a `Campaign` entity’s `entityMetaData` typically includes `name`, while an `AdGroup` entity’s also includes the parent `campaignId`.

## Properties

- `Any Key` (string)


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/changedetails/entitymetadata-data.dictionary)*