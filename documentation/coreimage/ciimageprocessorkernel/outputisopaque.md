# outputIsOpaque

**Framework**: Core Image  
**Kind**: property

Override this class property if your processor’s output stores 1.0 into the alpha channel of all pixels within the output extent.

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

If not overridden, false is returned.

## See Also

- [class var outputFormat: CIFormat](ciimageprocessorkernel/outputformat.md)
  Override this class property if you want your processor’s output to be in a specific pixel format.
- [class var synchronizeInputs: Bool](ciimageprocessorkernel/synchronizeinputs.md)
  Override this class property to return false if you want your processor to be given input objects that have not been synchronized for CPU access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/outputisopaque)*