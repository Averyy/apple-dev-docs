# ATSCreateFontQueryRunLoopSource(_:_:_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```swift
func ATSCreateFontQueryRunLoopSource(_ queryOrder: CFIndex, _ sourceOrder: CFIndex, _ callout: ATSFontQueryCallback!, _ context: UnsafePointer<ATSFontQuerySourceContext>!) -> Unmanaged<CFRunLoopSource>!
```

```c
CFRunLoopSourceRef ATSCreateFontQueryRunLoopSource(CFIndex queryOrder, CFIndex sourceOrder, ATSFontQueryCallback callout, const ATSFontQuerySourceContext *context);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1563673-atscreatefontqueryrunloopsource)*