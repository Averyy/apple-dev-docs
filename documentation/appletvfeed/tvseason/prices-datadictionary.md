# TvSeason.Prices

**Framework**: Apple TV Feed  
**Kind**: dictionary

A mapping of storefront to pricing information and availability.

**Availability**:
- AppleTVFeed 1.0+

## Declaration

```swift
object TvSeason.Prices
```

## Topics

### Related objects
- [object TvSeason.Prices.Price](tvseason/prices-data.dictionary/price.md)
  Information about a pricing offer.

## Properties

- `prices` ([TvSeason.Prices.Price]): A list of localized pricing information for the content.
- `storefront` (string): The two-letter country code that serves as the key for the map of values.

## See Also

- [object TvSeason.Artworks](tvseason/artworks-data.dictionary.md)
  A mapping of locale to localized artwork.
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
- [object TvSeason.Rating](tvseason/rating-data.dictionary.md)
  Information about a content rating.
- [object TvSeason.Url](tvseason/url-data.dictionary.md)
  A mapping of locale to localized URLs for the content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appletvfeed/tvseason/prices-data.dictionary)*