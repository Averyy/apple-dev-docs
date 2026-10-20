# upperBodyOnly

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the request requires detecting a full body or upper body only to produce a result.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var upperBodyOnly: Bool { get set }
```

```objc
@property (nonatomic) BOOL upperBodyOnly;
```

#### Discussion

The default value of [`true`](../../Swift/true.md) indicates that the request requires detecting a person’s upper body only to find the bound box around it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetecthumanrectanglesrequest/upperbodyonly)*