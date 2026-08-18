# ChangeDetails

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Field-level change record for a single API entity within a transaction.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object ChangeDetails
```

#### Overview

Each `ChangeDetails` record represents one entity’s complete change history for a single transaction. The `details` array contains [`ActivityDetail`](activitydetail.md) objects, each of which holds a `changes` array of field change objects capturing the `field` name, `oldValues`, and `newValues`.

##### Example

```json
{
  "transactionId": "998877665",
  "detailId": "AdGroup.555666777.998877665",
  "eventType": "UPDATE",
  "entityType": "AdGroup",
  "entityId": "555666777",
  "eventTime": "2025-03-15T14:30:00.000Z",
  "userType": "CUSTOMER",
  "modifiedBy": "111222333",
  "entityMetaData": {
    "name": "AwayFinder iOS - New Users 18-34",
    "campaignId": "444555666"
  },
  "details": [
    {
      "transactionId": "998877665",
      "changes": [
        {
          "field": "status",
          "oldValues": [
            "ENABLED"
          ],
          "newValues": [
            "PAUSED"
          ]
        }
      ]
    }
  ]
}
```

#### Discussion

##### Relationship to Auditsummary

`ChangeDetails` is the field-level expansion of an [`AuditSummary`](auditsummary.md) row. The `count` field on a summary row tells you how many field change entries to expect across all `ActivityDetail` objects in `details`.

##### Entitymetadata Vs Metas

`ChangeDetails` always populates `entityMetaData` (when metadata is available) regardless of the request’s `options.metadata` setting. It represents a point-in-time snapshot of key entity attributes captured at change time. This differs from the `metas` field on `AuditSummary`, which the request’s `options.metadata` query option controls.

##### Understand Oldvalues and Newvalues

Both fields are string arrays. For scalar fields, each array contains a single element. For array-valued fields, each array represents the full set of values before and after the change. Interpretation by event type:

| `eventType` | `oldValues` | `newValues` |
| --- | --- | --- |
| `CREATE` | Empty `[]` | Values at creation |
| `UPDATE` | Previous value(s) | Updated value(s) |
| `DELETE` | Last known value(s) | Typically empty `[]`, but may contain system-managed values (e.g., deletion flag, status, transaction ID) set at delete time |

## Topics

### Dictionaries
- [object ChangeDetails.EntityMetaData](changedetails/entitymetadata-data.dictionary.md)
  A key-value map of entity metadata captured at the time of the change, such as entity name and parent IDs.

## Properties

- `transactionId` (string): The unique identifier for the transaction that produced this change record.
- `detailId` (string): A unique identifier for this specific entity change within the transaction.
- `eventType` (AuditEventType): The type of change operation performed. See [`AuditEventType`](auditeventtype.md).
- `entityType` (string): The API entity type that changed, matching the name of the API entity in the Apple Ads Platform API (e.g. `Campaign`, `AdGroup`, `Keyword`). Not a closed enum. See [`Change History Endpoints`](change-history-endpoints.md) for the entity types this endpoint reports on.
- `entityId` (string): The platform ID of the entity that changed (e.g. a campaign ID or ad group ID).
- `eventTime` (date-time): The UTC timestamp of when the change occurred, in ISO 8601 format.
- `userType` (AuditUserType): The category of actor that performed the change. See [`AuditUserType`](auditusertype.md) for possible values. Read-only.
- `modifiedBy` (string): The identifier of the user or service that performed the change. We do not expose user email, only `modifiedBy`. Read-only.
- `entityMetaData` (ChangeDetails.EntityMetaData): A key-value map of entity metadata captured at the time of the change (e.g. entity name, parent IDs). See [`ChangeDetails.EntityMetaData`](changedetails/entitymetadata-data.dictionary.md). Keys and values are strings and vary by entity type. Read-only.
- `details` ([ActivityDetail]): An array of [`ActivityDetail`](activitydetail.md) objects. Each entry contains a `changes` array of field change objects, where every entry captures one field that changed in the transaction. Read-only.

## See Also

- [object ActivityDetail](activitydetail.md)
  A group of field-level changes that occurred within a single activity context in a change details record.
- [object AuditSummary](auditsummary.md)
  One row in the query change history response, grouping a single actor’s entity changes in one transaction by entity type and event type.
- [object AuditSummaryResponse](auditsummaryresponse.md)
  The response envelope returned by the Query Change History endpoint, wrapping an array of audit summary rows with pagination metadata.
- [object BaseAuditResponse](baseauditresponse.md)
  Common response envelope fields shared by all change history response objects.
- [object ChangeDetailsResponse](changedetailsresponse.md)
  The response envelope returned by the Get Change History Detail endpoint, wrapping an array of change detail records with pagination metadata.
- [object ErrorMessage](errormessage.md)
  Error information returned in a change history response when a request fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/changedetails)*