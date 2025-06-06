# isEnabled

**Framework**: Core Image  
**Kind**: instp

A Boolean value that determines whether the filter is enabled. Animatable.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var isEnabled: Bool { get set }
```

#### Discussion

The filter is applied to its input when this property is set to [`true`](https://developer.apple.com/documentation/swift/true) (the default).

Use this property in conjunction with the [`name`](cifilter/1437997-name.md) property when attaching filters to Core Animation layers and accessing or animating filter properties through key-value animations.  Core Animation can animate this property on a layer.

## See Also

- [var name: String](cifilter/1437997-name.md)
  A name associated with a filter.
- [var attributes: [String : Any]](cifilter/1437661-attributes.md)
  A dictionary of key-value pairs that describe the filter.
- [var inputKeys: [String]](cifilter/1438013-inputkeys.md)
  The names of all input parameters to the filter.
- [var outputKeys: [String]](cifilter/1438122-outputkeys.md)
  The names of all output parameters from the filter.
- [var outputImage: CIImage?](cifilter/1438169-outputimage.md)
  Returns a [`CIImage`](ciimage.md) object that encapsulates the operations configured in the filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/1438276-isenabled)*