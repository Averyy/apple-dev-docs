# metadata

**Framework**: Watch Connectivity  
**Kind**: property  
**Role**: Instance Property

A dictionary of additional information that was sent with the file.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var metadata: [String : Any]? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSDictionary<NSString *,id> * metadata;
```

## Discussion

The keys of the dictionary are strings. The values are property-list object types.

## See Also

### Getting the File Information
- [var fileURL: URL](./fileurl.md)
  The URL of the file that was received.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsessionfile/metadata)*