# URLScheme

**Framework**: WebKit  
**Kind**: struct

A type representing a valid URL scheme.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct URLScheme
```

#### Overview

Scheme names are case sensitive, must start with an ASCII letter, and may contain only ASCII letters, numbers, the “+” character, the “-” character, and the “.” character.

## Topics

### Initializers
- [init?(String)](urlscheme/init(_:).md)
  Creates a new `URLScheme` value from a valid scheme, which WebKit does not already handle.
### Instance Properties
- [let rawValue: String](urlscheme/rawvalue.md)
  The raw value of the scheme string.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [WebPage.Configuration](webpage/configuration.md)
  A configuration type that specifies the preferences and behaviors of a webpage.
- [WebPage.DeviceSensorAuthorization](webpage/devicesensorauthorization.md)
  A type that describes the authorization permissions policy for the device’s sensors a web resource may access.
- [protocol URLSchemeHandler](urlschemehandler.md)
  A protocol for loading resources with URL schemes that WebKit doesn’t handle.
- [enum URLSchemeTaskResult](urlschemetaskresult.md)
  A value used as part of a sequence of results from a [`URLSchemeHandler`](urlschemehandler.md), which can either be a `Data` or a `URLResponse`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/urlscheme)*