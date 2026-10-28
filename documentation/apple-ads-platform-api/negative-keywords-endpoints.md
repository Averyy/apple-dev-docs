# Negative Keywords Endpoints

**Framework**: Apple Ads Platform API  
**Role**: API Collection

Create, retrieve, update, query, and delete negative keywords that block ads for unwanted searches.

**Availability**:
- Apple Ads Platform API 1.0+

## Overview

Negative keywords suppress your ads for searches you want to exclude. Scope each one to a campaign or an ad group. A campaign-level negative applies across all of the campaign’s ad groups, so set `campaignId` and omit `adGroupId`. An ad group-level negative applies to a single ad group, so set `adGroupId` and omit `campaignId`.

Use these endpoints to manage negative keywords one at a time. For match types and constraints, see [Managing Keywords and Negative Keywords](./keywords-and-negative-keywords.md). To change many negative keywords in one request, see [Bulk Operations Endpoints](./bulk-operations-endpoints.md).

## Topics

- [Create a Negative Keyword](./post-negative-keywords.md)
  Create a negative keyword at the campaign or ad group level to prevent ads from showing for unwanted search terms.
- [Query Negative Keywords](./post-negative-keywords-query.md)
  Query negative keywords using structured filters, sorting, and pagination.
- [Get a Negative Keyword](./get-negative-keywords-_id_.md)
  Retrieve a single negative keyword by its unique identifier.
- [Update a Negative Keyword](./put-negative-keywords-_id_.md)
  Update a negative keyword’s status to enable or pause its search term exclusion.
- [Delete a Negative Keyword](./delete-negative-keywords-_id_.md)
  Soft-delete a negative keyword by ID.

## See Also

### Keywords
- [Managing Keywords and Negative Keywords](./keywords-and-negative-keywords.md)
  Create and manage keywords and negative keywords for ad groups and campaigns.
- [Keywords Endpoints](./keywords-endpoints.md)
  Create, retrieve, update, query, and delete the keywords that match your ad group’s ads to searches.
- [Keywords Data Objects](./keywords-data-objects.md)
  Build keyword create and update requests, and read keyword responses and query results.
- [Negative Keywords Data Objects](./negative-keywords-objects.md)
  Build negative keyword create and update requests, and read responses and query results.
- [Keywords Shared Data Types](./keywords-shared-data-types.md)
  Set the status and match type of keywords and negative keywords, and interpret a keyword’s display status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/negative-keywords-endpoints)*