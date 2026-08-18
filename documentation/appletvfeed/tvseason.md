# TvSeason

**Framework**: Apple TV Feed  
**Kind**: dictionary

The data structure that represents a TV season resource.

**Availability**:
- AppleTVFeed 1.0+

## Declaration

```swift
object TvSeason
```

## Topics

### Related objects
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
- [object TvSeason.Prices](tvseason/prices-data.dictionary.md)
  A mapping of storefront to pricing information and availability.
- [object TvSeason.Rating](tvseason/rating-data.dictionary.md)
  Information about a content rating.
- [object TvSeason.Url](tvseason/url-data.dictionary.md)
  A mapping of locale to localized URLs for the content.

## Properties

- `artworks` (TvSeason.Artworks): **(Required)** A mapping of locale to localized artwork.
- `castAndCrew` ([TvSeason.CastAndCrew]): **(Required)** A list of cast and crew for the TV season.
- `description` (TvSeason.Description): **(Required)** A mapping of locale to localized descriptions of the TV season.
- `externalContentIds` ([TvSeason.ExternalContentId]): **(Required)** A list of unique identifiers for the TV season in the catalog of another provider.
- `genres` ([TvSeason.Genre]): **(Required)** A list of genres associated with the TV season.
- `id` (string): **(Required)** The unique identifier for the TV season.
- `lastModifiedTime` (date-time): The time, in ISO 8601 format, of the entity’s most recent update.
- `name` (TvSeason.Name): **(Required)** A mapping of locale to localized names for the TV season.
- `originalPremiereDate` (string): The date of the original content release in YYYY-MM-DD format.
- `prices` (TvSeason.Prices): **(Required)** A mapping of storefront to pricing information and availability.
- `rating` ([TvSeason.Rating]): **(Required)** A list of ratings for the TV season in different rating systems.
- `seasonNumber` (integer): The sequence number of the TV season.
- `showId` (string): The unique identifier for the TV show that the season belongs to.
- `url` (TvSeason.Url): **(Required)** A mapping of two-letter country code to URLs for the TV season.

## See Also

- [object Movie](movie.md)
  The data structure that represents a movie resource.
- [object TvEpisode](tvepisode.md)
  The data structure that represents a TV episode resource.
- [object TvShow](tvshow.md)
  The data structure that represents a TV show resource.
- [object SportingEvent](sportingevent.md)
  The data structure that represents a sporting event resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appletvfeed/tvseason)*