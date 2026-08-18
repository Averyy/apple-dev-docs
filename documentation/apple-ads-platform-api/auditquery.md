# AuditQuery

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Request body for the Query Change History endpoint.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AuditQuery
```

#### Overview

`AuditQuery` is the request payload for `POST /v1/change-history/query`. Every valid request must include at least one `filters` entry targeting `eventTime` using `BETWEEN`, `GREATER_THAN`, or `LESS_THAN`. All other fields are optional and default to reasonable values when omitted.

##### Example

A minimal valid request looks like this:

```json
{
  "filters": [
    {
      "field": "eventTime",
      "operator": "BETWEEN",
      "value": [
        "2025-03-01",
        "2025-03-31"
      ]
    }
  ],
  "pagination": {
    "offset": 0,
    "pageSize": 50
  }
}
```

| Filterable Field | Supported Operators | Accepted Values |
| --- | --- | --- |
| `eventTime` | `BETWEEN`, `GREATER_THAN`, `LESS_THAN` | ISO 8601 date strings, e.g. `"2025-03-01"`. Maximum lookback is 6 months. `BETWEEN` requires two values. `GREATER_THAN` and `LESS_THAN` take one. |
| `entityType` | `IN` | Not a closed enum. A string matching the name of the API entity that changed, such as `Campaign`, `AdGroup`, `Keyword`, `NegativeKeyword`, `Ad`, `Creative`, `AdAccount`, `Org`, or `LocationGroup`. See [`Change History Endpoints`](change-history-endpoints.md) for the entity types this endpoint reports on. |
| `eventType` | `IN` | `CREATE`, `UPDATE`, `DELETE` |
| `userType` | `IN` | `CUSTOMER`, `CUSTOMER_API`, `APPLE_SUPPORT` |
| `campaignId` | `EQUALS`, `IN` | Campaign ID string(s). Available when `entityType` is `AdGroup`, `Keyword`, or `NegativeKeyword`. |
| `adGroupId` | `EQUALS`, `IN` | Ad group ID string(s). Available when `entityType` is `Keyword` or `NegativeKeyword`. |
| `userId` | `EQUALS`, `IN` | User ID string(s) |
| `txnId` | `EQUALS`, `IN` | Transaction ID string(s) |
| `entityId` | `EQUALS`, `IN` | The specific entity that changed. |
| `adAccountId` | `EQUALS`, `IN` | Ad account ID string(s). Available when entityType is Campaign or AdGroup. |

| Option Key | Accepted Values | Default | Description |
| --- | --- | --- | --- |
| `needTotals` | `"true"`, `"false"` | `"true"` | When `"true"`, the response `pagination.totalCount` reflects the full result set size. Set to `"false"` to skip the COUNT query for faster responses on large datasets. `pagination.totalCount` will then be `0`. |
| `timeZone` | `"UTC"`, `"ORTZ"` | `"UTC"` | Controls how the API interprets `eventTime` filter values. `"UTC"` treats values as UTC. `"ORTZ"` interprets values in the org’s configured timezone and converts them to UTC server-side before filtering. |
| `metadata` | `"none"`, `"latest"`, `"snapshot"` | `"none"` | Controls entity metadata in change detail responses. `"none"` returns no metadata. `"latest"` joins current entity metadata. `"snapshot"` uses metadata captured at the time of the event. |

#### Discussion

##### Required Filter

```json
{
  "field": "eventTime",
  "operator": "BETWEEN",
  "value": [
    "2025-01-01",
    "2025-01-31"
  ]
}
```

##### Combine Filters

The API combines multiple `filters` entries with logical AND. For example, to retrieve only `Campaign` `UPDATE` events in a time window:

```json
{
  "filters": [
    {
      "field": "eventTime",
      "operator": "BETWEEN",
      "value": [
        "2025-03-01",
        "2025-03-31"
      ]
    },
    {
      "field": "entityType",
      "operator": "IN",
      "value": [
        "Campaign"
      ]
    },
    {
      "field": "eventType",
      "operator": "IN",
      "value": [
        "UPDATE"
      ]
    }
  ]
}
```

To retrieve all changes within a specific campaign across any entity type (ad groups, keywords, ads):

```json
{
  "filters": [
    {
      "field": "eventTime",
      "operator": "BETWEEN",
      "value": [
        "2025-03-01",
        "2025-03-31"
      ]
    },
    {
      "field": "campaignId",
      "operator": "EQUALS",
      "value": "789012"
    }
  ]
}
```

To retrieve changes made by a specific user across multiple ad groups:

```json
{
  "filters": [
    {
      "field": "eventTime",
      "operator": "BETWEEN",
      "value": [
        "2025-03-01",
        "2025-03-31"
      ]
    },
    {
      "field": "adGroupId",
      "operator": "IN",
      "value": [
        "345678",
        "345679"
      ]
    },
    {
      "field": "userId",
      "operator": "EQUALS",
      "value": "12345678"
    }
  ]
}
```

##### Handle Time Zones

When `timeZone` is `"ORTZ"`, the server converts the `eventTime` filter values from the org’s configured timezone to UTC before executing the query. The `eventTime` values returned in the response are always in UTC regardless of this setting.

##### Performance Tips

- Set `needTotals` to `"false"` on high-volume queries where you do not need an accurate total count. Skipping the COUNT query can substantially reduce response latency.
- Apply `entityType` and `eventType` filters to limit result set size before paginating.

## Topics

### Dictionaries
- [object AuditQuery.Options](auditquery/options-data.dictionary.md)
  A flat key-value map of additional query controls.

## Properties

- `filters` ([AuditFilter]): An array of filter conditions applied to the audit log. Every request requires a filter on `eventTime`. Use `BETWEEN` for a bounded range or `GREATER_THAN`/`LESS_THAN` for an open-ended range. Requests that omit this filter return a `400 Bad Request` error. Additional filters on `entityType`, `eventType`, and `userType` narrow results further and can be combined in a single request. Each entry is an [`AuditFilter`](auditfilter.md) object with `field`, `operator`, and `value` keys. See the Filterable Field table below.
- `sorting` ([AuditSorting]): An array of sort directives. Each entry is an [`AuditSorting`](auditsorting.md) object specifying a `field` name and an `order` of `ASC` or `DESC`. When you omit this array, the API sorts results by `eventTime` descending.
- `pagination` (Pagination): Controls the page offset and page size for the response. See [`Pagination`](pagination.md). Uses `offset` (zero-based row index) and `pageSize` (maximum rows per page, must be ≥ 1).
- `options` (AuditQuery.Options): A flat key-value map of additional query controls. See [`AuditQuery.Options`](auditquery/options-data.dictionary.md). All keys and values are strings. See the Option Key table below.

## See Also

- [object AuditFilter](auditfilter.md)
  A single filter condition in an audit query request, specifying the field to filter on, the comparison operator, and one or more values to match against.
- [object AuditSorting](auditsorting.md)
  A sort directive in an audit query request, specifying a field to sort by and the direction.
- [object Pagination](pagination.md)
  Pagination state in change history list responses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/auditquery)*