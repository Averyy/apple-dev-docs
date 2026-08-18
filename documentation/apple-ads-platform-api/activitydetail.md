# ActivityDetail

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A group of field-level changes that occurred within a single activity context in a change details record.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object ActivityDetail
```

#### Discussion

##### Locate Activitydetail in the Response Hierarchy

Change history detail responses use a three-level nesting:

```None
ChangeDetails
 └── details: ActivityDetail[]
 └── changes: [{ field, oldValues, newValues }]
```

Each [`ChangeDetails`](changedetails.md) record has one or more `ActivityDetail` entries in its `details` array. Each `ActivityDetail` groups the field-level changes that share a common activity context within the transaction. In most cases, a single `ActivityDetail` contains all field changes for the entity.

##### Iterate Over Field Changes

To access individual field changes, iterate the `changes` array on each `ActivityDetail`:

```json
"details": [
  {
    "transactionId": "txn_abc123def456",
    "changes": [
      { "field": "status", "oldValues": ["PAUSED"], "newValues": ["ENABLED"] },
      { "field": "dailyBudget", "oldValues": ["50.00"], "newValues": ["100.00"] }
    ]
  }
]
```

The API encodes all values in `oldValues` and `newValues` as strings, regardless of the underlying field type. Parse them according to the field’s expected type.

##### Example

```json
{
  "transactionId": "txn_abc123def456",
  "changes": [
    {
      "field": "status",
      "oldValues": ["PAUSED"],
      "newValues": ["ENABLED"]
    },
    {
      "field": "dailyBudget",
      "oldValues": ["50.00"],
      "newValues": ["100.00"]
    }
  ]
}
```

## Topics

### Dictionaries
- [object ActivityDetail.Changes](activitydetail/changes-data.dictionary.md)
  A single field change entry, capturing the field name and its before and after values.

## Properties

- `transactionId` (string): The identifier of the transaction this activity belongs to. Matches the `transactionId` on the parent [`ChangeDetails`](changedetails.md) record. Read-only.
- `changes` ([ActivityDetail.Changes]): An array of [`ActivityDetail.Changes`](activitydetail/changes-data.dictionary.md) field change objects, one per field that changed in this activity. Each object contains three keys: `field` (string, the API field name that changed), `oldValues` (array of string, values before the change, empty for `CREATE` events), and `newValues` (array of string, values after the change, empty for `DELETE` events). Read-only.

## See Also

- [object AuditSummary](auditsummary.md)
  One row in the query change history response, grouping a single actor’s entity changes in one transaction by entity type and event type.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/activitydetail)*