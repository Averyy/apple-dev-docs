# Negative Keywords Data Objects

**Framework**: Apple Ads Platform API  
**Role**: API Collection

Build negative keyword create and update requests, and read responses and query results.

**Availability**:
- Apple Ads Platform API 1.0+

#### Overview

Each negative keyword call has a matching object. Send [`NegativeKeywordCreate`](./negativekeywordcreate.md) to create a negative keyword and [`NegativeKeywordUpdate`](./negativekeywordupdate.md) to change one. [`NegativeKeywordResponse`](./negativekeywordresponse.md) wraps the negative keyword that create and update calls return, and [`NegativeKeywordQueryResponse`](./negativekeywordqueryresponse.md) wraps the list that query calls return, along with pagination.

For the calls that use these objects, see [Negative Keywords Endpoints](./negative-keywords-endpoints.md). For scoping rules, match types, and constraints, see [Managing Keywords and Negative Keywords](./keywords-and-negative-keywords.md).

## Topics

- [object NegativeKeyword](./negativekeyword.md)
  A keyword exclusion that prevents ads from showing when a search query matches the excluded term.
- [object NegativeKeywordCreate](./negativekeywordcreate.md)
  The request body for creating a new negative keyword.
- [object NegativeKeywordUpdate](./negativekeywordupdate.md)
  The request body for updating an existing negative keyword.
- [object NegativeKeywordResponse](./negativekeywordresponse.md)
  The response object for a negative keyword operation.
- [object NegativeKeywordQueryResponse](./negativekeywordqueryresponse.md)
  The response object for a negative keyword query, containing matched results and pagination metadata.

## See Also

### Keywords
- [Managing Keywords and Negative Keywords](./keywords-and-negative-keywords.md)
  Create and manage keywords and negative keywords for ad groups and campaigns.
- [Keywords Endpoints](./keywords-endpoints.md)
  Create, retrieve, update, query, and delete the keywords that match your ad group’s ads to searches.
- [Negative Keywords Endpoints](./negative-keywords-endpoints.md)
  Create, retrieve, update, query, and delete negative keywords that block ads for unwanted searches.
- [Keywords Data Objects](./keywords-data-objects.md)
  Build keyword create and update requests, and read keyword responses and query results.
- [Keywords Shared Data Types](./keywords-shared-data-types.md)
  Set the status and match type of keywords and negative keywords, and interpret a keyword’s display status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/negative-keywords-objects)*