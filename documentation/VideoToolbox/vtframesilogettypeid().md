# VTFrameSiloGetTypeID()

**Framework**: Video Toolbox  
**Kind**: func  
**Role**: Function

Retrieves the Core Foundation type identifier for the frame silo object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func VTFrameSiloGetTypeID() -> CFTypeID
```

```c
extern CFTypeID VTFrameSiloGetTypeID();
```

## Return Value

The `CFTypeID` of the frame silo object.

## See Also

### Inspecting Frame Silos
- [func VTFrameSiloGetProgressOfCurrentPass(VTFrameSilo, progressOut: UnsafeMutablePointer<Float32>) -> OSStatus](./vtframesilogetprogressofcurrentpass%28_,progressout%29.md)
  Gets the progress of the current pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframesilogettypeid())*