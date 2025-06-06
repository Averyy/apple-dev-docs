# applyOrientationProperty

**Framework**: Core Image  
**Kind**: structdata

The key for transforming an image according to orientation metadata.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static let applyOrientationProperty: CIImageOption
```

#### Discussion

Images can contain metadata that reveals the orientation at capture time.  You can load this metadata into [`CIImage`](ciimage.md) with [`imageWithContentsOfURL:`](ciimage/1547027-imagewithcontentsofurl.md) or [`init(data:)`](ciimage/1437925-init.md) when the captured image contains orientation metadata.  Use any of the `initWith:options: `methods if the [`properties`](ciimageoption/1437679-properties.md) ([`NSDictionary`](https://developer.apple.com/documentation/foundation/nsdictionary) of metadata properties) option is also provided.

If the value of this key is true, then calls to [`imageWithContentsOfURL:options:`](ciimage/1546997-imagewithcontentsofurl.md) and [`imageWithData:options:`](ciimage/1547016-imagewithdata.md) will return the image transformed according to its orientation metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageoption/2915369-applyorientationproperty)*