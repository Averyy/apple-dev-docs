# init(_:)

**Framework**: WebKit  
**Kind**: init

Creates a new `URLScheme` value from a valid scheme, which WebKit does not already handle.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
init?(_ rawValue: String)
```

#### Discussion

To determine whether WebKit handles a specific scheme, call the `handlesURLScheme(_:)` static method of `WebPage`.

## Parameters

- `rawValue`: The raw value of the scheme string; if this is an invalid scheme, of if WebKit already handles   this scheme, the initializer returns  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/urlscheme/init(_:))*