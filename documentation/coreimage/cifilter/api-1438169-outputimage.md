# outputImage

**Framework**: Core Image  
**Kind**: instp

Returns a [`CIImage`](ciimage.md) object that encapsulates the operations configured in the filter.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var outputImage: CIImage? { get }
```

## See Also

- [var name: String](cifilter/1437997-name.md)
  A name associated with a filter.
- [var isEnabled: Bool](cifilter/1438276-isenabled.md)
  A Boolean value that determines whether the filter is enabled. Animatable.
- [var attributes: [String : Any]](cifilter/1437661-attributes.md)
  A dictionary of key-value pairs that describe the filter.
- [var inputKeys: [String]](cifilter/1438013-inputkeys.md)
  The names of all input parameters to the filter.
- [var outputKeys: [String]](cifilter/1438122-outputkeys.md)
  The names of all output parameters from the filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/1438169-outputimage)*