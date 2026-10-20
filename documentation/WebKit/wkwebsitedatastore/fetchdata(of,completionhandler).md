# fetchData(of:completionHandler:)

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
func fetchData(of dataTypes: Set<String>, completionHandler: @escaping @MainActor @Sendable (Data?, (any Error)?) -> Void)
```

```swift
func fetchData(of dataTypes: Set<String>) async throws -> Data
```

```objc
- (void) fetchDataOfTypes:(NSSet<NSString *> *) dataTypes completionHandler:(void (^)(NSData *, NSError *)) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebsitedatastore/fetchdata(of:completionhandler:))*