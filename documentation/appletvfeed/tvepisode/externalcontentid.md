# TvEpisode.ExternalContentId

**Framework**: Apple TV Feed  
**Kind**: dictionary

Information about an external content ID.

**Availability**:
- AppleTVFeed 1.0+

## Declaration

```swift
object TvEpisode.ExternalContentId
```

## Properties

- `catalogId` (string): **(Required)** The unique identifier for the external catalog. The possible values are `iTunes ADAM ID`, `TMS ID`, `TMDb`, `Gracenote TMS ID`, `atvtp (Apple TV+ ID)`.
- `id` (string): **(Required)** The unique identifier of the content in the specified catalog.

## See Also

- [object TvEpisode.Artworks](tvepisode/artworks-data.dictionary.md)
  A mapping of locale to localized artwork.
- [object TvEpisode.CastAndCrew](tvepisode/castandcrew-data.dictionary.md)
  Information about a cast or crew member, including translations of their name.
- [object TvEpisode.Description](tvepisode/description-data.dictionary.md)
  A mapping of locale to localized descriptions of the TV episode.
- [object TvEpisode.Genre](tvepisode/genre.md)
  A genre name and its structure.
- [object TvEpisode.Name](tvepisode/name-data.dictionary.md)
  A mapping of locale to localized names for the TV episode.
- [object TvEpisode.Prices](tvepisode/prices-data.dictionary.md)
  A mapping of storefront to pricing information and availability.
- [object TvEpisode.Rating](tvepisode/rating-data.dictionary.md)
  Information about a content rating.
- [object TvEpisode.Url](tvepisode/url-data.dictionary.md)
  A mapping of locale to localized URLs for the content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appletvfeed/tvepisode/externalcontentid)*