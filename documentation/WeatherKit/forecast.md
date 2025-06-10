# Forecast

**Framework**: WeatherKit  
**Kind**: struct

A forecast collection for minute, hourly, and daily forecasts.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct Forecast<Element> where Element : Decodable, Element : Encodable, Element : Equatable, Element : Sendable
```

#### Overview

[`Forecast`](forecast.md) conforms to the `RandomAccessCollection` protocol to support efficient random-access index traversal through forecast types. The protocol involves forwarding the required properties and methods to the underlying forecast collection. The implementation of `subscript` returns an instance of the `Element` type.

## Topics

### Creating the forecast
- [init(from: any Decoder) throws](forecast/init(from:)-390k1.md)
- [init(from: any Decoder) throws](forecast/init(from:)-4wobg.md)
- [init(from: any Decoder) throws](forecast/init(from:)-51k1n.md)
  Creates a new instance by decoding from the given decoder.
### Serializing objects
- [func encode(to: any Encoder) throws](forecast/encode(to:)-5zuqd.md)
- [func encode(to: any Encoder) throws](forecast/encode(to:)-6lmvg.md)
  Encodes this value into the given encoder.
- [func encode(to: any Encoder) throws](forecast/encode(to:)-fbco.md)
### Getting the properties
- [var endIndex: Forecast<Element>.Index](forecast/endindex.md)
  The forecast end index.
- [var forecast: [Element]](forecast/forecast.md)
  The forecast collection.
- [var metadata: WeatherMetadata](forecast/metadata.md)
  Descriptive information about the forecast data.
- [var startIndex: Forecast<Element>.Index](forecast/startindex.md)
  The forecast start index.
- [var summary: String](forecast/summary.md)
  A convenient localized description of the minute forecast.
### Accessing elements
- [subscript(Forecast<Element>.Index) -> Element](forecast/subscript(_:).md)
  The forecast element at the provided index.
- [typealias Index](forecast/index.md)
  The forecast index.
### Comparing forecasts
- [static func == (Forecast<MinuteWeather>, Forecast<MinuteWeather>) -> Bool](forecast/==(_:_:)-9xlo4.md)
### Operators
- [static func == (Forecast<Element>, Forecast<Element>) -> Bool](forecast/==(_:_:)-n0ps.md)
  Returns a Boolean value indicating whether two values are equal.
### Type Aliases
- [typealias Indices](forecast/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [typealias Iterator](forecast/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [typealias SubSequence](forecast/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
### Default Implementations
- [BidirectionalCollection Implementations](forecast/bidirectionalcollection-implementations.md)
- [Collection Implementations](forecast/collection-implementations.md)
- [Equatable Implementations](forecast/equatable-implementations.md)
- [RandomAccessCollection Implementations](forecast/randomaccesscollection-implementations.md)
- [Sequence Implementations](forecast/sequence-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [struct WeatherAlert](weatheralert.md)
  A weather alert issued for the requested  location by a governmental authority.
- [struct WeatherAvailability](weatheravailability.md)
  A structure that indicates the availability of data at the requested location.
- [struct MinuteWeather](minuteweather.md)
  A structure that represents the next hour minute forecasts.
- [struct HourWeather](hourweather.md)
  A structure that represents the weather conditions for the hour.
- [struct DayWeather](dayweather.md)
  A structure that represents the weather conditions for the day.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/forecast)*