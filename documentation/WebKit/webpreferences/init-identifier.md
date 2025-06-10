# init(identifier:)

**Framework**: WebKit  
**Kind**: init

Returns an initialized `WebPreferences` object, creating one if it does not exist.

**Availability**:
- macOS 10.3+

## Declaration

```swift
init!(identifier anIdentifier: String!)
```

#### Return Value

A newly initialized [`WebPreferences`](webpreferences.md) object with the identifier; if an existing `WebPreferences` object with that identifier exists, it is returned instead.

#### Discussion

The `anIdentifier` argument should be unique—it is prepended to the keys used to store the receiver’s attributes in the user defaults database. `WebView` objects can share a [`WebPreferences`](webpreferences.md) object by using the same preferences identifier.

Typically, you do not invoke this method directly. Instead, you set the preferences identifier by sending a [`preferencesIdentifier`](webview-swift.class/preferencesidentifier.md) message to your WebView object. This method is the designated initializer for the WebPreferences class.

## Parameters

- `anIdentifier`: A unique identifier for the   object

## See Also

- [var identifier: String!](webpreferences/identifier.md)
  The receiver’s identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpreferences/init(identifier:))*