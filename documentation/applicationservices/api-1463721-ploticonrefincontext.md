# PlotIconRefInContext(_:_:_:_:_:_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.1+

## Declaration

```swift
func PlotIconRefInContext(_ inContext: CGContext!, _ inRect: UnsafePointer<CGRect>!, _ inAlign: IconAlignmentType, _ inTransform: IconTransformType, _ inLabelColor: UnsafePointer<RGBColor>!, _ inFlags: PlotIconRefFlags, _ inIconRef: IconRef!) -> OSStatus
```

```c
OSStatus PlotIconRefInContext(CGContextRef inContext, const CGRect *inRect, IconAlignmentType inAlign, IconTransformType inTransform, const RGBColor *inLabelColor, PlotIconRefFlags inFlags, IconRef inIconRef);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1463721-ploticonrefincontext)*