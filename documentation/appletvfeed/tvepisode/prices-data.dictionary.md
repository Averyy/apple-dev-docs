# TvEpisode.Prices

**Framework**: Apple TV Feed  
**Kind**: dictionary  
**Role**: Object

A mapping of storefront to pricing information and availability.

**Availability**:
- AppleTVFeed 1.0+

## Declaration

```
object TvEpisode.Prices
```

## Topics

### Related objects
- [object TvEpisode.Prices.Price](./prices-data.dictionary/price.md)
  Information about a pricing offer.

## Properties

- `prices` ([TvEpisode.Prices.Price]): A list of localized pricing information for the content.
- `storefront` (string): The two-letter country code that serves as the key for the map of values.

## See Also

### Related objects
- [object TvEpisode.Artworks](./artworks-data.dictionary.md)
  A mapping of locale to localized artwork.
- [object TvEpisode.CastAndCrew](./castandcrew-data.dictionary.md)
  Information about a cast or crew member, including translations of their name.
- [object TvEpisode.Description](./description-data.dictionary.md)
  A mapping of locale to localized descriptions of the TV episode.
- [object TvEpisode.ExternalContentId](./externalcontentid.md)
  Information about an external content ID.
- [object TvEpisode.Genre](./genre.md)
  A genre name and its structure.
- [object TvEpisode.Name](./name-data.dictionary.md)
  A mapping of locale to localized names for the TV episode.
- [object TvEpisode.Rating](./rating-data.dictionary.md)
  Information about a content rating.
- [object TvEpisode.Url](./url-data.dictionary.md)
  A mapping of locale to localized URLs for the content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appletvfeed/tvepisode/prices-data.dictionary)*