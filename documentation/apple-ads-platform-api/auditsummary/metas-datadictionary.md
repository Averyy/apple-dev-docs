# AuditSummary.Metas

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

An array of per-entity metadata entries, populated when the request includes metadata options.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AuditSummary.Metas
```

#### Discussion

Each entry in `metas` corresponds to one changed entity within the transaction and entity-type grouping that the parent `AuditSummary` row describes. An entry has the shape:

```json
{
  "<EntityType>": "<entityId>",
  "detailId": "<EntityType.entityId.txnId>",
  "meta": { ...entity fields... }
}
```

- The array is empty by default.
- The request populates it only when you set `options.metadata` to `latest` or `snapshot`, with one entry per changed entity.
- `latest` fills `meta` with the entity’s current state from the live data store.
- `snapshot` fills `meta` with the entity’s state at the time of the event.
- You can use each entry’s `detailId` directly with `GET /v1/change-history/{detailId}` without constructing it manually.

Populating `metas` matters because an [`AuditSummary`](auditsummary.md) row doesn’t include `entityId` on its own, so you can’t construct a `detailId` from the row alone. Setting `options.metadata` (see [`AuditQuery.Options`](auditquery/options-data.dictionary.md)) to `latest` or `snapshot` gives you a ready-to-use `detailId` in each `metas` entry instead, so you don’t need a separate lookup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/auditsummary/metas-data.dictionary)*