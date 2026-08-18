# TvEpisode.Prices

**Framework**: Apple TV Feed  
**Kind**: dictionary

A mapping of storefront to pricing information and availability.

**Availability**:
- AppleTVFeed 1.0+

## Declaration

```swift
object TvEpisode.Prices
```

## Topics

### Related objects
- [object TvEpisode.Prices.Price](tvepisode/prices-data.dictionary/price.md)
  Information about a pricing offer.

## Properties

- `prices` ([TvEpisode.Prices.Price]): A list of localized pricing information for the content.
- `storefront` (string): The two-letter country code that serves as the key for the map of values.

## See Also

- [object TvEpisode.Artworks](tvepisode/artworks-data.dictionary.md)
  A mapping of locale to localized artwork.
- [object TvEpisode.CastAndCrew](tvepisode/castandcrew-data.dictionary.md)
  Information about a cast or crew member, including translations of their name.
- [object TvEpisode.Description](tvepisode/description-data.dictionary.md)
  A mapping of locale to localized descriptions of the TV episode.
- [object TvEpisode.ExternalContentId](tvepisode/externalcontentid.md)
  Information about an external content ID.
- [object TvEpisode.Genre](tvepisode/genre.md)
  A genre name and its structure.
- [object TvEpisode.Name](tvepisode/name-data.dictionary.md)
  A mapping of locale to localized names for the TV episode.
- [object TvEpisode.Rating](tvepisode/rating-data.dictionary.md)
  Information about a content rating.
- [object TvEpisode.Url](tvepisode/url-data.dictionary.md)
  A mapping of locale to localized URLs for the content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appletvfeed/tvepisode/prices-data.dictionary)*