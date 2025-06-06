# ignoreImageOrientation

**Framework**: Core Image  
**Kind**: structdata

A key for specifying whether to ignore the image orientation. The associated value is a Boolean value packaged as an [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) object.  The default value is [`false`](https://developer.apple.com/documentation/swift/false). An image is usually loaded in its proper orientation, as long as the associated metadata records its orientation. For special purposes you might want to load the image in its physical orientation. The exact meaning of "physical orientation” is dependent on the specific image.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.5+ - Deprecated in 12.0
- tvOS 10.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
static let ignoreImageOrientation: CIRAWFilterOption
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1437949-ignoreimageorientation)*