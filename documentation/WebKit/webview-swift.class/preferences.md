# preferences

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The receiver’s preferences.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

> **Deprecated**: No longer supported; please adopt WKWebView.

## Declaration

```swift
var preferences: WebPreferences! { get set }
```

```objc
@property (nonatomic, strong) WebPreferences * preferences;
```

## See Also

### Related Documentation
- [class func standard() -> WebPreferences!](../webpreferences/standard%28%29.md)
  Returns the standard set of preferences that may be used by all WebView objects.
### Getting and Setting Preferences
- [var preferencesIdentifier: String!](./preferencesidentifier.md)
  The identifier of the receiver’s preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/preferences)*