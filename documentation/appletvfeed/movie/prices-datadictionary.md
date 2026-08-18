# Movie.Prices

**Framework**: Apple TV Feed  
**Kind**: dictionary

A mapping of storefront to pricing information and availability.

**Availability**:
- AppleTVFeed 1.0+

## Declaration

```swift
object Movie.Prices
```

## Topics

### Related objects
- [object Movie.Prices.Price](movie/prices-data.dictionary/price.md)
  Information about a pricing offer.

## Properties

- `prices` ([Movie.Prices.Price]): A list of localized pricing information for the content.
- `storefront` (string): The two-letter country code that serves as the key for the map of values.

## See Also

- [object Movie.Artworks](movie/artworks-data.dictionary.md)
  A mapping of locale to localized artwork.
- [object Movie.CastAndCrew](movie/castandcrew-data.dictionary.md)
  Information about a cast or crew member, including translations of their name.
- [object Movie.Description](movie/description-data.dictionary.md)
  A mapping of locale to localized descriptions of the movie.
- [object Movie.ExternalContentId](movie/externalcontentid.md)
  Information about an external content ID.
- [object Movie.Genre](movie/genre.md)
  A genre name and its structure.
- [object Movie.Name](movie/name-data.dictionary.md)
  A mapping of locale to localized names for the movie.
- [object Movie.OriginalReleaseDate](movie/originalreleasedate-data.dictionary.md)
  A mapping of locale to localized release date.
- [object Movie.Rating](movie/rating-data.dictionary.md)
  Information about a content rating.
- [object Movie.Url](movie/url-data.dictionary.md)
  A mapping of locale to localized URLs for the content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appletvfeed/movie/prices-data.dictionary)*