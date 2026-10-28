# label

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

A succinct label that succinctly identifies the purpose of the image region.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var label: String { get set }
```

```objc
@property (nonatomic, copy) NSString * label;
```

## Discussion

The label should be a very short, localized string that identifies the purpose of the region, but does not necessarily convey the imagery displayed in that region.

## See Also

### Getting the Region Attributes
- [var frame: CGRect](./frame.md)
  A portion of the parent image, in the image’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaccessibilityimageregion/label)*