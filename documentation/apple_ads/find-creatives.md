# Find Creatives

**Framework**: Apple Ads  
**Kind**: httpRequest

Finds creatives within an organization.

**Availability**:
- Search Ads 5.0+

#### Discussion

Use this endpoint to find creatives using a [`Selector`](selector.md) [`Condition`](condition.md) to filter results. If you don’t specify selector conditions, all creatives return in the response. See [`Creative`](creative.md) for field descriptions and selector condition operators.

Values are case-sensitive strings. The `orderBy` selector supports the `Id` and `name` fields.

##### Payload Example Find Creatives

## Request Body

The request body that includes the selector [`Condition`](condition.md). [`Selector`](selector.md) objects define what data the API returns when fetching resources.

## See Also

- [Create a Creative](create-a-creative.md)
  Creates a creative object within an organization.
- [Get a Creative](get-a-creative.md)
  Fetches a creative by identifier.
- [Get All Creatives](get-all-creatives.md)
  Fetches all creatives within an organization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/find-creatives)*