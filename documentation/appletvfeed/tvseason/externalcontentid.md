# TvSeason.ExternalContentId

**Framework**: Apple TV Feed  
**Kind**: dictionary

Information about an external content ID.

**Availability**:
- AppleTVFeed 1.0+

## Declaration

```swift
object TvSeason.ExternalContentId
```

## Properties

- `catalogId` (string): **(Required)** The unique identifier for the external catalog. The possible values are `iTunes ADAM ID`, `TMS ID`, `TMDb`, `Gracenote TMS ID`, `atvtp (Apple TV+ ID)`.
- `id` (string): **(Required)** The unique identifier of the content in the specified catalog.

## See Also

- [object TvSeason.Artworks](tvseason/artworks-data.dictionary.md)
  A mapping of locale to localized artwork.
- [object TvSeason.CastAndCrew](tvseason/castandcrew-data.dictionary.md)
  Information about a cast or crew member, including translations of their name.
- [object TvSeason.Description](tvseason/description-data.dictionary.md)
  A mapping of locale to localized descriptions of the TV season.
- [object TvSeason.Genre](tvseason/genre.md)
  A genre name and its structure.
- [object TvSeason.Name](tvseason/name-data.dictionary.md)
  A mapping of locale to localized names for the TV season.
- [object TvSeason.Prices](tvseason/prices-data.dictionary.md)
  A mapping of storefront to pricing information and availability.
- [object TvSeason.Rating](tvseason/rating-data.dictionary.md)
  Information about a content rating.
- [object TvSeason.Url](tvseason/url-data.dictionary.md)
  A mapping of locale to localized URLs for the content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appletvfeed/tvseason/externalcontentid)*