# matchFound

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the web view found a match during the search.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- visionOS 1.0+

## Declaration

```swift
var matchFound: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL matchFound;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) if the web view found a match, or [`false`](../../Swift/false.md) if it didn’t.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkfindresult/matchfound)*