# navigationDelegate

**Framework**: Webkit  
**Kind**: property

The object you use to manage navigation behavior for the web view.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var navigationDelegate: (any WKNavigationDelegate)? { get set }
```

#### Discussion

Provide a delegate object when you want to manage or restrict navigation in your web content, track the progress of navigation requests, and handle authentication challenges for any new content. The object you specify must conform to the [`WKNavigationDelegate`](wknavigationdelegate.md) protocol.

## See Also

- [protocol WKNavigationDelegate](wknavigationdelegate.md)
  Methods for accepting or rejecting navigation changes, and for tracking the progress of navigation requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/navigationdelegate)*