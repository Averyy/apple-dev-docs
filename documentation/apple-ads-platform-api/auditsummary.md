# AuditSummary

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

One row in the query change history response, grouping a single actor’s entity changes in one transaction by entity type and event type.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AuditSummary
```

#### Overview

The query endpoint returns one `AuditSummary` row per unique (`userType`, `modifiedBy`, `transactionId`, `eventType`, `entityType`) combination. The `count` field reports how many entity changes of that type, user, and transaction grouping the row includes. Fetching full field-level data for those changes requires the per-entity `detailId`, which this summary object does not provide on its own. See the Discussion section below.

##### Example

```json
{
  "transactionId": "998877665",
  "eventType": "UPDATE",
  "eventTime": "2025-03-15T14:30:00.000Z",
  "entityType": "AdGroup",
  "count": 3,
  "metas": [],
  "userType": "CUSTOMER",
  "modifiedBy": "111222333"
}
```

#### Discussion

##### Use Count to Decide Fetch Strategy

Each `AuditSummary` row reports a `count` of entity changes for that entity type, user, and transaction grouping. The detail endpoint (`GET /v1/change-history/{detailId}`) requires a composite `detailId` in the form `EntityType.entityId.txnId`, but `AuditSummary` doesn’t include `entityId` directly.

That means when you don’t request metadata options, you can’t construct `detailId` from a row alone. When you set metadata options to `latest` or `snapshot`, though, each entry in `metas` already includes a ready-to-use `detailId`, so you don’t need a separate lookup.

## Topics

### Dictionaries
- [object AuditSummary.Metas](auditsummary/metas-data.dictionary.md)
  An array of per-entity metadata entries, populated when the request includes metadata options.

## Properties

- `transactionId` (string): The unique identifier for the transaction. This is one component of the composite `detailId` (`EntityType.entityId.txnId`) used by `GET /v1/change-history/{detailId}`, but `transactionId` alone is not sufficient to construct it. You also need `entityType` and `entityId`, and `entityId` is not present on this summary object.
- `eventType` (AuditEventType): The type of change operation performed in this transaction. See [`AuditEventType`](auditeventtype.md) for possible values.
- `eventTime` (date-time): The UTC timestamp of when the change occurred, in ISO 8601 format (e.g. `"2025-03-15T14:30:00.000Z"`).
- `entityType` (string): The API entity type that changed, matching the name of the API entity in the Apple Ads Platform API (e.g. `Campaign`, `AdGroup`, `Keyword`). Not a closed enum. See [`Change History Endpoints`](change-history-endpoints.md) for the entity types this endpoint reports on.
- `count` (integer): The number of entity changes of this entity type, user, and transaction grouping. Use it to gauge how many detail lookups (one per `entityId`) you need from the detail endpoint.
- `metas` ([AuditSummary.Metas]): An array of per-entity metadata entries, populated when the request includes metadata options. See [`AuditSummary.Metas`](auditsummary/metas-data.dictionary.md). Empty by default (`[]`). When you set the metadata option to latest, each entry holds the current entity state from the live data store. When you set it to snapshot, each entry holds the entity state at the time of the event. Each entry has the shape `{ "<EntityType>": "<entityId>", "detailId": "<EntityType.entityId.txnId>", "meta": { ...entity fields... } }`. Use the `detailId` on each entry directly with `GET /v1/change-history/{detailId}`.
- `userType` (AuditUserType): The category of actor that made the change. See [`AuditUserType`](auditusertype.md) for possible values. Possible values: `CUSTOMER`, `CUSTOMER_API`, `APPLE_SUPPORT`.
- `modifiedBy` (string): The identifier of the user or service that performed the change. We do not expose user email, only `modifiedBy`.

## See Also

- [object ActivityDetail](activitydetail.md)
  A group of field-level changes that occurred within a single activity context in a change details record.
- [object AuditSummaryResponse](auditsummaryresponse.md)
  The response envelope returned by the Query Change History endpoint, wrapping an array of audit summary rows with pagination metadata.
- [object BaseAuditResponse](baseauditresponse.md)
  Common response envelope fields shared by all change history response objects.
- [object ChangeDetails](changedetails.md)
  Field-level change record for a single API entity within a transaction.
- [object ChangeDetailsResponse](changedetailsresponse.md)
  The response envelope returned by the Get Change History Detail endpoint, wrapping an array of change detail records with pagination metadata.
- [object ErrorMessage](errormessage.md)
  Error information returned in a change history response when a request fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/auditsummary)*