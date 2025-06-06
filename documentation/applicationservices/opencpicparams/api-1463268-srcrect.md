# srcRect

**Framework**: Application Services  
**Kind**: structp

The optimal bounding rectangle for the resolution indicated by the `hRes` and `vRes` fields. To display a picture at a resolution other than that specified in the `hRes` and `vRes` fields, your application should compute an appropriate destination rectangle by scaling the image’s width and height by the destination resolution divided by the source resolution.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var srcRect: Rect
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/opencpicparams/1463268-srcrect)*