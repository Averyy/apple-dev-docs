# IconRefToHIShape(_:_:_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.5+

## Declaration

```swift
func IconRefToHIShape(_ iconRect: UnsafePointer<CGRect>!, _ align: IconAlignmentType, _ iconServicesUsageFlags: IconServicesUsageFlags, _ theIconRef: IconRef!) -> Unmanaged<HIShape>!
```

```c
HIShapeRef IconRefToHIShape(const CGRect *iconRect, IconAlignmentType align, IconServicesUsageFlags iconServicesUsageFlags, IconRef theIconRef);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1464005-iconreftohishape)*