# Forecast

**Framework**: WeatherKit  
**Kind**: struct  
**Role**: Structure

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

[`Forecast`](./forecast.md) conforms to the `RandomAccessCollection` protocol to support efficient random-access index traversal through forecast types. The protocol involves forwarding the required properties and methods to the underlying forecast collection. The implementation of `subscript` returns an instance of the `Element` type.

## Topics

### Creating the forecast
- [init(from: any Decoder) throws](./forecast/init%28from%29-390k1.md)
- [init(from: any Decoder) throws](./forecast/init%28from%29-4wobg.md)
### Serializing objects
- [func encode(to: any Encoder) throws](./forecast/encode%28to%29-5zuqd.md)
- [func encode(to: any Encoder) throws](./forecast/encode%28to%29-fbco.md)
### Getting the properties
- [var endIndex: Forecast<Element>.Index](./forecast/endindex.md)
  The forecast end index.
- [var forecast: [Element]](./forecast/forecast.md)
  The forecast collection.
- [var metadata: WeatherMetadata](./forecast/metadata.md)
  Descriptive information about the forecast data.
- [var startIndex: Forecast<Element>.Index](./forecast/startindex.md)
  The forecast start index.
- [var summary: String](./forecast/summary.md)
  A convenient localized description of the minute forecast.
### Accessing elements
- [subscript(Forecast<Element>.Index) -> Element](./forecast/subscript%28_%29.md)
  The forecast element at the provided index.
- [typealias Index](./forecast/index.md)
  The forecast index.
### Comparing forecasts
- [static func == (Forecast<MinuteWeather>, Forecast<MinuteWeather>) -> Bool](./forecast/eqeq%28_,_%29.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/bidirectionalcollection.md)
- [Collection](../Swift/collection.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [RandomAccessCollection](../Swift/randomaccesscollection.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [Sequence](../Swift/sequence.md)

## See Also

### Alerts and forecasts
- [struct WeatherAlert](./weatheralert.md)
  A weather alert issued for the requested  location by a governmental authority.
- [struct WeatherAvailability](./weatheravailability.md)
  A structure that indicates the availability of data at the requested location.
- [struct MinuteWeather](./minuteweather.md)
  A structure that represents the next hour minute forecasts.
- [struct HourWeather](./hourweather.md)
  A structure that represents the weather conditions for the hour.
- [struct DayWeather](./dayweather.md)
  A structure that represents the weather conditions for the day.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/forecast)*