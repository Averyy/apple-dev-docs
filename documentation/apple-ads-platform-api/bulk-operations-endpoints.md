# Bulk Operations Endpoints

**Framework**: Apple Ads Platform API

Create and update keywords and negative keywords in bulk.

**Availability**:
- Apple Ads Platform API 1.0+

#### Overview

> **Note**: Bulk delete endpoints for keywords and negative keywords are coming soon. To delete a keyword or negative keyword today, use the single-item [`Delete a Keyword`](delete-keywords-_id_.md) and [`Delete a Negative Keyword`](delete-negative-keywords-_id_.md) endpoints.

#### Overview

Bulk operations accept arrays of items in a single request. All bulk endpoints share the same `items` array structure: each item carries a client-supplied `correlationId` and a `data` object containing the operation payload. The response returns a `result` array with one entry per input item, keyed by `correlationId`.

Set `allowPartialSuccess: true` in the request to use partial success semantics. The response reports individual item failures per item without rolling back successful items. When omitted or `false`, any single failure rejects the entire batch.

#### Find Bulk Endpoints

Each entity that supports bulk operations exposes create and update endpoints at the following paths:

| Entity | Bulk Create | Bulk Update |
| --- | --- | --- |
| Keywords | `POST /v1/keywords/bulk-create` | `POST /v1/keywords/bulk-update` |
| Negative Keywords | `POST /v1/negative-keywords/bulk-create` | `POST /v1/negative-keywords/bulk-update` |

##### Create and Update

To create or update items in bulk, send a POST request to the entity’s bulk endpoint with an `items` array; the endpoint you call determines the shape of each item’s `data` object:

| Operation | Description |
| --- | --- |
| **Create** | Send the array to `/bulk-create`. Each item’s `data` contains the create payload. The response’s `result` array includes one entry per item with a `success` flag and per-item error details on failure. |
| **Update** | Send the array to `/bulk-update`. Each item’s `data` must include the entity’s `id` plus only the fields you want to change; omitted fields retain their current values. |

##### Handle Errors

Bulk endpoints use a partial-success model when the request sets `allowPartialSuccess: true`. The endpoint processes valid items, and the response includes per-item error details for any items that failed. When `allowPartialSuccess` is omitted or `false` (the default), any single item failure rejects the entire batch.

The response reports bulk-level validation failures (such as sending more items than the endpoint allows in a single request) in the outer `BulkResponse.error.details` field, not in the per-item `result` array. When the endpoint returns a bulk-level error, it processes no items regardless of the `allowPartialSuccess` setting. If you hit this rejection, split the request into smaller batches and retry each one.

##### Choose Between Bulk and Single Item Endpoints

Prefer bulk endpoints when creating or updating more than a handful of keywords or negative keywords at once, such as rolling out a new keyword list across many ad groups or pausing a large negative keyword list in one pass. A bulk request counts as a single call against your rate limit regardless of how many items it carries, so batching changes into bulk requests is the most effective way to stay under the limits described in [`Applying Rate Limits`](rate-limits.md) during large-scale operations.

Use the single-item endpoints for one-off changes, such as adjusting a single keyword’s bid, where there’s no batch to build. The single-item response shape is also simpler to handle in application code, since it returns a single `Error` object instead of a per-item `result` array keyed by `correlationId`.

## Topics

### Keywords
- [Bulk Create Keywords](post-keywords-bulk-create.md)
  Creates multiple keywords in a single request.
- [Bulk Update Keywords](post-keywords-bulk-update.md)
  Updates multiple keywords in a single request.
### Negative Keywords
- [Bulk Create Negative Keywords](post-negative-keywords-bulk-create.md)
  Create multiple negative keywords in a single request.
- [Bulk Update Negative Keywords](post-negative-keywords-bulk-update.md)
  Update multiple negative keywords in a single request.

## See Also

- [Bulk Data Objects](bulk-data-objects.md)
  Use these objects to build bulk keyword and negative keyword requests and read their responses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/bulk-operations-endpoints)*