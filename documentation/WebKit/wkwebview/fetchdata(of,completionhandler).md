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
func fetchData(of dataTypes: WKWebViewDataType, completionHandler: @escaping @MainActor @Sendable (Data?, (any Error)?) -> Void)
```

```swift
func fetchData(of dataTypes: WKWebViewDataType) async throws -> Data
```

```objc
- (void) fetchDataOfTypes:(WKWebViewDataType) dataTypes completionHandler:(void (^)(NSData *, NSError *)) completionHandler;
```

## See Also

### Saving and restoring data
- [func restoreData(Data, completionHandler: ((any Error)?) -> Void)](./restoredata%28_,completionhandler%29.md)
- [struct WKWebViewDataType](../wkwebviewdatatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/fetchdata(of:completionhandler:))*