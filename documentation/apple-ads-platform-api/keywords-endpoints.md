# Keywords Endpoints

**Framework**: Apple Ads Platform API  
**Role**: API Collection

Create, retrieve, update, query, and delete the keywords that match your ad group’s ads to searches.

**Availability**:
- Apple Ads Platform API 1.0+

## Overview

Keywords bid on search terms for an ad group, and a keyword’s match type controls which searches it matches. Negative keywords do the opposite and suppress your ads for searches you exclude. See [Negative Keywords Endpoints](./negative-keywords-endpoints.md).

Use these endpoints to manage keywords one at a time. For match types and bid behavior, see [Managing Keywords and Negative Keywords](./keywords-and-negative-keywords.md). To change many keywords in one request, see [Bulk Operations Endpoints](./bulk-operations-endpoints.md).

## Topics

- [Create a Keyword](./post-keywords.md)
  Create a new keyword in an ad group, setting the match type and optional bid amount.
- [Query Keywords](./post-keywords-query.md)
  Query keywords using structured filters, sorting, and pagination.
- [Get a Keyword](./get-keywords-_id_.md)
  Retrieve a single keyword by its unique identifier.
- [Update a Keyword](./put-keywords-_id_.md)
  Update a keyword’s bid amount or status to optimize spend and control delivery for that term.
- [Delete a Keyword](./delete-keywords-_id_.md)
  Soft-delete a keyword by ID, setting its deleted field to true and stopping bids on that term.

## See Also

### Keywords
- [Managing Keywords and Negative Keywords](./keywords-and-negative-keywords.md)
  Create and manage keywords and negative keywords for ad groups and campaigns.
- [Negative Keywords Endpoints](./negative-keywords-endpoints.md)
  Create, retrieve, update, query, and delete negative keywords that block ads for unwanted searches.
- [Keywords Data Objects](./keywords-data-objects.md)
  Build keyword create and update requests, and read keyword responses and query results.
- [Negative Keywords Data Objects](./negative-keywords-objects.md)
  Build negative keyword create and update requests, and read responses and query results.
- [Keywords Shared Data Types](./keywords-shared-data-types.md)
  Set the status and match type of keywords and negative keywords, and interpret a keyword’s display status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/keywords-endpoints)*