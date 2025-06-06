# insertDebugGroups

**Framework**: Metal Performance Shaders  
**Kind**: structdata

Enabling this option will cause various kernel `encode` methods to call the [`pushDebugGroup(_:)`](https://developer.apple.com/documentation/metal/mtlcommandencoder/pushdebuggroup(_:)) and [`popDebugGroup()`](https://developer.apple.com/documentation/metal/mtlcommandencoder/popdebuggroup()) methods. The debug string will be drawn from the kernel’s [`label`](mpskernel/1618803-label.md) property, if available, or the name of the class otherwise.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
static var insertDebugGroups: MPSKernelOptions { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpskerneloptions/1648897-insertdebuggroups)*