# preferencesIdentifier

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The identifier of the receiver’s preferences.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

> **Deprecated**: No longer supported; please adopt WKWebView.

## Declaration

```swift
var preferencesIdentifier: String! { get set }
```

```objc
@property (nonatomic, copy) NSString * preferencesIdentifier;
```

## Discussion

It is fixed to the keys used to store the receiver’s preferences in the user defaults database. `WebView` objects can share instances of the `WebPreferences` class by using the same preferences identifier.

## See Also

### Related Documentation
- [var autosaves: Bool](../webpreferences/autosaves.md)
  A Boolean that indicates whether or not the receiver’s attributes are automatically stored in the user defaults database.
### Getting and Setting Preferences
- [var preferences: WebPreferences!](./preferences.md)
  The receiver’s preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/preferencesidentifier)*