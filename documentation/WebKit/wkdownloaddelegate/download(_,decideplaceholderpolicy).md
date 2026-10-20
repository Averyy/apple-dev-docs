# download(_:decidePlaceholderPolicy:)

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
optional func download(_ download: WKDownload, decidePlaceholderPolicy completionHandler: @escaping @MainActor @Sendable (WKDownload.PlaceholderPolicy, URL?) -> Void)
```

```swift
optional func placeholderPolicy(forDownload download: WKDownload) async -> (WKDownload.PlaceholderPolicy, URL?)
```

```objc
- (void) download:(WKDownload *) download decidePlaceholderPolicy:(void (^)(enum WKDownloadPlaceholderPolicy, NSURL *)) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkdownloaddelegate/download(_:decideplaceholderpolicy:))*