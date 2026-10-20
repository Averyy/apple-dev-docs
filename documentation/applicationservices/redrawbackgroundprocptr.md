# RedrawBackgroundProcPtr

**Framework**: Application Services  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- macOS 10.0+

## Declaration

```swift
typealias RedrawBackgroundProcPtr = (ATSUTextLayout?, UniCharArrayOffset, Int, UnsafeMutablePointer<ATSTrapezoid>?, Int) -> DarwinBoolean
```

```c
typedef Boolean (*RedrawBackgroundProcPtr)(ATSUTextLayout iLayout, UniCharArrayOffset iTextOffset, UniCharCount iTextLength, ATSTrapezoid iUnhighlightArea[], ItemCount iTrapezoidCount);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/redrawbackgroundprocptr)*