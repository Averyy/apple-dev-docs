# preferredContentMode

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The content mode for the web view to use when it loads and renders a webpage.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var preferredContentMode: WKWebpagePreferences.ContentMode { get set }
```

```objc
@property (nonatomic) WKContentMode preferredContentMode;
```

#### Discussion

The default value of this property is [`WKWebpagePreferences.ContentMode.recommended`](./contentmode/recommended.md). The web view ignores this preference for subframe navigation.

## See Also

### Setting the preferred content mode
- [WKWebpagePreferences.ContentMode](./contentmode.md)
  Constants that indicate how to render web view content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebpagepreferences/preferredcontentmode)*