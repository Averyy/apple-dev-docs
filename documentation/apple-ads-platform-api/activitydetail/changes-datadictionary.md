# ActivityDetail.Changes

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A single field change entry, capturing the field name and its before and after values.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object ActivityDetail.Changes
```

#### Discussion

Each entry in the `changes` array describes a single field that changed during the activity.

##### Example

```json
{
  "field": "status",
  "oldValues": ["PAUSED"],
  "newValues": ["ENABLED"]
}
```

`changes` is the array field on the parent [`ActivityDetail`](activitydetail.md) object: `ChangeDetails` holds a `details` array of `ActivityDetail` objects, and each `ActivityDetail` groups the field-level changes that share a common activity context in this `changes` array.

## Properties

- `field` (string): The API field name that changed. Read-only.
- `oldValues` ([string]): Values before the change, as strings. Empty for `CREATE` events. Read-only.
- `newValues` ([string]): Values after the change, as strings. Empty for `DELETE` events. Read-only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/activitydetail/changes-data.dictionary)*