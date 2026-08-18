# Change History Endpoints

**Framework**: Apple Ads Platform API

Query audit summaries and retrieve change detail records for entities in an ad account.

**Availability**:
- Apple Ads Platform API 1.0+

#### Overview

Change History provides a chronological log of every create, update, and delete operation performed on campaign entities within an ad account. Each entry captures what changed, which entity the change affected, who made the change, and when it occurred. Use it alongside the Reports API to correlate configuration changes with shifts in campaign performance.

> ❗ **Important**: The query endpoint’s summary rows don’t carry a ready-to-use `detailId` by default. If you plan to look up field-level changes with the detail endpoint, set `options.metadata` to `latest` or `snapshot` on the query request so each row’s `metas` array includes a `detailId` you can pass straight to `GET /v1/change-history/{detailId}`. See Interpret the Response below for the full explanation.

#### Review the Endpoints

Change History exposes two endpoints: one to query audit summaries and one to retrieve field-level change details.

| Method | Path | Description |
| --- | --- | --- |
| `POST` | `/v1/change-history/query` | Queries audit summaries grouped by transaction, returning one row per (`userType`, `modifiedBy`, `transactionId`, `eventType`, `entityType`) combination with a `count` of entity changes for that grouping. See [`Query Change History`](query-audit-summary-_-grouped-by-transaction.md) for details. |
| `GET` | `/v1/change-history/{detailId}` | Retrieves field-level before and after values for a single entity change. See [`Get Change History Detail`](get-change-details-by-detailid.md) for details. |

##### Structure the Request

The change history query endpoint uses a different schema from other `/query` endpoints in the API. The request body supports the following top-level fields:

- `filters`: array of filter conditions. Every query request requires a time-range filter on `eventTime`. Use `BETWEEN` for a bounded range or `GREATER_THAN`/`LESS_THAN` for an open-ended range.
- `sorting`: array of sort objects, each with a `field` and `order` direction (`ASC` or `DESC`).
- `pagination`: `offset` and `pageSize` to control result pages.
- `options`: additional query controls. - `needTotals`: defaults to `"true"`. Set to `"false"` to skip the COUNT query and reduce response time, so `pagination.totalCount` is `0`.
- `timeZone`: controls how the API interprets `eventTime` filter values, using `UTC` (default) or `ORTZ` (converted to UTC server-side using the org’s configured timezone).
- `metadata`: controls which entity metadata appears in change detail responses, using `none` (default, no metadata), `latest` (joins current entity metadata), or `snapshot` (uses metadata captured at the time of the event).

##### Interpret the Response

All change history endpoints return a `dataType` field that identifies the response object type. The query endpoint returns `"dataType": "AuditSummary"` and the detail endpoint returns `"dataType": "ChangeDetail"`.

Each [`AuditSummary`](auditsummary.md) row represents one transaction grouping. The `count` field indicates how many entity changes of that entity type, user, and transaction grouping the row contains.

An `AuditSummary` row alone doesn’t carry the `detailId` needed to look up field-level changes: the detail endpoint’s `detailId` is a composite `EntityType.entityId.txnId` string, and a summary row has `entityType` and `transactionId` but not `entityId`. To get a ready-to-use `detailId`, set `options.metadata` to `latest` or `snapshot` on the query request. Each resulting row’s `metas` array then includes one entry per changed entity, and you can pass each entry’s `detailId` field directly to `GET /v1/change-history/{detailId}`. See [`AuditSummary`](auditsummary.md) for the full `metas` shape and the metadata option behavior.

Each [`ChangeDetails`](changedetails.md) record represents a single entity change within a transaction and contains a `details` array of [`ActivityDetail`](activitydetail.md) objects. Each [`ActivityDetail`](activitydetail.md) holds a `changes` array of field change objects, where each entry captures the `field` name, `oldValues`, and `newValues` as string arrays.

##### Filter Results

The following fields are available as filter targets on the query endpoint:

| Filter Field | Operators | Description |
| --- | --- | --- |
| `eventTime` | `BETWEEN`, `GREATER_THAN`, `LESS_THAN` | **Required.** Sets the time range for the query window: use `BETWEEN` with two ISO 8601 timestamps, or `GREATER_THAN`/`LESS_THAN` with a single timestamp. Maximum lookback is 6 months. |
| `entityType` | `IN` | Restrict results to specific entity types. See Identify Entity Types. |
| `eventType` | `IN` | Restrict results to specific change operations. See Identify Event Types. |
| `userType` | `IN` | Filter by the category of actor that made the change: `CUSTOMER` for UI users, `CUSTOMER_API` for API callers, or `APPLE_SUPPORT` for Apple support operations. |
| `adAccountId` | `EQUALS`, `IN` | Restrict results to changes within a specific ad account or set of ad accounts. Use when querying change history across multiple ad accounts under the same org. |
| `campaignId` | `EQUALS`, `IN` | Restrict results to changes on a specific campaign or set of campaigns. |
| `adGroupId` | `EQUALS`, `IN` | Restrict results to changes on a specific ad group or set of ad groups. |
| `userId` | `EQUALS`, `IN` | Restrict results to changes made by a specific user or set of users. |
| `entityId` | `EQUALS`, `IN` | Restrict results to changes on a specific entity. |
| `txnId` | `EQUALS`, `IN` | Restrict results to a specific transaction. |

##### Identify Entity Types

The `entityType` field in both summary and detail responses identifies which API entity the change affected. It isn’t a closed enum: its value matches the name of whatever API entity changed. Commonly observed values include the following:

| Value | Description |
| --- | --- |
| `Org` | Organization: the top-level account holder. |
| `AdAccount` | Ad account: scopes campaigns and billing. |
| `Campaign` | Campaign: top-level advertising structure. |
| `AdGroup` | Ad group: targeting and bidding unit within a campaign. |
| `Keyword` | Positive keyword targeting within an ad group. |
| `NegativeKeyword` | Negative keyword exclusion at campaign or ad group level. |
| `Ad` | Individual ad creative within an ad group. |
| `Creative` | Creative object defining pre-tap ad experience and destination. |
| `LocationGroup` | Location group used for geo-targeting in Apple Maps campaigns. |

##### Identify Event Types

The `eventType` field describes the nature of the change in a transaction. The event type determines how the API populates `oldValues` and `newValues` in field change objects:

| Value | Description |
| --- | --- |
| `CREATE` | The system creates a new entity. `oldValues` is empty on all associated field change objects. |
| `UPDATE` | The system modifies one or more fields on an existing entity. Both `oldValues` and `newValues` are populated. |
| `DELETE` | The system soft-deletes the entity. Because it implements deletion as a record update, `newValues` is populated. Expect fields such as the deleted flag, status, and transaction ID to appear with their updated values. `oldValues` reflects the pre-deletion state of each changed field. |

## Topics

- [Query Change History](query-audit-summary-_-grouped-by-transaction.md)
  Query audit summaries grouped by transaction across a specified time range.
- [Get Change History Detail](get-change-details-by-detailid.md)
  Retrieve field-level before and after values for a single entity change by its detail ID.

## See Also

- [Change History Response Objects](change-history-response-objects.md)
  Parse the audit summary and change detail objects returned by change history endpoints.
- [Change History Query Objects](change-history-query-objects.md)
  Build the filter, sort, and pagination inputs for change history query requests.
- [Change History Enumerations](change-history-enumerations.md)
  Look up the enumerated values accepted in change history query and response fields.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/change-history-endpoints)*