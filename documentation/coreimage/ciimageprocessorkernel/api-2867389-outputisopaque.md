# outputIsOpaque

**Framework**: Core Image  
**Kind**: cldata

Boolean determining whether or not processor outputs an opaque image.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class var outputIsOpaque: Bool { get }
```

#### Discussion

Override this property if your processor's output stores `1.0` into the alpha channel of all pixels within the output extent.  If not overridden, [`false`](https://developer.apple.com/documentation/swift/false) is returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/2867389-outputisopaque)*