# WKWebViewDataType

**Framework**: WebKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct WKWebViewDataType
```

```c
enum WKWebViewDataType : NSUInteger;
```

## Topics

### Initializers
- [init(rawValue: UInt)](./wkwebviewdatatype/init%28rawvalue%29.md)
### Type Properties
- [static var sessionStorage: WKWebViewDataType](./wkwebviewdatatype/sessionstorage.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Saving and restoring data
- [func fetchData(of: WKWebViewDataType, completionHandler: (Data?, (any Error)?) -> Void)](./wkwebview/fetchdata%28of,completionhandler%29.md)
- [func restoreData(Data, completionHandler: ((any Error)?) -> Void)](./wkwebview/restoredata%28_,completionhandler%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebviewdatatype)*