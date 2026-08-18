# TvSeason.Artworks

**Framework**: Apple TV Feed  
**Kind**: dictionary

A mapping of locale to localized artwork.

**Availability**:
- AppleTVFeed 1.0+

## Declaration

```swift
object TvSeason.Artworks
```

## Topics

### Related objects
- [object TvSeason.Artworks.Artwork](tvseason/artworks-data.dictionary/artwork-data.dictionary.md)
  The artwork related to this content.

## Properties

- `artwork` (TvSeason.Artworks.Artwork): The artwork related to this content.
- `locale` (string): The IETF language tag format locale that serves as the key for the map of values. Note: The locale can contain a wildcard; for example, `-au` matches all languages for Australia, and `en-*` matches all countries that have English as a language.

## See Also

- [object TvSeason.CastAndCrew](tvseason/castandcrew-data.dictionary.md)
  Information about a cast or crew member, including translations of their name.
- [object TvSeason.Description](tvseason/description-data.dictionary.md)
  A mapping of locale to localized descriptions of the TV season.
- [object TvSeason.ExternalContentId](tvseason/externalcontentid.md)
  Information about an external content ID.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appletvfeed/tvseason/artworks-data.dictionary)*