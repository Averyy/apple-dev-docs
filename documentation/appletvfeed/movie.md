# Movie

**Framework**: Apple TV Feed  
**Kind**: dictionary

The data structure that represents a movie resource.

**Availability**:
- AppleTVFeed 1.0+

## Declaration

```swift
object Movie
```

## Topics

### Related objects
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
- [object Movie.Prices](movie/prices-data.dictionary.md)
  A mapping of storefront to pricing information and availability.
- [object Movie.Rating](movie/rating-data.dictionary.md)
  Information about a content rating.
- [object Movie.Url](movie/url-data.dictionary.md)
  A mapping of locale to localized URLs for the content.

## Properties

- `artworks` (Movie.Artworks): **(Required)** A mapping of locale to localized artwork.
- `castAndCrew` ([Movie.CastAndCrew]): **(Required)** A list of cast and crew for the movie.
- `description` (Movie.Description): **(Required)** A mapping of locale to localized descriptions of the movie.
- `durationInMillis` (int64): The length of the movie in milliseconds.
- `externalContentIds` ([Movie.ExternalContentId]): **(Required)** A list of unique identifiers for the movie in the catalog of another provider.
- `genres` ([Movie.Genre]): **(Required)** A list of genres associated with the movie.
- `id` (string): **(Required)** The unique identifier for the movie.
- `lastModifiedTime` (date-time): The time, in ISO 8601 format, of the entity’s most recent update.
- `name` (Movie.Name): **(Required)** A mapping of locale to localized names for the movie.
- `originalReleaseDate` (Movie.OriginalReleaseDate): **(Required)** A mapping of locale to localized release dates for the movie.
- `prices` (Movie.Prices): **(Required)** A mapping of storefront to pricing information and availability.
- `rating` ([Movie.Rating]): **(Required)** A list of ratings for the movie in different rating systems.
- `studio` (string): The studio associated with the movie.
- `url` (Movie.Url): **(Required)** A mapping of two-letter country code to URLs for the movie.

## See Also

- [object TvEpisode](tvepisode.md)
  The data structure that represents a TV episode resource.
- [object TvSeason](tvseason.md)
  The data structure that represents a TV season resource.
- [object TvShow](tvshow.md)
  The data structure that represents a TV show resource.
- [object SportingEvent](sportingevent.md)
  The data structure that represents a sporting event resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appletvfeed/movie)*