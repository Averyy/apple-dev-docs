# restoreData(_:completionHandler:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func restoreData(_ data: Data, completionHandler: @escaping @MainActor @Sendable ((any Error)?) -> Void)
```

```swift
func restoreData(_ data: Data) async throws
```

```objc
- (void) restoreData:(NSData *) data completionHandler:(void (^)(NSError *)) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebsitedatastore/restoredata(_:completionhandler:))*