# Create Campaign Negative Keywords

**Framework**: Apple Ads  
**Kind**: httpRequest

Creates negative keywords for a campaign.

**Availability**:
- Search Ads 5.0+

#### Overview

> **Note**:  If you create duplicate keywords, the payload response indicates an error, but the call returns with a 200 status code.

- 400: An invalid query or missing required parameters.
- 401: An unauthenticated call fails to get the requested response.
- 403: Insufficient rights to the resource.
- 404: The API can’t locate the resource.
- 429: The API calls exceed rate-limit thresholds. See the Rate Limits subsection of [`Calling the Apple Ads API`](calling-the-apple-search-ads-api.md).
- 500: The Apple Ads server is temporarily down or unreachable. The request may be valid, but you need to retry it later.

#### Discussion

Negative keywords prevent your ad from showing up in App Store searches. Negative keywords can belong to a campaign or an ad group.

To create campaign negative keywords, use the associated `campaignId` in the URI.

##### Payload Example Create Campaign Negative Keywords

## Request Body

The request body that includes negative keyword details.

## See Also

- [Find Campaign Negative Keywords](find-campaign-negative-keywords.md)
  Fetches negative keywords for campaigns.
- [Get a Campaign Negative Keyword](get-a-campaign-negative-keyword.md)
  Fetches a specific negative keyword in a campaign.
- [Get All Campaign Negative Keywords](get-all-campaign-negative-keywords.md)
  Fetches all negative keywords in a campaign.
- [Update Campaign Negative Keywords](update-campaign-negative-keywords.md)
  Updates negative keywords in a campaign.
- [Delete Campaign Negative Keywords](delete-campaign-negative-keywords.md)
  Deletes negative keywords from a campaign.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/create-campaign-negative-keywords)*