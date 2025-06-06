# synchronizeInputs

**Framework**: Core Image  
**Kind**: cldata

Tells whether or not processor input should be synchronized for CPU access.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class var synchronizeInputs: Bool { get }
```

#### Discussion

Set to return [`false`](https://developer.apple.com/documentation/swift/false) if you want your processor to be given [`CIImageProcessorInput`](ciimageprocessorinput.md) objects not synchronized for CPU access.Set to return [`false`](https://developer.apple.com/documentation/swift/false) if your subclass uses the GPU.

Defaults to [`true`](https://developer.apple.com/documentation/swift/true) if not overridden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/2143066-synchronizeinputs)*