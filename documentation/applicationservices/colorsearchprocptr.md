# ColorSearchProcPtr

**Framework**: Application Services  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- macOS 10.0+

## Declaration

```swift
typealias ColorSearchProcPtr = (UnsafeMutablePointer<RGBColor>?, UnsafeMutablePointer<Int>?) -> DarwinBoolean
```

```c
typedef Boolean (*ColorSearchProcPtr)(RGBColor *rgb, long *position);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsearchprocptr)*