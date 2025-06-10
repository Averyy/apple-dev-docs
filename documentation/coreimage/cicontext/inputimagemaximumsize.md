# inputImageMaximumSize()

**Framework**: Core Image  
**Kind**: method

Returns the maximum size allowed for any image rendered into the context.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func inputImageMaximumSize() -> CGSize
```

#### Discussion

Some contexts limit the maximum size of an image that can be rendered into them. For example, the maximum size might reflect a limitation in the underlying graphics hardware.

## See Also

- [func outputImageMaximumSize() -> CGSize](cicontext/outputimagemaximumsize.md)
  Returns the maximum size allowed for any image created by the context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/inputimagemaximumsize())*