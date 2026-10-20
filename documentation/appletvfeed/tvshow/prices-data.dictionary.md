# TvShow.Prices

**Framework**: Apple TV Feed  
**Kind**: dictionary  
**Role**: Object

A mapping of storefront to pricing information and availability.

**Availability**:
- AppleTVFeed 1.0+

## Declaration

```
object TvShow.Prices
```

## Topics

### Related objects
- [object TvShow.Prices.Price](./prices-data.dictionary/price.md)
  Information about a pricing offer.

## Properties

- `prices` ([TvShow.Prices.Price]): A list of localized pricing information for the content.
- `storefront` (string): The two-letter country code that serves as the key for the map of values.

## See Also

### Related objects
- [object TvShow.Artworks](./artworks-data.dictionary.md)
  A mapping of locale to localized artwork.
- [object TvShow.CastAndCrew](./castandcrew-data.dictionary.md)
  Information about a cast or crew member, including translations of their name.
- [object TvShow.Description](./description-data.dictionary.md)
  A mapping of locale to localized descriptions of the TV show.
- [object TvShow.ExternalContentId](./externalcontentid.md)
  Information about an external content ID.
- [object TvShow.Genre](./genre.md)
  A genre name and its structure.
- [object TvShow.Name](./name-data.dictionary.md)
  A mapping of locale to localized names for the TV show.
- [object TvShow.Rating](./rating-data.dictionary.md)
  Information about a content rating.
- [object TvShow.Url](./url-data.dictionary.md)
  A mapping of locale to localized URLs for the content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appletvfeed/tvshow/prices-data.dictionary)*