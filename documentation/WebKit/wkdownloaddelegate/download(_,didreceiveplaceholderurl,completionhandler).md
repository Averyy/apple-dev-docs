# download(_:didReceivePlaceholderURL:completionHandler:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- macOS 11.3+
- visionOS 2.2+

## Declaration

```swift
optional func download(_ download: WKDownload, didReceivePlaceholderURL url: URL, completionHandler: @escaping @MainActor @Sendable () -> Void)
```

```swift
optional func download(_ download: WKDownload, didReceivePlaceholderURL url: URL) async
```

```objc
- (void) download:(WKDownload *) download didReceivePlaceholderURL:(NSURL *) url completionHandler:(void (^)(void)) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkdownloaddelegate/download(_:didreceiveplaceholderurl:completionhandler:))*