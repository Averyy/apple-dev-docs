# maxMovieRatingForCountry

**Framework**: TVMLKit JS  
**Kind**: instm  
**Role**: Instance Method

The maximum movie rating allowed for the specified country or region.

**Availability**:
- tvOS 9.0+

## Declaration

```
String maxMovieRatingForCountry(
    in String countryCode
);
```

## Return Value

A string representing the maximum allowed rating for a movie in the specified country or region; for example, PG-13.

## Parameters

- `countryCode`: An object containing the valid country code. If the code is invalid, the current country or region based on location is used.

## See Also

### Retrieving Restriction Information
- [allowsExplicit](./api-1627425-allowsexplicit.md)
  A boolean value that indicates whether any explicit media is allowed.
- [maxMovieRank](./api-1627305-maxmovierank.md)
  The maximum allowed ranking for a movie.
- [maxTVShowRank](./api-1627434-maxtvshowrank.md)
  The maximum allowed ranking for a television show.
- [maxTVShowRatingForCountry](./api-1627442-maxtvshowratingforcountry.md)
  The maximum television show rating allowed for the specified country or region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/restrictions/1627362-maxmovieratingforcountry)*