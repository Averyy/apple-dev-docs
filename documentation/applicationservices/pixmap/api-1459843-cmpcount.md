# cmpCount

**Framework**: Application Services  
**Kind**: structp

The number of components used to represent a color for a pixel. With indexed pixels, each pixel is a single value representing an index in a color table, and therefore this field contains the value 1; the index is the single component. With direct pixels, each pixel contains three components (one integer each for the intensities of red, green, and blue) so this field contains the value 3.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var cmpCount: Int16
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/pixmap/1459843-cmpcount)*