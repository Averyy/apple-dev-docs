# WKDataDetectorTypes

**Framework**: WebKit  
**Kind**: struct  
**Role**: Structure

The data detector types.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
struct WKDataDetectorTypes
```

```c
enum WKDataDetectorTypes : NSUInteger;
```

#### Overview

To perform no data detection, create an empty set of data detector types, indicated by the empty array literal, `[]`. For example:

```swift
let myDataDetector: WKDataDetectorTypes = []
```

## Topics

### Data Detector Types
- [static var phoneNumber: WKDataDetectorTypes](./wkdatadetectortypes/phonenumber.md)
  Detect phone numbers in text and create a link to call the specified number.
- [static var link: WKDataDetectorTypes](./wkdatadetectortypes/link.md)
  Detect URLs in text and turn them into links.
- [static var address: WKDataDetectorTypes](./wkdatadetectortypes/address.md)
  Detect addresses in text and turn them into links to display the location.
- [static var calendarEvent: WKDataDetectorTypes](./wkdatadetectortypes/calendarevent.md)
  Turn future dates and times into links to create calendar events.
- [static var trackingNumber: WKDataDetectorTypes](./wkdatadetectortypes/trackingnumber.md)
  Detect tracking numbers in text and turn them into links.
- [static var flightNumber: WKDataDetectorTypes](./wkdatadetectortypes/flightnumber.md)
  Detect flight numbers in text and turn them into links.
- [static var lookupSuggestion: WKDataDetectorTypes](./wkdatadetectortypes/lookupsuggestion.md)
  Detect Spotlight suggestions and turn them into links.
- [static var all: WKDataDetectorTypes](./wkdatadetectortypes/all.md)
  Detect all data types and turn them into links.
### Initializers
- [init(rawValue: UInt)](./wkdatadetectortypes/init%28rawvalue%29.md)
### Deprecated Types
- [static var spotlightSuggestion: WKDataDetectorTypes](./wkdatadetectortypes/spotlightsuggestion.md)
  Spotlight suggestions are detected and turned into links.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Identifying data types
- [var dataDetectorTypes: WKDataDetectorTypes](./wkwebviewconfiguration/datadetectortypes.md)
  The types of data detectors to apply to the web view’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkdatadetectortypes)*