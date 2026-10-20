# SportingEvent.CastAndCrew

**Framework**: Apple TV Feed  
**Kind**: dictionary  
**Role**: Object

Information about a cast or crew member, including translations of their name.

**Availability**:
- AppleTVFeed 1.0+

## Declaration

```
object SportingEvent.CastAndCrew
```

## Topics

### Related objects
- [object SportingEvent.CastAndCrew.Name](./castandcrew-data.dictionary/name-data.dictionary.md)
  A mapping of locale to localized names for the cast or crew member.

## Properties

- `birthday` (date): The birth date of the cast or crew member, in YYYY-MM-DD format.
- `character` (string): The name of the character played by a cast member.
- `name` (SportingEvent.CastAndCrew.Name): **(Required)** A mapping of locale to localized names for the cast or crew member.
- `role` (string): The role of the cast or crew member, for example, `Actor` or `Director`.

## See Also

### Related objects
- [object SportingEvent.Artworks](./artworks-data.dictionary.md)
  A mapping of locale to localized artwork.
- [object SportingEvent.Competitor](./competitor.md)
  Information about a competitor.
- [object SportingEvent.Description](./description-data.dictionary.md)
  A mapping of locale to localized descriptions of the sporting event.
- [object SportingEvent.ExternalContentId](./externalcontentid.md)
  Information about an external content ID.
- [object SportingEvent.LeagueAbbreviation](./leagueabbreviation-data.dictionary.md)
  A mapping of locale to localized abbreviations for the league of the sporting event.
- [object SportingEvent.LeagueName](./leaguename-data.dictionary.md)
  A mapping of locale to localized names for the league of the sporting event.
- [object SportingEvent.Name](./name-data.dictionary.md)
  A mapping of locale to localized names for the sporting event.
- [object SportingEvent.Prices](./prices-data.dictionary.md)
  A mapping of storefront to pricing information and availability.
- [object SportingEvent.Rating](./rating-data.dictionary.md)
  Information about a content rating.
- [object SportingEvent.ShortName](./shortname-data.dictionary.md)
  A mapping of locale to localized short versions of the sporting event name.
- [object SportingEvent.SportName](./sportname-data.dictionary.md)
  A mapping of locale to localized names for the sport of the event.
- [object SportingEvent.Url](./url-data.dictionary.md)
  A mapping of locale to localized URLs for the content.
- [object SportingEvent.VenueAddress](./venueaddress-data.dictionary.md)
  A mapping of locale to localized addresses for the event venue.
- [object SportingEvent.VenueName](./venuename-data.dictionary.md)
  A mapping of locale to localized names for the event venue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appletvfeed/sportingevent/castandcrew-data.dictionary)*