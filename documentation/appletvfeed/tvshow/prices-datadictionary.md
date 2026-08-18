# TvShow.Prices

**Framework**: Apple TV Feed  
**Kind**: dictionary

A mapping of storefront to pricing information and availability.

**Availability**:
- AppleTVFeed 1.0+

## Declaration

```swift
object TvShow.Prices
```

## Topics

### Related objects
- [object TvShow.Prices.Price](tvshow/prices-data.dictionary/price.md)
  Information about a pricing offer.

## Properties

- `prices` ([TvShow.Prices.Price]): A list of localized pricing information for the content.
- `storefront` (string): The two-letter country code that serves as the key for the map of values.

## See Also

- [object TvShow.Artworks](tvshow/artworks-data.dictionary.md)
  A mapping of locale to localized artwork.
- [object TvShow.CastAndCrew](tvshow/castandcrew-data.dictionary.md)
  Information about a cast or crew member, including translations of their name.
- [object TvShow.Description](tvshow/description-data.dictionary.md)
  A mapping of locale to localized descriptions of the TV show.
- [object TvShow.ExternalContentId](tvshow/externalcontentid.md)
  Information about an external content ID.
- [object TvShow.Genre](tvshow/genre.md)
  A genre name and its structure.
- [object TvShow.Name](tvshow/name-data.dictionary.md)
  A mapping of locale to localized names for the TV show.
- [object TvShow.Rating](tvshow/rating-data.dictionary.md)
  Information about a content rating.
- [object TvShow.Url](tvshow/url-data.dictionary.md)
  A mapping of locale to localized URLs for the content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appletvfeed/tvshow/prices-data.dictionary)*