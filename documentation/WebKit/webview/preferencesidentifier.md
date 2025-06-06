# preferencesIdentifier

**Framework**: Webkit  
**Kind**: property

The identifier of the receiver’s preferences.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
var preferencesIdentifier: String! { get set }
```

#### Discussion

It is fixed to the keys used to store the receiver’s preferences in the user defaults database. `WebView` objects can share instances of the `WebPreferences` class by using the same preferences identifier.

## See Also

- [var autosaves: Bool](webpreferences/autosaves.md)
  A Boolean that indicates whether or not the receiver’s attributes are automatically stored in the user defaults database.
- [var preferences: WebPreferences!](webview/preferences.md)
  The receiver’s preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview/preferencesidentifier)*