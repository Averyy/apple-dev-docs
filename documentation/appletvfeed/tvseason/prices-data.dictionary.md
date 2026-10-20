# TvSeason.Prices

**Framework**: Apple TV Feed  
**Kind**: dictionary  
**Role**: Object

A mapping of storefront to pricing information and availability.

**Availability**:
- AppleTVFeed 1.0+

## Declaration

```
object TvSeason.Prices
```

## Topics

### Related objects
- [object TvSeason.Prices.Price](./prices-data.dictionary/price.md)
  Information about a pricing offer.

## Properties

- `prices` ([TvSeason.Prices.Price]): A list of localized pricing information for the content.
- `storefront` (string): The two-letter country code that serves as the key for the map of values.

## See Also

### Related objects
- [object TvSeason.Artworks](./artworks-data.dictionary.md)
  A mapping of locale to localized artwork.
- [object TvSeason.CastAndCrew](./castandcrew-data.dictionary.md)
  Information about a cast or crew member, including translations of their name.
- [object TvSeason.Description](./description-data.dictionary.md)
  A mapping of locale to localized descriptions of the TV season.
- [object TvSeason.ExternalContentId](./externalcontentid.md)
  Information about an external content ID.
- [object TvSeason.Genre](./genre.md)
  A genre name and its structure.
- [object TvSeason.Name](./name-data.dictionary.md)
  A mapping of locale to localized names for the TV season.
- [object TvSeason.Rating](./rating-data.dictionary.md)
  Information about a content rating.
- [object TvSeason.Url](./url-data.dictionary.md)
  A mapping of locale to localized URLs for the content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appletvfeed/tvseason/prices-data.dictionary)*