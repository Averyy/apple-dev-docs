# TvShow

**Framework**: Apple TV Feed  
**Kind**: dictionary

The data structure that represents a TV show resource.

**Availability**:
- AppleTVFeed 1.0+

## Declaration

```swift
object TvShow
```

## Topics

### Related objects
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
- [object TvShow.Prices](tvshow/prices-data.dictionary.md)
  A mapping of storefront to pricing information and availability.
- [object TvShow.Rating](tvshow/rating-data.dictionary.md)
  Information about a content rating.
- [object TvShow.Url](tvshow/url-data.dictionary.md)
  A mapping of locale to localized URLs for the content.

## Properties

- `artworks` (TvShow.Artworks): ****(Required)**** A mapping of locale to localized artwork.
- `castAndCrew` ([TvShow.CastAndCrew]): ****(Required)**** A list of cast and crew for the TV show.
- `description` (TvShow.Description): ****(Required)**** A mapping of locale to localized descriptions of the TV show.
- `externalContentIds` ([TvShow.ExternalContentId]): ****(Required)**** A list of unique identifiers for the TV show in the catalog of another provider.
- `genres` ([TvShow.Genre]): ****(Required)**** A list of genres associated with the TV show.
- `id` (string): ****(Required)**** The unique identifier for the TV show.
- `lastModifiedTime` (date-time): The time, in ISO 8601 format, of the entity’s most recent update.
- `name` (TvShow.Name): ****(Required)**** A mapping of locale to localized names for the TV show.
- `originalPremiereDate` (string): The date of the original content release in YYYY-MM-DD format.
- `prices` (TvShow.Prices): ****(Required)**** A mapping of storefront to pricing information and availability.
- `rating` ([TvShow.Rating]): ****(Required)**** A list of ratings for the TV show in different rating systems.
- `url` (TvShow.Url): ****(Required)**** A mapping of two-letter country code to URLs for the TV show.

## See Also

- [object Movie](movie.md)
  The data structure that represents a movie resource.
- [object TvEpisode](tvepisode.md)
  The data structure that represents a TV episode resource.
- [object TvSeason](tvseason.md)
  The data structure that represents a TV season resource.
- [object SportingEvent](sportingevent.md)
  The data structure that represents a sporting event resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appletvfeed/tvshow)*