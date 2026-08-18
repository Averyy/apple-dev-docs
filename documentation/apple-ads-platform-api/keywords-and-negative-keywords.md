# Managing Keywords and Negative Keywords

**Framework**: Apple Ads Platform API

Create and manage keywords and negative keywords for ad groups and campaigns.

**Availability**:
- Apple Ads Platform API 1.0+

#### Overview

Keywords define which user searches trigger your ad. Negative keywords prevent your ad from appearing for searches you want to exclude.

#### Explore the Endpoints

The following endpoints create, retrieve, update, and delete keywords and negative keywords:

| Method | Path | Description |
| --- | --- | --- |
| `POST` | `/v1/keywords` | [`Create a Keyword`](post-keywords.md) creates a keyword. |
| `POST` | `/v1/keywords/query` | [`Query Keywords`](post-keywords-query.md) retrieves keywords matching the specified filters. |
| `GET` | `/v1/keywords/{id}` | [`Get a Keyword`](get-keywords-_id_.md) retrieves a single keyword by its ID. |
| `PUT` | `/v1/keywords/{id}` | [`Update a Keyword`](put-keywords-_id_.md) updates an existing keyword. |
| `DELETE` | `/v1/keywords/{id}` | [`Delete a Keyword`](delete-keywords-_id_.md) soft-deletes a keyword by its ID. |
| `POST` | `/v1/negative-keywords` | [`Create a Negative Keyword`](post-negative-keywords.md) creates a negative keyword. |
| `POST` | `/v1/negative-keywords/query` | [`Query Negative Keywords`](post-negative-keywords-query.md) retrieves negative keywords matching the specified filters. |
| `GET` | `/v1/negative-keywords/{id}` | [`Get a Negative Keyword`](get-negative-keywords-_id_.md) retrieves a single negative keyword by its ID. |
| `PUT` | `/v1/negative-keywords/{id}` | [`Update a Negative Keyword`](put-negative-keywords-_id_.md) updates an existing negative keyword. |
| `DELETE` | `/v1/negative-keywords/{id}` | [`Delete a Negative Keyword`](delete-negative-keywords-_id_.md) soft-deletes a negative keyword by its ID. |

##### Configure a Keyword

A keyword belongs to an ad group and associates a search term with a bid. When a user’s search query matches a keyword, the ad group becomes eligible to enter the auction for that query.

Each keyword requires:

- `text`: The keyword term to target. For `CATEGORY` match type on Maps campaigns, this must be a Maps business category identifier (for example, `dining.restaurant`).
- `matchType`: How the keyword matches user queries. The `EXACT` and `BROAD` types apply to App Store campaigns using the Search results placement. The `PHRASE` and `CATEGORY` types apply to Apple Maps campaigns. See [`KeywordMatchType`](keywordmatchtype.md).
- `adGroupId`: The ad group this keyword belongs to.

The `bid` field is optional on create. When provided, it overrides the ad group’s [`BidStrategy`](bidstrategy.md) `bid` for that specific keyword. Maximize Conversions bid strategy campaigns don’t use the `bid` field.

To enable or pause individual keywords without removing them, use [`KeywordStatus`](keywordstatus.md). A paused keyword remains in the ad group but doesn’t participate in auctions.

##### Configure a Negative Keyword

A negative keyword prevents your ad from serving when a user’s search matches the excluded term. You can scope negative keywords to either a campaign or an ad group:

- **Campaign-level**: Applies across all ad groups in the campaign. Set `campaignId` and omit `adGroupId`.
- **Ad group-level**: Applies only within a specific ad group. Set `adGroupId` and omit `campaignId`.

Negative keywords use the same `text` and `matchType` fields as keywords but don’t have a `bid` field, though `CATEGORY` match type doesn’t apply to negative keywords.

##### Choose a Match Type

The `matchType` field controls how a keyword’s text matches a user’s search query. See the table below for each type’s placement and behavior:

| Match Type | Placement | Behavior |
| --- | --- | --- |
| `BROAD` | App Store (Search results) | Matches the keyword and close variants, including misspellings, synonyms, and related terms. Maximizes reach. |
| `EXACT` | App Store (Search results) | Matches the keyword term precisely. Gives the most control over which queries trigger the ad. |
| `PHRASE` | Maps | Matches the keyword and close variants within Maps search, allowing flexibility while staying focused on the search intent. |
| `CATEGORY` | Maps | Matches user searches to a Maps business category (for example, `dining.restaurant`, `shopping.clothing`). Use category identifiers from the [`Query Business Categories`](query-categories.md) endpoint. |

Use `BROAD` as the recommended starting point for Search results campaigns on the App Store when you’re building out a keyword list. To control spend on specific high-value terms, use `EXACT`. For Maps campaigns, use `CATEGORY` to reach users searching for a type of business rather than a specific name.

##### Perform Bulk Operations

For bulk create, update, and delete across keywords and negative keywords, see [`Bulk Operations Endpoints`](bulk-operations-endpoints.md).

## See Also

- [Keywords Endpoints](keywords-endpoints.md)
  Endpoints for creating, retrieving, updating, and deleting keywords.
- [Negative Keywords Endpoints](negative-keywords-endpoints.md)
  Endpoints for creating, retrieving, updating, and deleting negative keywords.
- [Keywords Data Objects](keywords-data-objects.md)
  Request, response, and data objects for managing keywords in ad group campaigns.
- [Negative Keywords Data Objects](negative-keywords-objects.md)
  Request and response objects for negative keyword endpoints.
- [Keywords Shared Data Types](keywords-shared-data-types.md)
  Shared enumerations used by keyword and negative keyword objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/keywords-and-negative-keywords)*