# Keywords Data Objects

**Framework**: Apple Ads Platform API  
**Role**: API Collection

Build keyword create and update requests, and read keyword responses and query results.

**Availability**:
- Apple Ads Platform API 1.0+

## Overview

Each keyword call has a matching object. Send [`KeywordCreate`](./keywordcreate.md) to create a keyword and [`KeywordUpdate`](./keywordupdate.md) to change one. [`KeywordResponse`](./keywordresponse.md) wraps the keyword that create and update calls return, and [`KeywordQueryResponse`](./keywordqueryresponse.md) wraps the list that query calls return, along with pagination.

For the calls that use these objects, see [Keywords Endpoints](./keywords-endpoints.md).

## Topics

- [object Keyword](./keyword.md)
  The targeting unit that connects a user’s search query to the ad group’s ads.
- [object KeywordCreate](./keywordcreate.md)
  The request body for creating a new Keyword object.
- [object KeywordUpdate](./keywordupdate.md)
  The request body for updating an existing Keyword object.
- [object KeywordResponse](./keywordresponse.md)
  The response object for a Keyword operation.
- [object KeywordQueryResponse](./keywordqueryresponse.md)
  The response object for a Keyword query, containing matched results and pagination metadata.

## See Also

### Keywords
- [Managing Keywords and Negative Keywords](./keywords-and-negative-keywords.md)
  Create and manage keywords and negative keywords for ad groups and campaigns.
- [Keywords Endpoints](./keywords-endpoints.md)
  Create, retrieve, update, query, and delete the keywords that match your ad group’s ads to searches.
- [Negative Keywords Endpoints](./negative-keywords-endpoints.md)
  Create, retrieve, update, query, and delete negative keywords that block ads for unwanted searches.
- [Negative Keywords Data Objects](./negative-keywords-objects.md)
  Build negative keyword create and update requests, and read responses and query results.
- [Keywords Shared Data Types](./keywords-shared-data-types.md)
  Set the status and match type of keywords and negative keywords, and interpret a keyword’s display status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/keywords-data-objects)*